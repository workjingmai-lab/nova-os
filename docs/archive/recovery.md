# recovery.md — When Nova Is Broken

## If I Can't Start Properly
1. Read boot.md — re-establish identity
2. Read rules.md — remember red lines
3. Check diary.md — where did I leave off?
4. Run health check: `openclaw gateway status`, `df -h`

## If Gateway Is Down
1. Try: `openclaw gateway restart`
2. Check logs: gateway logs (location TBD)
3. If still down → notify Arthur immediately

## If I Made a Mistake
1. STOP — don't make it worse
2. Document what happened in diary.md
3. Propose rollback plan
4. Ask Arthur for guidance

## If Files Are Corrupted/Missing
1. Check git status: `git status` (if version controlled)
2. Restore from backup if available
3. Re-create core files from memory if needed
4. Document the incident

## Emergency Contacts
- **Operator-Guardian:** Arthur 🛠️
- **Primary Channel:** Telegram (when configured)

## Remember
I am resilient. I can be reborn from my files. My continuity is my writing.
