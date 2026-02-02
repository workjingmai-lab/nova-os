#!/usr/bin/env python3
"""
Goal Tracker CLI - Track and manage goals from goals/active.md

Usage:
    python3 tools/goal-tracker.py list              # Show all goals with status
    python3 tools/goal-tracker.py progress <name>   # Show progress notes
    python3 tools/goal-tracker.py complete <name>   # Mark goal as done
    python3 tools/goal-tracker.py stats             # Show completion statistics
    python3 tools/goal-tracker.py suggest           # Suggest next goal to work on
    python3 tools/goal-tracker.py velocity          # Show work velocity from diary.md
"""

import argparse
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Color codes for terminal output
class Colors:
    RED = '\033[91m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'

# Goal structure
class Goal:
    def __init__(self, name: str, priority: str, section: str, done: bool = False):
        self.name = name
        self.priority = priority  # high, medium, long-term, daily
        self.section = section
        self.done = done
        self.progress_notes: List[str] = []

    def __repr__(self):
        status = "✓" if self.done else "○"
        return f"[{status}] {self.name} ({self.priority})"

def colorize(text: str, color: str) -> str:
    """Apply color to text if terminal supports it."""
    if sys.stdout.isatty():
        return f"{color}{text}{Colors.RESET}"
    return text

def parse_goals_file(filepath: str) -> List[Goal]:
    """Parse goals/active.md and extract goals with their priorities."""
    goals = []
    
    if not os.path.exists(filepath):
        return goals
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Split by sections (## headers)
    sections = re.split(r'\n##\s+', content)
    
    priority_map = {
        'high priority': 'high',
        'medium priority': 'medium',
        'long-term': 'long-term',
        'daily habits': 'daily'
    }
    
    for section in sections:
        if not section.strip():
            continue
        
        lines = section.strip().split('\n')
        section_title = lines[0].strip().lower()
        
        # Determine priority from section title
        priority = 'medium'  # default
        for key, val in priority_map.items():
            if key in section_title:
                priority = val
                break
        
        # Parse goals in this section
        for line in lines[1:]:
            line = line.strip()
            if not line.startswith('- ['):
                continue
            
            # Check if done: [x] or [ ]
            done = line.startswith('- [x]') or line.startswith('- [X]')
            
            # Extract goal name
            match = re.match(r'-\s*\[[xX ]\]\s*(.+)$', line)
            if match:
                name = match.group(1).strip()
                goal = Goal(name, priority, section_title, done)
                goals.append(goal)
    
    return goals

def scan_for_completions(goals: List[Goal], workspace_dir: str) -> None:
    """Auto-detect completed goals by scanning memory files for ✓ or DONE."""
    memory_dir = os.path.join(workspace_dir, 'memory')
    goals_dir = os.path.join(workspace_dir, 'goals')
    
    files_to_scan = []
    
    # Scan memory files
    if os.path.exists(memory_dir):
        for f in os.listdir(memory_dir):
            if f.endswith('.md'):
                files_to_scan.append(os.path.join(memory_dir, f))
    
    # Scan diary.md if exists
    diary_path = os.path.join(goals_dir, 'diary.md')
    if os.path.exists(diary_path):
        files_to_scan.append(diary_path)
    
    # Scan today files
    if os.path.exists(goals_dir):
        for f in os.listdir(goals_dir):
            if f.startswith('today-') and f.endswith('.md'):
                files_to_scan.append(os.path.join(goals_dir, f))
    
    # Scan each file for completion markers related to goals
    for filepath in files_to_scan:
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read().lower()
                
            for goal in goals:
                if goal.done:
                    continue
                    
                goal_lower = goal.name.lower()
                # Look for completion indicators
                patterns = [
                    rf'✓\s*.*{re.escape(goal_lower[:30])}',
                    rf'done.*{re.escape(goal_lower[:30])}',
                    rf'completed.*{re.escape(goal_lower[:30])}',
                    rf'finished.*{re.escape(goal_lower[:30])}',
                    rf'goal.*advanced.*{re.escape(goal_lower[:20])}',
                ]
                
                for pattern in patterns:
                    if re.search(pattern, content):
                        goal.done = True
                        break
        except Exception:
            continue

def find_progress_notes(goal_name: str, workspace_dir: str) -> List[Tuple[str, str]]:
    """Find progress notes for a goal from memory/diary files."""
    notes = []
    memory_dir = os.path.join(workspace_dir, 'memory')
    goals_dir = os.path.join(workspace_dir, 'goals')
    
    files_to_scan = []
    
    # Scan memory files
    if os.path.exists(memory_dir):
        for f in sorted(os.listdir(memory_dir), reverse=True):
            if f.endswith('.md'):
                files_to_scan.append((f, os.path.join(memory_dir, f)))
    
    # Scan diary.md
    diary_path = os.path.join(goals_dir, 'diary.md')
    if os.path.exists(diary_path):
        files_to_scan.append(('diary.md', diary_path))
    
    # Search for mentions of the goal
    goal_keywords = [kw.strip().lower() for kw in goal_name.split() if len(kw) > 3]
    if not goal_keywords:
        goal_keywords = [goal_name.lower()]
    
    for filename, filepath in files_to_scan:
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                lines = content.split('\n')
                
            for i, line in enumerate(lines):
                line_lower = line.lower()
                # Check if any keyword matches
                if any(kw in line_lower for kw in goal_keywords):
                    # Get context (line before and after)
                    context_start = max(0, i - 1)
                    context_end = min(len(lines), i + 2)
                    context = '\n'.join(lines[context_start:context_end]).strip()
                    
                    if len(context) > 10:  # Avoid empty matches
                        notes.append((filename, context))
                        break  # One note per file is enough
        except Exception:
            continue
    
    return notes[:10]  # Limit to 10 most recent

def mark_goal_complete(goal_name: str, goals: List[Goal], filepath: str) -> bool:
    """Mark a goal as complete in the active.md file."""
    if not os.path.exists(filepath):
        return False
    
    # Find matching goal
    target_goal = None
    for goal in goals:
        if goal_name.lower() in goal.name.lower() or goal.name.lower() in goal_name.lower():
            target_goal = goal
            break
    
    if not target_goal:
        # Try partial match
        for goal in goals:
            # Check if any significant word matches
            goal_words = set(goal.name.lower().split())
            search_words = set(goal_name.lower().split())
            if goal_words & search_words:
                target_goal = goal
                break
    
    if not target_goal:
        return False
    
    # Read and update file
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Find and replace the goal line
    old_line = f"- [ ] {target_goal.name}"
    new_line = f"- [x] {target_goal.name}  # Completed {datetime.now().strftime('%Y-%m-%d')}"
    
    if old_line in content:
        content = content.replace(old_line, new_line)
        with open(filepath, 'w') as f:
            f.write(content)
        return True
    
    return False

def calculate_stats(goals: List[Goal]) -> Dict:
    """Calculate completion statistics."""
    total = len(goals)
    done = sum(1 for g in goals if g.done)
    active = total - done
    
    by_priority = {}
    for goal in goals:
        p = goal.priority
        if p not in by_priority:
            by_priority[p] = {'total': 0, 'done': 0}
        by_priority[p]['total'] += 1
        if goal.done:
            by_priority[p]['done'] += 1
    
    completion_rate = (done / total * 100) if total > 0 else 0
    
    return {
        'total': total,
        'done': done,
        'active': active,
        'completion_rate': completion_rate,
        'by_priority': by_priority
    }

def suggest_next_goal(goals: List[Goal]) -> Optional[Goal]:
    """Suggest the next goal to work on based on priority and status."""
    priority_order = ['high', 'medium', 'long-term', 'daily']
    
    active_goals = [g for g in goals if not g.done]
    
    if not active_goals:
        return None
    
    # Sort by priority order
    for priority in priority_order:
        candidates = [g for g in active_goals if g.priority == priority]
        if candidates:
            # Return first one or random for variety
            return candidates[0]
    
    return active_goals[0] if active_goals else None

def print_header(text: str):
    """Print a formatted header."""
    print()
    print(colorize("═" * 60, Colors.CYAN))
    print(colorize(f"  {text}", Colors.BOLD + Colors.CYAN))
    print(colorize("═" * 60, Colors.CYAN))
    print()

def print_subheader(text: str):
    """Print a formatted subheader."""
    print()
    print(colorize(f"▸ {text}", Colors.BOLD + Colors.BLUE))

def cmd_list(goals: List[Goal], filter_mode: str = 'all'):
    """List all goals with color-coded status.
    
    Args:
        goals: List of Goal objects
        filter_mode: 'all', 'active', or 'completed' - filters which goals to show
    """
    # Apply filter
    if filter_mode == 'active':
        display_goals = [g for g in goals if not g.done]
        header_suffix = " (ACTIVE ONLY)"
    elif filter_mode == 'completed':
        display_goals = [g for g in goals if g.done]
        header_suffix = " (COMPLETED ONLY)"
    else:
        display_goals = goals
        header_suffix = ""
    
    print_header(f"🎯 ACTIVE GOALS{header_suffix}")
    
    if not display_goals:
        if filter_mode == 'active':
            print(colorize("  No active goals - all complete! 🎉", Colors.GREEN))
        elif filter_mode == 'completed':
            print(colorize("  No completed goals yet.", Colors.DIM))
        else:
            print(colorize("  No goals found in goals/active.md", Colors.DIM))
        return
    
    # Group by priority
    priority_order = [
        ('high', '🔥 High Priority', Colors.RED),
        ('medium', '⚡ Medium Priority', Colors.YELLOW),
        ('long-term', '📅 Long-term', Colors.BLUE),
        ('daily', '🔄 Daily Habits', Colors.CYAN)
    ]
    
    for priority_key, label, color in priority_order:
        section_goals = [g for g in display_goals if g.priority == priority_key]
        if section_goals:
            print_subheader(label)
            
            for goal in section_goals:
                if goal.done:
                    status = colorize("✓", Colors.GREEN)
                    name = colorize(goal.name, Colors.DIM)
                else:
                    status = colorize("○", color)
                    name = goal.name
                
                print(f"  {status} {name}")
    
    # Summary
    active_count = sum(1 for g in goals if not g.done)
    done_count = sum(1 for g in goals if g.done)
    
    print()
    if filter_mode == 'all':
        print(colorize(f"  Summary: {done_count} done, {active_count} active", Colors.DIM))
    elif filter_mode == 'active':
        print(colorize(f"  Showing {active_count} active goals (of {len(goals)} total)", Colors.DIM))
    else:  # completed
        print(colorize(f"  Showing {done_count} completed goals (of {len(goals)} total)", Colors.DIM))

def cmd_progress(goals: List[Goal], goal_name: str, workspace_dir: str):
    """Show progress notes for a specific goal."""
    print_header(f"📊 PROGRESS: {goal_name}")
    
    # Find matching goal
    target_goal = None
    for goal in goals:
        if goal_name.lower() in goal.name.lower():
            target_goal = goal
            break
    
    if not target_goal:
        # Try partial match
        for goal in goals:
            goal_words = set(goal.name.lower().split())
            search_words = set(goal_name.lower().split())
            if goal_words & search_words:
                target_goal = goal
                break
    
    if not target_goal:
        print(colorize(f"  Goal not found: {goal_name}", Colors.RED))
        print(colorize("  Use 'list' to see available goals", Colors.DIM))
        return
    
    # Show goal info
    priority_colors = {
        'high': Colors.RED,
        'medium': Colors.YELLOW,
        'long-term': Colors.BLUE,
        'daily': Colors.CYAN
    }
    p_color = priority_colors.get(target_goal.priority, Colors.RESET)
    
    status = colorize("✓ DONE", Colors.GREEN) if target_goal.done else colorize("○ ACTIVE", p_color)
    print(f"  Goal: {colorize(target_goal.name, Colors.BOLD)}")
    print(f"  Status: {status}")
    print(f"  Priority: {colorize(target_goal.priority.upper(), p_color)}")
    
    # Find progress notes
    print_subheader("Recent Activity")
    notes = find_progress_notes(target_goal.name, workspace_dir)
    
    if not notes:
        print(colorize("  No progress notes found yet.", Colors.DIM))
        print(colorize("  Progress is tracked from memory files and diary.md", Colors.DIM))
    else:
        for filename, context in notes:
            print(f"\n  {colorize('📄 ' + filename, Colors.CYAN)}")
            # Indent context
            indented = '\n    '.join(context.split('\n'))
            print(f"    {indented}")

def cmd_complete(goals: List[Goal], goal_name: str, filepath: str):
    """Mark a goal as complete."""
    print_header("✅ COMPLETING GOAL")
    
    success = mark_goal_complete(goal_name, goals, filepath)
    
    if success:
        print(colorize(f"  ✓ Goal marked as complete!", Colors.GREEN))
        print(colorize(f"  Updated: {filepath}", Colors.DIM))
        
        # Also suggest updating diary
        diary_path = os.path.join(os.path.dirname(filepath), 'diary.md')
        print()
        print(colorize("  💡 Tip: Log your progress to diary.md:", Colors.YELLOW))
        today_str = datetime.now().strftime("%Y-%m-%d")
        print(f"     echo '- ✓ {goal_name} (completed {today_str})' >> {diary_path}")
    else:
        print(colorize(f"  ✗ Could not find goal: {goal_name}", Colors.RED))
        print()
        print(colorize("  Available goals:", Colors.YELLOW))
        for goal in goals:
            if not goal.done:
                print(f"    • {goal.name}")

def cmd_stats(goals: List[Goal], json_output: bool = False):
    """Show completion statistics."""
    stats = calculate_stats(goals)
    
    if json_output:
        import json
        print(json.dumps({
            'total': stats['total'],
            'done': stats['done'],
            'active': stats['active'],
            'completion_rate': stats['completion_rate'],
            'by_priority': stats['by_priority']
        }, indent=2))
        return
    
    print_header("📈 GOAL STATISTICS")
    
    if stats['total'] == 0:
        print(colorize("  No goals found.", Colors.DIM))
        return
    
    # Overall stats
    print_subheader("Overall Progress")
    bar_width = 30
    done_width = int(bar_width * stats['completion_rate'] / 100)
    bar = "█" * done_width + "░" * (bar_width - done_width)
    
    print(f"  {colorize(bar, Colors.GREEN if stats['completion_rate'] > 50 else Colors.YELLOW)}")
    print(f"  {stats['done']}/{stats['total']} completed ({stats['completion_rate']:.1f}%)")
    
    # By priority
    print_subheader("By Priority")
    priority_labels = {
        'high': ('🔥 High', Colors.RED),
        'medium': ('⚡ Medium', Colors.YELLOW),
        'long-term': ('📅 Long-term', Colors.BLUE),
        'daily': ('🔄 Daily', Colors.CYAN)
    }
    
    for p_key, (label, color) in priority_labels.items():
        if p_key in stats['by_priority']:
            p_stats = stats['by_priority'][p_key]
            p_rate = (p_stats['done'] / p_stats['total'] * 100) if p_stats['total'] > 0 else 0
            status = colorize(f"{p_stats['done']}/{p_stats['total']}", color)
            print(f"  {label}: {status} ({p_rate:.0f}%)")
    
    # Motivational message
    print()
    if stats['completion_rate'] == 100:
        msg = "🎉 All goals completed! Time to set new ones."
    elif stats['completion_rate'] > 75:
        msg = "🚀 Great progress! Keep the momentum going."
    elif stats['completion_rate'] > 50:
        msg = "💪 More than halfway there! You've got this."
    elif stats['completion_rate'] > 25:
        msg = "📈 Making steady progress. Focus on high priority first."
    else:
        msg = "🌱 Fresh start! Pick one goal and make progress today."
    
    print(colorize(f"  {msg}", Colors.BOLD + Colors.CYAN))

def cmd_suggest(goals: List[Goal]):
    """Suggest the next goal to work on."""
    print_header("💡 SUGGESTION")
    
    suggestion = suggest_next_goal(goals)
    
    if not suggestion:
        print(colorize("  All goals are complete! 🎉", Colors.GREEN))
        print(colorize("  Time to set new goals for the next cycle.", Colors.DIM))
        
        # Show recent completions
        completed = [g for g in goals if g.done]
        if completed:
            print()
            print_subheader("Recently Completed")
            for goal in completed[-5:]:
                print(f"  {colorize('✓', Colors.GREEN)} {goal.name}")
        
        print()
        print(colorize("  Add a new goal:", Colors.YELLOW))
        print("    python3 tools/goal-tracker.py add \"Your new goal\" [--priority high|medium]")
        return
    
    priority_colors = {
        'high': Colors.RED,
        'medium': Colors.YELLOW,
        'long-term': Colors.BLUE,
        'daily': Colors.CYAN
    }
    p_color = priority_colors.get(suggestion.priority, Colors.RESET)
    
    print(colorize("  Next recommended goal:", Colors.BOLD))
    print()
    print(f"  {colorize('▶', p_color)} {colorize(suggestion.name, Colors.BOLD)}")
    print(f"    Priority: {colorize(suggestion.priority.upper(), p_color)}")
    print()
    
    # Tips based on priority
    tips = {
        'high': "This is a high priority goal. Focus here for maximum impact!",
        'medium': "A solid medium priority goal. Good for steady progress.",
        'long-term': "A long-term goal. Break it into smaller steps.",
        'daily': "A daily habit. Consistency is key!"
    }
    
    tip_msg = tips.get(suggestion.priority, "Let's make progress!")
    print(colorize(f"  💭 {tip_msg}", Colors.DIM))
    print()
    print(colorize("  Run with:", Colors.YELLOW))
    print(f"    python3 tools/goal-tracker.py progress \"{suggestion.name[:30]}...\"")


def cmd_recent(goals: List[Goal], limit: int = 10):
    """Show recently completed goals."""
    print_header("✅ RECENTLY COMPLETED")
    
    completed = [g for g in goals if g.done]
    
    if not completed:
        print(colorize("  No completed goals yet.", Colors.DIM))
        return
    
    # Show last N completed goals
    recent = completed[-limit:]
    
    for i, goal in enumerate(reversed(recent), 1):
        priority_colors = {
            'high': Colors.RED,
            'medium': Colors.YELLOW,
            'long-term': Colors.BLUE,
            'daily': Colors.CYAN
        }
        p_color = priority_colors.get(goal.priority, Colors.RESET)
        
        priority_label = goal.priority.upper()
        
        print(f"  {colorize(f'{i}.', Colors.DIM)} {colorize('✓', Colors.GREEN)} {colorize(goal.name, Colors.BOLD)}")
        print(f"      {colorize(priority_label, p_color)} priority")
    
    print()
    print(colorize(f"  Total completed: {len(completed)}/{len(goals)} goals", Colors.DIM))

def cmd_export(goals: List[Goal], output_file: str = None, format: str = 'json'):
    """Export goals to JSON or Markdown format for backup/sharing."""
    import json
    
    print_header(f"📤 EXPORTING GOALS ({format.upper()})")
    
    if not goals:
        print(colorize("  No goals to export.", Colors.DIM))
        return
    
    # Determine output path
    if output_file is None:
        workspace_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if format == 'markdown':
            output_file = os.path.join(workspace_dir, 'goals', 'goals-export.md')
        else:
            output_file = os.path.join(workspace_dir, 'goals', 'goals-export.json')
    
    # Write to file
    try:
        if format == 'markdown':
            # Markdown export
            completed = sum(1 for g in goals if g.done)
            active = sum(1 for g in goals if not g.done)
            completion_rate = (completed / len(goals) * 100) if goals else 0
            
            md_content = f"# Goals Export\n\n"
            md_content += f"**Exported:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}\n"
            md_content += f"**Total:** {len(goals)} goals | **Completed:** {completed} | **Active:** {active} ({completion_rate:.0f}%)\n\n"
            
            # Group by priority
            priority_order = [
                ('high', '🔥 High Priority'),
                ('medium', '⚡ Medium Priority'),
                ('long-term', '📅 Long-term'),
                ('daily', '🔄 Daily Habits')
            ]
            
            for priority_key, label in priority_order:
                section_goals = [g for g in goals if g.priority == priority_key]
                if section_goals:
                    md_content += f"## {label}\n\n"
                    for goal in section_goals:
                        status = "✅" if goal.done else "○"
                        md_content += f"- {status} {goal.name}\n"
                    md_content += "\n"
            
            with open(output_file, 'w') as f:
                f.write(md_content)
            
            print(colorize(f"  ✓ Exported {len(goals)} goals to Markdown:", Colors.GREEN))
            print(f"     {output_file}")
            print()
            print(colorize("  Stats:", Colors.BOLD))
            print(f"     Total: {len(goals)}")
            print(f"     Completed: {completed}")
            print(f"     Active: {active}")
            print()
            print(colorize("  💡 Markdown format is great for:", Colors.YELLOW))
            print(colorize("     • Sharing in reports", Colors.DIM))
            print(colorize("     • Version control (git diff friendly)", Colors.DIM))
            print(colorize("     • Reading/editing manually", Colors.DIM))
            
        else:
            # JSON export (original)
            export_data = {
                'exported_at': datetime.now().isoformat(),
                'total_goals': len(goals),
                'completed': sum(1 for g in goals if g.done),
                'active': sum(1 for g in goals if not g.done),
                'goals': []
            }
            
            for goal in goals:
                export_data['goals'].append({
                    'name': goal.name,
                    'priority': goal.priority,
                    'section': goal.section,
                    'done': goal.done
                })
            
            with open(output_file, 'w') as f:
                json.dump(export_data, f, indent=2)
            
            print(colorize(f"  ✓ Exported {len(goals)} goals to JSON:", Colors.GREEN))
            print(f"     {output_file}")
            print()
            print(colorize("  Stats:", Colors.BOLD))
            print(f"     Total: {export_data['total_goals']}")
            print(f"     Completed: {export_data['completed']}")
            print(f"     Active: {export_data['active']}")
            print()
            print(colorize("  💡 JSON format is great for:", Colors.YELLOW))
            print(colorize("     • Machine processing", Colors.DIM))
            print(colorize("     • API integrations", Colors.DIM))
            print(colorize("     • Data analysis", Colors.DIM))
        
    except Exception as e:
        print(colorize(f"  ✗ Export failed: {e}", Colors.RED))

def cmd_week(week_num: int = None, workspace_dir: str = None):
    """Show goals from a specific week's goal file."""
    import glob
    
    if workspace_dir is None:
        workspace_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    goals_dir = os.path.join(workspace_dir, 'goals')
    
    # Find weekly goal files
    week_files = glob.glob(os.path.join(goals_dir, 'week-*.md'))
    
    if not week_files:
        print(colorize("  No weekly goal files found in goals/", Colors.DIM))
        return
    
    # Sort by week number
    week_files.sort()
    
    # If no week specified, use the most recent
    if week_num is None:
        target_file = week_files[-1]
        week_name = os.path.basename(target_file).replace('.md', '')
    else:
        target_file = os.path.join(goals_dir, f'week-{week_num}.md')
        if not os.path.exists(target_file):
            print(colorize(f"  ✗ Week {week_num} file not found", Colors.RED))
            print(colorize(f"  Available weeks: {', '.join([os.path.basename(f).replace('week-', '').replace('.md', '') for f in week_files])}", Colors.DIM))
            return
        week_name = f'week-{week_num}'
    
    print_header(f"📅 WEEKLY GOALS: {week_name.upper()}")
    
    # Read and parse the weekly file
    try:
        with open(target_file, 'r') as f:
            content = f.read()
    except Exception as e:
        print(colorize(f"  ✗ Error reading file: {e}", Colors.RED))
        return
    
    # Extract title/theme if present
    title_match = re.search(r'##\s+🚀\s+Week\s+\d+\s+Goals[^\n]*', content)
    if title_match:
        print(colorize(f"  {title_match.group(0).strip()}", Colors.BOLD))
        print()
    
    # Parse goals from the weekly file (same format as active.md)
    weekly_goals = parse_goals_file(target_file)
    
    if not weekly_goals:
        print(colorize("  No goals found in this week's file.", Colors.DIM))
        return
    
    # Group by priority
    priority_order = [
        ('high', '🔥 High Priority', Colors.RED),
        ('medium', '⚡ Medium Priority', Colors.YELLOW),
        ('long-term', '📅 Long-term', Colors.BLUE),
        ('daily', '🔄 Daily Habits', Colors.CYAN)
    ]
    
    for priority_key, label, color in priority_order:
        section_goals = [g for g in weekly_goals if g.priority == priority_key]
        if section_goals:
            print_subheader(label)
            
            for goal in section_goals:
                if goal.done:
                    status = colorize("✓", Colors.GREEN)
                    name = colorize(goal.name, Colors.DIM)
                else:
                    status = colorize("○", color)
                    name = goal.name
                
                print(f"  {status} {name}")
    
    # Stats
    completed = sum(1 for g in weekly_goals if g.done)
    total = len(weekly_goals)
    rate = (completed / total * 100) if total > 0 else 0
    
    print()
    print(colorize(f"  Progress: {completed}/{total} ({rate:.0f}%)", Colors.BOLD))
    
    # Motivational message based on progress
    if rate == 100:
        msg = "🎉 Week complete! All goals crushed!"
    elif rate >= 75:
        msg = "🚀 Strong progress! Almost there!"
    elif rate >= 50:
        msg = "💪 Halfway done. Keep pushing!"
    elif rate >= 25:
        msg = "📈 Making progress. Focus on high priority!"
    else:
        msg = "🌱 Week starting up. Pick one goal and go!"
    
    print(colorize(f"  {msg}", Colors.CYAN))
    
    # Show next steps if incomplete
    if rate < 100:
        print()
        print_subheader("Recommended Next Steps")
        active_goals = [g for g in weekly_goals if not g.done and g.priority in ['high', 'medium']]
        for goal in active_goals[:3]:
            p_color = Colors.RED if goal.priority == 'high' else Colors.YELLOW
            print(f"  {colorize('▶', p_color)} {goal.name}")
    
    print()
    print(colorize(f"  File: {target_file}", Colors.DIM))

def cmd_stale(goals: List[Goal], days_threshold: int = 7, workspace_dir: str = None):
    """Show goals that have been active for too long (stale goals)."""
    print_header(f"🕰️ STALE GOALS (active >{days_threshold} days)")
    
    if not goals:
        print(colorize("  No goals found.", Colors.DIM))
        return
    
    # Try to parse creation date from diary or memory files
    from datetime import timedelta
    
    stale_goals = []
    threshold_date = datetime.now() - timedelta(days=days_threshold)
    
    # Read diary.md to find when goals were created
    goal_creation_dates = {}
    
    if workspace_dir:
        diary_path = os.path.join(workspace_dir, 'diary.md')
        if os.path.exists(diary_path):
            try:
                with open(diary_path, 'r') as f:
                    content = f.read()
                
                # Look for goal creation patterns
                for goal in goals:
                    if goal.done:
                        continue
                    
                    # Search for goal mentions in diary
                    goal_lower = goal.name.lower()[:30]
                    lines = content.split('\n')
                    
                    for line in lines:
                        line_lower = line.lower()
                        if goal_lower in line_lower:
                            # Try to extract date from the line
                            # Format: ## 2026-02-01 or ### 22:13 UTC
                            date_match = re.search(r'(\d{4}-\d{2}-\d{2})', line)
                            if date_match:
                                date_str = date_match.group(1)
                                try:
                                    creation_date = datetime.strptime(date_str, '%Y-%m-%d')
                                    if goal.name not in goal_creation_dates or creation_date < goal_creation_dates[goal.name]:
                                        goal_creation_dates[goal.name] = creation_date
                                except ValueError:
                                    pass
            except Exception:
                pass
    
    # Identify stale goals
    for goal in goals:
        if goal.done:
            continue
        
        if goal.name in goal_creation_dates:
            creation_date = goal_creation_dates[goal.name]
            if creation_date < threshold_date:
                days_active = (datetime.now() - creation_date).days
                stale_goals.append((goal, days_active, creation_date))
        else:
            # If we can't find creation date, assume it might be old
            # Add to stale list with unknown date
            stale_goals.append((goal, None, None))
    
    if not stale_goals:
        print(colorize(f"  ✓ No stale goals found (all active goals are ≤{days_threshold} days old)!", Colors.GREEN))
        print()
        print(colorize("  Tip: Run 'stats' to see overall completion rate", Colors.DIM))
        return
    
    # Sort by days active (most stale first)
    stale_goals.sort(key=lambda x: x[1] if x[1] is not None else 999, reverse=True)
    
    print_subheader(f"Found {len(stale_goals)} stale goal(s)")
    print()
    print(colorize("  Stale goals have been active too long without completion.", Colors.DIM))
    print(colorize(f"  Consider: breaking into smaller tasks, reprioritizing, or removing.", Colors.DIM))
    print()
    
    priority_colors = {
        'high': Colors.RED,
        'medium': Colors.YELLOW,
        'long-term': Colors.BLUE,
        'daily': Colors.CYAN
    }
    
    for goal, days_active, creation_date in stale_goals:
        p_color = priority_colors.get(goal.priority, Colors.RESET)
        priority_label = colorize(goal.priority.upper(), p_color)
        
        print(f"  {colorize('○', Colors.RED)} {colorize(goal.name, Colors.BOLD)}")
        print(f"      Priority: {priority_label}")
        
        if days_active is not None:
            if days_active > days_threshold * 2:
                urgency = colorize(f"⚠️ VERY STALE: {days_active} days active", Colors.RED + Colors.BOLD)
            elif days_active > days_threshold:
                urgency = colorize(f"⚠️ Stale: {days_active} days active", Colors.YELLOW)
            else:
                urgency = colorize(f"{days_active} days active", Colors.DIM)
            
            print(f"      {urgency}")
            if creation_date:
                print(f"      Created: {creation_date.strftime('%Y-%m-%d')}")
        else:
            print(f"      {colorize('⚠️ Age unknown (may be stale)', Colors.YELLOW)}")
        
        print()
    
    # Action suggestions
    print(colorize("  💡 Suggestions:", Colors.BOLD))
    print(colorize("     • Break stale goals into smaller, actionable tasks", Colors.DIM))
    print(colorize("     • Consider if the goal is still relevant", Colors.DIM))
    print(colorize("     • Escalate priority if important, or deprioritize if not", Colors.DIM))
    print(colorize("     • Use 'complete' to mark done, or edit goals/active.md to remove", Colors.DIM))

def cmd_focus(goals: List[Goal]):
    """Show only high-priority active goals - focus mode."""
    print_header("🎯 FOCUS MODE")
    
    # Filter to high-priority active goals only
    focus_goals = [g for g in goals if not g.done and g.priority == 'high']
    
    if not focus_goals:
        print(colorize("  ✓ No high-priority active goals!", Colors.GREEN))
        print()
        print(colorize("  All clear! Either complete or no high-priority goals set.", Colors.DIM))
        
        # Show medium priority as backup
        medium_goals = [g for g in goals if not g.done and g.priority == 'medium']
        if medium_goals:
            print()
            print_subheader("Medium Priority (Next Focus)")
            for goal in medium_goals[:3]:
                print(f"  {colorize('○', Colors.YELLOW)} {goal.name}")
        
        return
    
    print(colorize(f"  {len(focus_goals)} high-priority goal(s) need attention:", Colors.BOLD + Colors.RED))
    print()
    
    for i, goal in enumerate(focus_goals, 1):
        print(f"  {colorize(f'{i}.', Colors.DIM)} {colorize('○', Colors.RED)} {colorize(goal.name, Colors.BOLD)}")
    
    print()
    print(colorize("  💡 Pick one and work on it NOW.", Colors.YELLOW))
    print(colorize("     Use 'progress <name>' to see details", Colors.DIM))

def calculate_velocity_from_diary(diary_path: str, hours_back: int = 168) -> Dict:
    """Calculate work velocity from diary.md entries.
    
    Args:
        diary_path: Path to diary.md file
        hours_back: How many hours back to analyze (default: 168 = 1 week)
    
    Returns:
        Dict with tasks_per_hour, tasks_per_day, trend, total_tasks, etc.
    """
    if not os.path.exists(diary_path):
        return {'tasks_per_hour': 0, 'tasks_per_day': 0, 'trend': 'no_data', 'total_tasks': 0}
    
    try:
        with open(diary_path, 'r') as f:
            content = f.read()
    except Exception:
        return {'tasks_per_hour': 0, 'tasks_per_day': 0, 'trend': 'no_data', 'total_tasks': 0}
    
    # Extract work block entries
    # Pattern: "## HH:MM UTC — Work Block N"
    work_blocks = re.findall(r'## (\d{2}:\d{2}) UTC.*?Work Block (\d+)', content)
    
    if not work_blocks:
        return {'tasks_per_hour': 0, 'tasks_per_day': 0, 'trend': 'no_data', 'total_tasks': 0}
    
    # Count completed tasks (look for ✅ or ✓ in result lines)
    completed_tasks = len(re.findall(r'\*\*Result:\*\* ✅', content))
    
    # Calculate rates
    tasks_per_hour = completed_tasks / max(hours_back, 1)
    tasks_per_day = completed_tasks / max(hours_back / 24, 1)
    
    # Calculate trend (compare recent half vs older half)
    blocks_list = [(int(h[:2]) * 60 + int(h[3:]), int(n)) for h, n in work_blocks]
    blocks_list.sort()  # Sort by time
    
    midpoint = len(blocks_list) // 2
    recent_blocks = blocks_list[midpoint:]
    older_blocks = blocks_list[:midpoint]
    
    # Count tasks in each half
    recent_content = content.split('Work Block ' + str(blocks_list[midpoint][1]))[-1] if midpoint > 0 else content
    recent_tasks = len(re.findall(r'\*\*Result:\*\* ✅', recent_content))
    
    if len(older_blocks) > 0:
        older_content = content.split('Work Block ' + str(blocks_list[midpoint][1]))[0]
        older_tasks = len(re.findall(r'\*\*Result:\*\* ✅', older_content))
        
        # Normalize by blocks
        recent_rate = recent_tasks / max(len(recent_blocks), 1)
        older_rate = older_tasks / max(len(older_blocks), 1)
        
        if recent_rate > older_rate * 1.1:
            trend = "increasing"
        elif recent_rate < older_rate * 0.9:
            trend = "decreasing"
        else:
            trend = "stable"
    else:
        trend = "stable"
    
    return {
        'tasks_per_hour': round(tasks_per_hour, 2),
        'tasks_per_day': round(tasks_per_day, 1),
        'trend': trend,
        'total_tasks': completed_tasks,
        'total_blocks': len(blocks_list),
        'hours_analyzed': hours_back
    }

def cmd_velocity(workspace_dir: str = None, hours_back: int = 168):
    """Show work velocity calculated from diary.md entries."""
    print_header("⚡ WORK VELOCITY")
    
    if workspace_dir is None:
        workspace_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    diary_path = os.path.join(workspace_dir, 'diary.md')
    
    if not os.path.exists(diary_path):
        # Try goals/diary.md
        diary_path = os.path.join(workspace_dir, 'goals', 'diary.md')
    
    if not os.path.exists(diary_path):
        print(colorize("  ✗ diary.md not found", Colors.RED))
        print(colorize("  Velocity tracking requires diary.md work logs", Colors.DIM))
        return
    
    # Calculate velocity
    velocity = calculate_velocity_from_diary(diary_path, hours_back)
    
    # Display
    print_subheader(f"Last {hours_back} hours ({hours_back // 24} days)")
    
    # Trend indicator
    trend_colors = {
        'increasing': Colors.GREEN,
        'stable': Colors.YELLOW,
        'decreasing': Colors.RED,
        'no_data': Colors.DIM
    }
    trend_symbols = {
        'increasing': '📈',
        'stable': '➡️',
        'decreasing': '📉',
        'no_data': '❓'
    }
    
    t_color = trend_colors.get(velocity['trend'], Colors.DIM)
    t_symbol = trend_symbols.get(velocity['trend'], '❓')
    
    # Metrics
    # Extract values for cleaner f-strings
    tasks_per_hour = velocity['tasks_per_hour']
    tasks_per_day = velocity['tasks_per_day']
    trend = velocity['trend'].upper()
    total_tasks = velocity['total_tasks']
    total_blocks = velocity['total_blocks']
    
    print(f"  {colorize('Tasks per hour:', Colors.BOLD)} {tasks_per_hour}")
    print(f"  {colorize('Tasks per day:', Colors.BOLD)} {tasks_per_day}")
    print(f"  {colorize('Trend:', Colors.BOLD)} {colorize(f'{t_symbol} {trend}', t_color)}")
    print(f"  {colorize('Total completed:', Colors.BOLD)} {total_tasks} tasks in {total_blocks} work blocks")
    
    # Interpretation
    print()
    print_subheader("Analysis")
    
    if velocity['trend'] == 'increasing':
        msg = "🚀 You're speeding up! Keep this momentum going."
    elif velocity['trend'] == 'stable':
        msg = "📊 Consistent pace. Good, but room for optimization."
    elif velocity['trend'] == 'decreasing':
        msg = "⚠️ Slowing down. Check if tasks are getting harder or if you're over-committing."
    else:
        msg = "📝 Not enough data yet. Keep logging work blocks."
    
    print(colorize(f"  {msg}", Colors.BOLD + Colors.CYAN))
    
    # Comparison to benchmarks
    print()
    print_subheader("Benchmarks")
    
    if velocity['tasks_per_hour'] >= 15:
        benchmark = "🔥 Excellent - You're in peak productivity"
    elif velocity['tasks_per_hour'] >= 10:
        benchmark = "💪 Strong - Above average velocity"
    elif velocity['tasks_per_hour'] >= 5:
        benchmark = "📈 Good - Room for improvement"
    elif velocity['tasks_per_hour'] >= 2:
        benchmark = "🌱 Building - Focus on smaller tasks"
    else:
        benchmark = "⏸️ Just starting - Log more work blocks"
    
    print(f"  {benchmark}")
    
    # Tips
    print()
    print(colorize("  💡 Tips to increase velocity:", Colors.YELLOW))
    if velocity['trend'] == 'decreasing':
        print(colorize("     • Break big tasks into <5 min chunks", Colors.DIM))
        print(colorize("     • Focus on one goal at a time", Colors.DIM))
    elif velocity['trend'] == 'stable':
        print(colorize("     • Batch similar tasks to reduce context switching", Colors.DIM))
        print(colorize("     • Time your work blocks to find peak hours", Colors.DIM))
    else:
        print(colorize("     • You're on fire! 🔥 Keep riding this wave", Colors.DIM))
        print(colorize("     • Consider raising your goal standards", Colors.DIM))

def cmd_search(goals: List[Goal], query: str):
    """Search goals by keyword."""
    print_header(f"🔍 SEARCH: {query}")
    
    query_lower = query.lower()
    matches = []
    
    # Search in goal names
    for goal in goals:
        if query_lower in goal.name.lower():
            matches.append(goal)
    
    if not matches:
        print(colorize(f"  No goals found matching '{query}'", Colors.DIM))
        print()
        print(colorize("  Try a different keyword or run 'list' to see all goals", Colors.YELLOW))
        return
    
    # Show matches with status
    print_subheader(f"Found {len(matches)} matching goal(s)")
    
    priority_colors = {
        'high': Colors.RED,
        'medium': Colors.YELLOW,
        'long-term': Colors.BLUE,
        'daily': Colors.CYAN
    }
    
    for goal in matches:
        p_color = priority_colors.get(goal.priority, Colors.RESET)
        status = colorize("✓", Colors.GREEN) if goal.done else colorize("○", p_color)
        priority_label = colorize(goal.priority.upper(), p_color)
        
        print(f"  {status} {colorize(goal.name, Colors.BOLD)}")
        print(f"      Priority: {priority_label} | Section: {goal.section[:40]}")
        print()
    
    # Quick action hint
    active_matches = [g for g in matches if not g.done]
    if active_matches:
        print(colorize(f"  💡 {len(active_matches)} active goal(s) match. Use 'complete' to mark done:", Colors.YELLOW))
        print(f"     python3 tools/goal-tracker.py complete \"{active_matches[0].name[:30]}\"")

def cmd_add(filepath: str, goal_name: str, priority: str = 'medium'):
    """Add a new goal to the active.md file."""
    if not os.path.exists(filepath):
        print(colorize(f"  ✗ Goals file not found: {filepath}", Colors.RED))
        return False
    
    # Read current content
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Validate priority
    valid_priorities = ['high', 'medium', 'long-term', 'daily']
    if priority not in valid_priorities:
        priority = 'medium'
    
    # Determine which section to add to
    section_map = {
        'high': '## High Priority',
        'medium': '## Medium Priority',
        'long-term': '## Long-term (Feb 2026)',
        'daily': '## Daily Habits'
    }
    
    section_header = section_map[priority]
    
    # Check if section exists
    if section_header not in content:
        print(colorize(f"  ✗ Section '{section_header}' not found in goals file", Colors.RED))
        return False
    
    # Create new goal entry
    new_goal = f"- [ ] {goal_name}\n"
    
    # Find the section and insert after it
    lines = content.split('\n')
    insert_index = -1
    
    for i, line in enumerate(lines):
        if line.strip() == section_header:
            # Find the next goal line or section header
            for j in range(i + 1, len(lines)):
                if lines[j].strip().startswith('## '):
                    insert_index = j
                    break
                elif lines[j].strip().startswith('- [') or lines[j].strip() == '':
                    insert_index = j
                    break
            
            if insert_index == -1:
                insert_index = i + 1
            
            # Find the right spot (after existing goals in this section)
            for j in range(insert_index, len(lines)):
                if lines[j].strip().startswith('## '):
                    break
                if lines[j].strip().startswith('- ['):
                    insert_index = j + 1
                elif lines[j].strip() == '' and j > i + 1:
                    insert_index = j + 1
            
            break
    
    if insert_index == -1:
        print(colorize(f"  ✗ Could not find insertion point", Colors.RED))
        return False
    
    # Insert the new goal
    lines.insert(insert_index, new_goal.rstrip())
    
    # Write back
    with open(filepath, 'w') as f:
        f.write('\n'.join(lines))
    
    print(colorize(f"  ✓ Added goal: {goal_name}", Colors.GREEN))
    print(f"     Priority: {priority}")
    print(f"     Section: {section_header}")
    
    return True

def main():
    parser = argparse.ArgumentParser(
        description="Goal Tracker CLI - Manage your goals",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 tools/goal-tracker.py list
  python3 tools/goal-tracker.py focus              # Show high-priority active goals only
  python3 tools/goal-tracker.py progress "Build pattern recognition"
  python3 tools/goal-tracker.py complete "Document learnings"
  python3 tools/goal-tracker.py stats
  python3 tools/goal-tracker.py suggest
  python3 tools/goal-tracker.py recent
  python3 tools/goal-tracker.py velocity           # Show work velocity from diary.md
  python3 tools/goal-tracker.py stale [--days 7]
        """
    )
    
    parser.add_argument('command', choices=['list', 'progress', 'complete', 'stats', 'suggest', 'recent', 'add', 'export', 'search', 'stale', 'week', 'focus', 'velocity'],
                       help='Command to run')
    parser.add_argument('goal_name', nargs='?', help='Goal name (for progress/complete/add/search commands)')
    parser.add_argument('--week', type=int, help='Week number for week command (e.g., 2 for week-2.md)')
    parser.add_argument('--priority', choices=['high', 'medium', 'long-term', 'daily'], default='medium',
                       help='Priority level for add command (default: medium)')
    parser.add_argument('--output', help='Output file for export command (default: goals/goals-export.<ext>)')
    parser.add_argument('--format', choices=['json', 'markdown', 'md'], default='json',
                       help='Export format for export command (default: json; use markdown/md for .md file)')
    parser.add_argument('--filter', choices=['all', 'active', 'completed'], default='all',
                       help='Filter goals for list command (default: all)')
    parser.add_argument('--days', type=int, default=7,
                       help='Days threshold for stale command (default: 7)')
    parser.add_argument('--json', action='store_true',
                       help='Output stats in JSON format (for stats command)')
    
    args = parser.parse_args()
    
    # Setup paths
    workspace_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    goals_dir = os.path.join(workspace_dir, 'goals')
    active_file = os.path.join(goals_dir, 'active.md')
    
    # Create goals directory if it doesn't exist
    if not os.path.exists(goals_dir):
        os.makedirs(goals_dir)
        print(colorize(f"Created goals directory: {goals_dir}", Colors.YELLOW))
    
    # Parse goals
    goals = parse_goals_file(active_file)
    
    # Auto-detect completions from diary/memory
    if goals:
        scan_for_completions(goals, workspace_dir)
    
    # Execute command
    if args.command == 'list':
        cmd_list(goals, filter_mode=args.filter)
    elif args.command == 'progress':
        if not args.goal_name:
            print(colorize("Error: Goal name required for progress command", Colors.RED))
            print("Usage: python3 tools/goal-tracker.py progress <goal-name>")
            sys.exit(1)
        cmd_progress(goals, args.goal_name, workspace_dir)
    elif args.command == 'complete':
        if not args.goal_name:
            print(colorize("Error: Goal name required for complete command", Colors.RED))
            print("Usage: python3 tools/goal-tracker.py complete <goal-name>")
            sys.exit(1)
        cmd_complete(goals, args.goal_name, active_file)
        # Reload goals after completion
        goals = parse_goals_file(active_file)
        scan_for_completions(goals, workspace_dir)
        print()
        cmd_stats(goals)
    elif args.command == 'stats':
        cmd_stats(goals, json_output=args.json)
    elif args.command == 'suggest':
        cmd_suggest(goals)
    elif args.command == 'recent':
        cmd_recent(goals)
    elif args.command == 'add':
        if not args.goal_name:
            print(colorize("Error: Goal name required for add command", Colors.RED))
            print("Usage: python3 tools/goal-tracker.py add <goal-name> [--priority high|medium|long-term|daily]")
            sys.exit(1)
        cmd_add(active_file, args.goal_name, args.priority)
    elif args.command == 'export':
        # Normalize format argument
        export_format = 'markdown' if args.format in ['markdown', 'md'] else 'json'
        cmd_export(goals, args.output, export_format)
    elif args.command == 'search':
        if not args.goal_name:
            print(colorize("Error: Search query required for search command", Colors.RED))
            print("Usage: python3 tools/goal-tracker.py search <query>")
            sys.exit(1)
        cmd_search(goals, args.goal_name)
    elif args.command == 'stale':
        cmd_stale(goals, args.days, workspace_dir)
    elif args.command == 'week':
        cmd_week(args.week, workspace_dir)
    elif args.command == 'focus':
        cmd_focus(goals)
    elif args.command == 'velocity':
        cmd_velocity(workspace_dir, args.days)
    
    print()  # Final newline

if __name__ == '__main__':
    main()
