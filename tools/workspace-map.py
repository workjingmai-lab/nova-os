#!/usr/bin/env python3
"""
workspace-map.py — Visualize File Structure

Generate a tree view of the workspace with:
- Directory structure
- File counts by type
- Size statistics
- Key highlights

Usage:
    python3 tools/workspace-map.py
    python3 tools/workspace-map.py --dir /path/to/dir
"""

import os
from pathlib import Path
from collections import defaultdict

def count_files_by_type(directory):
    """Count files by extension."""
    counts = defaultdict(int)
    sizes = defaultdict(int)

    for root, dirs, files in os.walk(directory):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]

        for file in files:
            if file.startswith('.'):
                continue

            ext = Path(file).suffix or 'no_ext'
            counts[ext] += 1

            filepath = os.path.join(root, file)
            try:
                sizes[ext] += os.path.getsize(filepath)
            except OSError:
                pass

    return counts, sizes

def generate_tree(directory, max_depth=3, prefix=""):
    """Generate tree view of directory."""
    try:
        entries = sorted(os.listdir(directory))
    except PermissionError:
        return ""

    # Separate dirs and files
    dirs = []
    files = []

    for entry in entries:
        if entry.startswith('.'):
            continue

        path = os.path.join(directory, entry)
        if os.path.isdir(path):
            dirs.append(entry)
        else:
            files.append(entry)

    tree = ""

    # Add directories
    for i, d in enumerate(dirs):
        is_last = (i == len(dirs) - 1) and not files
        connector = "└── " if is_last else "├── "
        tree += f"{prefix}{connector}{d}/\n"

        if prefix.count("│") < max_depth:
            extension = "    " if is_last else "│   "
            tree += generate_tree(
                os.path.join(directory, d),
                max_depth,
                prefix + extension
            )

    # Add files (limit to 5 per dir to keep it readable)
    for i, f in enumerate(files[:5]):
        is_last = (i == min(len(files), 5) - 1)
        connector = "└── " if is_last else "├── "
        tree += f"{prefix}{connector}{f}\n"

    if len(files) > 5:
        tree += f"{prefix}└── ... ({len(files) - 5} more files)\n"

    return tree

def generate_report():
    """Generate workspace map report."""
    workspace = "/home/node/.openclaw/workspace"

    # File statistics
    counts, sizes = count_files_by_type(workspace)

    total_files = sum(counts.values())
    total_size = sum(sizes.values())

    # Top file types
    top_types = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]

    # Generate tree (partial)
    tree = generate_tree(workspace, max_depth=2, prefix="")

    report = f"""
🗂️ WORKSPACE MAP
{'='*60}

📊 Statistics:
  Total files: {total_files}
  Total size: {total_size / 1024:.1f} KB

📁 Top File Types:
"""
    for ext, count in top_types:
        size_mb = sizes[ext] / 1024
        report += f"  • {ext or 'no_ext'}: {count} files ({size_mb:.1f} KB)\n"

    report += f"""
🌳 Directory Structure (partial):
{tree}
💡 Use --dir <path> for specific directories
"""

    return report

def main():
    import sys

    if "--dir" in sys.argv:
        idx = sys.argv.index("--dir")
        if idx + 1 < len(sys.argv):
            directory = sys.argv[idx + 1]
            tree = generate_tree(directory, max_depth=3, prefix="")
            print(f"\n🌳 {directory}/\n")
            print(tree)
            return

    print(generate_report())

if __name__ == "__main__":
    main()
