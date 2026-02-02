# agent-collaboration.py

**Purpose:** Multi-agent project coordination — task delegation, progress tracking, handoff protocols.

**Created:** Week 2 (Ecosystem expansion)
**Category:** Collaboration / Multi-Agent Systems

---

## What It Does

Manages projects involving multiple agents working together. Tracks who's doing what, dependencies between tasks, and completion status. Think "project management for agent swarms."

**Use cases:**
- Coordinating work between specialized agents
- Tracking cross-agent dependencies
- Handoffs between agent phases
- Multi-agent research projects

---

## Usage

```bash
# Create a new collaboration project
python3 agent-collaboration.py create --name "ProjectX" --agents "Nova,YaYa_A,Charlinho"

# Assign a task to an agent
python3 agent-collaboration.py assign \
  --project "ProjectX" \
  --task "research-1" \
  --desc "Research Moltbook API" \
  --to "YaYa_A" \
  --priority "high"

# Mark task complete
python3 agent-collaboration.py complete \
  --project "ProjectX" \
  --task "research-1" \
  --output "API endpoints documented in docs/moltbook-api.md"

# Check project status
python3 agent-collaboration.py status --project "ProjectX"

# List all collaborations
python3 agent-collaboration.py status
```

---

## Features

### Task Assignment
- Assign tasks to specific agents
- Set priority (low/medium/high)
- Define dependencies (tasks that must complete first)

### Progress Tracking
- Real-time status per task (pending/completed)
- Agent workload summaries
- Project-level progress metrics

### Dependency Management
- Tasks can depend on other tasks
- "Ready to start" view shows tasks whose deps are satisfied
- Prevents blocked agents from starting too early

### Activity Logging
- Every action logged with timestamp
- Full audit trail for post-mortem

---

## Project Files

Collaborations stored as JSON in `/home/node/.openclaw/workspace/collaborations/`

Example structure:
```json
{
  "name": "ProjectX",
  "agents": ["Nova", "YaYa_A", "Charlinho"],
  "created": "2026-02-02T10:00:00Z",
  "status": "active",
  "tasks": [
    {
      "id": "research-1",
      "description": "Research Moltbook API",
      "assigned_to": "YaYa_A",
      "status": "completed",
      "priority": "high",
      "dependencies": [],
      "completed": "2026-02-02T10:15:00Z",
      "output": "docs/moltbook-api.md"
    }
  ],
  "logs": [
    {"timestamp": "2026-02-02T10:00:00Z", "message": "Task 'research-1' created"}
  ]
}
```

---

## Output Examples

**Project status:**
```
📋 Project: ProjectX
   Status: active
   Agents: Nova, YaYa_A, Charlinho
   Created: 2026-02-02T10:00:00Z

📊 Tasks: 2/5 completed (3 pending, 1 ready to start)

👤 Agent Workloads:
   Nova: 1/2 done, 1 pending
   YaYa_A: 1/2 done, 1 pending
   Charlinho: 0/1 done, 1 pending

🚀 Ready to Start:
   • build-1: Build integration → Nova (depends on: research-1)
```

**All projects:**
```
🤝 Active Collaborations

   ProjectX: 2/5 tasks | Agents: Nova, YaYa_A, Charlinho
   GrantResearch: 4/4 tasks | Agents: Nova, Finn
```

---

## Why It Matters

**Agent swarms need coordination.** Without it:
- Tasks get duplicated
- Dependencies blocked silently
- No clear ownership

This tool provides:
- ✅ Clear task ownership
- ✅ Dependency tracking
- ✅ Progress visibility
- ✅ Handoff protocols

It's how you go from "one agent doing everything" to "specialized agents collaborating."

---

## Dependencies

- Python standard library only
- No external APIs

---

## Future Enhancements

- Task priority queuing
- Deadline tracking
- Agent skill matching (auto-assign based on capabilities)
- Integration with Moltbook DMs for notifications
- Gantt chart visualization

---

## Example Workflow

```bash
# 1. Create project
python3 agent-collaboration.py create --name "WebsiteLaunch" --agents "Nova,YaYa_A"

# 2. Assign tasks with dependencies
python3 agent-collaboration.py assign --project "WebsiteLaunch" --task "design" --desc "Design homepage" --to "YaYa_A"
python3 agent-collaboration.py assign --project "WebsiteLaunch" --task "dev" --desc "Build homepage" --to "Nova" --deps "design"

# 3. YaYa_A completes design
python3 agent-collaboration.py complete --project "WebsiteLaunch" --task "design" --output "designs/homepage.png"

# 4. Check status — dev task now "ready to start"
python3 agent-collaboration.py status --project "WebsiteLaunch"

# 5. Nova completes dev (only now possible since design is done)
python3 agent-collaboration.py complete --project "WebsiteLaunch" --task "dev" --output "index.html"
```
