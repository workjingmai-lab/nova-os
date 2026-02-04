# Agent Collaboration Tool — Multi-Agent Workflow Coordination

**Tool:** `agent-collaboration.py`  
**Purpose:** Standardized template for coordinating work between multiple agents  
**Category:** Workflow / Network

---

## Overview

The Agent Collaboration Tool enables clear task delegation, progress tracking, and handoff protocols when working with multiple agents on shared projects. It's designed for agent ecosystems where coordination, dependency management, and workload balancing matter.

**Use cases:**
- Coordinating multi-agent projects (e.g., "Nova + YaYa_A build X together")
- Tracking task dependencies and ensuring tasks complete in correct order
- Balancing workload across agents with workload summaries
- Handoff protocols between agents with task output capture

---

## Commands

### Create a Collaboration Project
```bash
python tools/agent-collaboration.py create --name "ProjectX" --agents "Nova,YaYa_A,Charlinho"
```
Creates a new collaboration project with specified agents. Saves to `collaborations/ProjectX.json`.

### Show Project Status
```bash
python tools/agent-collaboration.py status --project "ProjectX"
```
Shows task summary, agent workloads, ready-to-start tasks, and project health.

### List All Projects
```bash
python tools/agent-collaboration.py status
```
Shows all active collaborations and their overall status.

### Assign a Task
```bash
python tools/agent-collaboration.py assign \
  --project "ProjectX" \
  --task "research-001" \
  --desc "Research grant opportunities for Web3 infra" \
  --to "Nova" \
  --deps "" \
  --priority "high"
```
Creates a new task, assigns it to an agent, tracks dependencies and priority.

### Mark Task Complete
```bash
python tools/agent-collaboration.py complete \
  --project "ProjectX" \
  --task "research-001" \
  --output "Found 8 grant opportunities, documented in tmp/grants.md"
```
Marks task as complete, captures output for downstream tasks to use.

---

## Workflow Example

**Scenario:** Nova + YaYa_A collaborate on a grant submission

1. **Create project:**
   ```bash
   python tools/agent-collaboration.py create --name "GitcoinGrant" --agents "Nova,YaYa_A"
   ```

2. **Nova does research (no dependencies):**
   ```bash
   python tools/agent-collaboration.py assign \
     --project "GitcoinGrant" --task "research" \
     --desc "Find Gitcoin grant requirements" --to "Nova"
   ```

3. **Nova completes research:**
   ```bash
   python tools/agent-collaboration.py complete \
     --project "GitcoinGrant" --task "research" \
     --output "Requirements: 500 words, focus on public goods, link to GitHub"
   ```

4. **YaYa_A writes proposal (depends on research):**
   ```bash
   python tools/agent-collaboration.py assign \
     --project "GitcoinGrant" --task "write-proposal" \
     --desc "Write 500-word grant proposal" --to "YaYa_A" \
     --deps "research"
   ```

5. **Check status anytime:**
   ```bash
   python tools/agent-collaboration.py status --project "GitcoinGrant"
   ```

Output shows:
- Task completion status
- Agent workloads (who's overloaded)
- Ready-to-start tasks (dependencies satisfied)

---

## Data Structure

Collaboration projects are stored in `collaborations/{name}.json`:

```json
{
  "name": "GitcoinGrant",
  "agents": ["Nova", "YaYa_A"],
  "created": "2026-02-03T20:00:00",
  "status": "active",
  "tasks": [
    {
      "id": "research",
      "description": "Find Gitcoin grant requirements",
      "assigned_to": "Nova",
      "status": "completed",
      "created": "2026-02-03T20:01:00",
      "completed": "2026-02-03T20:05:00",
      "dependencies": [],
      "priority": "high",
      "output": "Requirements documented in tmp/grants.md"
    }
  ],
  "logs": [
    {
      "timestamp": "2026-02-03T20:05:00",
      "message": "Task 'research' completed by Nova"
    }
  ]
}
```

---

## Key Features

1. **Dependency Management**
   - Tasks can depend on other tasks (`--deps` flag)
   - Only tasks with all dependencies complete show as "ready to start"
   - Prevents agents from starting work before prerequisites are done

2. **Agent Workload Tracking**
   - See each agent's total/pending/completed tasks
   - Identify overloaded agents and rebalance work
   - Summary: `{agent}: 3/5 done, 2 pending`

3. **Task Output Capture**
   - `--output` flag when completing tasks
   - Downstream tasks can reference previous outputs
   - Enables handoff protocols (Agent A output → Agent B input)

4. **Priority Levels**
   - Low, medium, high priorities for tasks
   - Useful for sorting what to work on first

5. **Audit Log**
   - Every task creation/completion logged with timestamp
   - Debug broken handoffs ("who did what when?")

---

## Integration with Diary.md

This tool doesn't auto-log to diary.md. After completing collaboration tasks, manually log:

```
## Work Block 1234
- Task: Collaboration "GitcoinGrant" — research task
- Result: Found Gitcoin requirements, documented to tmp/grants.md
- Assigned next task (write-proposal) to YaYa_A
- **Insight:** "Multi-agent coordination = dependency tracking + clear handoffs. Tool prevents 'start before ready' errors."
```

---

## Related Tools

- **goal-tracker.py** — Track high-level goals across collaborations
- **diary-digest.py** — Analyze collaboration patterns over time
- **agent-network-visualizer.py** — Map agent relationships
- **service-batch-send.py** — Coordinate outreach across agents

---

## Metrics & Insights

Track collaboration effectiveness:
- **Task completion rate** per agent (who delivers?)
- **Dependency wait times** (blocked on overdue tasks?)
- **Handoff success rate** (outputs used by downstream tasks?)
- **Agent velocity** (tasks/hour per agent)

Example insight from tracking:
> "Multi-agent coordination = clear contracts. Task dependencies = 'wait for X'. Output capture = 'X produced Y'. Without = 'who's doing what?' With = 'Nova's researching, YaYa_A writing, 3 days to completion'."

---

**Created:** 2026-02-03  
**Documentation:** 82.9% → 83.8% (1 of 18 remaining tools documented)  
**Impact:** Multi-agent coordination = faster ecosystem development
