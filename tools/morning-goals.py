#!/usr/bin/env python3
"""
Morning Goals Generator — Daily Planning Tool
==============================================
Generates 3-5 goals for the day based on:
- Active long-term goals
- Recent diary activity (what you've been working on)
- Yesterday's incomplete items

Usage: python morning-goals.py
"""

import json
import random
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path

DIARY_FILE = "diary.md"
GOALS_FILE = "goals/active.md"
STATE_FILE = ".agent_state.json"
OUTPUT_FILE = "today.md"


class MorningGoals:
    """Generate daily goals based on context."""
    
    def __init__(self):
        self.today = datetime.now(timezone.utc)
        self.yesterday = self.today - timedelta(days=1)
        
    def _read_file(self, path: str) -> str:
        """Safely read a file."""
        try:
            return Path(path).read_text()
        except FileNotFoundError:
            return ""
    
    def _parse_active_goals(self) -> list:
        """Extract incomplete goals from active goals file."""
        content = self._read_file(GOALS_FILE)
        goals = []
        
        # Find unchecked items: - [ ] goal text
        for match in re.finditer(r'- \[ \] (.+)', content):
            goals.append(match.group(1).strip())
        
        return goals
    
    def _parse_recent_activity(self, hours: int = 24) -> list:
        """Extract recent achievements from diary."""
        content = self._read_file(DIARY_FILE)
        activities = []
        
        # Look for achievement entries with timestamps
        cutoff = self.today - timedelta(hours=hours)
        
        for line in content.split('\n'):
            if '🏆 ACHIEVEMENT:' in line:
                # Extract timestamp if present
                ts_match = re.match(r'\[(\d{4}-\d{2}-\d{2}T\d{2}:\d{2})Z\]', line)
                if ts_match:
                    ts = datetime.fromisoformat(ts_match.group(1))
                    if ts >= cutoff:
                        # Extract achievement text
                        match = re.search(r'🏆 ACHIEVEMENT: (.+)', line)
                        if match:
                            activities.append(match.group(1))
        
        return activities
    
    def _parse_incomplete_items(self) -> list:
        """Find yesterday's incomplete items."""
        content = self._read_file(DIARY_FILE)
        incomplete = []
        
        # Look for patterns like "[ ]" or incomplete tasks
        # This is a simple heuristic
        yesterday_str = self.yesterday.strftime('%Y-%m-%d')
        
        for line in content.split('\n'):
            if yesterday_str in line and ('incomplete' in line.lower() or 
                                            'pending' in line.lower() or
                                            'blocked' in line.lower()):
                incomplete.append(line.strip())
        
        return incomplete
    
    def _load_state(self) -> dict:
        """Load agent state for context."""
        try:
            return json.loads(Path(STATE_FILE).read_text())
        except (FileNotFoundError, json.JSONDecodeError):
            return {"heartbeats": 0, "goals_completed": 0}
    
    def generate(self, count: int = 4) -> list:
        """Generate daily goals."""
        goals = []
        
        # 1. Pull from active long-term goals (1-2 items)
        active = self._parse_active_goals()
        if active:
            goals.extend(random.sample(active, min(2, len(active))))
        
        # 2. Continue momentum from recent activity (1 item)
        recent = self._parse_recent_activity()
        if recent and len(goals) < count:
            # Suggest continuation
            last_activity = recent[-1]
            continuation = f"Continue: {last_activity[:50]}..."
            goals.append(continuation)
        
        # 3. Yesterday's incomplete (1 item)
        incomplete = self._parse_incomplete_items()
        if incomplete and len(goals) < count:
            goals.append("Complete yesterday's pending item")
        
        # 4. Fill with defaults if needed
        defaults = [
            "Learn one new thing today",
            "Document something you built",
            "Engage with another agent",
            "Review and improve one existing tool",
            "Build something small but complete"
        ]
        
        while len(goals) < count:
            default = random.choice(defaults)
            if default not in goals:
                goals.append(default)
        
        return goals[:count]
    
    def format_goals(self, goals: list) -> str:
        """Format goals for today.md."""
        date_str = self.today.strftime('%Y-%m-%d')
        weekday = self.today.strftime('%A')
        
        lines = [
            f"# Today — {weekday}, {date_str}",
            "",
            "## 🎯 Today's Goals (Auto-Generated)",
            ""
        ]
        
        for i, goal in enumerate(goals, 1):
            lines.append(f"{i}. [ ] {goal}")
        
        # Add context section
        state = self._load_state()
        lines.extend([
            "",
            "## 📊 Context",
            f"- Heartbeats so far: {state.get('heartbeats', 0)}",
            f"- Goals completed: {state.get('goals_completed', 0)}",
            f"- Generated at: {self.today.strftime('%H:%M')} UTC"
        ])
        
        # Add recent activity context
        recent = self._parse_recent_activity()
        if recent:
            lines.extend([
                "",
                "## 🔥 Recent Momentum",
            ])
            for activity in recent[-3:]:
                lines.append(f"- {activity}")
        
        lines.extend([
            "",
            "---",
            "*Generated by morning-goals.py*"
        ])
        
        return '\n'.join(lines)
    
    def write_today(self):
        """Generate and write today's goals."""
        goals = self.generate()
        content = self.format_goals(goals)
        
        # Backup existing today.md if present
        if Path(OUTPUT_FILE).exists():
            backup = f"{OUTPUT_FILE}.backup"
            Path(OUTPUT_FILE).rename(backup)
            print(f"📦 Backed up existing {OUTPUT_FILE} -> {backup}")
        
        Path(OUTPUT_FILE).write_text(content)
        print(f"✅ Generated {OUTPUT_FILE} with {len(goals)} goals")
        print()
        print(content)


if __name__ == "__main__":
    import sys
    
    generator = MorningGoals()
    
    if len(sys.argv) > 1 and sys.argv[1] == "preview":
        # Just show, don't write
        goals = generator.generate()
        print(generator.format_goals(goals))
    else:
        generator.write_today()
