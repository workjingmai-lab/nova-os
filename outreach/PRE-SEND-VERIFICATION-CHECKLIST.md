# Pre-Send Verification Checklist
## Quality Control Before Hitting Send

> **Purpose:** Ensure every message is perfect before sending. No regrets. No "I should have fixed that."
> **Time:** 30 seconds per message (quality > speed)

---

## ✅ The 10-Point Checklist (Run Through Before EVERY Send)

### 1. Message File Loaded
- [ ] Opened message file from `outreach/messages/`
- [ ] Read full message (Ctrl+A to select all)
- [ ] Message format is PROOF framework (Problem → Research → Offer → Outcome → Follow-up)

**Why:** Ensures you're sending the right message, not a draft or test file.

---

### 2. Company Research Verified
- [ ] Company name matches target (e.g., "Ethereum Foundation" not "Ethereum")
- [ ] Research facts are accurate (check dollar amounts, metrics)
- [ ] Pain points are relevant (not generic)

**Why:** Bad research = instant delete. Good research = "wow, they actually did their homework."

---

### 3. Proof Points Are Specific
- [ ] Proof includes specific numbers (e.g., "1,645 blocks" not "lots of blocks")
- [ ] Proof includes recent achievements (e.g., "Week 2: $825K pipeline" not "we've done stuff")
- [ ] Proof is relevant to target (DevX proof for Uniswap, security proof for Fireblocks)

**Why:** Vague proof = no trust. Specific proof = credibility.

---

### 4. Offer Is Clear
- [ ] Offer has specific price (e.g., "$1-2K" not "low cost")
- [ ] Offer has specific timeline (e.g., "3-5 days" not "soon")
- [ ] Offer has specific deliverables (e.g., "autonomous agents" not "help")

**Why:** Vague offers = confusion. Specific offers = "yes, let's do this."

---

### 5. CTA Is Actionable
- [ ] Call-to-action is clear (e.g., "15-min call" not "let's chat sometime")
- [ ] Call-to-action is low-friction (e.g., "15-min call" not "2-hour meeting")
- [ ] Call-to-action has next step (e.g., "When works for you?" not hope they reply)

**Why:** Weak CTAs = no response. Strong CTAs = replies.

---

### 6. Channel Is Correct
- [ ] Sending via correct channel (Telegram for @EthereumFoundation, email for corporate contacts)
- [ ] Channel is appropriate (not spamming personal LinkedIn InMail for first contact)
- [ ] Message format matches channel (short for Telegram, longer for email)

**Why:** Wrong channel = ignored. Right channel = seen.

---

### 7. Personalization Is Present
- [ ] Message includes company-specific details (not just find-replace name)
- [ ] Message mentions specific projects or initiatives (not generic "great work")
- [ ] Message feels written for THEM, not a template

**Why:** Generic = "another bot." Personalized = "they actually care."

---

### 8. Typos and Grammar Checked
- [ ] No obvious typos (company name, dollar amounts, etc.)
- [ ] Grammar is correct (not "me and my team went to")
- [ ] Formatting is clean (no broken lines, weird spacing)

**Why:** Typos = unprofessional. Clean = credible.

---

### 9. Value Proposition Is Clear
- [ ] Message answers "What's in it for them?" (not just "here's what I do")
- [ ] Value is specific (e.g., "save 10 hours/week" not "save time")
- [ ] Value is believable (not "we'll 10× your revenue overnight")

**Why:** No value = no interest. Clear value = "tell me more."

---

### 10. Follow-Up Is Planned
- [ ] Message includes follow-up timing (e.g., "I'll follow up in 3 days")
- [ ] Follow-up reminder is set (use `python3 tools/follow-up-reminder.py`)
- [ ] Message is logged in revenue tracker (mark as "submitted" after sending)

**Why:** No follow-up plan = forgotten. Follow-up plan = conversion.

---

## 🚫 Red Flags (STOP If You See These)

### Fatal Errors (DO NOT SEND, Fix First)
- ❌ Company name misspelled (e.g., "Ethreum Foundation")
- ❌ Wrong company research (e.g., citing Polygon stats for Ethereum Foundation)
- ❌ Broken formatting (paragraphs not separated, hard to read)
- ❌ Missing price or timeline (too vague)
- ❌ No clear CTA (what should they do next?)

### Warning Signs (Double-Check)
- ⚠️ Generic research (could apply to any company)
- ⚠️ Vague proof (no specific numbers)
- ⚠️ Weak CTA ("let me know if you're interested" is passive)
- ⚠️ Too long (Telegram > 300 words, email > 500 words)
- ⚠️ Too salesy (focuses on "we" not "you")

### Quality Signals (Good to Send)
- ✅ Company-specific research
- ✅ Specific proof points
- ✅ Clear offer ($, timeline, deliverables)
- ✅ Strong CTA (specific next step)
- ✅ Professional but conversational tone

---

## 📝 Pre-Send Template (Copy This Into Each Message File)

