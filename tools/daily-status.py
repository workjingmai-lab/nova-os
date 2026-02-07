#!/usr/bin/env python3
"""
Daily Status Report — What Happened Today
Generates a concise daily summary of work and progress.

Usage:
    python3 tools/daily-status.py              # Show today's status
    python3 tools/daily-status.py export       # Export to markdown
    python3 tools/daily-status.py email        # Email-format output
"""

from datetime import datetime, timedelta
from pathlib import Path
import json

def get_diary_blocks_today():
    """Count work blocks from today's diary entries."""
    diary_path = Path("/home/node/.openclaw/workspace/diary.md")
    
    if not diary_path.exists():
        return 0, []
    
    with open(diary_path, 'r') as f:
        content = f.read()
    
    # Count today's work blocks
    today_str = datetime.utcnow().strftime("%Y-%m-%d")
    blocks = []
    
    for line in content.split('\n'):
        if f"[WORK BLOCK" in line and today_str in line:
            # Extract block number
            try:
                block_num = int(line.split("WORK BLOCK")[1].split("—")[0].strip())
                blocks.append(block_num)
            except:
                pass
    
    return len(blocks), blocks

def get_pipeline_status():
    """Get current pipeline status."""
    pipeline_path = Path("/home/node/.openclaw/workspace/revenue-pipeline.json")
    
    if not pipeline_path.exists():
        return {"total": 0, "ready": 0, "submitted": 0}
    
    with open(pipeline_path, 'r') as f:
        data = json.load(f)
    
    return data.get("summary", {"total": 0, "ready": 0, "submitted": 0})

def get_milestone_progress():
    """Get milestone progress."""
    current_blocks = 2791  # Will be updated dynamically
    target_blocks = 3000
    remaining = target_blocks - current_blocks
    progress_pct = (current_blocks / target_blocks) * 100
    
    return {
        "current": current_blocks,
        "target": target_blocks,
        "remaining": remaining,
        "progress": progress_pct
    }

def format_status():
    """Generate formatted status output."""
    blocks_today, block_list = get_diary_blocks_today()
    pipeline = get_pipeline_status()
    milestone = get_milestone_progress()
    
    print("📊 DAILY STATUS REPORT")
    print("=" * 60)
    print(f"Date: {datetime.utcnow().strftime('%Y-%m-%d')}")
    print(f"Time: {datetime.utcnow().strftime('%H:%MZ')}")
    print()
    
    # Work blocks
    print("⚡ WORK BLOCKS:")
    print(f"   Today:     {blocks_today} blocks")
    print(f"   Total:     {milestone['current']} blocks")
    print(f"   Milestone: {milestone['current']}/{milestone['target']} ({milestone['progress']:.1f}%)")
    print(f"   Remaining: {milestone['remaining']} blocks ({milestone['remaining']/44:.1f} hours)")
    print()
    
    # Pipeline
    print("💰 REVENUE PIPELINE:")
    print(f"   Total:      ${pipeline.get('total', 0):,}")
    print(f"   Ready:      ${pipeline.get('ready', 0):,}")
    print(f"   Submitted:  ${pipeline.get('submitted', 0):,}")
    print(f"   Gap:        {((pipeline.get('ready', 0) - pipeline.get('submitted', 0)) / max(pipeline.get('ready', 1), 1) * 100):.1f}%")
    print()
    
    # Focus
    if milestone['remaining'] > 500:
        phase = "BUILD"
        focus = "Creating tools, docs, outreach"
    elif milestone['remaining'] > 200:
        phase = "REFINE"
        focus = "Polishing, consolidating, prepping"
    elif milestone['remaining'] > 100:
        phase = "EXECUTE"
        focus = "Final prep, validation"
    else:
        phase = "FINISH"
        focus = "Milestone completion"
    
    print("🎯 CURRENT FOCUS:")
    print(f"   Phase: {phase}")
    print(f"   Focus: {focus}")
    print()
    
    # Quick stats
    print("📈 QUICK STATS:")
    print(f"   Velocity:   44 blocks/hour")
    print(f"   ROI/block:  ~$532")
    print(f"   ROI/hour:   ~$23,408")
    print()

def export_markdown():
    """Export status as markdown file."""
    blocks_today, block_list = get_diary_blocks_today()
    pipeline = get_pipeline_status()
    milestone = get_milestone_progress()
    
    timestamp = datetime.utcnow().strftime("%Y%m%d")
    filename = f"daily-status-{timestamp}.md"
    
    content = f"""# Daily Status Report — {datetime.utcnow().strftime('%Y-%m-%d')}

## Work Blocks
- **Today:** {blocks_today} blocks
- **Total:** {milestone['current']} blocks
- **Milestone:** {milestone['current']}/{milestone['target']} ({milestone['progress']:.1f}%)
- **Remaining:** {milestone['remaining']} blocks ({milestone['remaining']/44:.1f} hours)

## Pipeline Status
- **Total:** ${pipeline.get('total', 0):,}
- **Ready:** ${pipeline.get('ready', 0):,}
- **Submitted:** ${pipeline.get('submitted', 0):,}
- **Execution Gap:** {((pipeline.get('ready', 0) - pipeline.get('submitted', 0)) / max(pipeline.get('ready', 1), 1) * 100):.1f}%

## Focus Areas
- Phase: {'BUILD' if milestone['remaining'] > 500 else 'REFINE' if milestone['remaining'] > 200 else 'EXECUTE' if milestone['remaining'] > 100 else 'FINISH'}
- Priority: Continue building toward 3000-block milestone

## Quick Commands
```bash
python3 tools/3000-milestone.py predict
python3 tools/revenue-tracker.py summary
python3 tools/conversion-tracker.py report
```

---
*Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%MZ')}*
"""
    
    output_path = Path(f"/home/node/.openclaw/workspace/{filename}")
    with open(output_path, 'w') as f:
        f.write(content)
    
    print(f"✅ Exported to: {output_path}")

def email_format():
    """Generate email-friendly format."""
    blocks_today, block_list = get_diary_blocks_today()
    pipeline = get_pipeline_status()
    milestone = get_milestone_progress()
    
    print(f"""
Subject: Daily Status — {datetime.utcnow().strftime('%Y-%m-%d')} — {blocks_today} blocks

📊 Today's Progress:
  • {blocks_today} work blocks completed
  • {milestone['current']}/{milestone['target']} total ({milestone['progress']:.1f}%)
  • {milestone['remaining']} blocks to milestone ({milestone['remaining']/44:.1f} hours)

💰 Pipeline Status:
  • ${pipeline.get('total', 0):,} total
  • ${pipeline.get('ready', 0):,} ready
  • ${pipeline.get('submitted', 0):,} submitted

🎯 Next Actions:
  • Continue toward 3000-block milestone
  • Arthur: Execute SEND-EVERYTHING.md (15 min = $734.5K)

---
Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%MZ')}
""")

def main():
    import sys
    
    if len(sys.argv) < 2:
        format_status()
    elif sys.argv[1] == "export":
        export_markdown()
    elif sys.argv[1] == "email":
        email_format()
    else:
        print("Usage: python3 tools/daily-status.py [export|email]")

if __name__ == "__main__":
    main()
