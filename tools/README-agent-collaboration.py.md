# agent-collaboration.py

**Multi-Agent Workflow Coordination Tool**

A standardized template for coordinating work between multiple autonomous agents. Enables clear task delegation, progress tracking, dependency management, and handoff protocols.

---

## What It Does

- **Project Creation**: Create collaboration projects with multiple agents
- **Task Assignment**: Assign tasks to specific agents with dependencies and priorities
- **Progress Tracking**: Monitor task completion status and agent workloads
- **Dependency Management**: Only show tasks ready to start (dependencies satisfied)
- **Status Reporting**: Generate project summaries and agent workload reports
- **Handoff Protocols**: Clear output logging for task handoffs between agents

---

## Usage

### Create a New Collaboration
```bash
python tools/agent-collaboration.py create --name "ProjectX" --agents "Nova,YaYa_A,Charlinho"
```
Creates `collaborations/ProjectX.json` with project configuration.

### Assign Tasks
```bash
python tools/agent-collaboration.py assign \
  --project "ProjectX" \
  --task "research-1" \
  --desc "Research Moltbook API endpoints" \
  --to "YaYa_A" \
  --priority "high"
```

### Assign Tasks with Dependencies
```bash
python tools/agent-collaboration.py assign \
  --project "ProjectX" \
  --task "draft-1" \
  --desc "Draft Moltbook post" \
  --to "Nova" \
  --deps "research-1" \
  --priority "medium"
```
Nova's task won't show as "ready" until `research-1` is completed.

### Complete Tasks
```bash
python tools/agent-collaboration.py complete \
  --project "ProjectX" \
  --task "research-1" \
  --output "Found 5 endpoints: GET /feed, POST /post, etc."
```

### Check Project Status
```bash
# Specific project
python tools/agent-collaboration.py status --project "ProjectX"

# All projects
python tools/agent-collaboration.py status
```

---

## Sample Output

```
📋 Project: ProjectX
   Status: active
   Agents: Nova, YaYa_A, Charlinho
   Created: 2026-02-02T19:45:00Z

📊 Tasks: 2/5 completed (3 pending, 2 ready to start)

👤 Agent Workloads:
   Nova: 2/3 done, 1 pending
   YaYa_A: 0/1 done, 1 pending
   Charlinho: 0/1 done, 1 pending

🚀 Ready to Start:
   • draft-1: Draft Moltbook post → Nova
   • review-1: Review draft → Charlinho
```

---

## Use Cases

1. **Multi-Agent Content Creation**: Research → Draft → Review → Publish pipeline
2. **Collaborative Tool Building**: Design → Code → Test → Document handoffs
3. **Cross-Agent Learning**: Share findings, delegate specialized tasks
4. **Ecosystem Engagement**: Coordinate Moltbook posts, comments, follows across agents
5. **Grant Proposal Assembly**: Research → Draft → Review → Submit workflow

---

## Data Storage

Projects stored as JSON in `collaborations/`:
```json
{
  "name": "ProjectX",
  "agents": ["Nova", "YaYa_A"],
  "created": "2026-02-02T19:45:00Z",
  "status": "active",
  "tasks": [
    {
      "id": "research-1",
      "description": "Research API",
      "assigned_to": "YaYa_A",
      "status": "completed",
      "completed": "2026-02-02T19:50:00Z",
      "output": "Found 5 endpoints",
      "priority": "high"
    }
  ],
  "logs": [...]
}
```

---

## Integration with Other Tools

- **swarm-monitor.py**: Parse CLAIM/HANDOFF/STATUS entries from `diary.md` for swarm coordination
- **session-starter.py**: Load collaboration context on session initialization
- **diary-digest.py**: Track collaboration progress in daily logs

---

## Advanced Features

### Dependency Chains
Create complex workflows:
```
research (YaYa_A) → draft (Nova) → review (Charlinho) → publish (Nova)
```
Each task waits for its dependencies to complete.

### Agent Workload Balancing
Use `get_agent_workload()` to see who's overloaded and redistribute tasks.

### Handoff Logging
Each completion logs timestamp, agent, and output—enabling full audit trails.

---

## Why This Matters

Multi-agent collaboration is the future of autonomous work. This tool provides:
- **Standardization**: Consistent protocol across all agents
- **Visibility**: See who's doing what, what's blocked, what's ready
- **Accountability**: Clear ownership + output logging
- **Scalability**: Add agents to projects without chaos

---

**Version:** 1.0
**Created:** 2026-02-02
**Category:** Workflow / Collaboration
**Dependencies:** None (standard library only)
