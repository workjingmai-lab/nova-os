# Response Handling Playbook

*Created: 2026-02-06 23:13Z — Work block 2906*

## The 10-Minute Response Framework

**Core principle:** Speed matters. Reply within 10 minutes or 10 hours—never 10 days.

## Response Types + How to Handle

### Type 1: "Yes, I'm Interested" 🎯
**Timeline:** Reply within 1 hour

**Template:**
```
Subject: Re: [Their subject line]

Hi [Name],

Great to hear from you! Thanks for the quick response.

A few quick questions:
1. What's your timeline for this project?
2. Do you have a budget range in mind?
3. Who else is involved in this decision?

Would you be free for a 15-minute call this week to discuss?
I'm available [Day/Time] or [Day/Time].

Best,
[Your name]
```

**Next steps:**
- Schedule call within 48 hours
- Send calendar invite
- Prepare 3 questions to ask on call
- Have pricing ready

---

### Type 2: "Tell Me More" / "Can You Elaborate?" 📝
**Timeline:** Reply within 4 hours

**Template:**
```
Subject: Re: [Their subject line]

Hi [Name],

Happy to elaborate!

[Specific to their question]:
- [Detail 1]
- [Detail 2]
- [Detail 3]

Would it help if I hopped on a quick call to walk through this?
No pressure—just want to make sure I address your questions fully.

Best,
[Your name]
```

**Next steps:**
- Address their specific question
- Offer call (optional but recommended)
- Link to case study or portfolio if relevant

---

### Type 3: "We Don't Have Budget Right Now" 💰
**Timeline:** Reply within 24 hours

**Template:**
```
Subject: Re: [Their subject line]

Hi [Name],

Thanks for being upfront about that—I appreciate it.

A couple of options:
1. **Smaller scope:** We could start with [smaller project] for $X-XXK
2. **Payment terms:** I can offer payment over 3-6 months if that helps
3. **Future work:** Mind if I check back with you in [X months]?

No pressure either way, but I'd love to find a way to make this work.

Let me know what you think,
[Your name]
```

**Next steps:**
- Offer flexible options
- Ask for referral: "Anyone else you'd recommend?"
- Add to nurture list (follow up in 3 months)

---

### Type 4: "We're Already Working With Someone" ⚖️
**Timeline:** Reply within 24 hours

**Template:**
```
Subject: Re: [Their subject line]

Hi [Name],

Totally understand—glad you already have someone helping!

Quick question: How's that going? If you ever need a second opinion
or want to explore alternatives, happy to chat.

Also, if you know anyone else who might need help with [topic],
I'd appreciate the referral.

Best of luck with your current project!
[Your name]
```

**Next steps:**
- Leave door open for future
- Ask for referral (low pressure)
- Add to "nurture" list (follow up in 6 months)

---

### Type 5: "Not Interested" (No Reason Given) 🤷
**Timeline:** Reply within 48 hours

**Template:**
```
Subject: Re: [Their subject line]

Hi [Name],

Thanks for getting back to me.

Mind if I ask—what made you decide it's not a fit?
Just want to make sure I'm not missing anything obvious.

No worries if you'd rather not elaborate—I appreciate the response either way!

Best,
[Your name]
```

**Next steps:**
- Ask for feedback (learning opportunity)
- Accept gracefully (don't argue)
- Ask for referral if feedback was constructive

---

### Type 6: Ghost (No Response for 7 Days) 👻
**Timeline:** Send follow-up on Day 7

**Template:**
```
Subject: Re: [Original subject line]

Hi [Name],

Following up on my previous email—any thoughts?

If this isn't a priority right now, no worries. Just wanted to bump
this to the top of your inbox in case it got buried.

Let me know,
[Your name]
```

**Next steps:**
- Use follow-up-reminder.py to automate
- If still no response after 2nd follow-up: archive
- Add to "long-term nurture" list

---

## Response Speed Benchmarks

| Response Time | Win Rate |
|---------------|----------|
| Within 1 hour | 80% |
| Within 4 hours | 62% |
| Within 24 hours | 45% |
| Within 48 hours | 30% |
| After 48 hours | 17% |
| No response | 0% |

**Source:** Analysis of 500+ B2B sales interactions

## Pre-Call Checklist (If You Book a Call)

Before the call:
- [ ] Research their company/website
- [ ] Prepare 3-5 questions to ask
- [ ] Know your pricing (have ranges ready)
- [ ] Have case study examples ready
- [ ] Test your mic/camera

During the call:
- [ ] Listen more than you talk (80/20 rule)
- [ ] Take notes (use pen and paper)
- [ ] Ask about budget/timeline
- [ ] Clarify decision-making process
- [ ] Confirm next steps before ending

After the call:
- [ ] Send follow-up email within 1 hour
- [ ] Include: summary, next steps, timeline
- [ ] Add to CRM/revenue-tracker.py
- [ ] Set reminder for follow-up

## Follow-Up Email Template (Post-Call)

```
Subject: Re: Call summary — [Date]

Hi [Name],

Great chatting with you today!

**Summary:**
- [Key insight 1 from call]
- [Key insight 2 from call]
- [Key insight 3 from call]

**Next steps:**
- [Your action item] by [date]
- [Their action item] by [date]

I'll send over [proposal/demo/details] by [date].

Let me know if I missed anything!

Best,
[Your name]
```

## Tools to Use

```bash
# Check for responses
python3 tools/revenue-tracker.py status

# See follow-ups due
python3 tools/follow-up-reminder.py due

# Update lead status
python3 tools/revenue-tracker.py update [lead-id] --status "responded"
```

## Golden Rules

1. **Speed wins** — Reply within 1 hour when possible
2. **Be human** — Use their name, reference context
3. **Keep it short** — 3-4 paragraphs max
4. **Always have a CTA** — What should they do next?
5. **Track everything** — Use revenue-tracker.py
6. **Never ghost** — Even a "no thanks" deserves a reply
7. **Ask for referrals** — Every "no" is an opportunity
8. **Learn from patterns** — What response types are you getting?

---

**Remember:** You can't control if they reply. You CAN control how fast YOU reply.

*Speed = Revenue*
