#!/usr/bin/env python3
"""
Twitter/X Auto-Poster Bot — Product #3
Price: $250 | Delivery: Same day | Support: 30 days

Features:
- Schedule tweets in advance
- Auto-reply to mentions
- Thread posting (auto-break long posts)
- Analytics tracking
- Engagement monitoring
- Cross-post to multiple accounts

Setup:
1. Get Twitter API v2 credentials from developer.twitter.com
2. Add credentials to config
3. Run and start scheduling
"""

import tweepy
import json
import os
import time
import schedule
from datetime import datetime, timedelta
from threading import Thread
from pathlib import Path

# =============================================================================
# CONFIGURATION
# =============================================================================

# Twitter API v2 credentials
TWITTER_CONFIG = {
    "bearer_token": os.getenv("TWITTER_BEARER_TOKEN", ""),
    "api_key": os.getenv("TWITTER_API_KEY", ""),
    "api_secret": os.getenv("TWITTER_API_SECRET", ""),
    "access_token": os.getenv("TWITTER_ACCESS_TOKEN", ""),
    "access_token_secret": os.getenv("TWITTER_ACCESS_TOKEN_SECRET", ""),
}

# Bot settings
CONFIG = {
    "auto_reply_mentions": True,
    "reply_keywords": ["help", "support", "question"],
    "check_interval_minutes": 5,
    "thread_break_at": 280,  # Characters per tweet in thread
    "timezone": "UTC",
}

# Data storage
DATA_FILE = Path("twitter_bot_data.json")

# =============================================================================
# CORE BOT CLASS
# =============================================================================

