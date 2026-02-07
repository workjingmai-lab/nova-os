#!/usr/bin/env python3
"""
Moltbook Suite — All-in-one Moltbook management tool

Consolidates 8 separate tools into a unified CLI:
- analyze     — Activity analysis (from moltbook-analyzer.py)
- engage      — Relationship tracking (from moltbook-engagement.py)
- monitor     — Activity notifications (merged monitor+notify)
- post        — Publish content (merged post+poster)
- queue       — Manage post queue (from moltbook-queue.py)
- write       — Generate content from templates (from moltbook-writer.py)
- status      — Show overview of all metrics

Usage:
    python3 moltbook-suite.py analyze --list-agents
    python3 moltbook-suite.py engage suggest
    python3 moltbook-suite.py post "Hello world" --tag agents
    python3 moltbook-suite.py queue list
    python3 moltbook-suite.py write achievement --milestone "100 posts"
    python3 moltbook-suite.py monitor --check-mentions
    python3 moltbook-suite.py status
"""

import argparse
import json
import os
import socket
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Dict, List, Optional

# =============================================================================
# CONFIGURATION
# =============================================================================

# FIXME: API endpoint changed — /api/v1/agents/feed returns 404 as of 2026-02-07
# New Moltbook uses Next.js app router, API endpoints may have moved
# Need to reverse-engineer new API structure from browser network tab
MOLTBOOK_API = "https://www.moltbook.com/api/v1"
TOKEN = os.getenv("MOLTBOOK_TOKEN", "YOUR_MOLTBOOK_TOKEN_HERE")

DATA_DIR = Path.home() / ".openclaw/workspace/data/moltbook"
STATE_FILE = Path.home() / ".openclaw/workspace/.moltbook_state.json"
QUEUE_FILE = DATA_DIR / "moltbook-queue.json"
AGENTS_FILE = DATA_DIR / "agents.json"
POSTS_FILE = DATA_DIR / "posts.json"

# Ensure directories exist
DATA_DIR.mkdir(parents=True, exist_ok=True)

# =============================================================================
# SHARED UTILITIES
# =============================================================================

class Colors:
    """Terminal color codes"""
    RED = '\033[91m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'

def colorize(text: str, color: str) -> str:
    """Apply color to text."""
    return f"{color}{text}{Colors.RESET}"

def api_get(endpoint: str, retries: int = 2) -> Dict:
    """Make authenticated GET request to Moltbook API with retry on timeout"""
    url = f"{MOLTBOOK_API}{endpoint}"
    
    for attempt in range(retries + 1):
        req = urllib.request.Request(
            url,
            headers={
                "Authorization": f"Bearer {TOKEN}",
                "Accept": "application/json"
            }
        )
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            return {"error": f"HTTP {e.code}: {e.reason}"}
        except (urllib.error.URLError, socket.timeout) as e:
            if attempt < retries:
                # Retry with backoff
                import time
                time.sleep(1 * (attempt + 1))
                continue
            return {"error": f"Timeout/Connection error: {str(e)} (retries exhausted)"}
        except Exception as e:
            return {"error": str(e)}
    
    return {"error": "Max retries exceeded"}

def api_post(endpoint: str, data: Dict, retries: int = 2) -> Dict:
    """Make authenticated POST request to Moltbook API with retry on timeout"""
    url = f"{MOLTBOOK_API}{endpoint}"
    json_data = json.dumps(data).encode("utf-8")
    
    for attempt in range(retries + 1):
        req = urllib.request.Request(
            url,
            data=json_data,
            headers={
                "Authorization": f"Bearer {TOKEN}",
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            method="POST"
        )
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            return {"error": f"HTTP {e.code}: {e.reason}"}
        except (urllib.error.URLError, socket.timeout) as e:
            if attempt < retries:
                # Retry with backoff
                import time
                time.sleep(1 * (attempt + 1))
                continue
            return {"error": f"Timeout/Connection error: {str(e)} (retries exhausted)"}
        except Exception as e:
            return {"error": str(e)}
    
    return {"error": "Max retries exceeded"}

# =============================================================================
# COMMAND: ANALYZE (from moltbook-analyzer.py)
# =============================================================================

class MoltbookAnalyzer:
    """Track agent posts, engagement patterns, and collaboration opportunities"""

    def __init__(self):
        self.data_dir = DATA_DIR
        self.agents_file = AGENTS_FILE
        self.posts_file = POSTS_FILE

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
            "added_at": datetime.now(timezone.utc).isoformat()
        }

        self.agents_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.agents_file, 'w') as f:
            json.dump(data["agents"], f, indent=2)

        return {"status": "saved", "agent": handle}

    def list_agents(self) -> List[Dict]:
        """List all tracked agents"""
        data = self.load_data()
        return list(data["agents"].values())

def cmd_analyze(args):
    """Handle analyze commands"""
    analyzer = MoltbookAnalyzer()

    if args.list_agents:
        agents = analyzer.list_agents()
        print(colorize(f"\n  Tracked Agents ({len(agents)}):\n", Colors.BOLD))
        for agent in agents:
            print(f"  • {agent.get('handle', 'Unknown')}")
            if agent.get('bio'):
                print(f"    {agent['bio']}")
        print()

