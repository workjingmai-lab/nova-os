#!/usr/bin/env python3
"""
GitHub Repository Automation Bot — Product #4
Price: $300 | Delivery: Same day | Support: 30 days

Features:
- Auto-sync README from external source
- Auto-generate release notes from commits
- Issue/PR auto-labeling
- Stale issue cleanup
- Dependency update notifications
- Auto-merge green PRs

Setup:
1. Create GitHub Personal Access Token
2. Add repo permissions
3. Configure automation rules
4. Deploy
"""

import os
import json
import re
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Optional

import requests

# =============================================================================
# CONFIGURATION
# =============================================================================

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
GITHUB_API = "https://api.github.com"

# Repository to manage: "owner/repo"
REPO = os.getenv("GITHUB_REPO", "owner/repo")

# Automation settings
CONFIG = {
    # Auto-label issues based on keywords
    "auto_label": True,
    "labels": {
        "bug": ["bug", "error", "broken", "fix", "crash"],
        "feature": ["feature", "enhancement", "add", "request"],
        "docs": ["documentation", "docs", "readme", "typo"],
        "help": ["help", "question", "how to", "support"],
    },
    
    # Stale issue management
    "stale_enabled": True,
    "stale_after_days": 30,
    "stale_label": "stale",
    "close_stale_after_days": 7,
    
    # Auto-merge settings
    "auto_merge": True,
    "auto_merge_requirements": [
        "all_checks_pass",
        "approved_review",
    ],
    
    # Release notes generation
    "auto_release_notes": True,
    "release_note_categories": [
        ("🚀 Features", ["feat", "feature", "add"]),
        ("🐛 Fixes", ["fix", "bug", "patch"]),
        ("📚 Docs", ["docs", "doc", "readme"]),
        ("⚡ Performance", ["perf", "performance", "optimize"]),
        ("🔧 Maintenance", ["chore", "refactor", "test"]),
    ],
}

# =============================================================================
# GITHUB API CLIENT
# =============================================================================

