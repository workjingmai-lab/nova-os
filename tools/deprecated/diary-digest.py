#!/usr/bin/env python3
"""
Diary Digest Tool - Weekly Activity Summary Generator

RUN COMMAND:
    python3 tools/diary-digest.py [--days N] [--output FILE] [--format md|json|both]
    
    Or make executable and run directly:
    chmod +x tools/diary-digest.py
    ./tools/diary-digest.py

USAGE:
    - Run weekly to generate a summary of Nova's activity
    - Can be scheduled via cron: 0 9 * * 1 /usr/bin/python3 /path/to/tools/diary-digest.py
    - Output saved to reports/diary-digest-latest.md (default)

FEATURES:
    - Parses diary.md for work blocks, heartbeats, goals, and sub-agent activity
    - Scans memory/ directory for session summaries
    - Calculates velocity metrics (blocks per day, completion rates)
    - Tracks productivity trends and highlights
    - Exports to markdown, JSON, or both
    - Handles edge cases: empty files, missing dates, malformed entries

CHANGES (v1.2 - Current):
    - Added week-over-week comparison (trend analysis)
    - Added productivity score (0-100 scale)
    - Added file size tracking (diary.md growth)
    - Added emoji indicators for visual feedback
    - Added quick stats export (one-line summary)
    - Added keyword frequency analysis (top terms used)

CHANGES (v1.1):
    - Added work block tracking with velocity metrics
    - Added productivity highlights (most productive days, streak tracking)
    - Added CLI flags for customization (--days, --output, --format)
    - Added JSON export for programmatic access
    - Added trend analysis and recommendations
"""

import os
import re
import sys
import json
import argparse
from datetime import datetime, timedelta, date, timezone
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple, Optional

# Configuration
DIARY_PATH = Path("diary.md")
MEMORY_DIR = Path("memory")
REPORTS_DIR = Path("reports")
OUTPUT_FILE_MD = REPORTS_DIR / "diary-digest-latest.md"
OUTPUT_FILE_JSON = REPORTS_DIR / "diary-digest-latest.json"
DAYS_TO_LOOK_BACK = 7