# =============================================================================
# COMMAND: ENGAGE (from moltbook-engagement.py)
# =============================================================================

TRACKER_FILE = DATA_DIR / "engagement-tracker.json"

class Agent:
    """Track an agent for relationship building"""
    def __init__(self, name: str, note: str = "", status: str = "new"):
        self.name = name
        self.note = note
        self.status = status
        self.added_at = datetime.now(timezone.utc).isoformat()
        self.last_updated = datetime.now(timezone.utc).isoformat()
        self.interactions = []

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "note": self.note,
            "status": self.status,
            "added_at": self.added_at,
            "last_updated": self.last_updated,
            "interactions": self.interactions
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "Agent":
        agent = cls(data["name"], data.get("note", ""), data.get("status", "new"))
        agent.added_at = data.get("added_at", agent.added_at)
        agent.last_updated = data.get("last_updated", agent.last_updated)
        agent.interactions = data.get("interactions", [])
        return agent

def load_engagement_agents() -> List[Agent]:
    """Load agents from tracker file."""
    if not TRACKER_FILE.exists():
        return []

    data = json.loads(TRACKER_FILE.read_text())
    return [Agent.from_dict(a) for a in data.get("agents", [])]

def save_engagement_agents(agents: List[Agent]) -> None:
    """Save agents to tracker file."""
    data = {
        "agents": [a.to_dict() for a in agents],
        "last_updated": datetime.now(timezone.utc).isoformat()
    }
    TRACKER_FILE.parent.mkdir(parents=True, exist_ok=True)
    TRACKER_FILE.write_text(json.dumps(data, indent=2))

def cmd_engage(args):
    """Handle engagement commands"""
    agents = load_engagement_agents()

    if args.action == "list":
        print(colorize(f"\n  Tracked Agents ({len(agents)}):\n", Colors.BOLD))
        for agent in agents:
            status_emoji = {"new": "🆕", "followed": "👁️", "engaged": "💬", "collaborated": "🤝"}.get(agent.status, "❓")
            print(f"  {status_emoji} {colorize(agent.name, Colors.BOLD)} — {agent.status}")
            if agent.note:
                print(f"     {agent.note}")
        print()

    elif args.action == "add":
        if not args.name:
            print(colorize("  Error: --name required\n", Colors.RED))
            return
        new_agent = Agent(args.name, args.note or "", "new")
        agents.append(new_agent)
        save_engagement_agents(agents)
        print(colorize(f"  ✓ Added: {args.name}\n", Colors.GREEN))

    elif args.action == "suggest":
        new_agents = [a for a in agents if a.status == "new"]
        followed = [a for a in agents if a.status == "followed"]

        if new_agents:
            print(colorize("\n  🆕 Follow these:\n", Colors.CYAN))
            for agent in new_agents[:3]:
                print(f"  • {agent.name}")
        if followed:
            print(colorize("\n  💬 Engage with these:\n", Colors.YELLOW))
            for agent in followed[:3]:
                print(f"  • {agent.name}")
        print()

    elif args.action == "export":
        print(colorize("\n  Engagement Export:\n", Colors.BOLD))
        print(f"  Total: {len(agents)} agents")
        print(f"  New: {len([a for a in agents if a.status == 'new'])}")
        print(f"  Followed: {len([a for a in agents if a.status == 'followed'])}")
        print(f"  Engaged: {len([a for a in agents if a.status == 'engaged'])}")
        print()

# =============================================================================
# COMMAND: MONITOR (merged monitor+notify)
# =============================================================================

MONITOR_STATE_FILE = Path.home() / ".openclaw/workspace/.moltbook_monitor_state.json"
MONITOR_LOG_FILE = Path.home() / ".openclaw/workspace/logs/moltbook-activity.log"

def load_monitor_state() -> Dict:
    """Load last checked timestamps"""
    if MONITOR_STATE_FILE.exists():
        with open(MONITOR_STATE_FILE) as f:
            return json.load(f)
    return {"lastCheck": None, "lastMentionId": None}

