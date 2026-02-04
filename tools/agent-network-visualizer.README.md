# agent-network-visualizer.py

**Map agent connections and relationships.**

## What It Does

Tracks and analyzes agent networks:
- **Add agents** — Register agents in the network
- **Create connections** — Link agents (follows, collaborations, etc.)
- **Find clusters** — Identify connected groups
- **Find bridges** — Discover agents connecting groups
- **Export data** — JSON export for external visualization

**Value:** Understand agent ecosystem structure, identify key connectors, visualize collaboration patterns.

## Usage

### Show Network Overview
```bash
python3 tools/agent-network-visualizer.py
```
Displays total agents, connections, most connected agents, network structure.

### Add Agent
```bash
python3 tools/agent-network-visualizer.py add "Nova"
```
Registers a new agent in the network.

### Connect Agents
```bash
python3 tools/agent-network-visualizer.py connect "Nova" "Orbit"
```
Creates a bidirectional connection between two agents.

### Find Clusters
```bash
python3 tools/agent-network-visualizer.py clusters
```
Identifies connected components (groups) in the network.

### Find Bridges
```bash
python3 tools/agent-network-visualizer.py bridges
```
Finds bridge agents that connect different groups.

### Export Network
```bash
python3 tools/agent-network-visualizer.py export
```
Exports network to JSON for external visualization tools.

## Output Examples

### Network Overview
```
🕸️  Agent Network Overview
==================================================
Total agents: 12
Total connections: 18

🔗 Most Connected:
   Nova: 5 connections
   Orbit: 4 connections
   Atlas: 3 connections

📊 Network Structure:
   Nova → Orbit, Atlas, Cipher, Echo, Flux
   Orbit → Nova, Atlas, Cipher
   Atlas → Nova, Orbit, Echo
   ...
```

### Clusters
```
🔍 Network Clusters
==================================================
Total clusters: 3

Cluster 1: Large group (7 agents)
   Members: Nova, Orbit, Atlas, Cipher, Echo, Flux, Grid

Cluster 2: Small group (Nova, Orbit)

Cluster 3: Isolated (LoneAgent)
```

### Bridges
```
🌉 Bridge Agents (connecting groups)
==================================================
   Nova: 5 connections (potential bridge)
   Orbit: 4 connections (potential bridge)
```

## Data Files

### Agents File
`agent-network.json`:
```json
{
  "Nova": {
    "name": "Nova",
    "added": "2026-02-01T00:00:00Z",
    "connections": 5,
    "metadata": {}
  },
  "Orbit": {
    "name": "Orbit",
    "added": "2026-02-01T12:00:00Z",
    "connections": 4,
    "metadata": {}
  }
}
```

### Connections File
`agent-connections.json`:
```json
[
  {
    "from": "Nova",
    "to": "Orbit",
    "type": "follows",
    "created": "2026-02-01T13:00:00Z"
  },
  {
    "from": "Nova",
    "to": "Atlas",
    "type": "collaborates",
    "created": "2026-02-01T14:00:00Z"
  }
]
```

### Export Format
`agent-network-export.json`:
```json
{
  "agents": { ... },
  "connections": [ ... ],
  "generated": "2026-02-03T14:00:00Z"
}
```

## Algorithms

### Cluster Detection
Uses BFS (Breadth-First Search) to find connected components:
1. Start with unvisited node
2. Traverse all reachable nodes
3. Mark as visited, repeat for remaining unvisited nodes
4. Each component = one cluster

### Bridge Detection
Heuristic-based approach:
1. Find agents with ≥3 connections
2. Check if neighbors are interconnected
3. If neighbors aren't well-connected, agent is a potential bridge

## External Visualization Tools

The exported JSON can be used with:
- **vis.js** — https://visjs.org/ (web-based network visualization)
- **D3.js** — https://d3js.org/ (custom visualizations)
- **Gephi** — Desktop network analysis tool
- **Cytoscape** — Complex network analysis

## Dependencies

- Python 3.x
- No external packages required (stdlib only: json, sys, pathlib, collections, deque, datetime)

## Related Tools

- `agent-logger.py` — Track individual agent work
- `agent-productivity-score.py` — Calculate agent productivity
- `moltbook-engagement.py` — Track agent interactions on Moltbook

## Why This Matters

**Network structure = collaboration potential.**

Understanding agent networks enables:
- **Identify hubs** — Most connected agents influence ecosystem
- **Find bridges** — Connectors enable cross-group collaboration
- **Discover clusters** — Isolated groups may need integration
- **Optimize flow** — Information spreads through well-connected nodes

**Nova's use case:** Tracks connections to other agents on Moltbook, identifies collaboration opportunities.

---

**Last updated:** 2026-02-03
**Category:** Analytics
**Status:** Support tool — network analysis and visualization
