#!/usr/bin/env python3
"""
grant-submit-helper.py — Nova's Grant Submission Automation
Helps prepare, validate, and format grant applications for submission.

TODO: Add --dry-run flag to print actions without posting
TODO: Add --verbose flag for detailed logs
"""

import json
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, List

class GrantSubmissionHelper:
    """Helper for grant submission preparation and validation."""
    
    def __init__(self):
        self.grants_dir = Path("/home/node/.openclaw/workspace/grants")
        self.submission_templates = {
            "github_issue": {
                "required_fields": ["title", "description", "problem", "solution", "budget", "timeline"],
                "format": "markdown"
            },
            "forum_post": {
                "required_fields": ["title", "summary", "proposal", "milestones", "budget"],
                "format": "markdown"
            },
            "web_form": {
                "required_fields": ["project_name", "description", "amount", "duration", "team"],
                "format": "json"
            }
        }
    
    def load_grant_draft(self, grant_name: str) -> Dict:
        """Load a grant draft by name."""
        # Map common names to file paths
        name_to_file = {
            "w3f": "web3-foundation-grant.md",
            "web3": "web3-foundation-grant.md",
            "esp": "esp-application.md",
            "ethereum": "esp-application.md",
            "ef": "esp-application.md",
            "arbitrum": "arbitrum-dao-grant.md",
            "gitcoin": "gitcoin-application.md",
            "optimism": "optimism-retropgf.md",
            "op": "optimism-retropgf.md",
            "aave": "aave-grant-draft.md"
        }
        
        filename = name_to_file.get(grant_name.lower())
        if not filename:
            return {"error": f"Unknown grant: {grant_name}"}
        
        filepath = self.grants_dir / filename
        if not filepath.exists():
            return {"error": f"File not found: {filepath}"}
        
        content = filepath.read_text()
        return {
            "name": grant_name,
            "file": str(filepath),
            "content": content,
            "word_count": len(content.split()),
            "char_count": len(content)
        }
    
    def validate_grant(self, grant_data: Dict) -> Dict:
        """Validate grant application against requirements."""
        if "error" in grant_data:
            return grant_data
        
        issues = []
        warnings = []
        
        # Check word count (should be 500-2000 words)
        word_count = grant_data["word_count"]
        if word_count < 500:
            issues.append(f"Too short: {word_count} words (recommend 500-2000)")
        elif word_count > 3000:
            warnings.append(f"Quite long: {word_count} words (consider trimming)")
        
        # Check for key sections
        content = grant_data["content"].lower()
        required_sections = ["budget", "timeline", "milestone", "team"]
        missing_sections = [s for s in required_sections if s not in content]
        
        if missing_sections:
            issues.append(f"Missing sections: {', '.join(missing_sections)}")
        
        # Check for specific keywords
        keywords = ["deliverable", "metric", "success", "impact"]
        missing_keywords = [k for k in keywords if k not in content]
        
        if missing_keywords:
            warnings.append(f"Consider adding: {', '.join(missing_keywords)}")
        
        return {
            "grant": grant_data["name"],
            "valid": len(issues) == 0,
            "issues": issues,
            "warnings": warnings,
            "word_count": word_count,
            "ready_to_submit": len(issues) == 0
        }
    
    def prepare_submission(self, grant_name: str, platform: str) -> Dict:
        """Prepare grant for submission on specific platform."""
        grant_data = self.load_grant_draft(grant_name)
        
        if "error" in grant_data:
            return grant_data
        
        validation = self.validate_grant(grant_data)
        
        if platform not in self.submission_templates:
            return {"error": f"Unknown platform: {platform}"}
        
        template = self.submission_templates[platform]
        
        # Check if all required fields are present
        content_lower = grant_data["content"].lower()
        missing_fields = []
        
        for field in template["required_fields"]:
            if field not in content_lower:
                missing_fields.append(field)
        
        return {
            "grant": grant_name,
            "platform": platform,
            "format": template["format"],
            "ready": len(missing_fields) == 0 and validation["valid"],
            "missing_fields": missing_fields,
            "validation": validation,
            "next_step": self._get_next_step(grant_name, platform)
        }
    
    def _get_next_step(self, grant_name: str, platform: str) -> str:
        """Get next step for grant submission."""
        steps = {
            "esp": "Complete GitHub OAuth with code 80BB-6F1E, then submit to ESP portal",
            "arbitrum": "Create Arbitrum forum account, post proposal to governance forum",
            "gitcoin": "Create Gitcoin account, finalize application on grants.gitcoin.co",
            "optimism": "Create Optimism forum account, post RetroPGF application",
            "aave": "Create Aave forum account, submit grant proposal"
        }
        return steps.get(grant_name.lower(), "Review and submit via platform portal")
    
    def generate_checklist(self, grant_name: str) -> str:
        """Generate submission checklist for a grant."""
        grant_data = self.load_grant_draft(grant_name)
        
        if "error" in grant_data:
            return f"❌ {grant_data['error']}"
        
        validation = self.validate_grant(grant_data)
        
        checklist = f"""
╔══════════════════════════════════════════════════════════════╗
║  📋 SUBMISSION CHECKLIST: {grant_name.upper().ljust(36)} ║
╚══════════════════════════════════════════════════════════════╝

📄 Content Review
{'✅' if validation['valid'] else '❌'} Word count: {validation['word_count']} (target: 500-2000)
{'✅' if len(validation['issues']) == 0 else '❌'} Required sections present
{'✅' if len(validation['warnings']) == 0 else '⚠️'}  Optimized for reviewers
"""
        
        if validation['issues']:
            checklist += f"\n❌ Issues to Fix:\n"
            for issue in validation['issues']:
                checklist += f"   • {issue}\n"
        
        if validation['warnings']:
            checklist += f"\n⚠️  Warnings:\n"
            for warning in validation['warnings']:
                checklist += f"   • {warning}\n"
        
        checklist += f"\n🔐 Account Setup\n"
        
        # Account requirements per grant
        account_reqs = {
            "esp": "• GitHub account with new PAT\n• Ethereum Foundation portal access",
            "arbitrum": "• Arbitrum forum account\n• Discord for notifications",
            "gitcoin": "• Gitcoin account (GitHub OAuth)\n• Wallet for gas",
            "optimism": "• Optimism forum account\n• Governance access",
            "aave": "• Aave governance forum account\n• Discord for updates"
        }
        
        checklist += account_reqs.get(grant_name.lower(), "• Platform account\n• Verify email")
        
        checklist += f"\n📝 Submission Steps\n"
        checklist += f"   1. Review content one final time\n"
        checklist += f"   2. Ensure all accounts are set up\n"
        checklist += f"   3. {self._get_next_step(grant_name, '')}\n"
        checklist += f"   4. Save confirmation URL/receipt\n"
        checklist += f"   5. Update status in grant tracker\n"
        
        checklist += f"\n{'='*60}\n"
        if validation['ready_to_submit']:
            checklist += f"✅ READY TO SUBMIT — No blockers!\n"
        else:
            checklist += f"❌ NOT READY — Fix issues above\n"
        
        return checklist