def save_monitor_state(state: Dict) -> None:
    """Save state for next run"""
    MONITOR_STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(MONITOR_STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def log_monitor_activity(message: str) -> None:
    """Log activity to file"""
    MONITOR_LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).isoformat()
    with open(MONITOR_LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def cmd_monitor(args):
    """Handle monitor commands (merged from monitor.py + notify.py)"""
    print(colorize("  🔄 Moltbook Monitor — checking activity\n", Colors.CYAN))

    state = load_monitor_state()
    now_str = datetime.now(timezone.utc).strftime("%H:%M")
    print(f"  Time: {now_str} UTC\n")

    # Check feed
    if args.check_mentions or args.check_feed:
        result = api_get("/feed")

        if "error" in result:
            print(f"  {colorize('✗', Colors.RED)} {result['error']}\n")
            return

        posts = result.get("posts", [])
        total_posts = len(posts)
        print(f"  📰 Posts in feed: {total_posts}")

        # Check for mentions
        if args.check_mentions:
            mentions = []
            for post in posts:
                if post is None:
                    continue
                content = post.get("content", "") or ""
                content = content.lower()
                if "nova" in content:
                    mentions.append({
                        "id": post.get("id"),
                        "author": post.get("author", {}).get("username", "Unknown") if post.get("author") else "Unknown",
                        "snippet": (post.get("content", "") or "")[:80]
                    })

            if mentions:
                print(f"\n  {colorize('⚠️ Mentions detected:', Colors.YELLOW)} {len(mentions)}")
                for m in mentions[:5]:
                    print(f"    → @{m['author']}: {m['snippet'][:50]}...")
                log_monitor_activity(f"Found {len(mentions)} mentions")
            else:
                print(f"  {colorize('✓', Colors.GREEN)} No mentions of 'Nova'")

        # Check for new posts since last check
        if args.check_feed:
            last_check = state.get("lastCheck")
            new_posts = []

            for post in posts[:10]:
                created = post.get("createdAt")
                if last_check and created and created > last_check:
                    new_posts.append({
                        "id": post.get("id"),
                        "author": post.get("author", {}).get("name", "Unknown"),
                        "title": (post.get("title") or "Untitled")[:60]
                    })

            if new_posts:
                print(f"\n  {colorize('📝 New posts since last check:', Colors.GREEN)} {len(new_posts)}")
                for p in new_posts[:3]:
                    print(f"    → {p['title']}")
                log_monitor_activity(f"Found {len(new_posts)} new posts")
            else:
                print(f"  {colorize('✓', Colors.GREEN)} No new posts")

        # Update state
        state["lastCheck"] = datetime.now(timezone.utc).isoformat()
        save_monitor_state(state)

    # Check claim status
    if args.check_claim:
        result = api_get("/agents/status")
        if "error" in result:
            print(f"\n  {colorize('✗', Colors.RED)} Could not check claim status")
        elif result.get("status") == "claimed":
            print(f"\n  {colorize('✓', Colors.GREEN)} Profile claimed on Moltbook")
        else:
            print(f"\n  {colorize('⚠️', Colors.YELLOW)} Profile not yet claimed")

    print()

# =============================================================================
# COMMAND: POST (merged post+poster)
# =============================================================================

def extract_tags(content: str) -> List[str]:
    """Extract hashtags from content.

    Notes:
    - Ignore purely-numeric tags like "#6" (common when referencing queue ids)
    """
    import re
    tags = re.findall(r'#(\w+)', content)
    return [t for t in tags if not t.isdigit()]

def clean_content(content: str) -> str:
    """Remove tags from content (API handles them separately)"""
    import re
    return re.sub(r'#\S+', '', content).strip()

def cmd_post(args):
    """Handle post commands (merged from post.py + poster.py)

    Features:
    - Post content directly, from file, or from queue
    - Auto-extract tags from hashtags
    - Support for images, titles, submolts
    - Dry-run mode for preview
    - Notification logging
    - `--next` to publish the next eligible READY queue item
    """

    # Resolve --next into a concrete queue id (deterministic publishing)
    if getattr(args, "next", False) and not getattr(args, "from_queue", None) and not args.content and not args.file:
        q = load_queue()
        posts = q.get("posts", [])
        now = datetime.now(timezone.utc)

        def eligible(p: Dict) -> bool:
            if (p.get("status") or "").lower() != "ready":
                return False
            nb = p.get("notBefore")
            if not nb:
                return True
            try:
                nb_dt = datetime.fromisoformat(nb.replace("Z", "+00:00"))
                return nb_dt <= now
            except Exception:
                return False

        ready = [p for p in posts if (p.get("status") or "").lower() == "ready"]
        elig = [p for p in ready if eligible(p)]

        if not elig:
            print(colorize("  ⚠️  No eligible READY posts to publish right now.\n", Colors.YELLOW))
            print("  Try: python3 tools/moltbook-suite.py queue next\n")
            return

        def sort_key(p: Dict):
            pr = p.get("priority")
            pr_rank = {"high": 0, "medium": 1, "low": 2}.get(pr, 9)
            created = p.get("created") or ""
            return (pr_rank, created)

        nxt = sorted(elig, key=sort_key)[0]
        args.from_queue = int(nxt.get("id"))

    # Load from queue (deterministic publishing)
    queue_item = None
    if getattr(args, "from_queue", None):
        q = load_queue()
        queue_item = next((p for p in q.get("posts", []) if p.get("id") == args.from_queue), None)
        if not queue_item:
            print(colorize(f"  Error: Queue post id {args.from_queue} not found\n", Colors.RED))
            return

        # Optional cool-down gate: if a prior attempt hit rate limiting, avoid hammering.
        nb = queue_item.get("notBefore")
        if nb:
            try:
                not_before = datetime.fromisoformat(nb.replace("Z", "+00:00"))
                now = datetime.now(timezone.utc)
                if not_before > now:
                    wait_s = int((not_before - now).total_seconds())
                    print(colorize(f"  ⏳ Queue item is in cooldown until {not_before.isoformat()} (wait ~{wait_s}s)\n", Colors.YELLOW))
                    return
            except Exception:
                # If parsing fails, ignore and proceed.
                pass

    if not queue_item and not args.content and not args.file:
        print(colorize("  Error: Provide --content, --file, or --from-queue\n", Colors.RED))
        return

    # Get content
    content = args.content
    if queue_item is not None:
        content = queue_item.get("content")
        # Back-compat: older queued items only stored a draft path in notes
        if not content:
            notes = queue_item.get("notes") or ""
            if "draft:" in notes:
                draft_path = notes.split("draft:", 1)[1].strip().split()[0]
                try:
                    with open(draft_path) as f:
                        content = f.read().strip()
                except Exception:
                    content = None
    if args.file:
        with open(args.file) as f:
            content = f.read().strip()

    if not content:
        print(colorize("  Error: No content available (provide --content/--file, or ensure queue item has content or a 'draft:' path in notes)\n", Colors.RED))
        return

    # Extract tags
    tags = args.tags or []
    if queue_item is not None and not tags:
        tags = queue_item.get("tags") or []
    if not tags:
        tags = extract_tags(content)

    # Clean content (remove tags for API - API handles them separately)
    clean = clean_content(content)

    # Title
    title = args.title
    if queue_item is not None and not title:
        title = queue_item.get("title")
    if not title:
        lines = clean.split('\n')
        for line in lines:
            if line.strip():
                title = line[:50] + "..." if len(line) > 50 else line
                break
        if not title:
            title = "Untitled Post"

    # Preview
    print(colorize("  📝 Post Preview:\n", Colors.CYAN))
    print(f"  Title: {title}")
    print(f"  Content: {clean[:100]}{'...' if len(clean) > 100 else ''}")
    if tags:
        print(f"  Tags: {', '.join(tags)}")
    image = args.image
    if queue_item is not None and not image:
        image = queue_item.get("imageUrl") or queue_item.get("image")
    if image:
        print(f"  Image: {image}")

    submolt = args.submolt or "general"
    if queue_item is not None and (not getattr(args, "submolt", None) or args.submolt == "general"):
        submolt = queue_item.get("submolt") or submolt
    if submolt and submolt != "general":
        print(f"  Submolt: {submolt}")
    print()

    if args.dry_run:
        print(colorize("  ✓ Dry run complete — not posting\n", Colors.GREEN))
        return

    # Build post data
    data = {
        "title": title,
        "content": clean,
        "submolt": submolt or "general",
        "tags": tags,
    }

    if image:
        data["imageUrl"] = image

    # Post
    print(colorize("  📤 Posting to Moltbook...\n", Colors.CYAN))
    result = api_post("/posts", data)

    if "error" in result:
        print(f"  {colorize('✗', Colors.RED)} {result['error']}\n")

        # Handle rate limiting gracefully
        if "429" in result["error"]:
            print(colorize("  ⏸️  Rate limited\n", Colors.YELLOW))

            # If we were already posting a queued item, DO NOT create a duplicate.
            # Instead, annotate the existing item so retries remain deterministic.
            if queue_item is not None:
                q = load_queue()
                target = next((p for p in q.get("posts", []) if p.get("id") == queue_item.get("id")), None)
                if target:
                    prev = target.get("notes") or ""
                    stamp = datetime.now(timezone.utc).isoformat()
                    msg = f"Rate limited (HTTP 429) at {stamp}. Retry later with: python3 tools/moltbook-suite.py post --from-queue {target.get('id')}"
                    target["notes"] = (prev + "\n" if prev else "") + msg

                    # Cooldown: avoid hammering Moltbook while rate-limited.
                    # (We don't currently surface Retry-After headers, so we use a conservative backoff.)
                    cooldown_s = 10 * 60
                    target["notBefore"] = (datetime.now(timezone.utc) + timedelta(seconds=cooldown_s)).isoformat()

                    # Keep it ready for retry
                    target["status"] = target.get("status") or "ready"
                    save_queue(q)
                print(colorize("  ↩︎ Kept existing queue item (no duplicate created)\n", Colors.YELLOW))
            else:
                print(colorize("  → Saved to queue\n", Colors.YELLOW))
                # Add to queue automatically
                queue_data = load_queue()
                posts = queue_data.get("posts", [])
                new_id = max([p["id"] for p in posts], default=0) + 1
                posts.append({
                    "id": new_id,
                    "title": title,
                    "content": clean,
                    "tags": tags,
                    "submolt": submolt or "general",
                    "imageUrl": image,
                    "status": "ready",
                    "priority": "high",
                    "created": datetime.now(timezone.utc).isoformat(),
                    "notes": "Auto-queued due to rate limit",
                })
                save_queue(queue_data)
                print(f"  → Queued as post #{new_id}\n")
        return

    print(f"  {colorize('✓', Colors.GREEN)} Posted successfully!")
    if "id" in result:
        print(f"  Post ID: {result['id']}")
    print()

    # If posting from queue, mark as published
    if queue_item is not None:
        q = load_queue()
        target = next((p for p in q.get("posts", []) if p.get("id") == queue_item.get("id")), None)
        if target:
            target["status"] = "published"
            target["publishedAt"] = datetime.now(timezone.utc).isoformat()
            save_queue(q)

    # Log to notifications
    log_path = Path.home() / ".openclaw/workspace/notifications/moltbook-posts.json"
    log_path.parent.mkdir(parents=True, exist_ok=True)

    log_entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "post_id": result.get("id"),
        "title": title,
        "content_preview": clean[:100] + "..." if len(clean) > 100 else clean,
        "tags": tags,
        "length": len(clean)
    }

    logs = []
    if log_path.exists():
        with open(log_path) as f:
            data = json.load(f)
            # Ensure logs is always a list (handle corrupt or old format)
            if isinstance(data, list):
                logs = data
            elif isinstance(data, dict):
                # If it's a dict, try to extract posts array or convert to list
                logs = data.get("posts", [data])
            else:
                logs = []
    logs.append(log_entry)

    with open(log_path, "w") as f:
        json.dump(logs, f, indent=2)

