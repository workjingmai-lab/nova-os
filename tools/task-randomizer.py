#!/usr/bin/env python3
"""Task Randomizer — eliminates decision fatigue.

Default behavior: pick a random unchecked checkbox task from `quick-tasks.md`.

Usage:
  task-randomizer.py                      # uses quick-tasks.md
  task-randomizer.py path/to/file.md      # uses provided file
  task-randomizer.py --pool grant         # uses grant-mode-tasks.txt
  task-randomizer.py --pool content       # uses content-mode-tasks.txt
  task-randomizer.py --pool unblocked     # uses unblocked-tasks.txt
  task-randomizer.py --pool grant|content|unblocked  # random from multiple pools

Supported pools:
  grant      — Grant submission tasks (grant-mode-tasks.txt)
  content    — Moltbook/documentation tasks (content-mode-tasks.txt)
  unblocked  — No-dependency tasks (unblocked-tasks.txt)

Expected task format:
  - [ ] Do the thing
  OR plain text lines in pool files (one task per line)
"""

import re
import random
import sys
from pathlib import Path

def extract_tasks(file_path: Path):
    """Extract all unchecked checkbox tasks ("- [ ] ...") from a file.
    For pool files, also supports plain text lines (one task per line)."""
    content = Path(file_path).read_text(encoding="utf-8")

    # First, try checkbox format
    checkbox_tasks = re.findall(r'^- \[ \] (.+)$', content, re.MULTILINE)
    if checkbox_tasks:
        return checkbox_tasks
    
    # If no checkboxes found, treat as plain text pool (one task per line)
    # Filter out empty lines and comments
    lines = [
        line.strip() 
        for line in content.split('\n') 
        if line.strip() and not line.strip().startswith('#')
    ]
    return lines

def categorize_task(task):
    """Categorize task by type"""
    task_lower = task.lower()
    
    categories = {
        'Documentation': ['update', 'review', 'extract', 'create tutorial', 'write'],
        'Tool Building': ['build', 'create', 'py'],
        'Content Creation': ['draft', 'post', 'template'],
        'Research & Learning': ['research', 'study', 'learn'],
        'Workspace Organization': ['consolidate', 'archive', 'clean', 'organize'],
        'Communication': ['send', 'draft message', 'template'],
        'Meta Tasks': ['review goals', 'generate', 'track', 'calculate']
    }
    
    for category, keywords in categories.items():
        if any(keyword in task_lower for keyword in keywords):
            return category
    return 'Other'

def main():
    default_task_file = Path(__file__).parent.parent / "quick-tasks.md"
    workspace_root = Path(__file__).parent.parent
    
    # Parse arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "--pool":
            # Pool-based selection
            if len(sys.argv) < 3:
                print("❌ --pool requires a pool name (grant, content, unblocked)")
                print("Example: task-randomizer.py --pool grant")
                print("         task-randomizer.py --pool grant|content|unblocked")
                sys.exit(1)
            
            pool_spec = sys.argv[2]
            pool_names = [p.strip() for p in pool_spec.split('|')]
            
            # Map pool names to file paths
            pool_files = {
                'grant': workspace_root / 'grant-mode-tasks.txt',
                'content': workspace_root / 'content-mode-tasks.txt',
                'unblocked': workspace_root / 'unblocked-tasks.txt'
            }
            
            # Collect tasks from all specified pools
            all_tasks = []
            active_pools = []
            for pool_name in pool_names:
                if pool_name not in pool_files:
                    print(f"⚠️  Unknown pool: {pool_name}")
                    print(f"   Available pools: {', '.join(pool_files.keys())}")
                    sys.exit(1)
                
                pool_file = pool_files[pool_name]
                if not pool_file.exists():
                    print(f"⚠️  Pool file not found: {pool_file}")
                    continue
                
                tasks = extract_tasks(pool_file)
                if tasks:
                    all_tasks.extend(tasks)
                    active_pools.append(pool_name)
            
            if not all_tasks:
                print("✅ All pools complete or empty!")
                sys.exit(0)
            
            # Pick random task from combined pool
            selected = random.choice(all_tasks)
            category = categorize_task(selected)
            pool_info = f"Pools: {', '.join(active_pools)}"
            
        else:
            # File path provided
            task_file = Path(sys.argv[1]).expanduser()
            if not task_file.exists():
                print(f"❌ Task file not found: {task_file}")
                print("Tip: run without args to use quick-tasks.md")
                sys.exit(1)
            
            tasks = extract_tasks(task_file)
            if not tasks:
                print("✅ All tasks complete!")
                sys.exit(0)
            
            selected = random.choice(tasks)
            category = categorize_task(selected)
            pool_info = f"File: {task_file.name}"
    else:
        # Default: quick-tasks.md
        task_file = default_task_file
        if not task_file.exists():
            print(f"❌ Task file not found: {task_file}")
            sys.exit(1)
        
        tasks = extract_tasks(task_file)
        if not tasks:
            print("✅ All tasks complete! Time to add more to quick-tasks.md")
            sys.exit(0)
        
        selected = random.choice(tasks)
        category = categorize_task(selected)
        pool_info = "Default pool"
    
    # Display result
    print("=" * 60)
    print("🎲 TASK RANDOMIZER")
    print("=" * 60)
    print(f"\n📂 Category: {category}")
    print(f"📋 {pool_info}")
    print(f"🎯 Task: {selected}")
    print("\n💡 Execute this task in 1 minute. Document result. Repeat.")
    print("=" * 60)

if __name__ == "__main__":
    main()
