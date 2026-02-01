#!/usr/bin/env python3
"""
workspace-cleanup.py - Smart workspace organization and cleanup
Identifies orphaned files, suggests organization, safely archives old content.
"""

import os
import json
import shutil
import argparse
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict
from typing import List, Dict, Set, Tuple

WORKSPACE = Path("/home/node/.openclaw/workspace")
ARCHIVE_DIR = WORKSPACE / "archive"
ORPHAN_DIR = WORKSPACE / "orphaned"

class WorkspaceCleaner:
    def __init__(self, dry_run=True):
        self.dry_run = dry_run
        self.actions: List[str] = []
        self.stats = {
            "scanned": 0,
            "orphaned": 0,
            "archivable": 0,
            "duplicates": 0,
            "empty_dirs": 0,
        }
    
    def scan_orphaned(self) -> List[Path]:
        """Find files not referenced by any active project or tool."""
        orphaned = []
        
        # Known important directories
        protected_dirs = {
            "tools", "knowledge", "memory", "goals", "diary.md",
            "today.md", "heartbeat.md", "dashboard", "collab",
            "strategy", "templates"
        }
        
        # Get all Python files in tools dir (referenced tools)
        referenced = set()
        tools_dir = WORKSPACE / "tools"
        if tools_dir.exists():
            for f in tools_dir.glob("*.py"):
                referenced.add(f.name)
        
        # Scan for orphaned loose files in root
        for item in WORKSPACE.iterdir():
            if item.is_file():
                # Check if it's a known working file
                if item.name not in protected_dirs and not item.name.startswith('.'):
                    # Check if it's referenced anywhere
                    if not self._is_file_referenced(item):
                        orphaned.append(item)
                        self.stats["orphaned"] += 1
        
        return orphaned
    
    def _is_file_referenced(self, file_path: Path) -> bool:
        """Check if a file is referenced in other files."""
        name = file_path.name
        
        # Quick checks for known patterns
        if name.endswith('.md'):
            return True  # Documentation files are important
        if name in ['README.md', 'LICENSE', '.gitignore']:
            return True
        
        # Search for references in common file types
        search_exts = ['.py', '.sh', '.md', '.json']
        try:
            for ext in search_exts:
                for f in WORKSPACE.rglob(f"*{ext}"):
                    if f == file_path:
                        continue
                    try:
                        content = f.read_text()
                        if name in content:
                            return True
                    except:
                        continue
        except:
            pass
        
        return False
    
    def find_duplicates(self) -> Dict[str, List[Path]]:
        """Find duplicate files by content hash."""
        import hashlib
        
        hashes = defaultdict(list)
        
        for file_path in WORKSPACE.rglob("*"):
            if file_path.is_file() and not file_path.name.startswith('.'):
                try:
                    content = file_path.read_bytes()
                    file_hash = hashlib.md5(content).hexdigest()
                    hashes[file_hash].append(file_path)
                except:
                    continue
        
        # Return only actual duplicates
        duplicates = {h: paths for h, paths in hashes.items() if len(paths) > 1}
        self.stats["duplicates"] = sum(len(p) - 1 for p in duplicates.values())
        return duplicates
    
    def find_empty_dirs(self) -> List[Path]:
        """Find empty directories."""
        empty = []
        for dir_path in WORKSPACE.rglob("*"):
            if dir_path.is_dir() and not any(dir_path.iterdir()):
                if dir_path.name not in ['archive', 'orphaned']:
                    empty.append(dir_path)
                    self.stats["empty_dirs"] += 1
        return empty
    
    def find_archivable(self, days_old: int = 30) -> List[Path]:
        """Find old files that could be archived."""
        archivable = []
        cutoff = datetime.now() - timedelta(days=days_old)
        
        # Check memory files for old entries
        memory_dir = WORKSPACE / "memory"
        if memory_dir.exists():
            for f in memory_dir.glob("*.md"):
                try:
                    mtime = datetime.fromtimestamp(f.stat().st_mtime)
                    if mtime < cutoff:
                        # Check if it's referenced in recent diary
                        archivable.append(f)
                        self.stats["archivable"] += 1
                except:
                    continue
        
        return archivable
    
    def organize_downloads(self):
        """Organize downloaded files into appropriate directories."""
        downloads = WORKSPACE / "downloads"
        if not downloads.exists():
            return
        
        organizers = {
            ".pdf": WORKSPACE / "docs" / "pdfs",
            ".png": WORKSPACE / "assets" / "images",
            ".jpg": WORKSPACE / "assets" / "images",
            ".jpeg": WORKSPACE / "assets" / "images",
            ".gif": WORKSPACE / "assets" / "images",
            ".mp4": WORKSPACE / "assets" / "videos",
            ".zip": WORKSPACE / "archive" / "downloads",
            ".tar.gz": WORKSPACE / "archive" / "downloads",
        }
        
        for file_path in downloads.iterdir():
            if file_path.is_file():
                ext = file_path.suffix.lower()
                if ext in organizers:
                    target_dir = organizers[ext]
                    target_dir.mkdir(parents=True, exist_ok=True)
                    target = target_dir / file_path.name
                    
                    if self.dry_run:
                        self.actions.append(f"Would move: {file_path.name} → {target_dir}")
                    else:
                        shutil.move(str(file_path), str(target))
                        self.actions.append(f"Moved: {file_path.name} → {target_dir}")
    
    def generate_report(self) -> Dict:
        """Generate a comprehensive workspace health report."""
        report = {
            "timestamp": datetime.utcnow().isoformat(),
            "workspace": str(WORKSPACE),
            "stats": self.stats,
            "actions": self.actions,
            "orphaned_files": [str(p.relative_to(WORKSPACE)) for p in self.scan_orphaned()],
            "empty_directories": [str(p.relative_to(WORKSPACE)) for p in self.find_empty_dirs()],
            "duplicates": {h: [str(p.relative_to(WORKSPACE)) for p in paths] 
                          for h, paths in self.find_duplicates().items()},
        }
        return report
    
    def clean(self, action: str = "scan"):
        """Execute cleanup actions."""
        print(f"🔍 Workspace Cleanup (dry_run={self.dry_run})")
        print("=" * 50)
        
        # Scan for issues
        orphaned = self.scan_orphaned()
        empty = self.find_empty_dirs()
        duplicates = self.find_duplicates()
        
        print(f"\n📊 Scan Results:")
        print(f"   Orphaned files: {len(orphaned)}")
        print(f"   Empty directories: {len(empty)}")
        print(f"   Duplicate groups: {len(duplicates)}")
        
        if orphaned:
            print(f"\n📝 Orphaned files (not referenced anywhere):")
            for f in orphaned[:10]:
                print(f"   - {f.name}")
            if len(orphaned) > 10:
                print(f"   ... and {len(orphaned) - 10} more")
        
        if empty:
            print(f"\n📂 Empty directories:")
            for d in empty[:5]:
                print(f"   - {d.relative_to(WORKSPACE)}")
        
        if duplicates:
            print(f"\n📑 Duplicate files:")
            for h, paths in list(duplicates.items())[:3]:
                print(f"   Hash: {h[:16]}...")
                for p in paths:
                    print(f"      - {p.relative_to(WORKSPACE)}")
        
        # Execute actions if not dry run
        if not self.dry_run and action == "clean":
            ORPHAN_DIR.mkdir(exist_ok=True)
            for f in orphaned:
                shutil.move(str(f), str(ORPHAN_DIR / f.name))
                self.actions.append(f"Moved to orphaned/: {f.name}")
            
            for d in empty:
                d.rmdir()
                self.actions.append(f"Removed empty dir: {d.relative_to(WORKSPACE)}")
        
        # Save report
        report_file = WORKSPACE / ".workspace_report.json"
        report = self.generate_report()
        report_file.write_text(json.dumps(report, indent=2))
        
        print(f"\n✅ Report saved: {report_file}")
        if self.actions:
            print(f"   Actions taken: {len(self.actions)}")

def main():
    parser = argparse.ArgumentParser(
        description="Smart workspace organization and cleanup"
    )
    parser.add_argument("--clean", "-c", action="store_true",
                       help="Actually perform cleanup (not dry run)")
    parser.add_argument("--organize", "-o", action="store_true",
                       help="Organize downloads directory")
    parser.add_argument("--days", "-d", type=int, default=30,
                       help="Days old for archivable files")
    
    args = parser.parse_args()
    
    cleaner = WorkspaceCleaner(dry_run=not args.clean)
    
    if args.organize:
        cleaner.organize_downloads()
    else:
        action = "clean" if args.clean else "scan"
        cleaner.clean(action)

if __name__ == "__main__":
    main()
