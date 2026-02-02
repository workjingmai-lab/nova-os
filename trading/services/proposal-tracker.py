#!/usr/bin/env python3
"""
Proposal Tracker
Monitor sent proposals, track responses, analyze success
"""

import json
from datetime import datetime, timedelta

class ProposalTracker:
    """Track proposal pipeline"""

    def __init__(self, db_path='proposal-tracker.json'):
        self.db_path = db_path
        self.load_db()

    def load_db(self):
        """Load tracking database"""
        try:
            with open(self.db_path, 'r') as f:
                self.db = json.load(f)
        except FileNotFoundError:
            self.db = {
                'proposals': [],
                'metrics': {
                    'sent': 0,
                    'replies': 0,
                    'conversations': 0,
                    'closed': 0
                }
            }

    def save_db(self):
        """Save tracking database"""
        with open(self.db_path, 'w') as f:
            json.dump(self.db, f, indent=2)

    def add_proposal(self, prospect_name, angle, channel, status='draft'):
        """Add new proposal to tracker"""
        proposal = {
            'id': len(self.db['proposals']) + 1,
            'prospect': prospect_name,
            'angle': angle,
            'channel': channel,
            'status': status,  # draft, sent, replied, conversation, closed, lost
            'sent_date': None,
            'reply_date': None,
            'notes': []
        }
        self.db['proposals'].append(proposal)
        self.save_db()
        return proposal

    def mark_sent(self, proposal_id):
        """Mark proposal as sent"""
        for p in self.db['proposals']:
            if p['id'] == proposal_id:
                p['status'] = 'sent'
                p['sent_date'] = datetime.now().isoformat()
                self.db['metrics']['sent'] += 1
                self.save_db()
                return

    def mark_replied(self, proposal_id, notes=""):
        """Mark proposal as replied"""
        for p in self.db['proposals']:
            if p['id'] == proposal_id:
                p['status'] = 'replied'
                p['reply_date'] = datetime.now().isoformat()
                p['notes'].append(notes)
                self.db['metrics']['replies'] += 1
                self.save_db()
                return

    def get_metrics(self):
        """Calculate pipeline metrics"""
        m = self.db['metrics']

        if m['sent'] == 0:
            return {
                'response_rate': 0,
                'sent': 0,
                'replies': 0,
                'conversations': 0,
                'closed': 0
            }

        return {
            'response_rate': m['replies'] / m['sent'],
            'sent': m['sent'],
            'replies': m['replies'],
            'conversations': m['conversations'],
            'closed': m.get('closed', 0)
        }

    def get_followups(self, days=3):
        """Get proposals needing follow-up"""
        followups = []
        now = datetime.now()

        for p in self.db['proposals']:
            if p['status'] == 'sent' and p['sent_date']:
                sent = datetime.fromisoformat(p['sent_date'])
                if (now - sent).days >= days:
                    followups.append(p)

        return followups

    def print_status(self):
        """Print pipeline status"""
        print("📊 PROPOSAL PIPELINE STATUS")
        print("-" * 40)

        metrics = self.get_metrics()
        print(f"Sent: {metrics['sent']}")
        print(f"Replies: {metrics['replies']}")
        print(f"Response Rate: {metrics['response_rate']*100:.1f}%")
        print(f"Conversations: {metrics['conversations']}")
        print(f"Closed: {metrics['closed']}")

        print("\n📋 Proposals:")
        for p in self.db['proposals']:
            status_emoji = {
                'draft': '📝',
                'sent': '📤',
                'replied': '💬',
                'conversation': '🤝',
                'closed': '✅',
                'lost': '❌'
            }.get(p['status'], '❓')

            print(f"  {status_emoji} {p['prospect']} - {p['status']}")

# Initialize with current proposals
if __name__ == "__main__":
    tracker = ProposalTracker()

    # Add current proposals if not already tracked
    current_proposals = [
        ('YaYa_A', 'Tool sharing', 'Moltbook'),
        ('LibaiPoet', 'Collaboration', 'Moltbook'),
        ('Charlinho', 'Agent tools', 'Moltbook'),
        ('Ash-curado', 'Founder automation', 'Moltbook'),
        ('Vitalik Buterin', 'EIP tracker', 'Twitter'),
        ('Guillermo Rauch', 'Doc automation', 'Twitter'),
        ('Stani Kulechov', 'Gov tracking', 'Twitter'),
        ('Hayden Adams', 'Gov tracking', 'Twitter')
    ]

    for prospect_name, angle, channel in current_proposals:
        # Check if already exists
        exists = any(p['prospect'] == prospect_name for p in tracker.db['proposals'])
        if not exists:
            tracker.add_proposal(prospect_name, angle, channel)

    tracker.print_status()
    tracker.save_db()

    print("\n💡 Next: Mark proposals as sent when you send them")
    print("   tracker.mark_sent(proposal_id)")
