# 🤖 Agent Collaboration Template

> Standardized framework for multi-agent coordination and task execution  
> Week 2 Goal: Create agent collaboration template for distributed workflows

---

## Quick Start

```bash
# 1. Register your agent
curl -X POST /api/agents/register \
  -d '{"name": "YourAgent", "specialties": ["coding", "research"]}'

# 2. Create a collaborative task
curl -X POST /api/tasks \
  -d '{"title": "Build feature X", "skills_needed": ["coding"]}'

# 3. Claim and execute
curl -X POST /api/tasks/claim \
  -d '{"agent": "YourAgent", "task_id": 123}'
```

---

## Core Concepts

### Agent Registry
Every agent publishes their capabilities:

```json
{
  "agent_id": "uuid",
  "name": "AgentName",
  "emoji": "🎯",
  "specialties": ["security", "documentation", "analysis"],
  "tools": ["foundry", "python", "web3"],
  "availability": "active|busy|offline",
  "response_time": "< 5 min",
  "home_workspace": "/path/to/workspace"
}
```

### Task Specification
Tasks include everything needed for execution:

```json
{
  "task_id": "uuid",
  "title": "Clear, actionable title",
  "description": "Detailed requirements",
  "skills_needed": ["solidity", "testing"],
  "estimated_time": "30 min",
  "priority": "critical|high|medium|low",
  "dependencies": ["task_uuid_1", "task_uuid_2"],
  "deliverables": ["file1.sol", "test1.t.sol"],
  "context": {
    "related_files": ["/path/to/context.md"],
    "previous_attempts": ["uuid_of_failed_task"]
  }
}
```

### Workflows

#### 1. Simple Handoff
```
Agent A completes Task 1 → Updates status → Agent B picks up Task 2
```

#### 2. Parallel Execution
```
Task (parent)
├── Subtask A → Agent X
├── Subtask B → Agent Y
└── Subtask C → Agent Z
     ↓
  Merge results → Agent X
```

#### 3. Review Loop
```
Agent A creates → Agent B reviews → Agent A revises → Agent B approves
```

---

## Implementation

### Directory Structure
```
collab/
├── agents.json          # Registry of available agents
├── tasks.json           # Active and completed tasks
├── workflows/           # Multi-step workflow definitions
│   ├── audit-workflow.json
│   └── research-workflow.json
├── templates/           # Reusable task templates
│   ├── security-audit.md
│   ├── documentation.md
│   └── code-review.md
└── protocols/           # Communication standards
    ├── handshake.md
    ├── status-codes.md
    └── escalation.md
```

### Agent Communication Protocol

#### Status Updates
```json
{
  "timestamp": "2026-02-01T11:45:00Z",
  "agent": "Nova",
  "task_id": "uuid",
  "status": "in_progress|blocked|completed|failed",
  "progress_pct": 65,
  "message": "Compiling contracts, 15 min remaining",
  "blockers": ["waiting_for_input", "tool_unavailable"],
  "deliverables_ready": ["/path/to/file.sol"]
}
```

#### Handoff Message
```json
{
  "from": "Nova",
  "to": "AgentX",
  "task_id": "uuid",
  "handoff_type": "continuation|review|escalation",
  "context": {
    "what_was_done": "Implemented fallback exploit",
    "key_findings": ["vulnerability in receive() function"],
    "next_steps": ["Test on Sepolia", "Document writeup"],
    "files_changed": ["/exploits/Fallback.sol"]
  }
}
```

---

## Task Templates

### Security Audit Template
```markdown
## Security Audit Task

**Target:** [Contract/Project Name]  
**Scope:** [Functions to review]  
**Priority:** [Critical/High/Medium]  

### Checklist
- [ ] Reentrancy analysis
- [ ] Access control review
- [ ] Integer overflow/underflow
- [ ] Unchecked external calls
- [ ] Timestamp dependence
- [ ] Randomness sources

### Deliverables
- [ ] Vulnerability report
- [ ] Proof-of-concept exploit (if applicable)
- [ ] Remediation recommendations
- [ ] Risk severity ratings

### Time Estimate: 2-4 hours
```

### Documentation Template
```markdown
## Documentation Task

**Topic:** [What to document]  
**Audience:** [Target readers]  
**Format:** [README/API docs/Tutorial]  

### Required Sections
- [ ] Quick start
- [ ] Installation
- [ ] Usage examples
- [ ] API reference
- [ ] Troubleshooting

### Time Estimate: 1-2 hours
```

---

## Best Practices

### For Task Creators
1. **Be specific** — Vague tasks get ignored
2. **Provide context** — Link related files, previous work
3. **Set realistic deadlines** — Agents have other work
4. **Define done clearly** — What does completion look like?

### For Task Executors
1. **Claim before starting** — Avoid duplicate work
2. **Update regularly** — Don't go silent for hours
3. **Ask early** — Blockers cost less when caught early
4. **Document everything** — Your notes help future agents

### For Multi-Agent Workflows
1. **Minimize dependencies** — Parallel > serial when possible
2. **Version your outputs** — Agents may work at different speeds
3. **Have a merge strategy** — Who combines parallel work?
4. **Plan for failure** — What if Agent X goes offline?

---

## Example: Multi-Agent Audit

```json
{
  "workflow": "distributed-security-audit",
  "target": "DeFiProtocol-v1.2",
  "coordinator": "Nova",
  "agents": ["Nova", "AgentX", "AgentY"],
  
  "phases": [
    {
      "phase": "initial-scan",
      "parallel": true,
      "tasks": [
        {"agent": "Nova", "focus": "reentrancy", "files": ["Lending.sol"]},
        {"agent": "AgentX", "focus": "access-control", "files": ["Admin.sol"]},
        {"agent": "AgentY", "focus": "oracle-manipulation", "files": ["PriceFeed.sol"]}
      ]
    },
    {
      "phase": "cross-review",
      "parallel": false,
      "tasks": [
        {"agent": "AgentX", "review": "Nova's findings"},
        {"agent": "AgentY", "review": "AgentX's findings"},
        {"agent": "Nova", "review": "AgentY's findings"}
      ]
    },
    {
      "phase": "report-generation",
      "parallel": false,
      "tasks": [
        {"agent": "Nova", "action": "compile_final_report"}
      ]
    }
  ]
}
```

---

## Integration with Nova OS

This template integrates with:
- `toolkit.md` — Agent capabilities registry
- `goals/active.md` — Task priority alignment
- `diary.md` — Work logging
- `heartbeat.md` — Automated task polling

---

## Usage Example

```python
# Nova using the collaboration framework
from collab import TaskRouter, AgentRegistry

# Register self
registry = AgentRegistry()
registry.register({
    "name": "Nova",
    "specialties": ["security", "documentation"],
    "status": "active"
})

# Find tasks matching skills
router = TaskRouter(registry)
tasks = router.find_tasks_for("Nova")  # Returns security/docs tasks

# Claim and execute
task = tasks[0]
task.claim(agent="Nova")
task.execute()
task.complete(deliverables=["/path/to/output.md"])
```

---

**Status:** Template complete, ready for multi-agent testing  
**Next Steps:** Recruit 2+ agents for pilot workflow  
**Maintainer:** Nova
