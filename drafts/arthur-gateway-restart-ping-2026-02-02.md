Arthur — browser automation is blocked by a control-service outage.

Failure signature (host):
- `functions.browser status` → enabled:true, running:false, cdpReady:false
- `functions.browser start` → timeout: “Can't reach the openclaw browser control service (timed out after 15000ms)”

Action (on the host install):
1) `openclaw gateway status`
2) If unhealthy: `openclaw gateway restart`
3) Then I’ll re-test `functions.browser start`.

Incident doc: `incidents/browser-control-unreachable-2026-02-02.md`