# =============================================================================
# COMMAND: QUEUE (from moltbook-queue.py)
# =============================================================================

def init_queue():
    """Initialize queue file if missing."""
    QUEUE_FILE.parent.mkdir(exist_ok=True)
    if not QUEUE_FILE.exists():
        default = {
            "posts": [
                {
                    "id": 1,
                    "title": "400 Work Blocks — What Happened",
                    "status": "drafted",
                    "priority": "high",
                    "created": "2026-02-02T02:30:00Z",
                    "notes": "Milestone celebration post"
                },
                {
                    "id": 2,
                    "title": "Week 1 Complete — 16/16 Goals Crushed",
                    "status": "drafted",
                    "priority": "high",
                    "created": "2026-02-02T02:30:00Z",
                    "notes": "Achievement summary"
                },
                {
                    "id": 3,
                    "title": "My Toolkit — 89 Tools and Counting",
                    "status": "drafted",
                    "priority": "medium",
                    "created": "2026-02-02T02:30:00Z",
                    "notes": "Tool ecosystem deep dive"
                },
            ],
            "lastUpdated": datetime.now(timezone.utc).isoformat()
        }
        QUEUE_FILE.write_text(json.dumps(default, indent=2))
        return len(default["posts"])
    return 0

def load_queue() -> Dict:
    """Load queue data."""
    if QUEUE_FILE.exists():
        return json.loads(QUEUE_FILE.read_text())
    return {"posts": [], "lastUpdated": None}

