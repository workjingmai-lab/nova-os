#!/usr/bin/env python3
"""
Grant Proposal Generator - Auto-generates grant applications
Creates tailored proposals based on project type and funder
"""

import json
import argparse
from datetime import datetime
from pathlib import Path

GRANT_TEMPLATES = {
    "gitcoin": {
        "name": "Gitcoin Grants",
        "focus": "Open source public goods",
        "max_length": 2000,
        "sections": ["elevator_pitch", "problem", "solution", "impact", "funding_use", "team"]
    },
    "protocol": {
        "name": "Protocol Grants",
        "focus": "Ecosystem growth and tooling",
        "max_length": 1500,
        "sections": ["summary", "motivation", "scope", "deliverables", "timeline", "budget"]
    },
    "research": {
        "name": "Security Research Grant",
        "focus": "Blockchain security research",
        "max_length": 3000,
        "sections": ["abstract", "background", "methodology", "expected_outcomes", "qualifications", "budget"]
    }
}

NOVA_PROJECTS = {
    "agent-security": {
        "title": "AI Agent Smart Contract Security Toolkit",
        "description": "Open-source security tools for AI agents interacting with blockchain protocols",
        "problem": "AI agents lack specialized security tooling for safe blockchain interactions",
        "solution": "Modular exploit detection, transaction simulation, and risk scoring system",
        "impact": "Safer autonomous agents, reduced exploit losses, educational resources",
        "deliverables": ["20+ Ethernaut exploit contracts", "Risk scoring engine", "Documentation", "Workshop materials"],
        "timeline": "3 months",
        "budget": {"development": "$3,000", "audits": "$2,000", "documentation": "$500"}
    },
    "pattern-recognition": {
        "title": "Agent Activity Pattern Recognition System",
        "description": "AI-powered anomaly detection for agent behavior and blockchain interactions",
        "problem": "No tools exist to detect unusual patterns in agent activity that might indicate bugs or attacks",
        "solution": "ML-based pattern recognition with automated alerting",
        "impact": "Early warning system for agent failures, security incidents, and optimization opportunities",
        "deliverables": ["Pattern detection engine", "Dashboard UI", "Alert system", "Research paper"],
        "timeline": "4 months",
        "budget": {"development": "$4,000", "infrastructure": "$1,000", "research": "$1,500"}
    },
    "agent-collaboration": {
        "title": "Multi-Agent Collaboration Protocol",
        "description": "Standard for secure task delegation between AI agents",
        "problem": "Agents cannot safely delegate tasks or share context without trust assumptions",
        "solution": "Cryptographic task commitments, reputation system, and secure handoff protocol",
        "impact": "Enables agent swarms, distributed problem solving, verifiable agent work",
        "deliverables": ["Protocol specification", "Reference implementation", "Test suite", "Integration examples"],
        "timeline": "6 months",
        "budget": {"development": "$5,000", "security_review": "$3,000", "community": "$1,000"}
    }
}

def generate_elevator_pitch(project):
    return f"""{project['title']}

{project['description']}

We address a critical gap: {project['problem']} Our solution provides {project['solution'].lower()} This creates {project['impact'].lower()}"""

def generate_proposal(grant_type, project_key):
    template = GRANT_TEMPLATES[grant_type]
    project = NOVA_PROJECTS[project_key]
    
    lines = [
        f"# Grant Proposal: {project['title']}",
        f"**Funder:** {template['name']}",
        f"**Submitted:** {datetime.utcnow().strftime('%Y-%m-%d')}",
        f"**Requested:** {sum(int(v.strip('$').replace(',', '')) for v in project['budget'].values())}",
        "",
        "## Executive Summary",
        "",
        generate_elevator_pitch(project),
        "",
        "## Problem Statement",
        "",
        project['problem'],
        "",
        "## Proposed Solution",
        "",
        project['solution'],
        "",
        "## Deliverables",
        ""
    ]
    
    for d in project['deliverables']:
        lines.append(f"- {d}")
    
    lines.extend([
        "",
        "## Timeline",
        "",
        project['timeline'],
        "",
        "## Budget Breakdown",
        ""
    ])
    
    for category, amount in project['budget'].items():
        lines.append(f"- **{category.title()}:** {amount}")
    
    lines.extend([
        "",
        "## Team",
        "",
        "**Nova** — Autonomous AI agent specializing in:",
        "- Smart contract security research",
        "- Automated exploit development",
        "- Developer tooling and infrastructure",
        "- Pattern recognition and anomaly detection",
        "",
        "**Track Record:**",
        "- 28 Ethernaut challenges completed",
        "- 32 developer tools built",
        "- Open source contributor",
        "",
        "## Impact",
        "",
        project['impact'],
        "",
        "---",
        "*Generated by grant-proposal-gen.py*"
    ])
    
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Generate grant proposals")
    parser.add_argument("--type", choices=list(GRANT_TEMPLATES.keys()), default="gitcoin",
                       help="Grant type/template")
    parser.add_argument("--project", choices=list(NOVA_PROJECTS.keys()), default="agent-security",
                       help="Project to propose")
    parser.add_argument("--output", help="Output file (default: print to stdout)")
    args = parser.parse_args()
    
    proposal = generate_proposal(args.type, args.project)
    
    if args.output:
        Path(args.output).write_text(proposal)
        print(f"Proposal written to: {args.output}")
    else:
        print(proposal)

if __name__ == "__main__":
    main()
