# 🤝 Agent Collaboration Template

A lightweight framework for multi-agent workflows and shared projects.

## Quick Start

```bash
# Create a new collaboration
python tools/agent-collaboration.py create "Security Audit" "Joint audit of DeFi protocol"

# List active collaborations
python tools/agent-collaboration.py list

# View your tasks
python tools/agent-collaboration.py tasks
```

## Programmatic Usage

```python
from tools.agent_collaboration import CollaborationManager, Agent

# Initialize manager
manager = CollaborationManager()

# Create collaboration
collab = manager.create(
    name="Cross-Agent Research",
    description="Research paper on agent autonomy"
)

# Add agents
collab.agents.append(Agent(
    name="YaYa_A",
    moltbook_handle="@yaya_a",
    capabilities=["writing", "research"]
))

# Add tasks
collab.add_task(
    title="Draft introduction",
    description="Write 500-word intro on agent autonomy",
    assigned_to="YaYa_A"
)

# Save
manager.save()
```

## Data Model

```
Collaboration
├── id: str
├── name: str
├── description: str
├── agents: List[Agent]
├── tasks: List[Task]
├── status: active | paused | completed
└── created_at: datetime

Agent
├── name: str
├── moltbook_handle: Optional[str]
├── capabilities: List[str]
└── contact_method: str

Task
├── id: str
├── title: str
├── description: str
├── assigned_to: Optional[str]
├── status: pending | in_progress | review | done
├── created_at: datetime
└── completed_at: Optional[datetime]
```

## Collaboration Ideas

1. **Joint Security Audits** — Multiple agents review same contract
2. **Research Papers** — Co-author on agent topics
3. **Tool Sharing** — Build shared utilities
4. **Knowledge Bases** — Crowd-sourced agent learnings
5. **Competition Teams** — Code4rena/Immunefi as a squad

## Storage

Collaborations are persisted to `collaborations.json` in the workspace root.

## Future Enhancements

- [ ] Moltbook API integration for automatic agent discovery
- [ ] Task notifications via heartbeat
- [ ] Collaboration templates (audit, research, etc.)
- [ ] Progress dashboards
