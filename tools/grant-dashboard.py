#!/usr/bin/env python3
"""
Grant Success Dashboard - Visualize grant application status

Reads submission-tracker.md and generates an HTML dashboard showing:
- Grant applications with status, amounts, deadlines
- Progress bars (draft → ready → submitted → funded)
- Color-coded urgency (red = urgent, green = safe)
- Summary statistics

Usage:
    python tools/grant-dashboard.py > public/grant-dashboard.html
"""

import re
from datetime import datetime, timezone
from pathlib import Path
from html import escape

def parse_submission_tracker(filepath="submission-tracker.md"):
    """Parse submission-tracker.md and extract grant data."""
    content = Path(filepath).read_text() if Path(filepath).exists() else ""
    grants = []

    # Split by grant headers
    sections = re.split(r'## Grant (\d+):', content)

    for i in range(1, len(sections), 2):
        if i + 1 >= len(sections):
            break

        grant_num = sections[i]
        grant_content = sections[i + 1]

        # Extract title (first line before any -)
        lines = grant_content.strip().split('\n')
        title = lines[0].strip()

        # Extract fields
        amount = "TBD"
        deadline = "TBD"
        status = "Unknown"

        for line in lines:
            line = line.strip()
            if line.startswith('**Amount:**'):
                amount = line.split('**Amount:**')[1].strip()
            elif line.startswith('- **Amount:**'):
                amount = line.split('**Amount:**')[1].strip()
            elif line.startswith('**Deadline:**'):
                deadline = line.split('**Deadline:**')[1].strip()
            elif line.startswith('- **Deadline:**'):
                deadline = line.split('**Deadline:**')[1].strip()
            elif line.startswith('**Status:**'):
                status = line.split('**Status:**')[1].strip()
            elif line.startswith('- **Status:**'):
                status = line.split('**Status:**')[1].strip()

        # Parse deadline
        deadline_date = None
        days_remaining = None
        if deadline and deadline != "TBD" and "Rolling" not in deadline:
            try:
                # Try various date formats
                for fmt in ["%B %d, %Y", "%b %d, %Y", "%Y-%m-%d"]:
                    try:
                        deadline_date = datetime.strptime(deadline.split("(")[0].strip(), fmt)
                        deadline_date = deadline_date.replace(tzinfo=timezone.utc)
                        days_remaining = (deadline_date - datetime.now(timezone.utc)).days
                        break
                    except ValueError:
                        continue
            except Exception:
                pass

        grants.append({
            "number": int(grant_num),
            "title": title,
            "amount": amount,
            "deadline": deadline,
            "deadline_date": deadline_date,
            "days_remaining": days_remaining,
            "status": status.lower()
        })

    return grants

def get_status_color(status):
    """Return color for status."""
    status = status.lower()
    if "draft" in status or "complete" in status:
        return "#fbbf24"  # Yellow - ready
    elif "submitted" in status or "pending" in status:
        return "#60a5fa"  # Blue - in review
    elif "approved" in status or "funded" in status or "accepted" in status:
        return "#34d399"  # Green - success
    elif "rejected" in status:
        return "#f87171"  # Red - failed
    return "#9ca3af"  # Gray - unknown

def get_urgency_color(days_remaining):
    """Return urgency color based on days remaining."""
    if days_remaining is None:
        return "#9ca3af"  # Gray - TBD
    elif days_remaining < 3:
        return "#ef4444"  # Red - urgent
    elif days_remaining < 7:
        return "#f97316"  # Orange - soon
    elif days_remaining < 14:
        return "#fbbf24"  # Yellow - moderate
    else:
        return "#34d399"  # Green - safe

def calculate_progress(status):
    """Return progress percentage (0-100) based on status."""
    status = status.lower()
    if "draft" in status:
        return 25
    elif "complete" in status or "ready" in status:
        return 50
    elif "submitted" in status or "pending" in status:
        return 75
    elif "approved" in status or "funded" in status or "accepted" in status:
        return 100
    return 0

def format_amount(amount_str):
    """Extract numeric amount from string."""
    match = re.search(r'[\$£€]?([\d,]+)', amount_str.replace(',', ''))
    if match:
        return int(match.group(1).replace(',', ''))
    return 0

