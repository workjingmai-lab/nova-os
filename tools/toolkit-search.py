#!/usr/bin/env python3
"""
toolkit-search.py - Search and discover tools in Nova's toolkit
Fast indexed search for scripts, utilities, and automation tools.
"""

import os
import json
import re
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional

WORKSPACE = Path("/home/node/.openclaw/workspace")
TOOLS_DIR = WORKSPACE / "tools"
INDEX_FILE = WORKSPACE / ".toolkit_index.json"

class ToolkitIndex:
    def __init__(self):
        self.tools: List[Dict] = []
        self.last_indexed: Optional[str] = None
    
    def scan_tools(self) -> List[Dict]:
        """Scan tools directory and extract metadata."""
        tools = []
        
        if not TOOLS_DIR.exists():
            return tools
        
        for file_path in TOOLS_DIR.glob("*.py"):
            tool_info = self._extract_tool_info(file_path)
            if tool_info:
                tools.append(tool_info)
        
        # Also check for shell scripts
        for file_path in TOOLS_DIR.glob("*.sh"):
            tool_info = self._extract_tool_info(file_path, is_shell=True)
            if tool_info:
                tools.append(tool_info)
        
        return sorted(tools, key=lambda x: x["name"])
    
    def _extract_tool_info(self, file_path: Path, is_shell=False) -> Optional[Dict]:
        """Extract metadata from a tool file."""
        try:
            content = file_path.read_text()
            name = file_path.stem
            
            # Extract docstring/description
            description = ""
            if is_shell:
                # Shell script comments
                match = re.search(r'^#\s*(.+?)(?:\n#\s*|\n\n)', content, re.MULTILINE)
                if match:
                    description = match.group(1).strip()
            else:
                # Python docstring
                match = re.search(r'"""(.+?)"""', content, re.DOTALL)
                if match:
                    desc_lines = match.group(1).strip().split('\n')
                    description = desc_lines[0].strip()
            
            # Extract CLI arguments
            cli_args = []
            if not is_shell:
                # Look for argparse or sys.argv usage
                arg_matches = re.findall(r'add_argument\([\'"](\w+)[\'"]', content)
                cli_args.extend(arg_matches)
                # Also look for argparse descriptions
                arg_help = re.findall(r'add_argument\(.+?help=[\'"](.+?)[\'"]', content)
                cli_args.extend([f"--{a}" for a in arg_help])
            
            # Detect categories based on content patterns
            categories = []
            category_patterns = {
                "api": ["requests", "api", "endpoint", "http"],
                "data": ["json", "csv", "pandas", "analysis"],
                "automation": ["cron", "schedule", "automate", "trigger"],
                "messaging": ["telegram", "discord", "message", "notify"],
                "monitoring": ["watch", "monitor", "alert", "check"],
                "web": ["html", "css", "dashboard", "serve"],
                "filesystem": ["file", "path", "directory", "scan"],
                "collaboration": ["agent", "collab", "task", "delegate"],
                "crypto": ["wallet", "ethereum", "solidity", "web3"],
            }
            content_lower = content.lower()
            for cat, patterns in category_patterns.items():
                if any(p in content_lower for p in patterns):
                    categories.append(cat)
            
            # Check for main block (runnable standalone)
            is_runnable = "if __name__" in content or is_shell
            
            # Get file stats
            stat = file_path.stat()
            
            return {
                "name": name,
                "filename": file_path.name,
                "description": description or "No description available",
                "path": str(file_path.relative_to(WORKSPACE)),
                "categories": categories or ["general"],
                "cli_args": cli_args,
                "is_runnable": is_runnable,
                "is_shell": is_shell,
                "size_kb": round(stat.st_size / 1024, 2),
                "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
            }
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")
            return None
    
    def build_index(self):
        """Build the toolkit index."""
        self.tools = self.scan_tools()
        self.last_indexed = datetime.utcnow().isoformat()
        
        index_data = {
            "last_indexed": self.last_indexed,
            "tool_count": len(self.tools),
            "tools": self.tools
        }
        
        INDEX_FILE.write_text(json.dumps(index_data, indent=2))
        print(f"✅ Indexed {len(self.tools)} tools")
        return index_data
    
    def load_index(self) -> Dict:
        """Load existing index or build if missing."""
        if INDEX_FILE.exists():
            data = json.loads(INDEX_FILE.read_text())
            self.tools = data.get("tools", [])
            self.last_indexed = data.get("last_indexed")
            return data
        else:
            print("No index found. Building...")
            return self.build_index()
    
    def search(self, query: str, category: Optional[str] = None) -> List[Dict]:
        """Search tools by name, description, or category."""
        if not self.tools:
            self.load_index()
        
        query_lower = query.lower()
        results = []
        
        for tool in self.tools:
            score = 0
            
            # Name match (highest priority)
            if query_lower in tool["name"].lower():
                score += 10
            
            # Description match
            if query_lower in tool["description"].lower():
                score += 5
            
            # Category match
            if query_lower in tool["categories"]:
                score += 3
            
            # CLI arg match
            if any(query_lower in arg.lower() for arg in tool["cli_args"]):
                score += 2
            
            # Category filter
            if category and category not in tool["categories"]:
                score = 0
            
            if score > 0:
                tool_result = tool.copy()
                tool_result["score"] = score
                results.append(tool_result)
        
        # Sort by score descending
        return sorted(results, key=lambda x: x["score"], reverse=True)
    
    def list_categories(self) -> Dict[str, int]:
        """List all categories with tool counts."""
        if not self.tools:
            self.load_index()
        
        categories = {}
        for tool in self.tools:
            for cat in tool["categories"]:
                categories[cat] = categories.get(cat, 0) + 1
        return dict(sorted(categories.items(), key=lambda x: x[1], reverse=True))
    
    def get_stats(self) -> Dict:
        """Get toolkit statistics."""
        if not self.tools:
            self.load_index()
        
        total_size = sum(t["size_kb"] for t in self.tools)
        shell_count = sum(1 for t in self.tools if t["is_shell"])
        
        return {
            "total_tools": len(self.tools),
            "python_tools": len(self.tools) - shell_count,
            "shell_scripts": shell_count,
            "total_size_kb": round(total_size, 2),
            "categories": len(self.list_categories()),
            "last_indexed": self.last_indexed
        }

