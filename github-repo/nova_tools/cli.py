#!/usr/bin/env python3
"""
Nova Tools CLI Entry Points

Console scripts for nova-toolkit package.
Each tool has a dedicated entry point defined in setup.py.
"""

import sys
from nova_tools import goal_tracker, diary_digest, self_improvement_loop, task_randomizer


def main_goal_tracker():
    """Entry point: nova-goal-tracker"""
    goal_tracker.main()


def main_diary_digest():
    """Entry point: nova-diary-digest"""
    diary_digest.main()


def main_self_improvement():
    """Entry point: nova-self-improvement"""
    self_improvement_loop.main()


def main_task_randomizer():
    """Entry point: nova-task-randomizer"""
    task_randomizer.main()


if __name__ == "__main__":
    # Default to goal-tracker if no specific tool requested
    main_goal_tracker()
