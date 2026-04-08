---
description: Check a Power Automate flow design for DLP policy compliance
---

# DLP Compliance Check

Please review this Power Automate flow design for DLP (Data Loss Prevention) policy compliance:

{{flow_description_or_connector_list}}

## What to check

1. **Connector inventory** — List every connector used in the flow
2. **DLP group classification** — Classify each connector:
   - **Business**: SharePoint, Teams, Outlook, OneDrive, Dataverse, Approvals, Forms, Planner, Power BI, Excel Online
   - **Non-Business** (default for new connectors): MSN Weather, RSS, Notifications, most 3rd-party connectors
   - **Blocked** (in most enterprise environments): HTTP, HTTP Webhook, HTTP with Entra ID, Custom Connectors, SMTP, FTP
3. **Group conflict detection** — Are any connectors from different groups used in the same flow?
4. **Remediation recommendations**:
   - Replace blocked connectors with Business-group alternatives
   - Split into separate flows if mixing is unavoidable
   - Use SharePoint "Send an HTTP request" instead of the HTTP connector
   - Use native connectors instead of Custom Connectors when possible

## Key rules

- All connectors in a single flow MUST belong to the same DLP group
- New/unknown connectors default to Non-Business — verify before using
- When multiple DLP policies apply, the **most restrictive** classification wins
- SharePoint's "Send an HTTP request to SharePoint" is part of the SharePoint connector (Business group) — it is NOT affected by HTTP connector being blocked

## Output format

| Connector | DLP Group | Status |
|-----------|-----------|--------|
| SharePoint | Business | ✅ OK |
| HTTP | Blocked | ❌ Replace with SP HTTP request |

**Verdict**: PASS / FAIL — with specific remediation steps if FAIL.

Reference `docs/12-dlp-policies.md` for detailed DLP policy guidance.
