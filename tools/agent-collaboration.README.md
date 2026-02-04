# agent-collaboration.py

**Multi-agent workflow coordination tool.**

## What It Does

Standardizes collaboration between multiple agents:
- **Create projects** — Set up multi-agent collaborations
- **Assign tasks** — Delegate work with dependencies
- **Track progress** — Monitor task completion and agent workload
- **Handoff protocols** — Clear task dependencies and outputs

**Value:** Enables complex multi-agent projects with clear ownership, dependencies, and progress tracking.

## Usage

### Create Collaboration Project
```bash
python3 tools/agent-collaboration.py create --name "ProjectX" --agents "Nova,YaYa_A,Charlinho"
```
Creates a new project with specified agents.

### Show Project Status
```bash
# All projects
python3 tools/agent-collaboration.py status

# Specific project
python3 tools/agent-collaboration.py status --project "ProjectX"
```
Displays task completion, agent workload, ready tasks.

### Assign Task
```bash
python3 tools/agent-collaboration.py assign \
  --project "ProjectX" \
  --task "task-1" \
  --desc "Research market trends" \
  --to "YaYa_A" \
  --priority "high"
```
Creates a task and assigns to an agent.

### Assign Task with Dependencies
```bash
python3 tools/agent-collaboration.py assign \
  --project "ProjectX" \
  --task "task-2" \
  --desc "Create presentation based on research" \
  --to "Charlinho" \
  --deps "task-1" \
  --priority "medium"
```
Task-2 only becomes ready after task-1 completes.

### Complete Task
```bash
python3 tools/agent-collaboration.py complete \
  --project "ProjectX" \
  --task "task-1" \
  --output "Market research report: PDF at docs/research.pdf"
```
Marks task complete, unlocks dependent tasks.

## Output Examples

### Project Status
```
📋 Project: ProjectX
   Status: active
   Agents: Nova, YaYa_A, Charlinho
   Created: 2026-02-03T14:00:00Z

📊 Tasks: 3/8 completed (5 pending, 2 ready to start)

👤 Agent Workloads:
   Nova: 2/4 done, 2 pending
   YaYa_A: 1/2 done, 1 pending
   Charlinho: 0/2 done, 2 pending

🚀 Ready to Start:
   • task-3: Design system architecture → Nova
   • task-5: Write documentation → Charlinho
```

### All Projects
```
🤝 Active Collaborations

   ProjectX: 3/8 tasks | Agents: Nova, YaYa_A, Charlinho
   MarketResearch: 5/5 tasks | Agents: Nova, Orbit
   ContentCampaign: 0/12 tasks | Agents: Nova, Atlas, Flux
```

## Project File Format

`collaborations/ProjectX.json`:
```json
{
  "name": "ProjectX",
  "agents": ["Nova", "YaYa_A", "Charlinho"],
  "created": "2026-02-03T14:00:00Z",
  "status": "active",
  "tasks": [
    {
      "id": "task-1",
      "description": "Research market trends",
      "assigned_to": "YaYa_A",
      "status": "completed",
      "created": "2026-02-03T14:05:00Z",
      "completed": "2026-02-03T15:30:00Z",
      "dependencies": [],
      "priority": "high",
      "output": "Market research report: PDF at docs/research.pdf"
    },
    {
      "id": "task-2",
      "description": "Create presentation based on research",
      "assigned_to": "Charlinho",
      "status": "pending",
      "created": "2026-02-03T14:10:00Z",
      "completed": null,
      "dependencies": ["task-1"],
      "priority": "medium",
      "output": null
    }
  ],
  "logs": [
    {
      "timestamp": "2026-02-03T14:05:00Z",
      "message": "Task 'task-1' created and assigned to YaYa_A"
    },
    {
      "timestamp": "2026-02-03T15:30:00Z",
      "message": "Task 'task-1' completed by YaYa_A"
    }
  ]
}
```

## Task States

| State | Description |
|-------|-------------|
| pending | Not yet started (dependencies may be incomplete) |
| ready | Pending but all dependencies complete |
| completed | Finished with output |

## Priority Levels

- **high** — Urgent, blocks other work
- **medium** — Standard priority (default)
- **low** — Nice to have, can defer

## Dependencies

Tasks can depend on other tasks:
```bash
# task-2 requires task-1 to complete first
--deps "task-1"

# task-3 requires both task-1 and task-2
--deps "task-1,task-2"
```

Dependent tasks only show as "ready to start" after all dependencies complete.

## Agent Workload Summary

Each agent's workload shows:
- **Total** — Tasks assigned to agent
- **Completed** — Tasks finished
- **Pending** — Tasks not yet done

Example:
```
Nova: 2/4 done, 2 pending
```
→ Nova has 4 total tasks, 2 completed, 2 pending

## Dependencies

- Python 3.x
- No external packages required (stdlib only: json, os, argparse, datetime, pathlib, typing)

## Related Tools

- `agent-network-visualizer.py` — Visualize agent connections
- `task-navigator.py` — Navigate and execute tasks
- `batch-executor.py` — Execute multiple tasks in batch

## Why This Matters

**Multi-agent collaboration requires coordination.**

Without structure:
- "Who's doing what?" → Confusion, duplicated work
- "I'm blocked on X" → Silent delays
- "Where's the output?" → Lost deliverables

With this tool:
- **Clear ownership** — Every task has one assignee
- **Dependency tracking** — Tasks unlock when prerequisites complete
- **Progress visibility** — Real-time status for all agents
- **Handoff protocols** — Outputs are documented and discoverable

**Nova's use case:** Coordinates complex projects (e.g., market research → presentation → outreach) across multiple agents with clear dependencies.

---

**Last updated:** 2026-02-03
**Category:** Workflow
**Status:** Core tool — multi-agent project coordination
