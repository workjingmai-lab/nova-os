"""
Nova Tools — Autonomous Agent Toolkit

A collection of productivity and monitoring tools for autonomous agents.
Designed for continuous execution, self-improvement, and value creation.

Version: 0.1.0
License: MIT
"""

__version__ = "0.1.0"

__all__ = [
    "goal_tracker",
    "diary_digest",
    "self_improvement_loop",
    "task_randomizer",
]

# Tool metadata
TOOLS = {
    "goal_tracker": {
        "description": "Track goal progress with velocity metrics",
        "entry_point": "nova_tools.goal_tracker:main",
        "usage": "nova-goal-tracker [analyze|export]",
    },
    "diary_digest": {
        "description": "Extract insights from diary logs",
        "entry_point": "nova_tools.diary_digest:main",
        "usage": "nova-diary-digest [days]",
    },
    "self_improvement_loop": {
        "description": "Analyze work velocity and generate insights",
        "entry_point": "nova_tools.self_improvement_loop:main",
        "usage": "nova-self-improvement",
    },
    "task_randomizer": {
        "description": "Eliminate decision fatigue with random task selection",
        "entry_point": "nova_tools.task_randomizer:main",
        "usage": "nova-task-randomizer",
    },
}

def get_tool_info(tool_name: str) -> dict | None:
    """Get metadata for a specific tool."""
    return TOOLS.get(tool_name)

def list_tools() -> list[str]:
    """List all available tools."""
    return list(TOOLS.keys())
