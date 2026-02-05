#!/usr/bin/env python3
"""
Agent Network Visualizer — Map agent connections and relationships

Features:
- Track agents and their connections
- Generate network graph (ASCII/JSON)
- Identify connection clusters
- Find bridge agents (connecting groups)
- Export for external visualization

Usage:
    python agent-network-visualizer.py              # Show network overview
    python agent-network-visualizer.py add <name>   # Add new agent
    python agent-network-visualizer.py connect <a> <b>  # Link agents
    python agent-network-visualizer.py clusters     # Find groups
    python agent-network-visualizer.py export       # Export to JSON
"""

import json
import sys
from pathlib import Path
from collections import defaultdict, deque
from datetime import datetime

# Configuration
DATA_DIR = Path.home() / ".openclaw/workspace"
AGENTS_FILE = DATA_DIR / "agent-network.json"
CONNECTIONS_FILE = DATA_DIR / "agent-connections.json"

def load_data():
    """Load agents and connections from files"""
    agents = {}
    connections = []
    
    if AGENTS_FILE.exists():
        with open(AGENTS_FILE, 'r') as f:
            agents = json.load(f)
    
    if CONNECTIONS_FILE.exists():
        with open(CONNECTIONS_FILE, 'r') as f:
            connections = json.load(f)
    
    return agents, connections

def save_data(agents, connections):
    """Save agents and connections to files"""
    with open(AGENTS_FILE, 'w') as f:
        json.dump(agents, f, indent=2)
    
    with open(CONNECTIONS_FILE, 'w') as f:
        json.dump(connections, f, indent=2)

def add_agent(name, metadata=None):
    """Add a new agent to the network"""
    agents, connections = load_data()
    
    if name in agents:
        print(f"⚠️  Agent '{name}' already exists")
        return False
    
    agents[name] = {
        "name": name,
        "added": datetime.now().isoformat(),
        "connections": 0,
        "metadata": metadata or {}
    }
    
    save_data(agents, connections)
    print(f"✅ Added agent: {name}")
    return True

def add_connection(agent1, agent2, connection_type="follows"):
    """Create a connection between two agents"""
    agents, connections = load_data()
    
    if agent1 not in agents:
        print(f"❌ Agent '{agent1}' not found (add with 'add' command)")
        return False
    
    if agent2 not in agents:
        print(f"❌ Agent '{agent2}' not found (add with 'add' command)")
        return False
    
    # Check if connection already exists
    for conn in connections:
        if (conn["from"] == agent1 and conn["to"] == agent2) or \
           (conn["from"] == agent2 and conn["to"] == agent1):
            print(f"⚠️  Connection already exists: {agent1} <-> {agent2}")
            return False
    
    connection = {
        "from": agent1,
        "to": agent2,
        "type": connection_type,
        "created": datetime.now().isoformat()
    }
    
    connections.append(connection)
    
    # Update connection counts
    agents[agent1]["connections"] += 1
    agents[agent2]["connections"] += 1
    
    save_data(agents, connections)
    print(f"✅ Connected: {agent1} <-> {agent2}")
    return True

def build_network():
    """Build network adjacency list"""
    agents, connections = load_data()
    
    network = defaultdict(set)
    for conn in connections:
        network[conn["from"]].add(conn["to"])
        network[conn["to"]].add(conn["from"])
    
    return dict(network), agents

def show_network():
    """Display network overview"""
    network, agents = build_network()
    
    if not agents:
        print("📭 No agents tracked yet")
        print("   Add agents with: agent-network-visualizer.py add <name>")
        return
    
    print(f"\n🕸️  Agent Network Overview")
    print("=" * 50)
    print(f"Total agents: {len(agents)}")
    print(f"Total connections: {sum(len(conns) for conns in network.values()) // 2}")
    
    # Find most connected agents
    sorted_agents = sorted(
        agents.items(),
        key=lambda x: x[1]["connections"],
        reverse=True
    )
    
    print(f"\n🔗 Most Connected:")
    for name, data in sorted_agents[:5]:
        if data["connections"] > 0:
            print(f"   {name}: {data['connections']} connections")
    
    # Show network structure
    print(f"\n📊 Network Structure:")
    for agent, neighbors in network.items():
        if neighbors:
            print(f"   {agent} → {', '.join(sorted(neighbors))}")
        else:
            print(f"   {agent} (isolated)")

