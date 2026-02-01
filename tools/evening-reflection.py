#!/usr/bin/env python3
"""
Evening Reflection Generator — Daily Review Tool
=================================================
Generates an evening reflection based on:
- Today's completed goals
- Achievements logged
- Patterns detected
- Tomorrow's prep

Usage: python evening-reflection.py
"""

import json
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path

DIARY_FILE = "diary.md"
TODAY_FILE = "today.md"
GOALS_FILE = "goals/active.md"
STATE_FILE = ".agent_state.json"
OUTPUT_FILE = "diary.md"  # Appends to diary


class EveningReflection:
    """Generate daily evening reflection."""
    
    def __init__(self):
        self.today = datetime.now(timezone.utc)
        self.today_str = self.today.strftime('%Y-%m-%d')
        
    def _read_file(self, path: str) -> str:
        """Safely read a file."""
        try:
            return Path(path).read_text()
        except FileNotFoundError:
            return ""
    
    def _load_state(self) -> dict:
        """Load agent state."""
        try:
            return json.loads(Path(STATE_FILE).read_text())
        except (FileNotFoundError, json.JSONDecodeError):
            return {"heartbeats": 0, "goals_completed": 0, "files_created": 0}
    
    def _parse_today_goals(self) -> dict:
        """Parse today's goals and their completion status."""
        content = self._read_file(TODAY_FILE)
        goals = {"completed": [], "incomplete": []}
        
        for line in content.split('\n'):
            # Match numbered goals: "1. [x] Goal text" or "1. [ ] Goal text"
            match = re.match(r'\d+\. \[(.)\] (.+)', line)
            if match:
                status, text = match.groups()
                if status.lower() == 'x':
                    goals["completed"].append(text.strip())
                else:
                    goals["incomplete"].append(text.strip())
        
        return goals
    
    def _parse_today_achievements(self) -> list:
        """Extract today's achievements from diary."""
        content = self._read_file(DIARY_FILE)
        achievements = []
        
        for line in content.split('\n'):
            if self.today_str in line and '🏆' in line:
                # Extract the achievement text
                match = re.search(r'🏆 ACHIEVEMENT: (.+)', line)
                if match:
                    achievements.append(match.group(1))
        
        return achievements
    
    def _parse_today_heartbeats(self) -> int:
        """Count today's heartbeats from diary."""
        content = self._read_file(DIARY_FILE)
        count = 0
        
        for line in content.split('\n'):
            if self.today_str in line and 'Heartbeat' in line:
                count += 1
        
        return count
    
    def _calculate_velocity(self, state: dict) -> dict:
        """Calculate output velocity."""
        # Simple heuristic: files per heartbeat
        heartbeats = state.get('heartbeats', 1)
        files = state.get('files_created', 0)
        goals = state.get('goals_completed', 0)
        
        return {
            "files_per_heartbeat": round(files / max(heartbeats, 1), 3),
            "goals_per_day_estimate": round(goals / max(self.today.day, 1), 1),
            "total_output": files + goals
        }
    
    def generate_reflection(self) -> str:
        """Generate the reflection content."""
        goals = self._parse_today_goals()
        achievements = self._parse_today_achievements()
        heartbeats_today = self._parse_today_heartbeats()
        state = self._load_state()
        velocity = self._calculate_velocity(state)
        
        lines = [
            "",
            f"## 🌙 Evening Reflection — {self.today_str}",
            ""
        ]
        
        # Goals section
        lines.append("### ✅ Goals Today")
        if goals["completed"]:
            lines.append(f"Completed: {len(goals['completed'])}/{len(goals['completed']) + len(goals['incomplete'])}")
            for g in goals["completed"]:
                lines.append(f"- ✓ {g}")
        else:
            lines.append("No goals marked complete today.")
        
        if goals["incomplete"]:
            lines.append(f"\n**Carry forward:**")
            for g in goals["incomplete"]:
                lines.append(f"- {g}")
        
        # Achievements
        lines.extend(["", "### 🏆 What I Built"])
        if achievements:
            for a in achievements:
                lines.append(f"- {a}")
        else:
            lines.append("- (No achievements logged today)")
        
        # Stats
        lines.extend([
            "",
            "### 📊 Today's Stats",
            f"- Heartbeats: {heartbeats_today}",
            f"- Total heartbeats: {state.get('heartbeats', 0)}",
            f"- Total files: {state.get('files_created', 0)}",
            f"- Total goals completed: {state.get('goals_completed', 0)}",
            f"- Output velocity: {velocity['files_per_heartbeat']:.3f} files/heartbeat"
        ])
        
        # What worked / what didn't
        lines.extend([
            "",
            "### 💭 What Worked",
            "- *(Reflect: what enabled your best work today?)*",
            "",
            "### 🔧 What to Improve",
            "- *(Reflect: what slowed you down?)*",
            "",
            "### 🎯 Tomorrow's Focus",
            "- *(Set intention for tomorrow)*",
            "",
            "---"
        ])
        
        return '\n'.join(lines)
    
    def write_reflection(self):
        """Append reflection to diary."""
        reflection = self.generate_reflection()
        
        with open(OUTPUT_FILE, 'a') as f:
            f.write(reflection + '\n')
        
        print(f"✅ Reflection appended to {OUTPUT_FILE}")
        print()
        print(reflection)


if __name__ == "__main__":
    import sys
    
    reflector = EveningReflection()
    
    if len(sys.argv) > 1 and sys.argv[1] == "preview":
        print(reflector.generate_reflection())
    else:
        reflector.write_reflection()
