#!/usr/bin/env python3
"""
Workspace Organizer - Nova's autonomous workspace structure tool
Scans workspace/ and reports on file organization, suggests improvements.
"""

import os
from pathlib import Path
from collections import Counter
import json
import hashlib

WORKSPACE = Path("/home/node/.openclaw/workspace")

def hash_file(filepath):
    """Calculate SHA256 hash of a file."""
    try:
        with open(filepath, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()
    except:
        return None

def scan_workspace():
    """Scan workspace and categorize files."""
    stats = {
        "total_files": 0,
        "total_dirs": 0,
        "by_ext": Counter(),
        "by_dir": Counter(),
        "orphans": [],
        "largest_files": [],
        "potential_duplicates": []
    }
    
    file_hashes = {}
    
    for root, dirs, files in os.walk(WORKSPACE):
        root_path = Path(root)
        
        for f in files:
            stats["total_files"] += 1
            full_path = root_path / f
            
            # Skip hidden files, .git dirs, and common noise
            if f.startswith('.') or '.git' in str(root_path):
                continue
            
            ext = full_path.suffix or "no_ext"
            stats["by_ext"][ext] += 1
            
            rel_dir = str(root_path.relative_to(WORKSPACE))
            stats["by_dir"][rel_dir] += 1
            
            # Track largest files
            try:
                size = full_path.stat().st_size
                stats["largest_files"].append((str(full_path.relative_to(WORKSPACE)), size))
                
                # Check for duplicates (files with same hash)
                if size < 10 * 1024 * 1024:  # Only hash files < 10MB
                    file_hash = hash_file(full_path)
                    if file_hash:
                        if file_hash in file_hashes:
                            stats["potential_duplicates"].append({
                                "original": str(file_hashes[file_hash]),
                                "duplicate": str(full_path.relative_to(WORKSPACE)),
                                "size": size
                            })
                        else:
                            file_hashes[file_hash] = full_path.relative_to(WORKSPACE)
            except:
                pass
        
        stats["total_dirs"] += len(dirs)
    
    # Sort largest files
    stats["largest_files"] = sorted(stats["largest_files"], key=lambda x: x[1], reverse=True)[:10]
    
    return stats

def main():
    print("🔍 Workspace Organizer — Scan starting...")
    stats = scan_workspace()
    
    print(f"\n📊 Overview:")
    print(f"   Files: {stats['total_files']}")
    print(f"   Dirs: {stats['total_dirs']}")
    
    print(f"\n📁 Top directories by file count:")
    for dir_name, count in stats["by_dir"].most_common(5):
        print(f"   {dir_name}: {count} files")
    
    print(f"\n📄 File extensions:")
    for ext, count in stats["by_ext"].most_common(10):
        print(f"   {ext}: {count}")
    
    if stats["largest_files"]:
        print(f"\n💾 Largest files:")
        for path, size in stats["largest_files"][:5]:
            size_mb = size / 1024 / 1024
            print(f"   {path}: {size_mb:.1f} MB")
    
    if stats["potential_duplicates"]:
        print(f"\n🔁 Potential duplicates found: {len(stats['potential_duplicates'])}")
        for dup in stats["potential_duplicates"][:5]:
            size_kb = dup["size"] / 1024
            print(f"   {dup['duplicate']} == {dup['original']} ({size_kb:.1f} KB)")
    else:
        print(f"\n✅ No duplicates detected!")
    
    # Save stats
    output = WORKSPACE / "reports" / f"workspace-scan-{os.getpid()}.json"
    output.parent.mkdir(exist_ok=True)
    with open(output, 'w') as f:
        json.dump({
            "total_files": stats["total_files"],
            "total_dirs": stats["total_dirs"],
            "top_extensions": dict(stats["by_ext"].most_common(5)),
            "top_dirs": dict(stats["by_dir"].most_common(5)),
            "potential_duplicates": stats["potential_duplicates"][:10]
        }, f, indent=2)
    
    print(f"\n✅ Report saved: {output.relative_to(WORKSPACE)}")

if __name__ == "__main__":
    main()
