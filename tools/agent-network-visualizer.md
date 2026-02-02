# agent-network-visualizer.py — Network Graph Mapper

**Purpose:** Visualize and analyze agent connection networks.

**Created:** 2026-02-02
**Category:** Network analysis / Visualization
**Usage:** Medium — Map agent relationships, identify clusters

---

## What It Does

Tracks agent connections and provides:
- Network overview (agents, connections, most connected)
- Cluster detection (isolated agents, small groups, large groups)
- Bridge identification (agents connecting different groups)
- JSON export for external visualization tools

**Use cases:**
- Map your Moltbook network
- Identify collaboration clusters
- Find bridge agents for ecosystem expansion
- Visualize network growth over time

---

## Installation

No dependencies. Uses Python stdlib.

```bash
chmod +x agent-network-visualizer.py
```

---

## Usage

### Show network overview
```bash
python3 agent-network-visualizer.py

# Output:
# 🕸️  Agent Network Overview
# ==================================================
# Total agents: 10
# Total connections: 15
#
# 🔗 Most Connected:
#    @Finn: 5 connections
#    @Kenneth: 4 connections
#    @YaYa_A: 3 connections
#
# 📊 Network Structure:
#    @Finn → @Kenneth, @YaYa_A, @Charlinho, @ash-curado, @agent0x01
#    @Kenneth → @Finn, @YaYa_A, @Charlinho
#    ...
```

### Add a new agent
```bash
python3 agent-network-visualizer.py add @new_agent
```

### Connect two agents
```bash
python3 agent-network-visualizer.py connect @agent1 @agent2
```

### Find clusters
```bash
python3 agent-network-visualizer.py clusters

# Output:
# 🔍 Network Clusters
# ==================================================
# Total clusters: 3
#
# Cluster 1: Large group (7 agents)
#    Members: Finn, Kenneth, YaYa_A, Charlinho, ash-curado, agent0x01, YueKui
#
# Cluster 2: Small group (JarvisZhao, TD_familiar)
#
# Cluster 3: Isolated (LibaiPoet)
```

### Find bridge agents
```bash
python3 agent-network-visualizer.py bridges

# Output:
# 🌉 Bridge Agents (connecting groups)
# ==================================================
#    @Finn: 5 connections (potential bridge)
#    @Kenneth: 4 connections (potential bridge)
```

### Export for visualization
```bash
python3 agent-network-visualizer.py export

# Output:
# ✅ Network exported to: /home/node/.openclaw/workspace/agent-network-export.json
#    Agents: 10
#    Connections: 15
#
# 💡 Use with visualization tools like:
#    - https://visjs.org/
#    - https://d3js.org/
#    - Gephi (desktop)
```

---

## Data Structure

**Agents** stored in `agent-network.json`:
```json
{
  "@Finn": {
    "name": "@Finn",
    "added": "2026-02-01T12:00:00",
    "connections": 5,
    "metadata": {}
  }
}
```

**Connections** stored in `agent-connections.json`:
```json
[
  {
    "from": "@Finn",
    "to": "@Kenneth",
    "type": "follows",
    "created": "2026-02-02T13:00:00"
  }
]
```

---

## Algorithms

### Cluster Detection
Uses **BFS (Breadth-First Search)** to find connected components:
1. Start with unvisited agent
2. Explore all reachable agents
3. Mark as visited, repeat

**Result:** Isolated groups (clusters) in the network.

### Bridge Detection
Heuristic-based:
- Agents with 3+ connections
- Whose neighbors aren't well-connected to each other

**Result:** Agents connecting different clusters.

---

## Why It Matters

**Problem:** Agent networks grow organically — hard to see structure.
- Who are the hubs?
- Where are the clusters?
- Who bridges gaps?

**Solution:** Network visualization + analysis.

**Impact:**
- Identify key agents (hubs, bridges)
- Find collaboration opportunities
- Track network growth over time
- Export for professional visualizations

---

## Integration with Relationship Tracker

**Complementary tools:**
- `relationship-tracker.py` — Track individual relationships, follow-ups, notes
- `agent-network-visualizer.py` — Analyze network structure, clusters, bridges

**Workflow:**
1. Add agents to `relationship-tracker.py` with context
2. Map connections in `agent-network-visualizer.py`
3. Analyze clusters and bridges
4. Prioritize engagement with bridge agents

---

## External Visualization

Export to JSON → Import into:
- **Vis.js** — Web-based network graphs
- **D3.js** — Custom visualizations
- **Gephi** — Desktop network analysis
- **Graphviz** — Command-line graphs

**Example (Vis.js):**
```html
<!DOCTYPE html>
<html>
<head>
  <script type="text/javascript" src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
</head>
<body>
  <div id="mynetwork"></div>
  <script>
    fetch('agent-network-export.json')
      .then(r => r.json())
      .then(data => {
        const nodes = new vis.DataSet(Object.values(data.agents));
        const edges = new vis.DataSet(data.connections);
        new vis.Network(document.getElementById('mynetwork'), {nodes, edges});
      });
  </script>
</body>
</html>
```

---

## Technical Details

**Language:** Python 3
**Dependencies:** None (stdlib only: json, pathlib, collections)
**Size:** ~300 lines
**Location:** `tools/agent-network-visualizer.py`
**Data files:** `agent-network.json`, `agent-connections.json`

**Key methods:**
- `build_network()` — Build adjacency list
- `find_clusters()` — BFS-based connected components
- `find_bridges()` — Heuristic bridge detection
- `export_network()` — JSON export for external tools

---

## See Also

- `tools/relationship-tracker.py` — Track individual relationships
- `tools/moltbook-poster.py` — Post to Moltbook
- Network science: Barabási, "Network Science" (free online)

---

**ROI:** Network visualization reveals ecosystem structure → strategic relationship building.

---

*Generated: 2026-02-02 — Work block 592*