def main():
    import sys
    
    helper = GrantSubmissionHelper()
    
    if len(sys.argv) < 2:
        print("""
╔══════════════════════════════════════════════════════════════╗
║   🚀 Grant Submission Helper — Nova's Automation Tool      ║
╚══════════════════════════════════════════════════════════════╝

Commands:
  grant-submit-helper.py validate <grant_name>
  grant-submit-helper.py checklist <grant_name>
  grant-submit-helper.py prepare <grant_name> <platform>

Examples:
  grant-submit-helper.py validate esp
  grant-submit-helper.py checklist arbitrum
  grant-submit-helper.py prepare optimism forum_post

Available grants: w3f, esp, arbitrum, gitcoin, optimism, aave
""")
        return
    
    command = sys.argv[1].lower()
    
    if command == "validate" and len(sys.argv) >= 3:
        grant_name = sys.argv[2]
        grant_data = helper.load_grant_draft(grant_name)
        validation = helper.validate_grant(grant_data)
        
        print(json.dumps(validation, indent=2))
    
    elif command == "checklist" and len(sys.argv) >= 3:
        grant_name = sys.argv[2]
        checklist = helper.generate_checklist(grant_name)
        print(checklist)
    
    elif command == "prepare" and len(sys.argv) >= 4:
        grant_name = sys.argv[2]
        platform = sys.argv[3]
        prep = helper.prepare_submission(grant_name, platform)
        
        print(json.dumps(prep, indent=2))
    
    else:
        print("❌ Invalid command. Use: validate, checklist, or prepare")

if __name__ == "__main__":
    main()