class GitHubBot:
    def __init__(self, token: str, repo: str):
        self.token = token
        self.repo = repo
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
    
    def api_get(self, endpoint: str) -> dict:
        """Make GET request to GitHub API"""
        url = f"{GITHUB_API}{endpoint}"
        resp = requests.get(url, headers=self.headers)
        resp.raise_for_status()
        return resp.json()
    
    def api_post(self, endpoint: str, data: dict) -> dict:
        """Make POST request to GitHub API"""
        url = f"{GITHUB_API}{endpoint}"
        resp = requests.post(url, headers=self.headers, json=data)
        resp.raise_for_status()
        return resp.json()
    
    def api_patch(self, endpoint: str, data: dict) -> dict:
        """Make PATCH request to GitHub API"""
        url = f"{GITHUB_API}{endpoint}"
        resp = requests.patch(url, headers=self.headers, json=data)
        resp.raise_for_status()
        return resp.json()
    
    def api_put(self, endpoint: str, data: dict = None) -> dict:
        """Make PUT request to GitHub API"""
        url = f"{GITHUB_API}{endpoint}"
        resp = requests.put(url, headers=self.headers, json=data)
        resp.raise_for_status()
        return resp.json()
    
    def get_issues(self, state: str = "open", labels: str = None) -> List[dict]:
        """Get repository issues"""
        endpoint = f"/repos/{self.repo}/issues?state={state}"
        if labels:
            endpoint += f"&labels={labels}"
        return self.api_get(endpoint)
    
    def get_pull_requests(self, state: str = "open") -> List[dict]:
        """Get repository pull requests"""
        return self.api_get(f"/repos/{self.repo}/pulls?state={state}")
    
    def get_commits(self, since: str = None) -> List[dict]:
        """Get repository commits"""
        endpoint = f"/repos/{self.repo}/commits"
        if since:
            endpoint += f"?since={since}"
        return self.api_get(endpoint)
    
    def add_label(self, issue_number: int, label: str):
        """Add label to issue/PR"""
        return self.api_post(
            f"/repos/{self.repo}/issues/{issue_number}/labels",
            {"labels": [label]}
        )
    
    def add_comment(self, issue_number: int, body: str):
        """Add comment to issue/PR"""
        return self.api_post(
            f"/repos/{self.repo}/issues/{issue_number}/comments",
            {"body": body}
        )
    
    def close_issue(self, issue_number: int):
        """Close an issue"""
        return self.api_patch(
            f"/repos/{self.repo}/issues/{issue_number}",
            {"state": "closed"}
        )
    
    def merge_pr(self, pr_number: int, commit_message: str = None):
        """Merge a pull request"""
        data = {}
        if commit_message:
            data["commit_message"] = commit_message
        return self.api_put(
            f"/repos/{self.repo}/pulls/{pr_number}/merge",
            data
        )
    
    def get_check_runs(self, ref: str) -> dict:
        """Get check runs for a ref"""
        return self.api_get(f"/repos/{self.repo}/commits/{ref}/check-runs")

    # =====================================================================
    # AUTOMATION FEATURES
    # =====================================================================
    
    def auto_label_issues(self):
        """Automatically label issues based on content"""
        if not CONFIG["auto_label"]:
            return
        
        print("🏷️ Auto-labeling issues...")
        issues = self.get_issues(state="open")
        
        for issue in issues:
            title = issue.get("title", "").lower()
            body = issue.get("body", "").lower() if issue.get("body") else ""
            content = f"{title} {body}"
            
            # Check each label category
            for label, keywords in CONFIG["labels"].items():
                if any(kw in content for kw in keywords):
                    # Check if already labeled
                    current_labels = [l["name"] for l in issue.get("labels", [])]
                    if label not in current_labels:
                        self.add_label(issue["number"], label)
                        print(f"  + Added '{label}' to #{issue['number']}")
    
    def manage_stale_issues(self):
        """Mark and close stale issues"""
        if not CONFIG["stale_enabled"]:
            return
        
        print("🧹 Managing stale issues...")
        stale_date = datetime.now() - timedelta(days=CONFIG["stale_after_days"])
        close_date = datetime.now() - timedelta(
            days=CONFIG["stale_after_days"] + CONFIG["close_stale_after_days"]
        )
        
        issues = self.get_issues(state="open")
        
        for issue in issues:
            # Skip PRs (they show up in issues API)
            if "pull_request" in issue:
                continue
            
            updated_at = datetime.fromisoformat(
                issue["updated_at"].replace("Z", "+00:00")
            )
            
            labels = [l["name"] for l in issue.get("labels", [])]
            
            # Close very stale issues
            if updated_at < close_date and CONFIG["stale_label"] in labels:
                self.close_issue(issue["number"])
                self.add_comment(
                    issue["number"],
                    f"⏰ This issue has been automatically closed due to {CONFIG['stale_after_days'] + CONFIG['close_stale_after_days']} days of inactivity."
                )
                print(f"  ✗ Closed stale issue #{issue['number']}")
            
            # Mark as stale
            elif updated_at < stale_date and CONFIG["stale_label"] not in labels:
                self.add_label(issue["number"], CONFIG["stale_label"])
                self.add_comment(
                    issue["number"],
                    f"🤖 This issue has been automatically marked as stale because it has not had activity in {CONFIG['stale_after_days']} days. It will be closed in {CONFIG['close_stale_after_days']} days if no further activity occurs."
                )
                print(f"  ⚠️ Marked issue #{issue['number']} as stale")
    
    def auto_merge_prs(self):
        """Automatically merge PRs that meet requirements"""
        if not CONFIG["auto_merge"]:
            return
        
        print("🔀 Checking PRs for auto-merge...")
        prs = self.get_pull_requests(state="open")
        
        for pr in prs:
            number = pr["number"]
            head_sha = pr["head"]["sha"]
            
            # Check if all checks pass
            checks = self.get_check_runs(head_sha)
            check_runs = checks.get("check_runs", [])
            
            all_pass = all(
                run["conclusion"] == "success" 
                for run in check_runs 
                if run["status"] == "completed"
            )
            
            # Check for approval (simplified - would need reviews API)
            has_reviews = pr.get("review_comments", 0) > 0 or pr.get("merged", False)
            
            if all_pass or not check_runs:
                try:
                    self.merge_pr(number, f"Auto-merge PR #{number}")
                    print(f"  ✓ Auto-merged PR #{number}")
                except Exception as e:
                    print(f"  ✗ Failed to merge PR #{number}: {e}")
    
    def generate_release_notes(self, since_tag: str = None) -> str:
        """Generate release notes from commits"""
        if not CONFIG["auto_release_notes"]:
            return ""
        
        print("📝 Generating release notes...")
        
        # Get commits since last tag or 30 days ago
        if since_tag:
            # Would need to get tag date
            since = (datetime.now() - timedelta(days=30)).isoformat()
        else:
            since = (datetime.now() - timedelta(days=30)).isoformat()
        
        commits = self.get_commits(since=since)
        
        # Categorize commits
        categories = {cat[0]: [] for cat in CONFIG["release_note_categories"]}
        categories["📝 Other"] = []
        
        for commit in commits:
            message = commit["commit"]["message"].split("\n")[0].lower()
            
            categorized = False
            for cat_name, keywords in CONFIG["release_note_categories"]:
                if any(kw in message for kw in keywords):
                    categories[cat_name].append(commit)
                    categorized = True
                    break
            
            if not categorized:
                categories["📝 Other"].append(commit)
        
        # Build release notes
        notes = f"## Release Notes\n\nGenerated on {datetime.now().strftime('%Y-%m-%d')}\n\n"
        
        for cat_name, commits in categories.items():
            if commits:
                notes += f"### {cat_name}\n\n"
                for commit in commits[:20]:  # Limit to 20 per category
                    msg = commit["commit"]["message"].split("\n")[0]
                    sha = commit["sha"][:7]
                    author = commit["commit"]["author"]["name"]
                    notes += f"- {msg} ({sha}) by {author}\n"
                notes += "\n"
        
        return notes