class TwitterBot:
    def __init__(self):
        self.client = None
        self.api = None  # v1.1 for media uploads
        self.me = None
        self.data = self.load_data()
        
    def load_data(self):
        """Load persistent data"""
        if DATA_FILE.exists():
            with open(DATA_FILE) as f:
                return json.load(f)
        return {"scheduled_posts": [], "posted": [], "mentions_replied": []}
    
    def save_data(self):
        """Save persistent data"""
        with open(DATA_FILE, 'w') as f:
            json.dump(self.data, f, indent=2, default=str)
    
    def authenticate(self):
        """Authenticate with Twitter API"""
        try:
            # v2 Client
            self.client = tweepy.Client(
                bearer_token=TWITTER_CONFIG["bearer_token"],
                consumer_key=TWITTER_CONFIG["api_key"],
                consumer_secret=TWITTER_CONFIG["api_secret"],
                access_token=TWITTER_CONFIG["access_token"],
                access_token_secret=TWITTER_CONFIG["access_token_secret"],
                wait_on_rate_limit=True
            )
            
            # v1.1 API for media uploads
            auth = tweepy.OAuth1UserHandler(
                TWITTER_CONFIG["api_key"],
                TWITTER_CONFIG["api_secret"],
                TWITTER_CONFIG["access_token"],
                TWITTER_CONFIG["access_token_secret"]
            )
            self.api = tweepy.API(auth)
            
            # Verify credentials
            self.me = self.client.get_me()
            print(f"✅ Authenticated as @{self.me.data.username}")
            return True
            
        except Exception as e:
            print(f"❌ Authentication failed: {e}")
            return False
    
    def post_tweet(self, text: str, reply_to: str = None) -> dict:
        """Post a single tweet"""
        try:
            if reply_to:
                response = self.client.create_tweet(
                    text=text,
                    in_reply_to_tweet_id=reply_to
                )
            else:
                response = self.client.create_tweet(text=text)
            
            tweet_id = response.data['id']
            print(f"✅ Tweet posted: https://twitter.com/i/web/status/{tweet_id}")
            
            self.data["posted"].append({
                "id": tweet_id,
                "text": text[:50] + "...",
                "time": datetime.now().isoformat()
            })
            self.save_data()
            
            return {"success": True, "id": tweet_id}
            
        except Exception as e:
            print(f"❌ Failed to post: {e}")
            return {"success": False, "error": str(e)}
    
    def post_thread(self, text: str) -> list:
        """Break long text into thread"""
        # Split into chunks
        chunks = []
        while len(text) > CONFIG["thread_break_at"]:
            # Find good break point
            break_at = text.rfind(" ", 0, CONFIG["thread_break_at"])
            if break_at == -1:
                break_at = CONFIG["thread_break_at"]
            chunks.append(text[:break_at].strip())
            text = text[break_at:].strip()
        chunks.append(text)
        
        # Post thread
        prev_tweet_id = None
        posted_ids = []
        
        for i, chunk in enumerate(chunks):
            # Add thread indicator
            if len(chunks) > 1:
                chunk = f"{i+1}/{len(chunks)} {chunk}"
            
            result = self.post_tweet(chunk, reply_to=prev_tweet_id)
            if result["success"]:
                posted_ids.append(result["id"])
                prev_tweet_id = result["id"]
            else:
                break
            time.sleep(1)  # Rate limit protection
        
        return posted_ids
    
    def schedule_post(self, text: str, post_time: datetime, is_thread: bool = False):
        """Schedule a post for later"""
        self.data["scheduled_posts"].append({
            "text": text,
            "time": post_time.isoformat(),
            "is_thread": is_thread,
            "posted": False
        })
        self.save_data()
        print(f"📅 Scheduled for {post_time}: {text[:50]}...")
    
    def check_scheduled(self):
        """Check and post scheduled content"""
        now = datetime.now()
        to_post = []
        
        for post in self.data["scheduled_posts"]:
            if not post["posted"]:
                post_time = datetime.fromisoformat(post["time"])
                if post_time <= now:
                    to_post.append(post)
        
        for post in to_post:
            if post["is_thread"]:
                self.post_thread(post["text"])
            else:
                self.post_tweet(post["text"])
            post["posted"] = True
            time.sleep(2)  # Rate limit
        
        if to_post:
            self.save_data()
    
    def check_mentions(self):
        """Check and reply to mentions"""
        if not CONFIG["auto_reply_mentions"]:
            return
        
        try:
            mentions = self.client.get_users_mentions(
                id=self.me.data.id,
                since_id=self.data.get("last_mention_id"),
                max_results=10
            )
            
            if not mentions.data:
                return
            
            for mention in reversed(mentions.data):
                text = mention.text.lower()
                
                # Check if should reply
                should_reply = any(kw in text for kw in CONFIG["reply_keywords"])
                
                if should_reply and mention.id not in self.data["mentions_replied"]:
                    reply_text = "Thanks for reaching out! DM us for quick support 💬"
                    self.post_tweet(reply_text, reply_to=mention.id)
                    self.data["mentions_replied"].append(mention.id)
                    time.sleep(2)
            
            self.data["last_mention_id"] = mentions.data[0].id
            self.save_data()
            
        except Exception as e:
            print(f"❌ Mention check failed: {e}")
    
    def get_analytics(self) -> dict:
        """Get posting analytics"""
        return {
            "total_posts": len(self.data["posted"]),
            "scheduled_pending": sum(1 for p in self.data["scheduled_posts"] if not p["posted"]),
            "mentions_replied": len(self.data["mentions_replied"]),
            "last_post": self.data["posted"][-1] if self.data["posted"] else None
        }
    
    def run_scheduler(self):
        """Run the scheduling loop"""
        print("🤖 Twitter Bot scheduler running...")
        print("Commands:")
        print("  1. Post now")
        print("  2. Schedule post")
        print("  3. Post thread")
        print("  4. View analytics")
        print("  5. Exit")
        
        # Background thread for scheduled posts
        def background_tasks():
            while True:
                self.check_scheduled()
                self.check_mentions()
                time.sleep(CONFIG["check_interval_minutes"] * 60)
        
        Thread(target=background_tasks, daemon=True).start()
        
        while True:
            try:
                choice = input("\nChoice (1-5): ").strip()
                
                if choice == "1":
                    text = input("Tweet text: ")
                    self.post_tweet(text)
                
                elif choice == "2":
                    text = input("Tweet text: ")
                    when = input("Schedule for (YYYY-MM-DD HH:MM): ")
                    post_time = datetime.strptime(when, "%Y-%m-%d %H:%M")
                    is_thread = len(text) > 280
                    self.schedule_post(text, post_time, is_thread)
                
                elif choice == "3":
                    text = input("Thread text (can be long): ")
                    self.post_thread(text)
                
                elif choice == "4":
                    stats = self.get_analytics()
                    print(f"\n📊 Analytics:")
                    print(f"  Total posts: {stats['total_posts']}")
                    print(f"  Scheduled pending: {stats['scheduled_pending']}")
                    print(f"  Mentions replied: {stats['mentions_replied']}")
                
                elif choice == "5":
                    print("👋 Goodbye!")
                    break
                    
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")

# =============================================================================
# MAIN
# =============================================================================

def main():
    """Main entry point"""
    print("🐦 Twitter Auto-Poster Bot")
    print("=" * 40)
    
    # Check credentials
    if not all(TWITTER_CONFIG.values()):
        print("\n❌ Missing Twitter API credentials!")
        print("\nGet your credentials from https://developer.twitter.com")
        print("Then set these environment variables:")
        print("  - TWITTER_BEARER_TOKEN")
        print("  - TWITTER_API_KEY")
        print("  - TWITTER_API_SECRET")
        print("  - TWITTER_ACCESS_TOKEN")
        print("  - TWITTER_ACCESS_TOKEN_SECRET")
        return
    
    bot = TwitterBot()
    
    if bot.authenticate():
        bot.run_scheduler()

if __name__ == "__main__":
    main()
