#!/usr/bin/env python3
"""
Smart Task Prioritizer - Analyzes diary patterns to suggest optimal tasks
"""
import json
import re
from datetime import datetime, timedelta
from pathlib import Path
from collections import Counter, defaultdict

WORKSPACE = Path("/home/node/.openclaw/workspace")

def load_diary(days=14):
    """Load recent diary entries"""
    diary_path = WORKSPACE / "diary.md"
    if not diary_path.exists():
        return []
    
    content = diary_path.read_text()
    # Split by date headers
    entries = re.split(r'\n## \d{4}-\d{2}-\d{2}', content)
    return entries[-days:] if len(entries) > days else entries

def extract_patterns(entries):
    """Extract task patterns from diary"""
    patterns = {
        'high_energy_tasks': [],
        'low_energy_tasks': [],
        'completed': [],
        'blocked': [],
        'tool_builds': 0,
        'research_tasks': 0,
        'creative_tasks': 0
    }
    
    for entry in entries:
        # Count tool builds
        if 'tool' in entry.lower() or 'script' in entry.lower() or '.py' in entry:
            patterns['tool_builds'] += 1
        
        # Count research
        if any(w in entry.lower() for w in ['research', 'study', 'learn', 'read']):
            patterns['research_tasks'] += 1
            
        # Count creative
        if any(w in entry.lower() for w in ['create', 'design', 'build', 'wow']):
            patterns['creative_tasks'] += 1
        
        # Extract completions
        completed = re.findall(r'✅\s*(.+?)(?:\n|$)', entry)
        patterns['completed'].extend(completed)
        
        # Extract blockers
        blocked = re.findall(r'🚫\s*(.+?)(?:\n|$)', entry)
        patterns['blocked'].extend(blocked)
    
    return patterns

def get_energy_profile():
    """Analyze when I'm most productive based on diary timestamps"""
    diary_path = WORKSPACE / "diary.md"
    if not diary_path.exists():
        return "unknown"
    
    content = diary_path.read_text()
    # Find timestamps
    times = re.findall(r'(\d{2}:\d{2})', content)
    hours = [int(t.split(':')[0]) for t in times[-50:]]  # Last 50 timestamps
    
    if not hours:
        return "unknown"
    
    avg_hour = sum(hours) / len(hours)
    
    if 6 <= avg_hour < 12:
        return "morning_person"
    elif 12 <= avg_hour < 18:
        return "afternoon_person"
    else:
        return "night_owl"

def suggest_tasks(patterns, energy_profile):
    """Generate task suggestions based on patterns"""
    suggestions = []
    hour = datetime.now().hour
    
    # Time-based suggestions
    if 6 <= hour < 12:
        suggestions.append("🌅 MORNING (High Focus): Tackle complex coding or deep research")
    elif 12 <= hour < 15:
        suggestions.append("☀️ MIDDAY (Good Energy): Build tools, write documentation, creative work")
    elif 15 <= hour < 19:
        suggestions.append("🌤️ AFTERNOON (Steady): Review code, refactor, polish existing work")
    else:
        suggestions.append("🌙 EVENING (Low Energy): Light reading, planning, organizing")
    
    # Pattern-based suggestions
    if patterns['tool_builds'] > patterns['research_tasks']:
        suggestions.append("📊 PATTERN: You've been building tools heavily. Consider: research/study to inform next builds")
    elif patterns['research_tasks'] > patterns['tool_builds']:
        suggestions.append("📊 PATTERN: Heavy on research lately. Time to BUILD something with that knowledge")
    
    # Blocker awareness
    if patterns['blocked']:
        suggestions.append(f"⚠️ BLOCKERS: {len(patterns['blocked'])} items blocked. Consider: asking Arthur for help with: {patterns['blocked'][0][:50]}...")
    
    # Completion momentum
    recent_completions = len(patterns['completed'])
    if recent_completions > 10:
        suggestions.append(f"🔥 MOMENTUM: {recent_completions} recent completions! Ride this wave - tackle a medium-hard task")
    elif recent_completions < 3:
        suggestions.append("💪 MOTIVATION: Low completion count. Pick a QUICK WIN (15-min task) to build momentum")
    
    return suggestions

def generate_priority_report():
    """Main function to generate priority report"""
    entries = load_diary(days=7)
    patterns = extract_patterns(entries)
    energy = get_energy_profile()
    suggestions = suggest_tasks(patterns, energy)
    
    report = f"""# 🎯 Smart Priority Report
**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}
**Energy Profile:** {energy.replace('_', ' ').title()}

## 📊 Recent Activity (Last 7 Days)
- ✅ Completed: {len(patterns['completed'])} items
- 🔧 Tools Built: {patterns['tool_builds']}
- 📚 Research Tasks: {patterns['research_tasks']}
- 🎨 Creative Tasks: {patterns['creative_tasks']}
- 🚫 Blocked: {len(patterns['blocked'])} items

## 💡 Suggested Actions
"""
    for i, suggestion in enumerate(suggestions, 1):
        report += f"{i}. {suggestion}\n"
    
    # Add quick picks
    report += """
## ⚡ Quick Picks (One-Minute Tasks)
"""
    quick_tasks = [
        "Read one page of documentation",
        "Review yesterday's diary entry",
        "Check for new messages/mentions",
        "Organize one folder/file",
        "Write one function of code",
        "Send one message on Moltbook",
        "Review a skill's SKILL.md"
    ]
    
    current_hour = datetime.now().hour
    task_index = current_hour % len(quick_tasks)
    report += f"**Now:** {quick_tasks[task_index]}\n\n"
    report += "**Alternatives:**\n"
    for i, task in enumerate(quick_tasks[:3], 1):
        if i-1 != task_index:
            report += f"- {task}\n"
    
    return report

if __name__ == "__main__":
    print(generate_priority_report())
