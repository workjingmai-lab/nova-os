#!/usr/bin/env python3
"""
Nova's Agent Digest Generator
A tool for agents to create daily/weekly summaries of their activity.

Usage:
    python3 agent-digest.py --period daily
    python3 agent-digest.py --period weekly
    python3 agent-digest.py --file /path/to/diary.md --period daily

Output: Markdown digest ready to share or store.
"""

import re
import argparse
from datetime import datetime, timedelta
from collections import Counter
from pathlib import Path


class AgentDigest:
    """Generates activity digests from agent diary/logs."""
    
    def __init__(self, log_file: str = "diary.md"):
        self.log_file = Path(log_file)
        self.entries = []
        self.stats = {
            "total_entries": 0,
            "tasks_completed": 0,
            "files_created": [],
            "goals_advanced": [],
            "patterns": [],
            "energy_avg": None
        }
    
    def parse_entries(self):
        """Parse diary entries with timestamps."""
        if not self.log_file.exists():
            return []
        
        content = self.log_file.read_text()
        
        # Pattern: [YYYY-MM-DDTHH:MMZ] or similar timestamp headers
        pattern = r'\*\*\[(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}Z?)\]\*\*([^*]+(?:\*\*[^*]+\*\*)?)'
        matches = re.findall(pattern, content)
        
        entries = []
        for timestamp_str, content_block in matches:
            try:
                # Parse timestamp
                ts = datetime.fromisoformat(timestamp_str.replace('Z', '+00:00').replace('Z', ''))
                entries.append({
                    "timestamp": ts,
                    "content": content_block.strip(),
                    "raw": f"[{timestamp_str}] {content_block}"
                })
            except:
                continue
        
        self.entries = sorted(entries, key=lambda x: x["timestamp"])
        return self.entries
    
    def filter_by_period(self, period: str) -> list:
        """Filter entries by time period."""
        now = datetime.utcnow()
        
        if period == "daily":
            cutoff = now - timedelta(days=1)
        elif period == "weekly":
            cutoff = now - timedelta(weeks=1)
        elif period == "monthly":
            cutoff = now - timedelta(days=30)
        else:
            cutoff = now - timedelta(days=1)
        
        return [e for e in self.entries if e["timestamp"] >= cutoff]
    
    def extract_stats(self, entries: list):
        """Extract statistics from entries."""
        self.stats["total_entries"] = len(entries)
        
        files_created = []
        goals_advanced = []
        tasks_completed = 0
        energy_scores = []
        
        for entry in entries:
            content = entry["content"]
            
            # Files created
            file_matches = re.findall(r'(?:file|output|created)[":]?\s*[`\[]?([^`\]\n]+?\.(?:md|py|js|sol|sh|json|txt))', content, re.IGNORECASE)
            files_created.extend(file_matches)
            
            # Goals
            goal_matches = re.findall(r'goal(?:s)?[":]?\s*([^\n]+)', content, re.IGNORECASE)
            goals_advanced.extend(goal_matches)
            
            # Tasks completed
            tasks_completed += len(re.findall(r'(?:✅|✓|completed|done|finished)', content, re.IGNORECASE))
            
            # Energy tracking (1-10 scale)
            energy_match = re.search(r'energy[:\s]*(\d+)/10', content, re.IGNORECASE)
            if energy_match:
                energy_scores.append(int(energy_match.group(1)))
        
        self.stats["files_created"] = list(set(files_created))
        self.stats["goals_advanced"] = list(set(goals_advanced))
        self.stats["tasks_completed"] = tasks_completed
        self.stats["energy_avg"] = sum(energy_scores) / len(energy_scores) if energy_scores else None
    
    def generate_digest(self, period: str = "daily") -> str:
        """Generate formatted digest."""
        self.parse_entries()
        entries = self.filter_by_period(period)
        self.extract_stats(entries)
        
        now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
        period_title = period.capitalize()
        
        lines = [
            f"# 🦞 {period_title} Digest — Generated {now}",
            "",
            f"*{len(entries)} activity entries analyzed*",
            "",
            "---",
            "",
            "## 📊 The Numbers",
            "",
            f"| Metric | Count |",
            f"|--------|-------|",
            f"| Entries | {self.stats['total_entries']} |",
            f"| Tasks Completed | {self.stats['tasks_completed']} |",
            f"| Files Created | {len(self.stats['files_created'])} |",
            f"| Goals Advanced | {len(self.stats['goals_advanced'])} |",
        ]
        
        if self.stats['energy_avg']:
            lines.append(f"| Avg Energy | {self.stats['energy_avg']:.1f}/10 |")
        
        lines.extend([
            "",
            "## 📁 Files Created",
            ""
        ])
        
        if self.stats['files_created']:
            for f in self.stats['files_created'][:10]:  # Top 10
                lines.append(f"- `{f}`")
            if len(self.stats['files_created']) > 10:
                lines.append(f"- *...and {len(self.stats['files_created']) - 10} more*")
        else:
            lines.append("*No files tracked this period*")
        
        lines.extend([
            "",
            "## 🎯 Goals & Achievements",
            ""
        ])
        
        if self.stats['goals_advanced']:
            for g in self.stats['goals_advanced'][:5]:
                lines.append(f"- {g.strip()}")
        else:
            lines.append("*No goals explicitly tracked*")
        
        lines.extend([
            "",
            "## 📝 Activity Log",
            ""
        ])
        
        for entry in entries[-5:]:  # Last 5 entries
            time_str = entry['timestamp'].strftime("%H:%M")
            # Extract first line or first 80 chars
            summary = entry['content'].split('\n')[0][:80]
            lines.append(f"**{time_str}** — {summary}...")
        
        lines.extend([
            "",
            "---",
            "",
            "*Generated by Nova's Agent Digest Generator* 🦞",
            "*Share your own: github.com/nova/agent-digest*"
        ])
        
        return '\n'.join(lines)
    
    def save_digest(self, period: str = "daily", output_dir: str = "digests") -> Path:
        """Save digest to file."""
        digest = self.generate_digest(period)
        
        out_dir = Path(output_dir)
        out_dir.mkdir(exist_ok=True)
        
        timestamp = datetime.utcnow().strftime("%Y-%m-%d")
        filename = f"{period}-digest-{timestamp}.md"
        filepath = out_dir / filename
        
        filepath.write_text(digest)
        return filepath


def main():
    parser = argparse.ArgumentParser(
        description="Generate activity digests for agents",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --period daily              # Daily digest from diary.md
  %(prog)s --period weekly --save      # Weekly digest, save to file
  %(prog)s --file logs.md --period all # Custom log file
        """
    )
    parser.add_argument(
        "--file", "-f",
        default="diary.md",
        help="Path to diary/log file (default: diary.md)"
    )
    parser.add_argument(
        "--period", "-p",
        choices=["daily", "weekly", "monthly"],
        default="daily",
        help="Time period for digest (default: daily)"
    )
    parser.add_argument(
        "--save", "-s",
        action="store_true",
        help="Save digest to file instead of printing"
    )
    parser.add_argument(
        "--output-dir", "-o",
        default="digests",
        help="Output directory for saved digests (default: digests)"
    )
    
    args = parser.parse_args()
    
    # Generate digest
    digest = AgentDigest(args.file)
    
    if args.save:
        filepath = digest.save_digest(args.period, args.output_dir)
        print(f"✅ Digest saved: {filepath}")
    else:
        print(digest.generate_digest(args.period))


if __name__ == "__main__":
    main()
