#!/usr/bin/env python3
"""
Diary Digest Tool - Weekly Activity Summary Generator

RUN COMMAND:
    python3 tools/diary-digest.py
    
    Or make executable and run directly:
    chmod +x tools/diary-digest.py
    ./tools/diary-digest.py

USAGE:
    - Run weekly to generate a summary of Nova's activity
    - Can be scheduled via cron: 0 9 * * 1 /usr/bin/python3 /path/to/tools/diary-digest.py
    - Output saved to reports/diary-digest-latest.md

FEATURES:
    - Parses diary.md for heartbeat entries, goals, and sub-agent activity
    - Scans memory/ directory for session summaries
    - Calculates health trends and activity metrics
    - Handles edge cases: empty files, missing dates, malformed entries
"""

import os
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple, Optional

# Configuration
DIARY_PATH = Path("diary.md")
MEMORY_DIR = Path("memory")
REPORTS_DIR = Path("reports")
OUTPUT_FILE = REPORTS_DIR / "diary-digest-latest.md"
DAYS_TO_LOOK_BACK = 7


class DiaryDigest:
    """Generates weekly activity summaries from diary and memory files."""
    
    def __init__(self):
        self.cutoff_date = datetime.now() - timedelta(days=DAYS_TO_LOOK_BACK)
        self.stats = {
            "heartbeats": {"FULL": 0, "SLOW": 0, "DEEP": 0, "UNKNOWN": 0},
            "sub_agents": [],
            "goals_advanced": [],
            "anomalies": [],
            "sessions": [],
            "entries_parsed": 0,
        }
        self.health_scores = []  # For trend calculation
        
    def parse_timestamp(self, ts_str: str) -> Optional[datetime]:
        """Parse various timestamp formats found in diary entries."""
        formats = [
            "%Y-%m-%dT%H:%M:%SZ",
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
        
        # Pattern for diary entries with timestamp
        # Matches: [TYPE] YYYY-MM-DDTHH:MM:SSZ followed by content until next [ or end
        # TYPE can contain letters, spaces, underscores
        entry_pattern = r'^\[([\w\s]+)\]\s+(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)(.*?)(?=\n\[|\Z)'
        
        for match in re.finditer(entry_pattern, content, re.MULTILINE | re.DOTALL):
            entry_type = match.group(1).strip()
            timestamp_str = match.group(2)
            content_block = match.group(3).strip()
            
            timestamp = self.parse_timestamp(timestamp_str)
            if timestamp and timestamp >= self.cutoff_date:
                entries.append({
                    "type": entry_type,
                    "timestamp": timestamp,
                    "content": content_block,
                    "source": "diary.md"
                })
        
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
        
        # Factor in sub-agent activity
        subagent_count = len(self.stats["sub_agents"])
        goal_count = len(self.stats["goals_advanced"])
        
        if health_ratio > 0.7 and subagent_count >= 2 and goal_count >= 1:
            return "IMPROVING"
        elif health_ratio > 0.5 or (subagent_count >= 1 or goal_count >= 1):
            return "STABLE"
        elif health_ratio < 0.3 or len(self.stats["anomalies"]) > 3:
            return "DECLINING"
        else:
            return "STABLE"
    
    def generate_summary(self) -> str:
        """Generate the markdown summary report."""
        now = datetime.now()
        start_date = self.cutoff_date
        
        report = f"""# 📊 Diary Digest - Weekly Activity Summary

**Period:** {start_date.strftime("%Y-%m-%d")} to {now.strftime("%Y-%m-%d")}  
**Generated:** {now.strftime("%Y-%m-%d %H:%M:%S UTC")}

---

## 📈 Activity Overview

| Metric | Count |
|--------|-------|
| **Total Entries Parsed** | {self.stats["entries_parsed"]} |
| **Memory Sessions** | {len(self.stats["sessions"])} |
| **Sub-Agents Spawned** | {len(self.stats["sub_agents"])} |
| **Goals Advanced** | {len(self.stats["goals_advanced"])} |
| **Anomalies Detected** | {len(self.stats["anomalies"])} |

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
            report += """✅ Strong activity levels with productive sub-agent work and goal progression. 
Full heartbeats dominate, indicating healthy system operation.
"""
        elif trend == "STABLE":
            report += """✅ Consistent activity with moderate goal advancement. 
System operating within normal parameters.
"""
        elif trend == "DECLINING":
            report += """⚠️ Lower than normal activity detected. Fewer heartbeats or reduced sub-agent activity.
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
- **Lookback period:** {DAYS_TO_LOOK_BACK} days

---

*Generated by Diary Digest Tool v1.0*  
*Run manually or schedule via cron for weekly updates*
"""
        
        return report
    
    def _pct(self, value: int) -> str:
        """Calculate percentage string for a heartbeat count."""
        total = sum(self.stats["heartbeats"].values())
        if total == 0:
            return "0"
        return f"{(value / total) * 100:.1f}"
    
    def run(self) -> str:
        """Execute the digest generation."""
        print("🔍 Diary Digest: Starting analysis...")
        
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
        
        # Generate report
        print("  📝 Generating report...")
        report = self.generate_summary()
        
        # Write output
        try:
            OUTPUT_FILE.write_text(report, encoding="utf-8")
            print(f"  ✅ Report saved to: {OUTPUT_FILE}")
            
            # Also save a dated copy for historical tracking
            dated_file = REPORTS_DIR / f"diary-digest-{datetime.now().strftime('%Y-%m-%d')}.md"
            dated_file.write_text(report, encoding="utf-8")
            print(f"  ✅ Historical copy saved to: {dated_file}")
        except IOError as e:
            print(f"  ❌ Error saving report: {e}")
            return report
        
        # Print summary to stdout
        print("\n" + "=" * 50)
        print("DIGEST SUMMARY")
        print("=" * 50)
        print(f"Period:     {self.cutoff_date.strftime('%Y-%m-%d')} to {datetime.now().strftime('%Y-%m-%d')}")
        print(f"Heartbeats: FULL={self.stats['heartbeats']['FULL']}, SLOW={self.stats['heartbeats']['SLOW']}, DEEP={self.stats['heartbeats']['DEEP']}")
        print(f"Sub-agents: {len(self.stats['sub_agents'])}")
        print(f"Goals:      {len(self.stats['goals_advanced'])}")
        print(f"Health:     {self.calculate_health_trend()}")
        print(f"Output:     {OUTPUT_FILE}")
        print("=" * 50)
        
        return report


def main():
    """Main entry point."""
    digest = DiaryDigest()
    digest.run()


if __name__ == "__main__":
    main()
