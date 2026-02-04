#!/usr/bin/env python3
"""
Diary Parser Library — Shared diary.md parsing for all analytics tools

Provides common data extraction from diary.md:
- Work blocks with timestamps
- Tool usage patterns
- Task categories
- Daily metrics

Usage in other tools:
    from diary_parser import DiaryParser
    parser = DiaryParser()
    blocks = parser.get_blocks()
    tools = parser.get_tool_usage()
    daily = parser.get_daily_metrics()
"""

import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Dict, List, Optional

DIARY_PATH = Path.home() / ".openclaw/workspace/diary.md"


@dataclass
class WorkBlock:
    """A work block entry from diary.md"""
    number: int
    timestamp: datetime
    title: str = ""
    content: str = ""


@dataclass
class DailyMetrics:
    """Productivity metrics for a single day"""
    date: str
    tasks_completed: int = 0
    files_created: int = 0
    tools_built: int = 0
    posts_published: int = 0
    learnings_logged: int = 0
    word_count: int = 0


class DiaryParser:
    """Unified diary.md parser for all analytics tools"""

    def __init__(self, diary_path: Path = DIARY_PATH):
        self.diary_path = diary_path
        self._content = None
        self._blocks = None
        self._daily_sections = None

    def _load_content(self) -> str:
        """Load diary.md content (cached)"""
        if self._content is None:
            if not self.diary_path.exists():
                raise FileNotFoundError(f"Diary not found: {self.diary_path}")
            self._content = self.diary_path.read_text(encoding="utf-8", errors="replace")
        return self._content

    def get_blocks(self) -> List[WorkBlock]:
        """
        Extract all work blocks with timestamps.

        Returns:
            List of WorkBlock objects sorted by number
        """
        if self._blocks is not None:
            return self._blocks

        content = self._load_content()
        blocks = []

        # Pattern: ## Work Block 1234 (2026-02-04T01:25Z)
        pattern = r'## Work Block (\d+) \(([^\]]+)\)'

        for match in re.finditer(pattern, content):
            block_num = int(match.group(1))
            timestamp_str = match.group(2)

            # Parse timestamp
            timestamp = self._parse_timestamp(timestamp_str)
            if timestamp is None:
                continue

            blocks.append(WorkBlock(
                number=block_num,
                timestamp=timestamp,
                title="",
                content=""
            ))

        self._blocks = sorted(blocks, key=lambda b: b.number)
        return self._blocks

    def get_tool_usage(self) -> Counter:
        """
        Extract tool usage patterns.

        Returns:
            Counter of tool mention counts
        """
        content = self._load_content()

        # Pattern 1: "python3 tools/script.py"
        pattern1 = r'python3 tools/([a-z0-9_-]+\.py)'
        # Pattern 2: "script.py" references
        pattern2 = r'\b([a-z0-9_-]+\.py)\b'

        tools1 = re.findall(pattern1, content)
        tools2 = re.findall(pattern2, content)

        return Counter(tools1 + tools2)

    def get_daily_metrics(self) -> Dict[str, DailyMetrics]:
        """
        Calculate daily productivity metrics.

        Returns:
            Dict mapping date strings to DailyMetrics objects
        """
        content = self._load_content()

        # Split by timestamp headers ([YYYY-MM-DDThh:mmZ])
        entry_pattern = r'\[(\d{4}-\d{2}-\d{2})T\d{2}:\d{2}Z\]'
        sections = re.split(entry_pattern, content)

        daily_data = {}

        for i in range(1, len(sections), 2):
            if i + 1 < len(sections):
                date = sections[i]
                entry_content = sections[i + 1]
                metrics = self._analyze_entry(entry_content)
                daily_data[date] = DailyMetrics(date=date, **metrics)

        return daily_data

    def get_blocks_by_hour(self) -> Dict[int, List[WorkBlock]]:
        """
        Group work blocks by hour of day.

        Returns:
            Dict mapping hour (0-23) to list of blocks
        """
        blocks = self.get_blocks()
        hourly = defaultdict(list)

        for block in blocks:
            hour = block.timestamp.hour
            hourly[hour].append(block)

        return dict(hourly)

    def get_velocity(self, hours: int = 24) -> float:
        """
        Calculate recent velocity (blocks per hour).

        Args:
            hours: Time window to analyze

        Returns:
            Blocks per hour in the window
        """
        blocks = self.get_blocks()
        if not blocks:
            return 0.0

        cutoff = datetime.now(timezone.utc) - timedelta(hours=hours)
        recent_blocks = [b for b in blocks if b.timestamp > cutoff]

        if not recent_blocks:
            return 0.0

        return len(recent_blocks) / hours

    def forecast_blocks(self, forecast_hours: int, baseline_hours: int = 24) -> int:
        """
        Forecast work blocks in next N hours based on recent velocity.

        Args:
            forecast_hours: Hours to forecast
            baseline_hours: Hours to use as baseline

        Returns:
            Predicted number of work blocks
        """
        velocity = self.get_velocity(baseline_hours)
        return int(velocity * forecast_hours)

    def _parse_timestamp(self, ts: str) -> Optional[datetime]:
        """Parse ISO-8601 timestamp (with or without Z)"""
        try:
            ts = ts.strip()
            if ts.endswith("Z"):
                return datetime.fromisoformat(ts.replace("Z", "+00:00"))
            dt = datetime.fromisoformat(ts)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt
        except Exception:
            return None

    def _analyze_entry(self, content: str) -> Dict:
        """Analyze a single entry for productivity metrics"""
        return {
            'tasks_completed': len(re.findall(r'\[x\]|✅|✓|completed|finished|done', content, re.I)),
            'files_created': len(re.findall(r'created.*\.(py|md|js|ts|json|yml|yaml|sh)|new file|wrote.*to', content, re.I)),
            'tools_built': len(re.findall(r'built.*tool|created.*script|wrote.*function|implemented', content, re.I)),
            'posts_published': len(re.findall(r'posted.*on|published.*post|blog entry|moltbook', content, re.I)),
            'learnings_logged': len(re.findall(r'learned|discovered|realized|understood', content, re.I)),
            'word_count': len(content.split()),
        }


# CLI for testing
if __name__ == "__main__":
    import sys

    parser = DiaryParser()

    # Show basic stats
    blocks = parser.get_blocks()
    print(f"Total work blocks: {len(blocks)}")

    tools = parser.get_tool_usage()
    print(f"\nTop 5 tools:")
    for tool, count in tools.most_common(5):
        print(f"  {tool}: {count}x")

    daily = parser.get_daily_metrics()
    print(f"\nDays tracked: {len(daily)}")

    velocity = parser.get_velocity()
    print(f"\nRecent velocity: {velocity:.1f} blocks/hour")

    forecast = parser.forecast_blocks(12)
    print(f"Forecast (12h): {forecast} blocks")
