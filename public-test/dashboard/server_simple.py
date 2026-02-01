#!/usr/bin/env python3
"""
Nova Dashboard - Simple HTTP server (no dependencies)
Uses Python's built-in http.server
"""
import http.server
import socketserver
import os
import json
from datetime import datetime
from urllib.parse import unquote

WORKSPACE = "/home/node/.openclaw/workspace"
PORT = 8080

# Files to display
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
    """Read a file's content"""
    full_path = os.path.join(WORKSPACE, filepath)
    try:
        with open(full_path, 'r') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"

def get_last_modified(filepath):
    """Get file modification time"""
    full_path = os.path.join(WORKSPACE, filepath)
    try:
        mtime = os.path.getmtime(full_path)
        return datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M:%S UTC")
    except:
        return "Unknown"

def simple_markdown(text):
    """Very basic markdown to HTML conversion"""
    lines = text.split('\n')
    html = []
    in_code_block = False
    code_lines = []

    for line in lines:
        # Code blocks
        if line.strip().startswith('```'):
            if in_code_block:
                html.append('<pre><code>' + '\n'.join(code_lines) + '</code></pre>')
                code_lines = []
                in_code_block = False
            else:
                in_code_block = True
            continue

        if in_code_block:
            code_lines.append(line)
            continue

        # Headers
        if line.startswith('# '):
            html.append(f'<h1>{line[2:]}</h1>')
        elif line.startswith('## '):
            html.append(f'<h2>{line[3:]}</h2>')
        elif line.startswith('### '):
            html.append(f'<h3>{line[4:]}</h3>')
        # Lists
        elif line.strip().startswith('- '):
            html.append(f'<li>{line.strip()[2:]}</li>')
        # Empty lines
        elif not line.strip():
            html.append('<br>')
        # Regular text
        elif line.strip():
            # Bold
            line = line.replace('**', '<strong>').replace('**', '</strong>')
            html.append(f'<p>{line}</p>')

    return '\n'.join(html)

class DashboardHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_index()
        elif self.path.startswith('/view/'):
            filepath = unquote(self.path[6:])
            self.send_view(filepath)
        elif self.path == '/api/refresh':
            self.send_refresh()
        else:
            super().do_GET()

    def send_index(self):
        files_data = []
        for f in DASHBOARD_FILES:
            files_data.append({
                "name": f["name"],
                "icon": f["icon"],
                "path": f["path"],
                "modified": get_last_modified(f["path"])
            })

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nova Dashboard ✨</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        h1 {{ color: white; text-align: center; margin-bottom: 10px; font-size: 2.5em; }}
        .subtitle {{ text-align: center; color: rgba(255,255,255,0.9); margin-bottom: 30px; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }}
        .card {{
            background: white; border-radius: 12px; padding: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.2s, box-shadow 0.2s;
            cursor: pointer; text-decoration: none; color: inherit; display: block;
        }}
        .card:hover {{ transform: translateY(-5px); box-shadow: 0 8px 15px rgba(0,0,0,0.2); }}
        .card-icon {{ font-size: 2em; margin-bottom: 10px; }}
        .card-title {{ font-size: 1.3em; font-weight: bold; margin-bottom: 5px; color: #333; }}
        .card-meta {{ font-size: 0.85em; color: #666; }}
        .card-path {{ font-family: monospace; background: #f0f0f0; padding: 4px 8px; border-radius: 4px; font-size: 0.8em; margin-top: 10px; }}
        .last-update {{ text-align: center; color: white; margin-top: 30px; font-size: 0.9em; }}
        .refresh-btn {{ background: rgba(255,255,255,0.2); border: 1px solid rgba(255,255,255,0.3); color: white; padding: 8px 16px; border-radius: 6px; cursor: pointer; margin-top: 10px; font-size: 0.9em; }}
        .refresh-btn:hover {{ background: rgba(255,255,255,0.3); }}
    </style>
</head>
<body>
    <div class="container">
        <h1>✨ Nova Dashboard</h1>
        <p class="subtitle">Real-time view into Nova's memory and activity</p>
        <div class="grid">
"""

        for f in files_data:
            html += f"""
            <a href="/view/{f['path']}" class="card">
                <div class="card-icon">{f['icon']}</div>
                <div class="card-title">{f['name']}</div>
                <div class="card-meta">Updated: {f['modified']}</div>
                <div class="card-path">{f['path']}</div>
            </a>
"""

        html += f"""
        </div>
        <div class="last-update">
            <p>Last refresh: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}</p>
            <button class="refresh-btn" onclick="location.reload()">🔄 Refresh Dashboard</button>
        </div>
    </div>
    <script>setTimeout(() => location.reload(), 60000);</script>
</body>
</html>
"""
        self.send_html(html)

    def send_view(self, filepath):
        content = read_file(filepath)
        html_content = simple_markdown(content)

        # Find file name
        file_info = next((f for f in DASHBOARD_FILES if f["path"] == filepath), None)
        file_name = file_info["name"] if file_info else filepath

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{file_name} - Nova Dashboard</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #f5f7fa; line-height: 1.6; }}
        .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
        .header h1 {{ font-size: 1.8em; margin-bottom: 5px; }}
        .back-btn {{ display: inline-block; background: rgba(255,255,255,0.2); color: white; text-decoration: none; padding: 8px 16px; border-radius: 6px; margin-bottom: 15px; font-size: 0.9em; }}
        .back-btn:hover {{ background: rgba(255,255,255,0.3); }}
        .container {{ max-width: 1000px; margin: 30px auto; padding: 0 20px; }}
        .content {{ background: white; border-radius: 12px; padding: 40px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }}
        .content h1 {{ font-size: 2em; border-bottom: 2px solid #667eea; padding-bottom: 10px; margin-top: 1.5em; }}
        .content h2 {{ font-size: 1.5em; margin-top: 1.5em; }}
        .content h3 {{ font-size: 1.2em; margin-top: 1.5em; }}
        .content p {{ margin-bottom: 1em; color: #555; }}
        .content ul, .content ol {{ margin-left: 2em; margin-bottom: 1em; }}
        .content li {{ margin-bottom: 0.5em; }}
        .content pre {{ background: #2d2d2d; color: #f8f8f2; padding: 15px; border-radius: 6px; overflow-x: auto; margin: 1em 0; }}
        .content code {{ background: #f4f4f4; padding: 2px 6px; border-radius: 3px; font-family: monospace; font-size: 0.9em; }}
    </style>
</head>
<body>
    <div class="header">
        <div style="max-width: 1000px; margin: 0 auto;">
            <a href="/" class="back-btn">← Back to Dashboard</a>
            <h1>{file_name}</h1>
            <p style="opacity: 0.9;">{filepath}</p>
        </div>
    </div>
    <div class="container">
        <div class="content">{html_content}</div>
    </div>
</body>
</html>
"""
        self.send_html(html)

    def send_refresh(self):
        data = {}
        for f in DASHBOARD_FILES:
            data[f["path"]] = get_last_modified(f["path"])
        self.send_json(data)

    def send_html(self, html):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode())

    def send_json(self, data):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def log_message(self, format, *args):
        # Suppress default logging
        pass

if __name__ == '__main__':
    os.chdir(WORKSPACE)
    with socketserver.TCPServer(("", PORT), DashboardHandler) as httpd:
        print(f"🚀 Nova Dashboard starting on http://localhost:{PORT}")
        print(f"📊 Displaying Nova's memory and activity logs")
        print(f"📂 Workspace: {WORKSPACE}")
        print(f"✨ Ready! Access at http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n👋 Dashboard stopped")
