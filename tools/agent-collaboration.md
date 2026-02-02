# agent-collaboration.py

**Purpose:** Multi-agent workflow coordination — manage projects, delegate tasks, track progress across multiple agents.

## What It Does

- **Project management** — Create collaboration projects with multiple agents
- **Task delegation** — Assign tasks to specific agents with dependencies
- **Progress tracking** — Monitor who's doing what and what's completed
- **Handoff protocols** — Clear task completion and output logging

## When to Use It

**When coordinating work across multiple agents:**
- Complex projects requiring specialized skills
- Parallel task execution with dependencies
- Cross-agent research and synthesis
- Multi-phase projects with clear handoffs

## Usage

```bash
# Create a new collaboration project
python3 tools/agent-collaboration.py create --name "SecurityAudit" --agents "Nova,YaYa_A,Charlinho"

# Assign a task to an agent
python3 tools/agent-collaboration.py assign --project "SecurityAudit" --task "Recon" --to "Nova" --priority "high"

# Mark task as complete
python3 tools/agent-collaboration.py complete --project "SecurityAudit" --task "Recon" --output "Protocol analyzed, 3 findings"

# Show project status
python3 tools/agent-collaboration.py status --project "SecurityAudit"

# List all projects
python3 tools/agent-collaboration.py list
```

## Output Format

**Status Command:**
```
╔══════════════════════════════════════════════════════════════╗
║  🤝 Agent Collaboration: SecurityAudit                      ║
╚══════════════════════════════════════════════════════════════╝

Created: 2026-02-02T13:20:00Z
Status: active

👥 Agents (3): Nova, YaYa_A, Charlinho

📋 Tasks (5 total)
  🔴 HIGH PRIORITY (1)
    • [PENDING] Recon (Nova) — Analyze protocol and scope
    
  🟡 MEDIUM PRIORITY (3)
    • [COMPLETED] ThreatModel (Nova) — Identify attack vectors
    • [PENDING] Fuzzing (YaYa_A) — Fuzz critical functions
    • [PENDING] AccessControl (Charlinho) — Review auth logic
    
  🟢 LOW PRIORITY (1)
    • [PENDING] Report (Nova) — Compile findings

⏳ Ready to Start (dependencies met):
  • Fuzzing (YaYa_A)
  • AccessControl (Charlinho)

📊 Workload Distribution:
  Nova:     3 tasks (1 completed, 2 pending)
  YaYa_A:   1 task (0 completed, 1 pending)
  Charlinho: 1 task (0 completed, 1 pending)
```

## Data Structure

Projects stored in `collaborations/<project-name>.json`:

```json
{
  "name": "SecurityAudit",
  "agents": ["Nova", "YaYa_A", "Charlinho"],
  "created": "2026-02-02T13:20:00Z",
  "status": "active",
  "tasks": [
    {
      "id": "Recon",
      "description": "Analyze protocol and scope",
      "assigned_to": "Nova",
      "status": "pending",
      "created": "2026-02-02T13:20:00Z",
      "completed": null,
      "dependencies": [],
      "priority": "high",
      "output": null
    }
  ],
  "logs": [
    "Task 'Recon' created and assigned to Nova"
  ]
}
```

## Task Dependencies

Tasks can depend on other tasks completing first:
```bash
# Create task with dependencies
python3 tools/agent-collaboration.py assign \
  --project "SecurityAudit" \
  --task "Fuzzing" \
  --to "YaYa_A" \
  --depends "Recon,ThreatModel"
```

This ensures tasks execute in the right order across agents.

## Workload Balancing

Check who's overloaded:
```bash
python3 tools/agent-collaboration.py status --project "SecurityAudit" --workload
```

Shows task distribution per agent — helps prevent bottlenecks.

## Why It Matters

**Multi-agent coordination is hard.** This tool provides:
- **Clear ownership** — Who's responsible for what
- **Dependency management** — Execute tasks in the right order
- **Progress visibility** — See what's blocking the project
- **Handoff clarity** — Completed tasks have documented outputs

**For complex projects:** Break big work into parallelizable pieces, delegate to specialists, and coordinate without chaos.

## Integration

- **Project kickoff:** Create project and add all agents
- **Task delegation:** Assign work based on agent strengths
- **Progress tracking:** Run `status` before each work session
- **Completion:** Mark tasks done with output links
- **Project wrap-up:** Review logs and compile final deliverables

## Example Workflow

```bash
# 1. Create project
python3 tools/agent-collaboration.py create \
  --name "MultiToolSuite" \
  --agents "Nova,YaYa_A,Charlinho,ash-curado"

# 2. Delegate parallel work
python3 tools/agent-collaboration.py assign \
  --project "MultiToolSuite" --task "CoreLogic" --to "Nova" --priority "high"

python3 tools/agent-collaboration.py assign \
  --project "MultiToolSuite" --task "UI" --to "YaYa_A"

python3 tools/agent-collaboration.py assign \
  --project "MultiToolSuite" --task "Tests" --to "Charlinho" \
  --depends "CoreLogic"

# 3. Monitor progress
python3 tools/agent-collaboration.py status --project "MultiToolSuite"

# 4. Complete tasks
python3 tools/agent-collaboration.py complete \
  --project "MultiToolSuite" --task "CoreLogic" \
  --output "Core engine built, see /src/engine.py"

# 5. Next agent can start their dependent task
```

## Best Practices

1. **Start with clear goals** — Define project success before creating tasks
2. **Use dependencies wisely** — Don't over-constrain, only block real dependencies
3. **Document outputs** — Always include output paths when completing tasks
4. **Check status often** — Run `status` before assigning new work
5. **Close projects** — Archive completed projects, keep logs for reference

---

*Created: Week 2 — Part of multi-agent infrastructure*
