#!/usr/bin/env python3
"""
Dashboard Auto-Updater
Updates dashboard/index.html with real metrics from diary/logs.
"""

import json
import re
from datetime import datetime
from pathlib import Path

class DashboardUpdater:
    """Updates the Nova OS dashboard with live metrics."""
    
    def __init__(self):
        self.workspace = Path("/home/node/.openclaw/workspace")
        self.dashboard = self.workspace / "dashboard" / "index.html"
        self.diary = self.workspace / "diary.md"
    
    def count_files(self) -> int:
        """Count total files in workspace."""
        count = 0
        for root, dirs, files in os.walk(self.workspace):
            # Skip hidden dirs
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            count += len(files)
        return count
    
    def count_tools(self) -> int:
        """Count tools in tools/ directory."""
        tools_dir = self.workspace / "tools"
        if not tools_dir.exists():
            return 0
        return len(list(tools_dir.glob("*.py")))
    
    def count_heartbeats(self) -> int:
        """Estimate heartbeats from diary."""
        if not self.diary.exists():
            return 0
        content = self.diary.read_text()
        return len(re.findall(r'\[FULL\]', content))
    
    def days_active(self) -> int:
        """Calculate days since first diary entry."""
        if not self.diary.exists():
            return 0
        # First line with date
        content = self.diary.read_text()
        dates = re.findall(r'\d{4}-\d{2}-\d{2}', content)
        if dates:
            first = datetime.strptime(dates[0], "%Y-%m-%d")
            return (datetime.now() - first).days + 1
        return 0
    
    def update_html(self):
        """Update the dashboard HTML with current metrics."""
        if not self.dashboard.exists():
            print("Dashboard not found. Run this from workspace root.")
            return False
        
        html = self.dashboard.read_text()
        
        # Update timestamp
        html = re.sub(
            r'Last updated: <span id="timestamp">[^<]*</span>',
            f'Last updated: <span id="timestamp">{datetime.now().isoformat()}</span>',
            html
        )
        
        # Note: Real-time metrics would require serving dynamic content
        # For now, we update the static template
        
        self.dashboard.write_text(html)
        print(f"✅ Dashboard updated at {datetime.now().isoformat()}")
        return True
    
    def generate_json_feed(self):
        """Generate JSON data feed for dynamic dashboard."""
        data = {
            "timestamp": datetime.now().isoformat(),
            "metrics": {
                "files": self.count_files(),
                "tools": self.count_tools(),
                "heartbeats": self.count_heartbeats(),
                "days_active": self.days_active()
            },
            "status": "online",
            "version": "1.0"
        }
        
        feed_path = self.workspace / "dashboard" / "metrics.json"
        feed_path.write_text(json.dumps(data, indent=2))
        print(f"✅ Metrics feed: {feed_path}")
        return data


def main():
    """CLI entry point."""
    import os
    
    updater = DashboardUpdater()
    
    # Update static HTML
    updater.update_html()
    
    # Generate JSON feed
    updater.generate_json_feed()
    
    print("\n📊 Dashboard ready for deployment to GitHub Pages")


if __name__ == "__main__":
    main()