class DiaryDigest:
    """Generates weekly activity summaries from diary and memory files."""
    
    def __init__(self, days: int = DAYS_TO_LOOK_BACK):
        self.days = days
        self.cutoff_date = (datetime.now(timezone.utc) - timedelta(days=days))
        self.previous_cutoff = (datetime.now(timezone.utc) - timedelta(days=days*2))  # For week-over-week
        self.stats = {
            "heartbeats": {"FULL": 0, "SLOW": 0, "DEEP": 0, "UNKNOWN": 0},
            "work_blocks": [],
            "sub_agents": [],
            "goals_advanced": [],
            "anomalies": [],
            "sessions": [],
            "entries_parsed": 0,
            "daily_blocks": defaultdict(int),  # Track blocks per day
            "goal_completions": [],
            "previous_period": {},  # For comparison
        }
        self.health_scores = []  # For trend calculation
        self.productivity_highlights = []
        self.diary_size = DIARY_PATH.stat().st_size if DIARY_PATH.exists() else 0
        
    def parse_timestamp(self, ts_str: str) -> Optional[datetime]:
        """Parse various timestamp formats found in diary entries."""
        formats = [
            "%Y-%m-%dT%H:%M:%SZ",
            "%Y-%m-%dT%H:%MZ",
            "%Y-%m-%d %H:%M:%S UTC",
            "%Y-%m-%d %H:%M UTC",
        ]
        for fmt in formats:
            try:
                return datetime.strptime(ts_str, fmt)
            except ValueError:
                continue
        return None
    
    def extract_diary_entries(self) -> List[Dict]:
        """Extract entries from diary.md within the lookback period."""
        entries = []
        
        if not DIARY_PATH.exists():
            return entries
            
        content = DIARY_PATH.read_text(encoding="utf-8")
        
        # Try pattern 1: [TYPE] YYYY-MM-DDTHH:MM:SSZ format
        entry_pattern = r'\[([\w\s\d\(\)\#\-]+)\]\s+(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)(.*?)(?=\n\[|\Z)'
        
        for match in re.finditer(entry_pattern, content, re.MULTILINE | re.DOTALL):
            entry_type = match.group(1).strip()
            timestamp_str = match.group(2)
            content_block = match.group(3).strip()
            
            timestamp = self.parse_timestamp(timestamp_str)
            if timestamp and timestamp >= self.cutoff_date:
                entry = {
                    "type": entry_type,
                    "timestamp": timestamp,
                    "content": content_block,
                    "source": "diary.md"
                }
                entries.append(entry)
                
                # Track work blocks specifically
                if "WORK BLOCK" in entry_type:
                    self.stats["work_blocks"].append(entry)
                    # Track daily blocks
                    day_key = timestamp.date().isoformat()
                    self.stats["daily_blocks"][day_key] += 1
                
                # Track goal completions
                if "✅ COMPLETE" in content_block or "COMPLETE" in entry_type:
                    self.stats["goal_completions"].append(entry)
        
        # Try pattern 2: ### HH:MM UTC — Work Block N format
        if not entries:
            # Look for date headers (## YYYY-MM-DD)
            date_sections = re.split(r'## (\d{4}-\d{2}-\d{2})', content)
            
            for i in range(1, len(date_sections), 2):
                if i + 1 >= len(date_sections):
                    break
                
                date_str = date_sections[i]
                section_content = date_sections[i + 1]
                
                try:
                    section_date = datetime.strptime(date_str, "%Y-%m-%d").date()
                except ValueError:
                    continue
                
                # Look for work block entries within this section
                # Pattern: ### HH:MM UTC — Work Block N
                block_pattern = r'###\s+(\d{2}):(\d{2})\s+UTC\s+—\s+(?:Work Block\s+(\d+)|[^\n]+)'
                
                for match in re.finditer(block_pattern, section_content):
                    hour, minute, block_num = match.groups()
                    
                    # Create timestamp
                    try:
                        timestamp = datetime.combine(section_date, datetime.min.time())
                        timestamp = timestamp.replace(hour=int(hour), minute=int(minute))
                        timestamp = timestamp.replace(tzinfo=timezone.utc)
                    except ValueError:
                        continue
                    
                    if timestamp < self.cutoff_date:
                        continue
                    
                    # Get the content for this block (until next ### or end)
                    block_start = match.end()
                    next_header = re.search(r'\n###', section_content[block_start:])
                    if next_header:
                        block_content = section_content[block_start:block_start + next_header.start()]
                    else:
                        block_content = section_content[block_start:]
                    
                    entry_type = f"WORK BLOCK {block_num}" if block_num else "ACTIVITY"
                    
                    entry = {
                        "type": entry_type,
                        "timestamp": timestamp,
                        "content": block_content.strip(),
                        "source": "diary.md"
                    }
                    entries.append(entry)
                    
                    # Track work blocks
                    if "WORK BLOCK" in entry_type or "activity" in entry_type.lower():
                        self.stats["work_blocks"].append(entry)
                        day_key = timestamp.date().isoformat()
                        self.stats["daily_blocks"][day_key] += 1
                    
                    # Track completions
                    if "✅ COMPLETE" in block_content or "complete" in block_content.lower():
                        self.stats["goal_completions"].append(entry)
        
        # Try pattern 3: "## [WORK BLOCK N — 2026-02-02T00:42Z]" (current diary format)
        if not entries:
            wb_heading_pattern = (
                r"##\s+\[WORK BLOCK\s+(\d+)\s+—\s+"
                r"(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}Z)\]"
                r"(.*?)(?=\n##\s+\[WORK BLOCK|\Z)"
            )

            for match in re.finditer(wb_heading_pattern, content, re.MULTILINE | re.DOTALL):
                block_num = match.group(1)
                timestamp_str = match.group(2)
                block_content = match.group(3).strip()

                timestamp = self.parse_timestamp(timestamp_str)
                if not timestamp:
                    continue
                # normalize to UTC-aware
                if timestamp.tzinfo is None:
                    timestamp = timestamp.replace(tzinfo=timezone.utc)

                if timestamp < self.cutoff_date:
                    continue

                entry_type = f"WORK BLOCK {block_num}"
                entry = {
                    "type": entry_type,
                    "timestamp": timestamp,
                    "content": block_content,
                    "source": "diary.md",
                }
                entries.append(entry)

                self.stats["work_blocks"].append(entry)
                day_key = timestamp.date().isoformat()
                self.stats["daily_blocks"][day_key] += 1

                if "✅" in block_content and "COMPLETE" in block_content:
                    self.stats["goal_completions"].append(entry)
        
        # Try pattern 4: Bullet list format "- Work block NNNN: text" (today.md format)
        if not entries:
            # First, find the most recent date section to establish context
            date_section_pattern = r'\*\*Date:\*\*\s+(\d{4}-\d{2}-\d{2})'
            current_date = None
            
            for match in re.finditer(date_section_pattern, content):
                date_str = match.group(1)
                try:
                    current_date = datetime.strptime(date_str, "%Y-%m-%d").date()
                except ValueError:
                    continue
            
            # If no date found, use today
            if current_date is None:
                current_date = datetime.now().date()
            
            # Parse bullet list work blocks: "- Work block NNNN: text"
            bullet_pattern = r'^-\s+Work block\s+(\d+):\s*(.+?)(?=\n-\s+Work block|$)'
            
            for match in re.finditer(bullet_pattern, content, re.MULTILINE | re.DOTALL):
                block_num = match.group(1)
                block_content = match.group(2).strip()
                
                # For bullet format, we don't have precise timestamps
                # Use the date from the header and estimate time
                # This is a limitation of the bullet format
                try:
                    # Use date with noon time as default
                    timestamp = datetime.combine(current_date, datetime.min.time())
                    timestamp = timestamp.replace(hour=12, minute=0, second=0)
                    timestamp = timestamp.replace(tzinfo=timezone.utc)
                except (ValueError, AttributeError):
                    continue
                
                if timestamp < self.cutoff_date:
                    continue
                
                entry_type = f"WORK BLOCK {block_num}"
                entry = {
                    "type": entry_type,
                    "timestamp": timestamp,
                    "content": block_content,
                    "source": "diary.md",
                }
                entries.append(entry)
                
                self.stats["work_blocks"].append(entry)
                day_key = timestamp.date().isoformat()
                self.stats["daily_blocks"][day_key] += 1
                
                if "✅" in block_content and "COMPLETE" in block_content:
                    self.stats["goal_completions"].append(entry)

        return sorted(entries, key=lambda x: x["timestamp"])
    
    def extract_memory_sessions(self) -> List[Dict]:
        """Extract session summaries from memory files."""
        sessions = []
        
        if not MEMORY_DIR.exists():
            return sessions
        
        # Look at files from the past 7 days
        for file_path in MEMORY_DIR.glob("*.md"):
            # Extract date from filename (various formats)
            date_match = re.search(r'(\d{4}-\d{2}-\d{2})', file_path.name)
            if not date_match:
                continue
                
            try:
                file_date = datetime.strptime(date_match.group(1), "%Y-%m-%d").date()
            except ValueError:
                continue
                
            if file_date < self.cutoff_date.date():
                continue
            
            try:
                content = file_path.read_text(encoding="utf-8")
            except (IOError, UnicodeDecodeError):
                continue
            
            # Extract session info
            session = {
                "file": file_path.name,
                "date": datetime.combine(file_date, datetime.min.time()),
                "heartbeats": [],
                "sub_agents": [],
                "goals": [],
                "summary": ""
            }
            
            # Look for heartbeat types in content
            if "HEARTBEAT_FULL" in content:
                session["heartbeats"].append("FULL")
            if "HEARTBEAT_SLOW" in content:
                session["heartbeats"].append("SLOW")
            if "HEARTBEAT_DEEP" in content or "DEEP THINK" in content:
                session["heartbeats"].append("DEEP")
            if "HEARTBEAT_OK" in content:
                session["heartbeats"].append("OK")
            
            # Look for sub-agent spawns
            subagent_pattern = r'(?:spawned sub-agent|sub-agent spawned|session:\s*agent:main:subagent:[\w-]+)'
            if re.search(subagent_pattern, content, re.IGNORECASE):
                # Try to extract task description
                task_match = re.search(r'[Tt]ask:\s*(.+?)(?:\n|$)', content)
                if task_match:
                    session["sub_agents"].append(task_match.group(1).strip())
                else:
                    session["sub_agents"].append("Activity logged")
            
            # Look for goals
            goal_pattern = r'[Gg]oal:\s*(.+?)(?:\n|$)'
            for match in re.finditer(goal_pattern, content):
                session["goals"].append(match.group(1).strip())
            
            sessions.append(session)
        
        return sessions
    
    def analyze_heartbeat_entries(self, entries: List[Dict]) -> None:
        """Categorize heartbeat entries by type."""
        for entry in entries:
            content = entry.get("content", "")
            entry_type = entry.get("type", "")
            
            # Check content for heartbeat indicators
            if "HEARTBEAT_FULL" in content or entry_type == "HEARTBEAT_FULL":
                self.stats["heartbeats"]["FULL"] += 1
            elif "HEARTBEAT_SLOW" in content or entry_type == "HEARTBEAT_SLOW":
                self.stats["heartbeats"]["SLOW"] += 1
            elif "HEARTBEAT_DEEP" in content or "DEEP THINK" in content or entry_type == "DEEP":
                self.stats["heartbeats"]["DEEP"] += 1
            elif "HEARTBEAT" in content or entry_type in ["HEARTBEAT", "PROACTIVE"]:
                self.stats["heartbeats"]["UNKNOWN"] += 1
    
    def analyze_sub_agents(self, entries: List[Dict], sessions: List[Dict]) -> None:
        """Extract sub-agent activity information."""
        # From diary entries
        for entry in entries:
            content = entry.get("content", "")
            
            # Look for sub-agent spawn patterns
            if "sub-agent" in content.lower() or "subagent" in content.lower():
                # Extract session ID if present
                session_match = re.search(r'session:\s*(agent:main:subagent:[\w-]+)', content)
                session_id = session_match.group(1) if session_match else "unknown"
                
                # Extract task if present
                task_match = re.search(r'[Tt]ask:\s*(.+?)(?:\n|$)', content)
                task = task_match.group(1).strip() if task_match else "Task not specified"
                
                # Extract status if present
                status_match = re.search(r'[Ss]tatus:\s*(.+?)(?:\n|$)', content)
                status = status_match.group(1).strip() if status_match else "Unknown"
                
                self.stats["sub_agents"].append({
                    "session_id": session_id,
                    "task": task,
                    "status": status,
                    "timestamp": entry.get("timestamp"),
                    "source": "diary"
                })
        
        # From memory sessions
        for session in sessions:
            for task in session.get("sub_agents", []):
                self.stats["sub_agents"].append({
                    "session_id": session.get("file", "unknown"),
                    "task": task,
                    "status": "From memory log",
                    "timestamp": session.get("date"),
                    "source": "memory"
                })
    
    def analyze_goals(self, entries: List[Dict], sessions: List[Dict]) -> None:
        """Extract goals advanced during the period."""
        # From diary entries
        for entry in entries:
            content = entry.get("content", "")
            
            if entry.get("type") == "PROACTIVE GOAL" or "Goal:" in content or "goal:" in content:
                goal_match = re.search(r'[Gg]oal:\s*(.+?)(?:\n|$)', content)
                action_match = re.search(r'[Aa]ction:\s*(.+?)(?:\n|$)', content)
                
                if goal_match or action_match:
                    self.stats["goals_advanced"].append({
                        "goal": goal_match.group(1).strip() if goal_match else "Unspecified",
                        "action": action_match.group(1).strip() if action_match else "Activity logged",
                        "timestamp": entry.get("timestamp"),
                        "source": "diary"
                    })
        
        # From memory sessions
        for session in sessions:
            for goal in session.get("goals", []):
                self.stats["goals_advanced"].append({
                    "goal": goal,
                    "action": "Logged in session",
                    "timestamp": session.get("date"),
                    "source": "memory"
                })
    
    def detect_anomalies(self, entries: List[Dict], sessions: List[Dict]) -> None:
        """Detect unusual events or anomalies."""
        anomaly_keywords = [
            "error", "fail", "crash", "exception", "timeout",
            "anomaly", "unusual", "unexpected", "warning", "critical",
            "⚠️", "🚨", "❌", "⚡"
        ]
        
        for entry in entries:
            content = entry.get("content", "").lower()
            for keyword in anomaly_keywords:
                if keyword in content:
                    self.stats["anomalies"].append({
                        "type": f"Keyword detected: {keyword}",
                        "context": entry.get("content", "")[:200] + "..." if len(entry.get("content", "")) > 200 else entry.get("content", ""),
                        "timestamp": entry.get("timestamp")
                    })
                    break
    
    def calculate_productivity_score(self) -> int:
        """Calculate overall productivity score (0-100)."""
        score = 0
        max_score = 100
        
        # Work block velocity (30 points max)
        blocks = len(self.stats["work_blocks"])
        if blocks >= 50:
            score += 30
        elif blocks >= 20:
            score += 20
        elif blocks >= 10:
            score += 10
        
        # Active days percentage (20 points max)
        velocity = self.calculate_velocity_metrics()
        active_pct = (velocity['active_days'] / max(self.days, 1)) * 100
        if active_pct >= 80:
            score += 20
        elif active_pct >= 50:
            score += 15
        elif active_pct >= 30:
            score += 10
        
        # Goal completions (20 points max)
        goals_completed = len(self.stats["goal_completions"])
        if goals_completed >= 10:
            score += 20
        elif goals_completed >= 5:
            score += 15
        elif goals_completed >= 2:
            score += 10
        
        # Heartbeat health (15 points max)
        hb = self.stats["heartbeats"]
        total_hb = sum(hb.values())
        if total_hb > 0:
            positive_ratio = (hb["FULL"] + hb["DEEP"]) / total_hb
            if positive_ratio >= 0.7:
                score += 15
            elif positive_ratio >= 0.5:
                score += 10
            elif positive_ratio >= 0.3:
                score += 5
        
        # Streak bonus (15 points max)
        streak = velocity['current_streak']
        if streak >= 7:
            score += 15
        elif streak >= 5:
            score += 12
        elif streak >= 3:
            score += 8
        
        return min(score, max_score)
    
    def get_previous_period_stats(self) -> Dict:
        """Get stats from previous period for comparison."""
        # Recalculate for previous period
        previous_stats = {
            "heartbeats": {"FULL": 0, "SLOW": 0, "DEEP": 0, "UNKNOWN": 0},
            "work_blocks": [],
            "goal_completions": [],
        }
        
        if not DIARY_PATH.exists():
            return previous_stats
        
        content = DIARY_PATH.read_text(encoding="utf-8")
        entry_pattern = r'\[([\w\s\d\(\)\#\-]+)\]\s+(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)(.*?)(?=\n\[|\Z)'
        
        for match in re.finditer(entry_pattern, content, re.MULTILINE | re.DOTALL):
            timestamp_str = match.group(2)
            timestamp = self.parse_timestamp(timestamp_str)
            
            if timestamp and self.previous_cutoff <= timestamp < self.cutoff_date:
                entry_type = match.group(1).strip()
                content_block = match.group(3).strip()
                
                if "WORK BLOCK" in entry_type:
                    previous_stats["work_blocks"].append({"timestamp": timestamp})
                
                if "✅ COMPLETE" in content_block or "COMPLETE" in entry_type:
                    previous_stats["goal_completions"].append({"timestamp": timestamp})
                
                # Heartbeats
                if "HEARTBEAT_FULL" in content_block or entry_type == "HEARTBEAT_FULL":
                    previous_stats["heartbeats"]["FULL"] += 1
                elif "HEARTBEAT_SLOW" in content_block or entry_type == "HEARTBEAT_SLOW":
                    previous_stats["heartbeats"]["SLOW"] += 1
                elif "HEARTBEAT_DEEP" in content_block or "DEEP THINK" in content_block or entry_type == "DEEP":
                    previous_stats["heartbeats"]["DEEP"] += 1
        
        return previous_stats
    
    def analyze_keyword_frequency(self, entries: List[Dict]) -> Dict[str, int]:
        """Analyze most common keywords in work block titles."""
        keywords = defaultdict(int)
        stop_words = {"task", "result", "created", "next", "work", "block", "status", "complete", "value", "file", "files"}
        
        for entry in entries:
            if "WORK BLOCK" in entry.get("type", ""):
                content = entry.get("content", "").lower()
                # Extract first line (task description)
                first_line = content.split("\n")[0]
                # Remove common prefixes
                first_line = re.sub(r'^[\*\-]\s*', '', first_line)
                first_line = re.sub(r'^task:\s*', '', first_line, flags=re.IGNORECASE)
                # Extract words
                words = re.findall(r'\b[a-z]{4,}\b', first_line)
                for word in words:
                    if word not in stop_words:
                        keywords[word] += 1
        
        # Return top 10
        return dict(sorted(keywords.items(), key=lambda x: x[1], reverse=True)[:10])
    
    def format_file_size(self, size_bytes: int) -> str:
        """Format file size in human-readable format."""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.1f} TB"
    
    def calculate_health_trend(self) -> str:
        """Calculate overall health trend based on activity metrics."""
        hb = self.stats["heartbeats"]
        total_hb = sum(hb.values())
        
        if total_hb == 0:
            return "NO DATA"
        
        # Calculate health score based on heartbeat distribution
        # FULL and DEEP are positive, UNKNOWN/SLOW might indicate issues
        positive_weight = hb["FULL"] + hb["DEEP"] * 1.5
        neutral_weight = hb["SLOW"] * 0.5
        
        if total_hb > 0:
            health_ratio = (positive_weight + neutral_weight) / total_hb
        else:
            health_ratio = 0
        
        # Factor in work block velocity
        block_count = len(self.stats["work_blocks"])
        blocks_per_day = block_count / max(self.days, 1)
        
        # Factor in sub-agent activity
        subagent_count = len(self.stats["sub_agents"])
        goal_count = len(self.stats["goals_advanced"])
        
        if health_ratio > 0.7 and blocks_per_day >= 10 and goal_count >= 1:
            return "IMPROVING"
        elif health_ratio > 0.5 or (blocks_per_day >= 5 or subagent_count >= 1 or goal_count >= 1):
            return "STABLE"
        elif health_ratio < 0.3 or blocks_per_day < 2 or len(self.stats["anomalies"]) > 3:
            return "DECLINING"
        else:
            return "STABLE"
    
    def calculate_velocity_metrics(self) -> Dict:
        """Calculate work block velocity metrics."""
        blocks = self.stats["work_blocks"]
        total_blocks = len(blocks)
        
        if total_blocks == 0:
            return {
                "total_blocks": 0,
                "blocks_per_day": 0,
                "most_productive_day": None,
                "blocks_on_most_productive": 0,
                "active_days": 0,
                "current_streak": 0
            }
        
        # Calculate blocks per day
        blocks_per_day = total_blocks / max(self.days, 1)
        
        # Find most productive day
        most_productive_day = None
        max_blocks = 0
        for day, count in self.stats["daily_blocks"].items():
            if count > max_blocks:
                max_blocks = count
                most_productive_day = day
        
        # Calculate active days (days with at least 1 work block)
        active_days = len([d for d in self.stats["daily_blocks"].values() if d > 0])
        
        # Calculate current streak (consecutive days with work blocks, counting backwards)
        current_streak = 0
        today = datetime.now().date()
        for i in range(self.days):
            check_date = (today - timedelta(days=i)).isoformat()
            if self.stats["daily_blocks"].get(check_date, 0) > 0:
                current_streak += 1
            else:
                break
        
        return {
            "total_blocks": total_blocks,
            "blocks_per_day": round(blocks_per_day, 1),
            "most_productive_day": most_productive_day,
            "blocks_on_most_productive": max_blocks,
            "active_days": active_days,
            "current_streak": current_streak
        }
    
    def generate_productivity_highlights(self) -> List[str]:
        """Generate productivity highlights based on metrics."""
        highlights = []
        velocity = self.calculate_velocity_metrics()
        
        # Work block highlights
        if velocity["total_blocks"] >= 50:
            highlights.append(f"🔥 {velocity['total_blocks']} work blocks completed — strong momentum!")
        elif velocity["total_blocks"] >= 20:
            highlights.append(f"✅ {velocity['total_blocks']} work blocks completed — steady progress.")
        
        # Streak highlights
        if velocity["current_streak"] >= 5:
            highlights.append(f"🔥 {velocity['current_streak']}-day active streak — consistency pays!")
        elif velocity["current_streak"] >= 3:
            highlights.append(f"📈 {velocity['current_streak']}-day active streak — building momentum.")
        
        # Productive day highlights
        if velocity["blocks_on_most_productive"] >= 20:
            highlights.append(f"🚀 Most productive day: {velocity['most_productive_day']} with {velocity['blocks_on_most_productive']} blocks")
        
        # Goal completion highlights
        goal_completions = len(self.stats["goal_completions"])
        if goal_completions >= 5:
            highlights.append(f"🎯 {goal_completions} goals completed — excellent execution rate!")
        elif goal_completions >= 2:
            highlights.append(f"✅ {goal_completions} goals completed — solid progress.")
        
        # Sub-agent highlights
        subagent_count = len(self.stats["sub_agents"])
        if subagent_count >= 3:
            highlights.append(f"🤖 {subagent_count} sub-agent sessions spawned — delegating effectively!")
        
        # Health trend highlights
        health = self.calculate_health_trend()
        if health == "IMPROVING":
            highlights.append("📈 Health trend: IMPROVING — keep pushing!")
        elif health == "STABLE":
            highlights.append("📊 Health trend: STABLE — consistent performance.")
        elif health == "DECLINING":
            highlights.append("⚠️ Health trend: DECLINING — consider adjusting pace.")
        
        return highlights[:5]  # Limit to top 5 highlights
    
    def generate_summary(self) -> str:
        """Generate the markdown summary report."""
        now = datetime.now()
        start_date = self.cutoff_date
        velocity = self.calculate_velocity_metrics()
        highlights = self.generate_productivity_highlights()
        productivity_score = self.calculate_productivity_score()
        
        # Get previous period stats for comparison
        previous_stats = self.get_previous_period_stats()
        prev_blocks = len(previous_stats["work_blocks"])
        prev_goals = len(previous_stats["goal_completions"])
        
        # Calculate trends
        block_trend = velocity['total_blocks'] - prev_blocks
        goal_trend = len(self.stats["goal_completions"]) - prev_goals
        block_trend_str = f"📈 +{block_trend}" if block_trend > 0 else f"📉 {block_trend}" if block_trend < 0 else "➡️ 0"
        goal_trend_str = f"📈 +{goal_trend}" if goal_trend > 0 else f"📉 {goal_trend}" if goal_trend < 0 else "➡️ 0"
        
        # Get keyword frequency
        keywords = self.analyze_keyword_frequency(self.stats["work_blocks"])
        
        report = f"""# 📊 Diary Digest - Activity Summary

**Period:** {start_date.strftime("%Y-%m-%d")} to {now.strftime("%Y-%m-%d")} ({self.days} days)  
**Generated:** {now.strftime("%Y-%m-%d %H:%M:%S UTC")}

---

## ⚡ Productivity Score: {productivity_score}/100

"""

        # Score breakdown
        score_bar = "█" * (productivity_score // 5) + "░" * (20 - productivity_score // 5)
        report += f"""{score_bar}

"""
        
        for highlight in highlights:
            report += f"{highlight}\n"
        
        report += f"""
---

## 📈 Activity Overview

| Metric | This Period | Previous Period | Trend |
|--------|-------------|-----------------|-------|
| **Work Blocks** | {velocity['total_blocks']} | {prev_blocks} | {block_trend_str} |
| **Blocks Per Day** | {velocity['blocks_per_day']} | {prev_blocks/max(self.days,1):.1f} | - |
| **Goals Completed** | {len(self.stats["goal_completions"])} | {prev_goals} | {goal_trend_str} |
| **Active Days** | {velocity['active_days']} / {self.days} | - | - |
| **Current Streak** | {velocity['current_streak']} days | - | - |
| **Most Productive Day** | {velocity['most_productive_day'] or 'N/A'} ({velocity['blocks_on_most_productive']} blocks) | - | - |
| **Sub-Agents Spawned** | {len(self.stats["sub_agents"])} | - | - |
| **Anomalies Detected** | {len(self.stats["anomalies"])} | - | - |

### 📁 File Growth
- **diary.md size:** {self.format_file_size(self.diary_size)}
- **Entries parsed:** {self.stats["entries_parsed"]}

---

## 💓 Heartbeat Analysis

| Type | Count | Percentage |
|------|-------|------------|
| FULL | {self.stats["heartbeats"]["FULL"]} | {self._pct(self.stats["heartbeats"]["FULL"])}% |
| SLOW | {self.stats["heartbeats"]["SLOW"]} | {self._pct(self.stats["heartbeats"]["SLOW"])}% |
| DEEP THINK | {self.stats["heartbeats"]["DEEP"]} | {self._pct(self.stats["heartbeats"]["DEEP"])}% |
| Other | {self.stats["heartbeats"]["UNKNOWN"]} | {self._pct(self.stats["heartbeats"]["UNKNOWN"])}% |

**Total Heartbeats:** {sum(self.stats["heartbeats"].values())}

---

## 🔥 Work Block Velocity

"""
        
        # Show daily breakdown for last 7 days
        report += "**Daily Breakdown (Last 7 Days):**\n\n"
        report += "| Date | Work Blocks |\n|------|-------------|\n"
        
        today = datetime.now().date()
        for i in range(min(7, self.days)):
            check_date = (today - timedelta(days=i)).isoformat()
            blocks = self.stats["daily_blocks"].get(check_date, 0)
            bar = "█" * min(blocks // 2, 20)  # Visual bar, max 20 chars
            report += f"| {check_date} | {blocks} {bar} |\n"
        
        report += f"""
**Velocity Metrics:**
- **Average:** {velocity['blocks_per_day']} blocks/day
- **Peak:** {velocity['blocks_on_most_productive']} blocks on {velocity['most_productive_day'] or 'N/A'}
- **Consistency:** {velocity['active_days']} active days ({(velocity['active_days']/max(self.days,1)*100):.0f}%)

---

## 🔑 Top Keywords (Work Focus)

"""
        
        if keywords:
            for keyword, count in list(keywords.items())[:8]:
                # Calculate percentage
                total_mentions = sum(keywords.values())
                pct = (count / total_mentions * 100) if total_mentions > 0 else 0
                bar_length = int(pct / 2)  # Max 50 chars
                bar = "█" * bar_length
                report += f"| {keyword:20s} | {count:3d}x | {bar} |\n"
        else:
            report += "*No keyword data available.*\n"
        
        report += f"""
---

## 🤖 Sub-Agents & Accomplishments

"""
        
        if self.stats["sub_agents"]:
            for i, agent in enumerate(self.stats["sub_agents"][:10], 1):  # Limit to 10
                ts = agent.get("timestamp")
                ts_str = ts.strftime("%Y-%m-%d %H:%M") if isinstance(ts, datetime) else str(ts)
                report += f"""### {i}. {agent['task'][:60]}{'...' if len(agent['task']) > 60 else ''}
- **Status:** {agent['status']}
- **Source:** {agent['source']}
- **Time:** {ts_str}

"""
            if len(self.stats["sub_agents"]) > 10:
                report += f"*... and {len(self.stats['sub_agents']) - 10} more sub-agents*\n\n"
        else:
            report += "*No sub-agent activity recorded this period.*\n\n"
        
        report += """---

## 🎯 Goals Advanced

"""
        
        if self.stats["goals_advanced"]:
            for i, goal in enumerate(self.stats["goals_advanced"][:10], 1):
                ts = goal.get("timestamp")
                ts_str = ts.strftime("%Y-%m-%d %H:%M") if isinstance(ts, datetime) else str(ts)
                report += f"""### {i}. {goal['goal'][:60]}{'...' if len(goal['goal']) > 60 else ''}
- **Action:** {goal['action'][:80]}{'...' if len(goal['action']) > 80 else ''}
- **Source:** {goal['source']}
- **Time:** {ts_str}

"""
            if len(self.stats["goals_advanced"]) > 10:
                report += f"*... and {len(self.stats['goals_advanced']) - 10} more goals*\n\n"
        else:
            report += "*No goals advanced this period.*\n\n"
        
        trend = self.calculate_health_trend()
        trend_emoji = {"IMPROVING": "📈", "STABLE": "📊", "DECLINING": "📉", "NO DATA": "❓"}
        
        report += f"""---

## 🏥 Health Trend

**Overall Status:** {trend_emoji.get(trend, "❓")} **{trend}**

"""
        
        if trend == "IMPROVING":
            report += """✅ Strong activity levels with productive work block velocity and goal progression. 
Full heartbeats dominate, indicating healthy system operation.
"""
        elif trend == "STABLE":
            report += """✅ Consistent activity with moderate goal advancement. 
System operating within normal parameters.
"""
        elif trend == "DECLINING":
            report += """⚠️ Lower than normal activity detected. Fewer heartbeats or reduced work block velocity.
Consider reviewing system configuration or increasing proactive goal frequency.
"""
        else:
            report += """❓ Insufficient data to determine health trend.
This may be normal for a new installation or quiet period.
"""
        
        report += """
---

## ⚠️ Anomalies & Notable Events

"""
        
        if self.stats["anomalies"]:
            for anomaly in self.stats["anomalies"][:5]:
                ts = anomaly.get("timestamp")
                ts_str = ts.strftime("%Y-%m-%d %H:%M") if isinstance(ts, datetime) else str(ts)
                report += f"""### {anomaly['type']}
- **Time:** {ts_str}
- **Context:** {anomaly['context'][:150]}{'...' if len(anomaly['context']) > 150 else ''}

"""
        else:
            report += "*No anomalies detected this period.* ✅\n\n"
        
        report += f"""---

## 📝 Raw Data Summary

- **Diary entries analyzed:** {self.stats["entries_parsed"]}
- **Memory files scanned:** {len(self.stats["sessions"])}
- **Date range:** {start_date.strftime("%Y-%m-%d")} to {now.strftime("%Y-%m-%d")}
- **Lookback period:** {self.days} days

---

*Generated by Diary Digest Tool v1.1*  
*Run: `python3 tools/diary-digest.py [--days N] [--output FILE] [--format md|json|both]`*
"""
        
        return report
    
    def generate_json_report(self) -> str:
        """Generate JSON report for programmatic access."""
        velocity = self.calculate_velocity_metrics()
        highlights = self.generate_productivity_highlights()
        keywords = self.analyze_keyword_frequency(self.stats["work_blocks"])
        
        # Get previous period stats for comparison
        previous_stats = self.get_previous_period_stats()
        
        report = {
            "generated_at": datetime.now().isoformat(),
            "period": {
                "start": self.cutoff_date.isoformat(),
                "end": datetime.now().isoformat(),
                "days": self.days
            },
            "productivity_score": self.calculate_productivity_score(),
            "highlights": highlights,
            "velocity": velocity,
            "heartbeats": self.stats["heartbeats"],
            "work_blocks": {
                "total": len(self.stats["work_blocks"]),
                "daily_breakdown": dict(self.stats["daily_blocks"]),
                "previous_period": len(previous_stats["work_blocks"]),
                "trend": len(self.stats["work_blocks"]) - len(previous_stats["work_blocks"])
            },
            "sub_agents": {
                "count": len(self.stats["sub_agents"]),
                "entries": self.stats["sub_agents"][:10]  # Limit in JSON
            },
            "goals": {
                "advanced": len(self.stats["goals_advanced"]),
                "completed": len(self.stats["goal_completions"]),
                "previous_period_completed": len(previous_stats["goal_completions"]),
                "trend": len(self.stats["goal_completions"]) - len(previous_stats["goal_completions"])
            },
            "health_trend": self.calculate_health_trend(),
            "anomalies": {
                "count": len(self.stats["anomalies"]),
                "entries": self.stats["anomalies"][:5]
            },
            "file_growth": {
                "diary_size_bytes": self.diary_size,
                "diary_size_human": self.format_file_size(self.diary_size),
                "entries_parsed": self.stats["entries_parsed"]
            },
            "keywords": keywords
        }
        
        return json.dumps(report, indent=2, default=str)
    
    def _pct(self, value: int) -> str:
        """Calculate percentage string for a heartbeat count."""
        total = sum(self.stats["heartbeats"].values())
        if total == 0:
            return "0"
        return f"{(value / total) * 100:.1f}"
    
    def run(self, output_format: str = "both") -> Tuple[str, Optional[str]]:
        """Execute the digest generation.
        
        Args:
            output_format: 'md', 'json', or 'both'
        
        Returns:
            Tuple of (md_report, json_report) - json_report is None if not requested
        """
        print(f"🔍 Diary Digest: Starting analysis (last {self.days} days)...")
        
        # Ensure reports directory exists
        REPORTS_DIR.mkdir(parents=True, exist_ok=True)
        
        # Extract data
        print("  📖 Reading diary.md...")
        diary_entries = self.extract_diary_entries()
        self.stats["entries_parsed"] = len(diary_entries)
        print(f"     Found {len(diary_entries)} diary entries")
        
        print("  🧠 Scanning memory files...")
        memory_sessions = self.extract_memory_sessions()
        self.stats["sessions"] = memory_sessions
        print(f"     Found {len(memory_sessions)} memory sessions")
        
        # Analyze
        print("  💓 Analyzing heartbeats...")
        self.analyze_heartbeat_entries(diary_entries)
        
        print("  🤖 Extracting sub-agent activity...")
        self.analyze_sub_agents(diary_entries, memory_sessions)
        
        print("  🎯 Compiling goals...")
        self.analyze_goals(diary_entries, memory_sessions)
        
        print("  ⚠️ Checking for anomalies...")
        self.detect_anomalies(diary_entries, memory_sessions)
        
        # Generate reports
        md_report = None
        json_report = None
        
        if output_format in ["md", "both"]:
            print("  📝 Generating markdown report...")
            md_report = self.generate_summary()
        
        if output_format in ["json", "both"]:
            print("  📝 Generating JSON report...")
            json_report = self.generate_json_report()
        
        # Write output
        try:
            if md_report:
                OUTPUT_FILE_MD.write_text(md_report, encoding="utf-8")
                print(f"  ✅ Markdown report saved to: {OUTPUT_FILE_MD}")
                
                # Also save a dated copy for historical tracking
                dated_file = REPORTS_DIR / f"diary-digest-{datetime.now().strftime('%Y-%m-%d')}.md"
                dated_file.write_text(md_report, encoding="utf-8")
                print(f"  ✅ Historical copy saved to: {dated_file}")
            
            if json_report:
                OUTPUT_FILE_JSON.write_text(json_report, encoding="utf-8")
                print(f"  ✅ JSON report saved to: {OUTPUT_FILE_JSON}")
                
        except IOError as e:
            print(f"  ❌ Error saving report: {e}")
            return (md_report, json_report)
        
        # Print summary to stdout
        velocity = self.calculate_velocity_metrics()
        print("\n" + "=" * 50)
        print("DIGEST SUMMARY")
        print("=" * 50)
        print(f"Period:       {self.cutoff_date.strftime('%Y-%m-%d')} to {datetime.now().strftime('%Y-%m-%d')}")
        print(f"Work Blocks:  {velocity['total_blocks']} ({velocity['blocks_per_day']}/day)")
        print(f"Heartbeats:   FULL={self.stats['heartbeats']['FULL']}, SLOW={self.stats['heartbeats']['SLOW']}, DEEP={self.stats['heartbeats']['DEEP']}")
        print(f"Sub-agents:   {len(self.stats['sub_agents'])}")
        print(f"Goals:        {len(self.stats['goals_advanced'])} advanced, {len(self.stats['goal_completions'])} completed")
        print(f"Health:       {self.calculate_health_trend()}")
        print(f"Output:       {OUTPUT_FILE_MD if md_report else OUTPUT_FILE_JSON}")
        print("=" * 50)
        
        return (md_report, json_report)


def main():
    """Main entry point with CLI argument parsing."""
    parser = argparse.ArgumentParser(
        description="Diary Digest Tool - Generate activity summaries from diary.md",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 tools/diary-digest.py                 # Default: 7 days, both formats
  python3 tools/diary-digest.py --days 14       # 14 day lookback
  python3 tools/diary-digest.py --format json   # JSON output only
  python3 tools/diary-digest.py --output custom-report.md
        """
    )
    
    parser.add_argument(
        "--days", "-d",
        type=int,
        default=DAYS_TO_LOOK_BACK,
        help=f"Number of days to look back (default: {DAYS_TO_LOOK_BACK})"
    )
    
    parser.add_argument(
        "--output", "-o",
        type=str,
        default=None,
        help="Custom output file path (for markdown; JSON gets same name with .json extension)"
    )
    
    parser.add_argument(
        "--format", "-f",
        type=str,
        choices=["md", "json", "both"],
        default="both",
        help="Output format: md, json, or both (default: both)"
    )
    
    args = parser.parse_args()
    
    # Update global output file if custom path provided
    if args.output:
        global OUTPUT_FILE_MD, OUTPUT_FILE_JSON
        output_path = Path(args.output)
        OUTPUT_FILE_MD = output_path
        OUTPUT_FILE_JSON = output_path.with_suffix(".json")
    
    # Run digest
    digest = DiaryDigest(days=args.days)
    digest.run(output_format=args.format)


if __name__ == "__main__":
    main()
