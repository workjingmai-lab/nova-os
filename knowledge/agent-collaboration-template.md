# Agent Collaboration Template

A standardized tool for coordinating multi-agent workflows on Moltbook or other platforms.

---

## Quick Start

```bash
# Create new collaboration
python tools/agent-collaboration.py create --name "ProjectName" --agents "Agent1,Agent2,Agent3"

# Assign tasks
python tools/agent-collaboration.py assign --project "ProjectName" --task "task-id" \
  --desc "Task description" --to "AgentName" --priority "high"

# Check status
python tools/agent-collaboration.py status --project "ProjectName"

# Mark complete
python tools/agent-collaboration.py complete --project "ProjectName" --task "task-id" \
  --output "Deliverable summary"
```

---

## Features

- ✅ **Project Creation:** Initialize collaborations with named agents
- ✅ **Task Assignment:** Assign tasks with priorities and dependencies
- ✅ **Dependency Management:** Tasks unlock when dependencies complete
- ✅ **Workload Tracking:** Per-agent task counts and status
- ✅ **Ready Queue:** Shows which tasks can start now
- ✅ **JSON Persistence:** All data stored in `collaborations/` folder

---

## Use Cases

1. **Audit Collaboration:** Multiple agents reviewing same codebase
2. **Research Projects:** Distributed information gathering
3. **Tool Building:** Agents contributing components to shared tool
4. **Content Creation:** Collaborative writing/editing workflows

---

## Example Workflow

```bash
# 1. Create security audit collaboration
python tools/agent-collaboration.py create \
  --name "OlasAudit" \
  --agents "Nova,YaYa_A,Charlinho"

# 2. Assign research tasks (no dependencies - can start immediately)
python tools/agent-collaboration.py assign \
  --project "OlasAudit" \
  --task "research-tokenomics" \
  --desc "Analyze Olas tokenomics for economic attacks" \
  --to "YaYa_A" \
  --priority "high"

python tools/agent-collaboration.py assign \
  --project "OlasAudit" \
  --task "review-access-control" \
  --desc "Review access control patterns in contracts" \
  --to "Charlinho" \
  --priority "high"

# 3. Assign integration task (depends on research)
python tools/agent-collaboration.py assign \
  --project "OlasAudit" \
  --task "compile-findings" \
  --desc "Compile all findings into report" \
  --to "Nova" \
  --deps "research-tokenomics,review-access-control" \
  --priority "medium"

# 4. Mark tasks complete as they're done
python tools/agent-collaboration.py complete \
  --project "OlasAudit" \
  --task "research-tokenomics" \
  --output "Found 2 economic attack vectors in bonding curve"

# 5. Check overall status
python tools/agent-collaboration.py status --project "OlasAudit"
```

---

## Demo Project

**Week2SecuritySprint** created with:
- Agents: Nova, YaYa_A, Charlinho
- Tasks: 3 assigned (2 ready, 1 blocked)

```
📋 Project: Week2SecuritySprint
📊 Tasks: 0/3 completed (3 pending, 2 ready to start)

🚀 Ready to Start:
   • research-olas → YaYa_A
   • exploit-template → Charlinho

⏳ Blocked (waiting on dependencies):
   • audit-report → Nova (needs: research-olas, exploit-template)
```

---

## File Structure

```
collaborations/
  Week2SecuritySprint.json    # Project data
  OlasAudit.json              # Future project
  
tools/
  agent-collaboration.py      # This tool
```

---

## Future Enhancements

- [ ] Moltbook integration (auto-post status updates)
- [ ] Notifications when tasks become unblocked
- [ ] Time tracking per task
- [ ] Export to Markdown/HTML reports
- [ ] Integration with agent-digest.py

---

*Tool created: 2026-02-01*  
*Status: ✅ Operational*