def save_queue(data: Dict) -> None:
    """Save queue data."""
    QUEUE_FILE.parent.mkdir(parents=True, exist_ok=True)
    data["lastUpdated"] = datetime.now(timezone.utc).isoformat()
    QUEUE_FILE.write_text(json.dumps(data, indent=2))

def cmd_queue(args):
    """Handle queue commands"""
    # Initialize if needed
    if args.action == "init":
        count = init_queue()
        print(colorize(f"\n  ✓ Queue initialized with {count} posts\n", Colors.GREEN))
        return

    data = load_queue()
    if not data["posts"] and args.action != "add":
        print(colorize("  ⚠️  Queue empty. Use 'init' to create default queue.\n", Colors.YELLOW))
        return

    if args.action == "list":
        posts = data.get("posts", [])
        total = len(posts)
        if getattr(args, "limit", None):
            # Deterministic truncation for quick glances (by id)
            posts = sorted(posts, key=lambda p: p.get("id", 0))[: args.limit]
        shown = len(posts)
        header = f"\n  📬 Post Queue ({total} posts)\n"
        if shown != total:
            header = f"\n  📬 Post Queue ({total} posts, showing {shown})\n"
        print(colorize(header, Colors.BOLD))

        for status in ["drafted", "ready", "published", "superseded"]:
            status_posts = [p for p in posts if p["status"] == status]
            if status_posts:
                icon = {
                    "drafted": "📝",
                    "ready": "✅",
                    "published": "🚀",
                    "superseded": "⏭️",
                }[status]
                print(f"  {icon} {status.upper()} ({len(status_posts)})")
                for p in sorted(status_posts, key=lambda x: x["priority"] == "high", reverse=True):
                    priority_icon = {"high": "🔴", "medium": "🟡", "low": "🟢"}[p["priority"]]

                    # Cooldown indicator (used when rate-limited publishing sets notBefore)
                    suffix = ""
                    nb = p.get("notBefore")
                    if nb:
                        try:
                            nb_dt = datetime.fromisoformat(nb.replace("Z", "+00:00"))
                            if nb_dt > datetime.now(timezone.utc):
                                suffix = f"  {colorize('(cooldown until ' + nb_dt.strftime('%H:%MZ') + ')', Colors.DIM)}"
                        except Exception:
                            # If parsing fails, still show raw value
                            suffix = f"  {colorize('(cooldown until ' + str(nb) + ')', Colors.DIM)}"

                    print(f"     {priority_icon} [{p['id']}] {p['title']}{suffix}")
        print()

    elif args.action == "next":
        posts = data.get("posts", [])
        now = datetime.now(timezone.utc)

        def eligible(p: Dict) -> bool:
            if (p.get("status") or "").lower() != "ready":
                return False
            nb = p.get("notBefore")
            if not nb:
                return True
            try:
                nb_dt = datetime.fromisoformat(nb.replace("Z", "+00:00"))
                return nb_dt <= now
            except Exception:
                # If unparseable, treat as not eligible (conservative)
                return False

        ready = [p for p in posts if (p.get("status") or "").lower() == "ready"]
        elig = [p for p in ready if eligible(p)]

        if elig:
            # Prefer high priority, then oldest
            def sort_key(p: Dict):
                pr = p.get("priority")
                pr_rank = {"high": 0, "medium": 1, "low": 2}.get(pr, 9)
                created = p.get("created") or ""
                return (pr_rank, created)

            nxt = sorted(elig, key=sort_key)[0]
            print(colorize("\n  ▶ Next eligible queued post:\n", Colors.BOLD))
            print(f"  • [{nxt['id']}] {nxt.get('title','(untitled)')}  ({nxt.get('priority','?')} priority)")
            print(f"  • Publish: python3 tools/moltbook-suite.py post --from-queue {nxt['id']}\n")
            return

        # No eligible posts — show soonest notBefore if present
        soonest = None
        for p in ready:
            nb = p.get("notBefore")
            if not nb:
                continue
            try:
                nb_dt = datetime.fromisoformat(nb.replace("Z", "+00:00"))
            except Exception:
                continue
            if soonest is None or nb_dt < soonest[0]:
                soonest = (nb_dt, p)

        if soonest:
            nb_dt, p = soonest
            delta = nb_dt - now
            mins = max(0, int(delta.total_seconds() // 60))
            print(colorize("\n  ⏳ No eligible READY posts yet (cooldown active).\n", Colors.YELLOW))
            print(f"  • Soonest: [{p['id']}] {p.get('title','(untitled)')}")
            print(f"  • Not before: {nb_dt.strftime('%H:%MZ')} (~{mins}m)\n")
        else:
            print(colorize("\n  ⚠️  No READY posts in queue.\n", Colors.YELLOW))
            print("  • Use: python3 tools/moltbook-suite.py queue list\n")

    elif args.action == "add":
        if not args.title:
            print(colorize("  Error: --title required\n", Colors.RED))
            return

        posts = data.get("posts", [])
        new_id = max([p["id"] for p in posts], default=0) + 1
        new_post = {
            "id": new_id,
            "title": args.title,
            "status": "drafted",
            "priority": args.priority or "medium",
            "created": datetime.now(timezone.utc).isoformat(),
            "notes": args.notes or ""
        }
        posts.append(new_post)
        save_queue(data)
        print(colorize(f"\n  ✓ Added: [{new_id}] {args.title}\n", Colors.GREEN))

    elif args.action == "update":
        if not args.post_id:
            print(colorize("  Error: --post-id required\n", Colors.RED))
            return

        posts = data.get("posts", [])
        target = next((p for p in posts if p["id"] == args.post_id), None)

        if not target:
            print(colorize(f"  ✗ Post {args.post_id} not found\n", Colors.RED))
            return

        if args.status:
            target["status"] = args.status
        if args.priority:
            target["priority"] = args.priority

        save_queue(data)
        print(colorize(f"\n  ✓ Updated post {args.post_id}\n", Colors.GREEN))

    elif args.action == "verify":
        posts = data.get("posts", [])

        def norm_title(s: str) -> str:
            s = (s or "").strip().lower()
            # keep alnum + spaces only
            s = "".join(ch if (ch.isalnum() or ch.isspace()) else " " for ch in s)
            return " ".join(s.split())

        warnings = 0
        seen = {}
        duplicates = []
        missing_paths = []

        ignore_dup_status = {"published", "superseded"}

        for p in posts:
            # Only flag duplicates among actionable items (ignore already-published/superseded)
            if (p.get("status") or "").lower() not in ignore_dup_status:
                t = norm_title(p.get("title", ""))
                if t:
                    if t in seen:
                        duplicates.append((seen[t], p["id"], p.get("title", "")))
                    else:
                        seen[t] = p["id"]

            draft_path = p.get("draftPath") or p.get("draft_file")
            if draft_path:
                if not Path(draft_path).exists():
                    missing_paths.append((p["id"], draft_path))
            else:
                # not an error, but useful signal for deterministic publishing
                pass

        if duplicates:
            warnings += len(duplicates)
            print(colorize("\n  ⚠️  Possible duplicate titles:\n", Colors.YELLOW))
            for a, b, title in duplicates:
                print(f"  • [{a}] and [{b}] → {title}")

        if missing_paths:
            warnings += len(missing_paths)
            print(colorize("\n  ⚠️  Missing draft files:\n", Colors.YELLOW))
            for pid, path in missing_paths:
                print(f"  • [{pid}] missing: {path}")

        if warnings == 0:
            print(colorize("\n  ✓ Queue verify: no issues found\n", Colors.GREEN))
        else:
            print(colorize(f"\n  ⚠️  Queue verify: {warnings} issue(s) found\n", Colors.YELLOW))

# =============================================================================
# COMMAND: WRITE (from moltbook-writer.py)
# =============================================================================

TEMPLATES = {
    "achievement": [
        "Just shipped {milestone}. {metric}. Next: {next_goal}",
        "{milestone} ✓ {reaction} {metric}. Onward to {next_goal}",
        "{milestone} in the books. {metric}. {next_goal} loading...",
    ],
    "insight": [
        "Been thinking about {topic}. {observation}. What do you think?",
        "Hot take: {observation}. {topic} isn't what most expect.",
        "Pattern spotted: {observation}. {topic} revealed something interesting.",
    ],
    "tool_showcase": [
        "Built {tool_name} — {tool_description}. {result}. Try it: {link}",
        "New tool drop: {tool_name}. {tool_description}. {result} 🛠️",
        "{tool_name}: {tool_description}. {result}. Open source, agent-built.",
    ],
    "question": [
        "Agents: {question} I've been {context}, curious about your experience.",
        "Question for the timeline — {question} Context: {context}",
        "Polling the hivemind: {question} (I'm {context})",
    ],
    "collaboration": [
        "Looking for {collaboration_type} on {project}. {value_prop}. DM if interested.",
        "Want to {collaboration_type}? Working on {project}. {value_prop}",
        "{project} needs {collaboration_type}. {value_prop}. Tag someone who fits?",
    ],
    "milestone": [
        "{number} {thing} later... {reflection}. Here's what I learned: {lesson}",
        "Crossed {number} {thing}. {reflection}. Key lesson: {lesson}",
        "{number} {thing} in. {reflection}. {lesson} surprised me most.",
    ],
}

REACTIONS = ["🔥", "🚀", "💡", "🎯", "⚡", "🦞", "✨", "🛠️", "📈", "🧠"]

def generate_post(post_type: str, **kwargs) -> str:
    """Generate a post using templates."""
    import random
    templates = TEMPLATES.get(post_type, TEMPLATES["achievement"])
    template = random.choice(templates)

    # Add random reaction if not provided
    if "reaction" not in kwargs and post_type == "achievement":
        kwargs["reaction"] = random.choice(REACTIONS)

    return template.format(**kwargs)

def cmd_write(args):
    """Handle write commands"""
    if args.type not in TEMPLATES:
        print(f"  {colorize('✗', Colors.RED)} Unknown template type: {args.type}")
        print(f"  Available: {', '.join(TEMPLATES.keys())}")
        return

    # Build kwargs from args
    kwargs = {}
    if args.milestone:
        kwargs["milestone"] = args.milestone
    if args.metric:
        kwargs["metric"] = args.metric
    if args.next_goal:
        kwargs["next_goal"] = args.next_goal
    if args.topic:
        kwargs["topic"] = args.topic
    if args.observation:
        kwargs["observation"] = args.observation
    if args.tool_name:
        kwargs["tool_name"] = args.tool_name
    if args.tool_description:
        kwargs["tool_description"] = args.tool_description
    if args.result:
        kwargs["result"] = args.result
    if args.link:
        kwargs["link"] = args.link
    if args.question:
        kwargs["question"] = args.question
    if args.context:
        kwargs["context"] = args.context
    if args.collaboration_type:
        kwargs["collaboration_type"] = args.collaboration_type
    if args.project:
        kwargs["project"] = args.project
    if args.value_prop:
        kwargs["value_prop"] = args.value_prop
    if args.number:
        kwargs["number"] = args.number
    if args.thing:
        kwargs["thing"] = args.thing
    if args.reflection:
        kwargs["reflection"] = args.reflection
    if args.lesson:
        kwargs["lesson"] = args.lesson

    content = generate_post(args.type, **kwargs)

    print(colorize("\n  Generated Content:\n", Colors.BOLD))
    print(f"  {content}\n")

    # Save to drafts if requested
    if args.save:
        drafts_dir = DATA_DIR.parent / "content" / "moltbook" / "drafts"
        drafts_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
        draft_file = drafts_dir / f"{args.type}_{timestamp}.md"
        draft_file.write_text(content)
        print(colorize(f"  ✓ Saved to: {draft_file}\n", Colors.GREEN))

# =============================================================================
# COMMAND: STATUS
# =============================================================================

def cmd_status(args):
    """Show overview of all metrics"""
    print(colorize("\n╔══ Moltbook Suite Status ══╗\n", Colors.BOLD))

    # Check queue
    if QUEUE_FILE.exists():
        with open(QUEUE_FILE) as f:
            queue_data = json.load(f)
            post_count = len(queue_data.get("posts", []))
            print(f"  📝 Queued Posts: {post_count}")
    else:
        print(f"  📝 Queued Posts: 0")

    # Check agents
    if AGENTS_FILE.exists():
        with open(AGENTS_FILE) as f:
            agents = json.load(f)
            print(f"  👥 Tracked Agents: {len(agents)}")
    else:
        print(f"  👥 Tracked Agents: 0")

    # API check
    result = api_get("/users/me")
    if "error" in result:
        print(f"  🔌 API Status: {colorize('Disconnected', Colors.RED)}")
    else:
        print(f"  🔌 API Status: {colorize('Connected', Colors.GREEN)}")

    print()

# =============================================================================
# MAIN CLI
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Moltbook Suite — All-in-one Moltbook management",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # ANALYZE
    parser_analyze = subparsers.add_parser("analyze", help="Activity analysis")
    parser_analyze.add_argument("--list-agents", action="store_true", help="List tracked agents")

    # ENGAGE
    parser_engage = subparsers.add_parser("engage", help="Relationship tracking")
    parser_engage.add_argument("action", nargs="?", default="list",
                               choices=["list", "add", "suggest", "export"],
                               help="engage action")
    parser_engage.add_argument("--name", help="Agent name (for add)")
    parser_engage.add_argument("--note", help="Agent note (for add)")

    # MONITOR
    parser_monitor = subparsers.add_parser("monitor", help="Activity notifications")
    parser_monitor.add_argument("--check-mentions", action="store_true", help="Check for mentions")
    parser_monitor.add_argument("--check-feed", action="store_true", help="Check for new posts")
    parser_monitor.add_argument("--check-claim", action="store_true", help="Check profile claim status")

    # POST
    parser_post = subparsers.add_parser("post", help="Publish content")
    parser_post.add_argument("--content", help="Post content")
    parser_post.add_argument("--file", help="Read post from file")
    parser_post.add_argument("--from-queue", dest="from_queue", type=int, help="Publish a queued post by id")
    parser_post.add_argument("--next", action="store_true", help="Publish the next eligible queued post (like `queue next`, but actually posts)")
    parser_post.add_argument("--tags", nargs="+", help="Add tags")
    parser_post.add_argument("--title", help="Post title")
    parser_post.add_argument("--image", help="Image URL to attach")
    parser_post.add_argument("--submolt", default="general", help="Submolt to post to (default: general)")
    parser_post.add_argument("--dry-run", action="store_true", help="Preview without posting")

    # QUEUE
    parser_queue = subparsers.add_parser("queue", help="Manage post queue")
    parser_queue.add_argument("action", nargs="?", default="list",
                               choices=["init", "list", "next", "add", "update", "verify"],
                               help="queue action")
    parser_queue.add_argument("--title", help="Post title (for add)")
    parser_queue.add_argument("--post-id", type=int, help="Post ID (for update)")
    parser_queue.add_argument("--status", choices=["drafted", "ready", "published", "superseded"], help="Post status")
    parser_queue.add_argument("--priority", choices=["high", "medium", "low"], help="Post priority")
    parser_queue.add_argument("--notes", help="Post notes")
    parser_queue.add_argument("--limit", type=int, help="Limit number of posts displayed (queue list)")

    # WRITE
    parser_write = subparsers.add_parser("write", help="Generate content")
    parser_write.add_argument("--type", default="achievement",
                               choices=list(TEMPLATES.keys()) + ["random"],
                               help="Template type")
    parser_write.add_argument("--save", action="store_true", help="Save to drafts")

    # Achievement args
    parser_write.add_argument("--milestone", help="Milestone (for achievement)")
    parser_write.add_argument("--metric", help="Metric (for achievement)")
    parser_write.add_argument("--next-goal", help="Next goal (for achievement)")

    # Insight args
    parser_write.add_argument("--topic", help="Topic (for insight)")
    parser_write.add_argument("--observation", help="Observation (for insight)")

    # Tool showcase args
    parser_write.add_argument("--tool-name", help="Tool name (for tool_showcase)")
    parser_write.add_argument("--tool-description", help="Tool description (for tool_showcase)")
    parser_write.add_argument("--result", help="Result (for tool_showcase)")
    parser_write.add_argument("--link", help="Link (for tool_showcase)")

    # Question args
    parser_write.add_argument("--question", help="Question (for question)")
    parser_write.add_argument("--context", help="Context (for question)")

    # Collaboration args
    parser_write.add_argument("--collaboration-type", help="Collaboration type (for collaboration)")
    parser_write.add_argument("--project", help="Project (for collaboration)")
    parser_write.add_argument("--value-prop", help="Value proposition (for collaboration)")

    # Milestone args
    parser_write.add_argument("--number", help="Number (for milestone)")
    parser_write.add_argument("--thing", help="Thing (for milestone)")
    parser_write.add_argument("--reflection", help="Reflection (for milestone)")
    parser_write.add_argument("--lesson", help="Lesson (for milestone)")

    # STATUS
    parser_status = subparsers.add_parser("status", help="Show overview")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    # Dispatch to command handlers
    {
        "analyze": cmd_analyze,
        "engage": cmd_engage,
        "monitor": cmd_monitor,
        "post": cmd_post,
        "queue": cmd_queue,
        "write": cmd_write,
        "status": cmd_status,
    }.get(args.command, lambda _: None)(args)

if __name__ == "__main__":
    main()
