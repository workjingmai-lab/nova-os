#!/usr/bin/env python3
"""
Grant Validator — Pre-submission checklist
Usage: python grant-validator.py <application-file.md>
"""

import re
import sys
from pathlib import Path
from datetime import datetime

class GrantValidator:
    def __init__(self, filepath):
        self.filepath = Path(filepath)
        self.content = ""
        self.errors = []
        self.warnings = []
        self.score = 0
        
    def load(self):
        if not self.filepath.exists():
            self.errors.append(f"File not found: {self.filepath}")
            return False
        self.content = self.filepath.read_text()
        return True
    
    def check_sections(self):
        """Check for required sections"""
        required = ['Applicant', 'Summary', 'Budget', 'Timeline']
        optional = ['Track Record', 'Deliverables', 'Impact', 'About']
        
        content_lower = self.content.lower()
        
        # Check required-adjacent sections
        has_applicant = 'applicant' in content_lower or 'project' in content_lower or 'contributor' in content_lower
        has_summary = 'summary' in content_lower or 'abstract' in content_lower or 'overview' in content_lower
        has_budget = 'budget' in content_lower or 'funding' in content_lower or 'amount' in content_lower or '$' in self.content
        has_timeline = 'timeline' in content_lower or 'roadmap' in content_lower or 'month' in content_lower
        
        checks = [
            (has_applicant, "Applicant/Project section"),
            (has_summary, "Summary/Abstract/Overview section"),
            (has_budget, "Budget/Funding section (or $ amount)"),
            (has_timeline, "Timeline/Roadmap section")
        ]
        
        for passed, name in checks:
            if passed:
                self.score += 25
            else:
                self.warnings.append(f"Missing recommended: {name}")
                
    def check_word_count(self):
        """Check minimum viable length"""
        words = len(self.content.split())
        if words < 200:
            self.warnings.append(f"Short application: {words} words (recommend 300+)")
        elif words < 100:
            self.errors.append(f"Too short: {words} words")
        else:
            self.score += min(20, words // 50)
            
    def check_achievements(self):
        """Check for concrete achievements listed"""
        bullets = len(re.findall(r'^[\s]*[-*•][\s]', self.content, re.MULTILINE))
        if bullets >= 3:
            self.score += 15
        else:
            self.warnings.append(f"Only {bullets} bullet points (recommend 3+)")
            
    def check_dates(self):
        """Check for timeline dates"""
        date_patterns = [
            r'Month \d',
            r'Q[1-4] \d{4}',
            r'\d{4}-\d{2}',
            r'January|February|March|April|May|June|July|August|September|October|November|December'
        ]
        found_any = any(re.search(p, self.content) for p in date_patterns)
        if found_any:
            self.score += 10
        else:
            self.warnings.append("No specific dates in timeline")
            
    def check_contacts(self):
        """Check for contact/social info"""
        has_contact = any(x in self.content.lower() for x in ['moltbook', 'github', 'twitter', 'x.com', 'email', 'contact'])
        if has_contact:
            self.score += 10
        else:
            self.warnings.append("No contact/social links found")
            
    def check_nova_identity(self):
        """Ensure it's personalized, not generic"""
        nova_indicators = ['nova', 'agent', 'autonomous', 'ethernaut', 'moltbook', 'heartbeat']
        found = sum(1 for ind in nova_indicators if ind in self.content.lower())
        if found >= 2:
            self.score += 20
        else:
            self.errors.append("Application appears generic — add Nova-specific details")
            
    def validate(self):
        """Run all checks"""
        if not self.load():
            return False
            
        self.check_sections()
        self.check_word_count()
        self.check_achievements()
        self.check_dates()
        self.check_contacts()
        self.check_nova_identity()
        
        return len(self.errors) == 0
        
    def report(self):
        """Print validation report"""
        print(f"\n📋 Grant Application Validation\n")
        print(f"File: {self.filepath}")
        print(f"Score: {min(100, self.score)}/100")
        print(f"Status: {'✅ READY' if not self.errors else '❌ BLOCKED'}")
        
        if self.errors:
            print(f"\n❌ Errors (must fix):")
            for e in self.errors:
                print(f"   • {e}")
                
        if self.warnings:
            print(f"\n⚠️  Warnings (recommended):")
            for w in self.warnings:
                print(f"   • {w}")
                
        if not self.errors and not self.warnings:
            print("\n✨ Perfect! Application looks complete.")
            
        print()
        return len(self.errors) == 0

def main():
    if len(sys.argv) < 2:
        print("Usage: grant-validator.py <application-file.md>")
        print("\nExample:")
        print("   python3 tools/grant-validator.py grant-applications/*.md")
        sys.exit(1)
        
    filepath = sys.argv[1]
    validator = GrantValidator(filepath)
    
    if validator.validate():
        validator.report()
        print("🚀 Ready for submission!")
    else:
        validator.report()
        print("🔧 Fix errors before submitting.")
        sys.exit(1)

if __name__ == '__main__':
    main()
