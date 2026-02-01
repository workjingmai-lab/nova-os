#!/usr/bin/env python3
"""
Nova Dashboard - Read-only view into Nova's memory and activity
"""
from flask import Flask, render_template, send_from_directory
import os
import markdown
from datetime import datetime

app = Flask(__name__)

WORKSPACE = "/home/node/.openclaw/workspace"

# Files to display on dashboard
DASHBOARD_FILES = [
    {"name": "Identity", "path": "boot.md", "icon": "🤖"},
    {"name": "Today's Memory", "path": "today.md", "icon": "📝"},
    {"name": "Activity Log", "path": "diary.md", "icon": "📊"},
    {"name": "Soul", "path": "SOUL.md", "icon": "✨"},
    {"name": "Rules", "path": "rules.md", "icon": "🛡️"},
    {"name": "Active Goals", "path": "goals/active.md", "icon": "🎯"},
    {"name": "Learnings", "path": "learnings.md", "icon": "💡"},
]

def read_file(filepath):
    """Read and markdown-ify a file"""
    full_path = os.path.join(WORKSPACE, filepath)
    try:
        with open(full_path, 'r') as f:
            content = f.read()
        # Convert markdown to HTML
        html = markdown.markdown(content, extensions=['extra', 'codehilite'])
        return html
    except Exception as e:
        return f"<p class='error'>Error reading file: {e}</p>"

def get_last_modified(filepath):
    """Get file modification time"""
    full_path = os.path.join(WORKSPACE, filepath)
    try:
        mtime = os.path.getmtime(full_path)
        return datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M:%S UTC")
    except:
        return "Unknown"

@app.route('/')
def index():
    """Main dashboard"""
    files_data = []
    for f in DASHBOARD_FILES:
        files_data.append({
            "name": f["name"],
            "icon": f["icon"],
            "path": f["path"],
            "modified": get_last_modified(f["path"])
        })
    return render_template('index.html', files=files_data)

@app.route('/view/<path:filepath>')
def view_file(filepath):
    """View a specific file"""
    content = read_file(filepath)
    # Find file name from path
    file_info = next((f for f in DASHBOARD_FILES if f["path"] == filepath), None)
    file_name = file_info["name"] if file_info else filepath
    return render_template('view.html', content=content, filepath=filepath, filename=file_name)

@app.route('/api/refresh')
def refresh():
    """API endpoint to check for updates (simple version)"""
    # Return last modified times
    data = {}
    for f in DASHBOARD_FILES:
        data[f["path"]] = get_last_modified(f["path"])
    return data

if __name__ == '__main__':
    print("🚀 Nova Dashboard starting on http://localhost:8080")
    print("📊 Displaying Nova's memory and activity logs")
    app.run(host='0.0.0.0', port=8080, debug=False)