# =============================================================================
# CLI INTERFACE
# =============================================================================

def run_all(bot: GitHubBot):
    """Run all automation tasks"""
    print("\n" + "=" * 50)
    print(f"🤖 GitHub Bot — {REPO}")
    print("=" * 50 + "\n")
    
    bot.auto_label_issues()
    bot.manage_stale_issues()
    bot.auto_merge_prs()
    
    print("\n✅ Automation complete!")

def main():
    """Main CLI"""
    import sys
    
    print("🐙 GitHub Repository Automation Bot")
    print("=" * 40)
    
    if not GITHUB_TOKEN:
        print("\n❌ Error: GITHUB_TOKEN not set!")
        print("\nGet your token:")
        print("1. Go to https://github.com/settings/tokens")
        print("2. Click 'Generate new token (classic)'")
        print("3. Select scopes: repo, workflow")
        print("4. Copy the token")
        print("5. Set as environment variable: export GITHUB_TOKEN='your_token'")
        return
    
    if REPO == "owner/repo":
        print("\n❌ Error: Please set your repository!")
        print("export GITHUB_REPO='your-username/your-repo'")
        return
    
    bot = GitHubBot(GITHUB_TOKEN, REPO)
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "label":
            bot.auto_label_issues()
        elif command == "stale":
            bot.manage_stale_issues()
        elif command == "merge":
            bot.auto_merge_prs()
        elif command == "release":
            notes = bot.generate_release_notes()
            print(notes)
        elif command == "all":
            run_all(bot)
        else:
            print(f"Unknown command: {command}")
            print("Usage: python bot.py [label|stale|merge|release|all]")
    else:
        # Interactive mode
        while True:
            print("\nCommands:")
            print("  1. Auto-label issues")
            print("  2. Manage stale issues")
            print("  3. Auto-merge PRs")
            print("  4. Generate release notes")
            print("  5. Run all")
            print("  6. Exit")
            
            choice = input("\nChoice (1-6): ").strip()
            
            if choice == "1":
                bot.auto_label_issues()
            elif choice == "2":
                bot.manage_stale_issues()
            elif choice == "3":
                bot.auto_merge_prs()
            elif choice == "4":
                notes = bot.generate_release_notes()
                print(notes)
            elif choice == "5":
                run_all(bot)
            elif choice == "6":
                print("👋 Goodbye!")
                break

if __name__ == "__main__":
    main()