def print_tool(tool: Dict, verbose=False):
    """Print tool information in a formatted way."""
    print(f"\n📦 {tool['name']}")
    print(f"   {tool['description']}")
    print(f"   Categories: {', '.join(tool['categories'])}")
    print(f"   File: {tool['path']} ({tool['size_kb']} KB)")
    
    if tool['cli_args'] and verbose:
        print(f"   CLI args: {', '.join(tool['cli_args'])}")
    
    if verbose:
        print(f"   Modified: {tool['modified']}")

def main():
    parser = argparse.ArgumentParser(
        description="Search and discover tools in Nova's toolkit"
    )
    parser.add_argument("query", nargs="?", help="Search query")
    parser.add_argument("--rebuild", "-r", action="store_true", 
                       help="Rebuild the index")
    parser.add_argument("--category", "-c", help="Filter by category")
    parser.add_argument("--list", "-l", action="store_true",
                       help="List all tools")
    parser.add_argument("--categories", "-C", action="store_true",
                       help="List categories")
    parser.add_argument("--stats", "-s", action="store_true",
                       help="Show toolkit statistics")
    parser.add_argument("--verbose", "-v", action="store_true",
                       help="Verbose output")
    parser.add_argument("--top", "-n", type=int, default=10,
                       help="Limit results (default: 10)")
    
    args = parser.parse_args()
    
    index = ToolkitIndex()
    
    if args.rebuild:
        index.build_index()
        return
    
    if args.stats:
        stats = index.get_stats()
        print("📊 Toolkit Statistics")
        print(f"   Total tools: {stats['total_tools']}")
        print(f"   Python tools: {stats['python_tools']}")
        print(f"   Shell scripts: {stats['shell_scripts']}")
        print(f"   Total size: {stats['total_size_kb']} KB")
        print(f"   Categories: {stats['categories']}")
        print(f"   Last indexed: {stats['last_indexed']}")
        return
    
    if args.categories:
        cats = index.list_categories()
        print("📂 Categories")
        for cat, count in cats.items():
            print(f"   {cat}: {count} tool(s)")
        return
    
    if args.list:
        index.load_index()
        print(f"📦 All Tools ({len(index.tools)} total)")
        for tool in index.tools[:args.top]:
            print_tool(tool, args.verbose)
        if len(index.tools) > args.top:
            print(f"\n... and {len(index.tools) - args.top} more")
        return
    
    if args.query:
        results = index.search(args.query, args.category)
        if results:
            print(f"🔍 Found {len(results)} tool(s) for '{args.query}':")
            for tool in results[:args.top]:
                print_tool(tool, args.verbose)
        else:
            print(f"❌ No tools found for '{args.query}'")
            # Suggest similar
            all_tools = index.load_index().get("tools", [])
            suggestions = [t for t in all_tools if any(
                c.startswith(args.query[0]) for c in t["categories"]
            )][:3]
            if suggestions:
                print("\n💡 Did you mean:")
                for s in suggestions:
                    print(f"   - {s['name']} ({s['categories'][0]})")
        return
    
    # No args - show help and stats
    index.load_index()
    stats = index.get_stats()
    print("🧰 Nova's Toolkit Search")
    print(f"   {stats['total_tools']} tools indexed | {stats['categories']} categories")
    print("\nUsage:")
    print("   toolkit-search.py <query>       # Search tools")
    print("   toolkit-search.py --list        # List all tools")
    print("   toolkit-search.py --categories  # List categories")
    print("   toolkit-search.py --stats       # Show statistics")
    print("   toolkit-search.py --rebuild     # Rebuild index")

if __name__ == "__main__":
    main()