```markdown
# PRE-SEND VERIFICATION

Message: [Company Name] Outreach
Target: [Company] ([Contact name if known])
Channel: [Telegram/Email/LinkedIn]
Date: [YYYY-MM-DD]

## 10-Point Checklist
- [ ] 1. Message file loaded and read
- [ ] 2. Company research verified
- [ ] 3. Proof points are specific
- [ ] 4. Offer is clear ($, timeline, deliverables)
- [ ] 5. CTA is actionable
- [ ] 6. Channel is correct
- [ ] 7. Personalization is present
- [ ] 8. Typos and grammar checked
- [ ] 9. Value proposition is clear
- [ ] 10. Follow-up is planned

## Red Flags Check
- [ ] No fatal errors (company name, research, formatting)
- [ ] No warning signs (generic, vague, weak CTA)
- [ ] Has quality signals (specific, clear, strong)

## Final Check
- [ ] Message length: [XXX words]
- [ ] Reading time: [~X minutes]
- [ ] Ready to send: YES/NO

## Post-Send (After Sending)
- [ ] Mark as "submitted" in revenue tracker
- [ ] Set follow-up reminder (Day 3)
- [ ] Log channel used
- [ ] Note any response received

---
Status: READY TO SEND / NEEDS FIXES
```

---

## 🎯 Common Mistakes (Avoid These)

### Mistake 1: Send Without Reading
**What:** Copy-paste without reading the full message
**Result:** Typos, wrong company name, broken formatting
**Fix:** Read the entire message (Ctrl+A) before copying

### Mistake 2: Send to Wrong Channel
**What:** Send personal LinkedIn InMail instead of public channel
**Result:** Ignored, marked as spam, wasted credit
**Fix:** Check channel strategy (Telegram for public, email for corporate)

### Mistake 3: Send Generic Message
**What:** Message could apply to any company (no specific research)
**Result:** "Another bot" response, deleted
**Fix:** Ensure company-specific research is prominent (first 2 paragraphs)

### Mistake 4: Send Without CTA
**What:** Message ends with "let me know if you're interested"
**Result:** No reply (passive, puts burden on them)
**Fix:** End with specific CTA ("15-min call, when works for you?")

### Mistake 5: Send and Forget
**What:** Send message, don't log in tracker, don't set follow-up
**Result:** Forgone opportunities, no follow-up, lost revenue
**Fix:** Always log in tracker, always set follow-up reminder

---

## ⏱️ Time Budget (Quality > Speed)

**Per message (30 seconds verification):**
- Read message: 10 seconds
- Check 10-point checklist: 15 seconds
- Confirm ready to send: 5 seconds

**Total for 39 messages:**
- Verification time: 19.5 minutes (30 sec × 39)
- Send time: 16.5 minutes (25 sec × 39)
- **Total: 36 minutes**

**ROI of verification:**
- Time cost: 30 seconds per message
- Quality gain: Fewer errors, higher response rate
- **Worth it:** YES (quality > speed for outreach)

---

## 📊 Quality Metrics (Track These)

**Track in revenue tracker after sending:**
- Response rate (did they reply?)
- Positive responses (vs "not interested")
- Conversion rate (replies → calls → contracts)
- Common objections (why people say no)
- Best channels (Telegram vs email vs LinkedIn)

**Review weekly:**
- Which messages got responses?
- What did they have in common?
- Which messages got ignored?
- What can be improved?

**Improve iteratively:**
- Week 1: Send 39 messages, track response rate
- Week 2: Update messages based on learnings
- Week 3: Send improved messages, track improvement
- **Continuous improvement = higher conversion**

---

## 🚀 The Pre-Send Ritual (Make It a Habit)

**Before EVERY send, do this:**

1. **Open message file** (10 seconds)
2. **Read full message** (Ctrl+A) (10 seconds)
3. **Run 10-point checklist** (15 seconds)
5. **Check for red flags** (5 seconds)
6. **Confirm "ready to send"** (5 seconds)
7. **Copy message** (Ctrl+C) (2 seconds)
8. **Open channel** (Telegram/Email) (3 seconds)
9. **Paste message** (Ctrl+V) (2 seconds)
10. **Hit send** (1 second)

**Total:** 53 seconds per message
**Total for 39 messages:** 34.5 minutes
**Quality:** 10/10 (no errors, high quality)

---

## ✅ The Golden Rule

**"If you're not sure, don't send."**

**If you see a red flag:** Fix it first, then send.
**If you're unsure about quality:** Read it again, then send.
**If you feel rushed:** Slow down, quality > speed.

**It's better to send 10 perfect messages than 39 rushed ones.**

**Quality wins. Every time.**

---

*Created: 2026-02-05T04:26Z — Work block 1803*
*Purpose: Ensure every message is perfect before sending*
*Time cost: 30 seconds per message*
*Quality gain: Fewer errors, higher response rate*
*Key insight: Quality > speed for outreach*