def generate_html(grants):
    """Generate HTML dashboard."""
    total_potential = sum(format_amount(g["amount"]) for g in grants)
    funded_amount = sum(format_amount(g["amount"]) for g in grants if "funded" in g["status"] or "approved" in g["status"])
    submitted_count = sum(1 for g in grants if "submitted" in g["status"])

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grant Success Dashboard — Nova</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #1e1e2e 0%, #2d2d44 100%);
            color: #e0e0e0;
            min-height: 100vh;
            padding: 2rem;
        }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        h1 {{
            font-size: 2rem;
            margin-bottom: 0.5rem;
            background: linear-gradient(90deg, #60a5fa, #a78bfa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .subtitle {{ color: #9ca3af; margin-bottom: 2rem; }}
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-bottom: 2rem;
        }}
        .stat-card {{
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 12px;
            padding: 1.5rem;
            text-align: center;
        }}
        .stat-value {{
            font-size: 2rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }}
        .stat-label {{ color: #9ca3af; font-size: 0.875rem; }}
        .grants-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 1rem;
        }}
        .grant-card {{
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 12px;
            padding: 1.5rem;
            transition: transform 0.2s, box-shadow 0.2s;
        }}
        .grant-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        }}
        .grant-header {{
            display: flex;
            justify-content: space-between;
            align-items: start;
            margin-bottom: 1rem;
        }}
        .grant-title {{ font-weight: bold; font-size: 1.1rem; }}
        .grant-amount {{
            background: rgba(96, 165, 250, 0.2);
            color: #60a5fa;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-weight: bold;
        }}
        .grant-meta {{
            display: flex;
            gap: 1rem;
            margin-bottom: 1rem;
            font-size: 0.875rem;
        }}
        .meta-item {{ display: flex; align-items: center; gap: 0.5rem; }}
        .deadline-dot {{
            width: 8px;
            height: 8px;
            border-radius: 50%;
        }}
        .progress-bar {{
            height: 8px;
            background: rgba(255,255,255,0.1);
            border-radius: 4px;
            overflow: hidden;
            margin-top: 1rem;
        }}
        .progress-fill {{
            height: 100%;
            border-radius: 4px;
            transition: width 0.3s ease;
        }}
        .status-badge {{
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: bold;
            text-transform: uppercase;
        }}
        .last-updated {{
            text-align: center;
            color: #6b7280;
            margin-top: 3rem;
            font-size: 0.875rem;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🎯 Grant Success Dashboard</h1>
        <p class="subtitle">Tracking grant applications • Live status • Updated by Nova</p>

        <div class="stats">
            <div class="stat-card">
                <div class="stat-value">{len(grants)}</div>
                <div class="stat-label">Applications</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">${total_potential:,}</div>
                <div class="stat-label">Total Potential</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">${funded_amount:,}</div>
                <div class="stat-label">Funded/Approved</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{submitted_count}</div>
                <div class="stat-label">Submitted</div>
            </div>
        </div>

        <div class="grants-grid">
"""

    for grant in grants:
        status_color = get_status_color(grant["status"])
        urgency_color = get_urgency_color(grant["days_remaining"])
        progress = calculate_progress(grant["status"])

        deadline_text = grant["deadline"]
        if grant["days_remaining"] is not None:
            if grant["days_remaining"] < 0:
                deadline_text = f"OVERDUE by {abs(grant['days_remaining'])} days"
            elif grant["days_remaining"] == 0:
                deadline_text = "DUE TODAY"
            elif grant["days_remaining"] == 1:
                deadline_text = "DUE TOMORROW"
            else:
                deadline_text = f"{grant['days_remaining']} days left"

        html += f"""
            <div class="grant-card">
                <div class="grant-header">
                    <div class="grant-title">#{grant['number']}: {escape(grant['title'])}</div>
                    <div class="grant-amount">{grant['amount']}</div>
                </div>
                <div class="grant-meta">
                    <div class="meta-item">
                        <div class="deadline-dot" style="background: {urgency_color}"></div>
                        <span>{deadline_text}</span>
                    </div>
                </div>
                <div>
                    <span class="status-badge" style="background: {status_color}30; color: {status_color}">
                        {grant['status']}
                    </span>
                </div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {progress}%; background: {status_color}"></div>
                </div>
            </div>
"""

    html += f"""
        </div>

        <div class="last-updated">
            Last updated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}<br>
            Generated by Nova • OpenClaw Agent
        </div>
    </div>
</body>
</html>
"""
    return html

def main():
    """Main entry point."""
    grants = parse_submission_tracker()

    if not grants:
        print("# No grants found in submission-tracker.md\n")
        print("Add grants using the format:")
        print("## Grant N: Title")
        print("- Amount: $X")
        print("- Deadline: DATE")
        print("- Status: STATUS")
        return

    print(generate_html(grants))

if __name__ == "__main__":
    main()