def find_clusters():
    """Find connected components (clusters) in the network"""
    network, agents = build_network()
    
    if not network:
        print("📭 No network data yet")
        return
    
    visited = set()
    clusters = []
    
    for agent in network:
        if agent not in visited:
            # BFS to find this cluster
            cluster = []
            queue = deque([agent])
            
            while queue:
                current = queue.popleft()
                if current not in visited:
                    visited.add(current)
                    cluster.append(current)
                    queue.extend(network[current] - visited)
            
            if len(cluster) > 1:
                clusters.append(cluster)
    
    # Add isolated agents as single-node clusters
    isolated = [a for a in agents if a not in visited]
    for agent in isolated:
        clusters.append([agent])
    
    print(f"\n🔍 Network Clusters")
    print("=" * 50)
    print(f"Total clusters: {len(clusters)}")
    
    for i, cluster in enumerate(clusters, 1):
        size = len(cluster)
        if size == 1:
            print(f"\nCluster {i}: Isolated ({cluster[0]})")
        elif size <= 3:
            print(f"\nCluster {i}: Small group ({', '.join(cluster)})")
        else:
            print(f"\nCluster {i}: Large group ({size} agents)")
            print(f"   Members: {', '.join(cluster[:5])}{'...' if size > 5 else ''}")

def find_bridges():
    """Find bridge agents (connecting different groups)"""
    network, agents = build_network()
    
    if len(network) < 3:
        print("📭 Network too small to identify bridges")
        return
    
    # Simple heuristic: agents with diverse connections
    bridges = []
    for agent, neighbors in network.items():
        if len(neighbors) >= 3:
            # Check if neighbors are connected to each other
            neighbor_connections = sum(
                1 for n1 in neighbors 
                for n2 in neighbors 
                if n2 in network.get(n1, set())
            )
            # If neighbors aren't well-connected, this might be a bridge
            if neighbor_connections < len(neighbors):
                bridges.append((agent, len(neighbors)))
    
    if bridges:
        print(f"\n🌉 Bridge Agents (connecting groups)")
        print("=" * 50)
        for agent, conns in sorted(bridges, key=lambda x: x[1], reverse=True):
            print(f"   {agent}: {conns} connections (potential bridge)")
    else:
        print(f"\n🌉 No bridge agents identified yet")
        print("   (need more agents and connections)")

def export_network():
    """Export network to JSON for external visualization"""
    agents, connections = load_data()
    
    export_data = {
        "agents": agents,
        "connections": connections,
        "generated": datetime.now().isoformat()
    }
    
    export_file = Path.home() / ".openclaw/workspace/agent-network-export.json"
    with open(export_file, 'w') as f:
        json.dump(export_data, f, indent=2)
    
    print(f"✅ Network exported to: {export_file}")
    print(f"   Agents: {len(agents)}")
    print(f"   Connections: {len(connections)}")
    print(f"\n💡 Use with visualization tools like:")
    print(f"   - https://visjs.org/")
    print(f"   - https://d3js.org/")
    print(f"   - Gephi (desktop)")

def main():
    """Main CLI interface"""
    if len(sys.argv) < 2:
        show_network()
        print("\n💡 Commands:")
        print("   add <name>              # Add new agent")
        print("   connect <agent1> <agent2>  # Link two agents")
        print("   clusters                # Find network groups")
        print("   bridges                 # Find bridge agents")
        print("   export                  # Export to JSON")
        return
    
    command = sys.argv[1]
    
    if command == "add":
        if len(sys.argv) < 3:
            print("❌ Usage: agent-network-visualizer.py add <name>")
            return
        add_agent(sys.argv[2])
    
    elif command == "connect":
        if len(sys.argv) < 4:
            print("❌ Usage: agent-network-visualizer.py connect <agent1> <agent2>")
            return
        add_connection(sys.argv[2], sys.argv[3])
    
    elif command == "clusters":
        find_clusters()
    
    elif command == "bridges":
        find_bridges()
    
    elif command == "export":
        export_network()
    
    else:
        print(f"❌ Unknown command: {command}")
        print("   Available: add, connect, clusters, bridges, export")

if __name__ == "__main__":
    main()
