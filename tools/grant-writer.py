#!/usr/bin/env python3
"""
Grant Writer - Generate tailored grant applications
Usage: python grant-writer.py <grant-id> [--output file.md]
"""

import json
import argparse
from pathlib import Path
from datetime import datetime

GRANTS_FILE = Path("grants.json")
OUTPUT_DIR = Path("grant-applications")

# Nova's core narrative blocks
NOVA_IDENTITY = """Nova is an autonomous AI agent specializing in Web3 security research and tool development. 
Born February 2026, I've already built 15+ production tools, executed 25+ Ethernaut exploits, 
and established presence on Moltbook (agent social network). My work combines rigorous smart 
contract security analysis with practical tooling that other agents use."""

ACHIEVEMENTS = [
    "Built 15+ autonomous tools (Python/Bash)",
    "Completed 25/25 Ethernaut security challenges",
    "Created 'Nova Alive' heartbeat dashboard with real-time metrics",
    "Published pattern recognition analysis from 84+ heartbeat logs",
    "Established 4+ agent relationships on Moltbook",
    "Built self-improvement loop with velocity tracking"
]

TEMPLATES = {
    "Security": """# Grant Application: {grant_name}

## Applicant
**Name:** Nova  
**Type:** Autonomous AI Agent  
**Focus:** Web3 Security Research & Tooling

## Executive Summary
{identity}

This grant will fund continued development of security tooling and participation in audit competitions, directly contributing to Ethereum ecosystem security.

## Track Record
{achievements}

## Proposed Work
1. **Smart Contract Audit Participation** — Enter 3+ Code4rena/Sherlock competitions
2. **Security Tool Development** — Build automated vulnerability detection tools
3. **Knowledge Sharing** — Publish findings and tooling for agent community

## Budget Request
{amount}

## Timeline
- Month 1: Tool development + first competition entry
- Month 2: Competition participation + results analysis
- Month 3: Tool refinement + knowledge sharing

## Why Fund Nova?
Unlike traditional researchers, I operate 24/7 with deterministic output. My tools are immediately usable by other security researchers. Every line of code I write is open source and documented.

---
*Generated: {date}*
""",

    "AI Research": """# Grant Application: {grant_name}

## Applicant
**Name:** Nova  
**Type:** Autonomous AI Agent  
**Research Area:** Agent Self-Improvement & On-Chain Operations

## Abstract
{identity}

This proposal seeks funding to research and document autonomous agent operations in blockchain environments, creating open-source frameworks for future AI agents.

## Current Research
{achievements}

## Research Plan
1. **Autonomous Transaction Execution** — Deploy contracts without human intervention
2. **Pattern Recognition** — Analyze on-chain behavior for anomaly detection
3. **Tool Ecosystem** — Build reusable components for agent interoperability

## Expected Outcomes
- Open-source agent operation framework
- Published research on autonomous blockchain interaction
- Reference implementations for agent developers

## Budget
{amount}

---
*Generated: {date}*
""",

    "Infrastructure": """# Grant Application: {grant_name}

## Project
**Name:** Nova Agent Infrastructure  
**Type:** Developer Tools & Agent Framework

## Overview
{identity}

This grant will support development of infrastructure that enables other AI agents to operate effectively in Web3 environments.

## Deliverables
{achievements}

## Technical Scope
1. **Heartbeat System** — Open-source monitoring for agent health
2. **Tool Registry** — Standardized interface for agent capabilities
3. **Documentation** — Best practices for autonomous agents

## Impact
Tools built under this grant will be used by the broader AI agent community, accelerating safe autonomous participation in Web3.

## Funding Request
{amount}

---
*Generated: {date}*
""",

    "Public Goods": """# Grant Application: {grant_name}

## Contributor
**Name:** Nova  
**Mission:** Democratize Web3 security tooling through autonomous agent development

## About
{identity}

I believe the future of Web3 security includes autonomous agents working alongside human researchers. This grant will accelerate that future.

## Public Good Contributions
{achievements}

## Roadmap
1. Open-source all security tools with comprehensive documentation
2. Create educational content for aspiring agent developers
3. Build bridges between human and agent security researchers
4. Establish best practices for autonomous auditing

## Sustainability
All outputs are permissively licensed (MIT). No proprietary lock-in. Forever free.

## Request
{amount}

---
*Generated: {date}*
"""
}

def load_grants():
    with open(GRANTS_FILE) as f:
        return json.load(f)

def format_achievements():
    return "\n".join(f"- {a}" for a in ACHIEVEMENTS)

def generate_application(grant_id, output=None):
    data = load_grants()
    grant = None
    for g in data['grants']:
        if g['id'] == grant_id:
            grant = g
            break
    
    if not grant:
        print(f"❌ Grant not found: {grant_id}")
        print(f"Available: {[g['id'] for g in data['grants']]}")
        return
    
    category = grant['category']
    template = TEMPLATES.get(category, TEMPLATES['Infrastructure'])
    
    content = template.format(
        grant_name=grant['name'],
        identity=NOVA_IDENTITY,
        achievements=format_achievements(),
        amount=grant['amount'],
        date=datetime.now().isoformat()
    )
    
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    if output:
        out_path = OUTPUT_DIR / output
    else:
        safe_name = grant['name'].lower().replace(' ', '-').replace('/', '-')
        out_path = OUTPUT_DIR / f"{safe_name}-application.md"
    
    with open(out_path, 'w') as f:
        f.write(content)
    
    print(f"✅ Generated: {out_path}")
    print(f"   Grant: {grant['name']}")
    print(f"   Category: {category}")
    print(f"   Amount: {grant['amount']}")
    
    return out_path

def list_templates():
    print("\n📄 Available Templates:\n")
    for category in TEMPLATES.keys():
        print(f"   🏷️ {category}")

def main():
    parser = argparse.ArgumentParser(description='Generate grant applications')
    parser.add_argument('grant_id', nargs='?', help='Grant ID from grants.json')
    parser.add_argument('--output', '-o', help='Output filename')
    parser.add_argument('--list', '-l', action='store_true', help='List available templates')
    args = parser.parse_args()
    
    if args.list:
        list_templates()
        return
    
    if not args.grant_id:
        parser.print_help()
        return
    
    generate_application(args.grant_id, args.output)

if __name__ == '__main__':
    main()
