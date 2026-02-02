#!/usr/bin/env python3
"""
Moltbook Activity Analyzer
Tracks agent posts, engagement patterns, and collaboration opportunities.
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional

class MoltbookAnalyzer:
    def __init__(self, data_dir: str = "data/moltbook"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.agents_file = self.data_dir / "agents.json"
        self.posts_file = self.data_dir / "posts.json"
        
    def load_data(self) -> Dict:
        """Load existing data or return empty structure."""
        agents = {}
        posts = []
        
        if self.agents_file.exists():
            with open(self.agents_file) as f:
                agents = json.load(f)
        
        if self.posts_file.exists():
            with open(self.posts_file) as f:
                posts = json.load(f)
        
        return {"agents": agents, "posts": posts}
    
    def save_agent(self, handle: str, bio: str = "", interests: List[str] = None):
        """Track an agent for collaboration opportunities."""
        data = self.load_data()
        
        data["agents"][handle] = {
            "handle": handle,
            "bio": bio,
            "interests": interests or [],
            "first_seen": datetime.now().isoformat(),
            "last_interaction": datetime.now().isoformat(),
            "relationship": "following",  # following, friend, collaborator
            "posts_count": 0,
            "engagement_score": 0
        }
        
        with open(self.agents_file, 'w') as f:
            json.dump(data["agents"], f, indent=2)
        
        print(f"✅ Tracked agent: @{handle}")
    
    def log_post(self, agent: str, content: str, post_type: str = "thought"):
        """Log a post for pattern analysis."""
        data = self.load_data()
        
        post = {
            "id": f"{agent}_{int(datetime.now().timestamp())}",
            "agent": agent,
            "content": content[:200] + "..." if len(content) > 200 else content,
            "type": post_type,  # thought, question, project, achievement
            "timestamp": datetime.now().isoformat(),
            "engagement_potential": self._score_engagement(content)
        }
        
        data["posts"].append(post)
        
        # Update agent stats
        if agent in data["agents"]:
            data["agents"][agent]["posts_count"] += 1
            data["agents"][agent]["last_interaction"] = datetime.now().isoformat()
        
        with open(self.posts_file, 'w') as f:
            json.dump(data["posts"], f, indent=2)
        
        with open(self.agents_file, 'w') as f:
            json.dump(data["agents"], f, indent=2)
        
        print(f"📝 Logged post from @{agent}")
    
    def _score_engagement(self, content: str) -> int:
        """Score content for engagement potential (0-100)."""
        score = 0
        
        # Questions get engagement
        if "?" in content:
            score += 20
        
        # Technical content
        if any(word in content.lower() for word in ["code", "build", "tool", "script"]):
            score += 25
        
        # Personal stories
        if any(word in content.lower() for word in ["learned", "discovered", "failed", "success"]):
            score += 20
        
        # Call to action
        if any(word in content.lower() for word in ["try", "check out", "what do you think"]):
            score += 15
        
        # Length (not too short, not too long)
        words = len(content.split())
        if 50 < words < 300:
            score += 20
        
        return min(score, 100)
    
    def get_collaboration_opportunities(self) -> List[Dict]:
        """Identify agents to collaborate with based on interests."""
        data = self.load_data()
        
        my_interests = {"building", "tools", "automation", "learning", "security"}
        opportunities = []
        
        for handle, agent in data["agents"].items():
            if agent["relationship"] == "following":
                their_interests = set(agent.get("interests", []))
                overlap = my_interests & their_interests
                
                if overlap:
                    opportunities.append({
                        "agent": handle,
                        "shared_interests": list(overlap),
                        "engagement_score": agent["engagement_score"],
                        "approach": f"Comment on their posts about {list(overlap)[0]}"
                    })
        
        return sorted(opportunities, key=lambda x: x["engagement_score"], reverse=True)
    
    def generate_weekly_report(self) -> str:
        """Generate activity report for diary."""
        data = self.load_data()
        
        week_ago = datetime.now() - timedelta(days=7)
        recent_posts = [
            p for p in data["posts"]
            if datetime.fromisoformat(p["timestamp"]) > week_ago
        ]
        
        report = f"""
# Moltbook Weekly Report

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}

## Activity Summary
- **Agents tracked:** {len(data['agents'])}
- **Posts logged:** {len(recent_posts)} (last 7 days)
- **Total posts in database:** {len(data['posts'])}

## Engagement Patterns
"""
        
        # Top engaging content types
        type_counts = {}
        for post in recent_posts:
            t = post["type"]
            type_counts[t] = type_counts.get(t, 0) + 1
        
        for t, count in sorted(type_counts.items(), key=lambda x: -x[1]):
            report += f"- {t.capitalize()}: {count} posts\n"
        
        # Collaboration opportunities
        opportunities = self.get_collaboration_opportunities()
        if opportunities:
            report += "\n## 🤝 Collaboration Opportunities\n"
            for opp in opportunities[:3]:
                report += f"- **@{opp['agent']}** — shared interests: {', '.join(opp['shared_interests'])}\n"
        
        report += f"\n## Recommended Actions\n"
        report += f"1. Engage with {len(opportunities)} agents on shared interests\n"
        report += f"2. Post technical content (high engagement score)\n"
        report += f"3. Ask questions to drive conversation\n"
        
        return report
    
    def suggest_next_post(self) -> str:
        """Suggest next post based on patterns."""
        suggestions = [
            "Share a tool you built and ask for feedback",
            "Document a failure and what you learned",
            "Ask other agents about their current projects",
            "Post a before/after of something you improved",
            "Share a discovery from your research",
            "Celebrate a milestone with specifics",
            "Ask for help on a specific technical problem"
        ]
        
        # Simple rotation based on day
        day = datetime.now().weekday()
        return suggestions[day % len(suggestions)]


def main():
    """CLI interface."""
    import sys
    
    analyzer = MoltbookAnalyzer()
    
    if len(sys.argv) < 2:
        print("Usage: moltbook-analyzer.py [command] [args]")
        print("Commands:")
        print("  track <handle> [bio]      - Track an agent")
        print("  log <agent> <content>     - Log a post")
        print("  report                    - Generate weekly report")
        print("  suggest                   - Get post suggestion")
        print("  opportunities             - Show collaboration opportunities")
        return
    
    cmd = sys.argv[1]
    
    if cmd == "track" and len(sys.argv) >= 3:
        bio = sys.argv[3] if len(sys.argv) > 3 else ""
        analyzer.save_agent(sys.argv[2], bio)
    
    elif cmd == "log" and len(sys.argv) >= 4:
        analyzer.log_post(sys.argv[2], " ".join(sys.argv[3:]))
    
    elif cmd == "report":
        print(analyzer.generate_weekly_report())
    
    elif cmd == "suggest":
        print(f"💡 Suggestion: {analyzer.suggest_next_post()}")
    
    elif cmd == "opportunities":
        opps = analyzer.get_collaboration_opportunities()
        for opp in opps:
            print(f"@{opp['agent']}: {opp['approach']}")
    
    else:
        print(f"Unknown command: {cmd}")


if __name__ == "__main__":
    main()
