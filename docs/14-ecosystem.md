## Ecosystem Integration & Frontier Capabilities

> 🚀 This chapter covers deep integration with AI/Copilot, Teams Adaptive Cards, Power Apps,
> Dataverse, Desktop Flows (RPA), Custom Connectors, and governance toolkits.

### AI Builder & Copilot Integration

#### Copilot in Power Automate

```
Use Cases:
1. Create Flow from natural language
 e.g., "When a SharePoint item is created, send approval"
 → Copilot generates: trigger + condition + approval + notification

2. Edit existing Flow with Copilot
 → Copilot adds Outlook Send email action

3. Ask Copilot questions about your Flow

Entry:
 make.powerautomate.com → Open Flow → Click Copilot icon
```

#### AI Builder Models

| Model | Purpose | Asset Management Scenario |
|---|---|---|
| **Document Processing** | Extract data from PDF/images | Auto-import from scanned inventory forms |
| **Text Classification** | Categorize text | Auto-classify request types |
| **Sentiment Analysis** | Analyze sentiment | Analyze user feedback |
| **Entity Extraction** | Extract entities from text | Extract tool name + requester from email |
| **GPT (Create text with GPT)** | Generate text | Auto-generate confirmation messages |
| **Object Detection** | Detect objects in images | Photo-verify return condition |

#### Using AI Builder in Flows

```
# Example: Generate personalized notification with GPT

Flow structure:
 ├── Trigger: Service Requests (new item)
 ├── Get item details
 ├── AI Builder: Create text with GPT
 │ Input: Item title, requester name, date
 │ ← Output: AI-generated message
 └── Send email (V2): Include AI-generated content
```

> ⚠️ **AI Builder Credits**
> AI Builder requires credits — monthly quota, additional credits cost extra.

### Teams + Adaptive Cards Patterns

#### Adaptive Cards Basics

Adaptive Cards are cross-platform UI cards enabling **rich interactions** in Teams (buttons, forms, selectors).

```json
// Asset management approval card example
{
 "type": "AdaptiveCard",
 "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
 "version": "1.4",
 "body": [
 {
 "type": "TextBlock",
 "text": "🔧 ",
 "weight": "Bolder",
 "size": "Large"
 },
 {
 "type": "FactSet",
 "facts": [
 { "title": "", "value": "${AssetName}" },
 { "title": "", "value": "${RequesterName}" },
 { "title": "", "value": "${RequestDate}" }
 ]
 },
 {
 "type": "TextBlock",
 "text": "",
 "wrap": true
 }
 ],
 "actions": [
 {
 "type": "Action.Submit",
 "title": "✅ ",
 "style": "positive",
 "data": { "action": "approve", "requestId": "${RequestId}" }
 },
 {
 "type": "Action.Submit",
 "title": "❌ ",
 "style": "destructive",
 "data": { "action": "reject", "requestId": "${RequestId}" }
 }
 ]
}
```

#### Sending Adaptive Cards in Flow

```
# 1: " Adaptive Card "
# Post adaptive card and wait for a response

Teams → Adaptive Card
 Team: Contoso
 Channel:
 Card: ( JSON)
 : " @{body('Post_adaptive_card')?['responderDisplayName']} "
 ← : body('Post_adaptive_card')?['data']?['action']

# 2: " Adaptive Card"
# Post card without waiting

# 3: "Post Adaptive Card to a Teams user and wait"
# Send to specific user and wait
```

#### Teams @Mention / @

```
# @mention a user in Teams message
<at></at>

# HTML :
<at>admin</at>
```

#### Teams Notification Best Practices

```
✅ :
 - Adaptive Card
 - "Post and wait"

❌ :
 - Flow Teams
 - debug
```

### Power Apps ↔ Power Automate Integration

#### Triggering Flow from Power Apps

```
# 1. Flow "Power Apps (V2)"
# 3. ( "Respond to a PowerApp or flow" )
# 4. Power Apps : → Power Automate → Flow

Power Apps: Button formula example:
 // Flow
 Set(varResult,
 AssetMgmt_CreateRequest.Run(
 ThisItem.ID, // AssetId
 User.Email // RequesterEmail
 )
 );
 If(varResult.Status = "Success",
 Notify("!", NotificationType.Success),
 Notify(varResult.Message, NotificationType.Error)
 );
```

#### Flow Operating Power Apps Data

```
# Power Apps Dataverse SharePoint

: Power Apps → SharePoint ← Flow
 ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
 │ Power Apps │─────→│ SharePoint │←─────│ Power Automate│
 │ │ │ │ │ │
 │ │ │ Service Requests │ │ │
 └──────────────┘ └──────────────┘ └──────────────┘
```

### Custom Connector Development

#### When to Build Custom Connectors

```
 - REST API
 - SaaS
 - Flow API

 - → HTTP DLP
```

#### Creating a Custom Connector

```
 1: OpenAPI/Swagger
 make.powerautomate.com → → → OpenAPI
 swagger.json →

 1. : URL
 2. : API Key / OAuth 2.0 / Basic Auth
 3. : API endpoint

 Authentication Types:
 ┌─────────────────┬──────────────────────────────┐
 │ / Method │ / Use Case │
 ├─────────────────┼──────────────────────────────┤
 │ No Auth │ API │
 │ API Key │ API │
 │ Basic Auth │ │
 │ OAuth 2.0 │ Microsoft GraphGoogle │
 │ Microsoft Entra │ API │
 └─────────────────┴──────────────────────────────┘
```

> Custom connectors may be blocked by DLP policies. Check your environment policies first.

### RPA / Desktop Flows & RPA

#### Desktop Flows Overview

Desktop flows automate **local desktop application** operations — traditional RPA.

```
 Run Modes:
 ┌────────────────┬─────────────────────────────────┐
 │ │ │
 │ Attended │ Runs while user is logged in │
 ├────────────────┼─────────────────────────────────┤
 │ │ │
 │ Unattended │ Runs in background (dedicated VM) │
 └────────────────┴─────────────────────────────────┘

 Toolchain:
 Power Automate Desktop (PAD)
```

#### RPA Scenario Examples

```
 ├── OCR scan (PAD OCR)
 ├── Extract to Excel
 ├── Upload to SharePoint

 ├── Generate report → PDF
 ├── PAD Excel → SharePoint upload
 └── Archive PDF → SharePoint

 ├── PAD data scraping (via API)
 ├── Export to CSV
 └── Upload CSV → SharePoint
```

### Dataverse Integration Patterns

#### When to Migrate from SP to Dataverse

| Dimension | SharePoint Lists | Dataverse |
|---|---|---|
| Capacity | ≤ 30M items(), <5000 view threshold | Unlimited rows |
| Relational | Lookup columns only | Full relational model |
| Transactions | No native support | Built-in transactions |
| Security | Site + list permissions | Row-level security (RLS) |
| Throttling | 5000 items API limit | Higher throughput |
| Offline | No | Power Apps offline |
| License | M365 included | Automate Premium required |

#### Dataverse Triggers

```
# "When a row is added, modified, or deleted" trigger
# More reliable than SharePoint webhook triggers

 Table: Asset Inventory
 Change type: Added, Modified, Deleted
 Scope: Organization / Business Unit / User
 Filter rows: Status eq 'Available'
 Select columns: toolid, title, status
```

### Governance & CoE Toolkit

#### Center of Excellence (CoE) Starter Kit

 Power Platform Flow/App
Microsoft's official governance toolkit for Power Platform — discover, clean up, and audit.

```
CoE: Core Components:
 ┌────────────────────────────┐
 │ 1. (Core) │ → Flow/App
 ├────────────────────────────┤
 │ 2. (Governance) │ → Flow DLP
 ├────────────────────────────┤
 │ 3. (Nurture) │ → Maker
 ├────────────────────────────┤
 │ 4. (Audit) │ → Flow
 └────────────────────────────┘

: https://aka.ms/CoEStarterKit
```

#### Power Automate Management Connector

```
# Flow Flow —
# Manage Flows with Flows — meta-programming

 Available Actions:
 - (List My Flows)
 - (Get Flow)
 - (Get Flow Runs)
 - (Create Flow)
 - (Edit Flow)
 - / (Enable/Disable Flow)
 - (Delete Flow)

# Example: Daily check for failing Flows and alert

 ( 9:00):
 ├── → Flow
 ├── Apply to each:
 │ ├── (24, Status=Failed)
 │ └── : > 3?
 │ └── : failedFlows
 └── : failedFlows ?
 └── : (Teams/Email)
```

#### Environment Strategy

```
 Recommended Environment Structure:
 ┌──────────────────────────────────────────┐
 │ Default ( DLP) │
 │ → │
 │ → │
 ├──────────────────────────────────────────┤
 │ Project-Dev │
 │ → Lab Manager │
 │ → & │
 ├──────────────────────────────────────────┤
 │ Project-Prod │
 │ → │
 │ → │
 └──────────────────────────────────────────┘
```

---

## Appendix C: Cookbook Recipes

### Approval Auto-Escalation

**Scenario**: Approval not responded within 24h, auto-escalate to manager.

```
: Service Requests
 │
 ├── (Create an approval) —
 │ :
 │
 ├── Do until: or( isResponded, escalationCount >= 2)
 │ │
 │ ├── 24
 │ │
 │ ├── (Wait for an approval, timeout 1)
 │ │
 │ └── : ?
 │ ├── : Set isResponded = true
 │ └── :
 │ ├── escalationCount++
 │ ├── (O365 Users → Get manager)
 │ ├──
 │ └── Teams : ""
 │
 └── ApprovalStatus
```

### Daily Overdue Tool Reminder

```
: 09:00
 │
 ├── Get items (Service Requests):
 │ Filter: ApprovalStatus eq 'Approved'
 │
 ├── Filter array:
 │ Where: StartDate < addDays(utcNow(), -7)
 │ ← 7
 │
 ├── : ?
 │ │
 │ └── :
 │ ├── Apply to each :
 │ │ └── :
 │ │ " {AssetName} 7 "
 │ │
 │ └── HTML →
 │ " {length} ..."
 │
 └── (: )
```

### Weekly Asset Management Statistics

```
: 09:00
 │
 ├── 7 Service Requests
 │ Filter: Created gt '@{addDays(utcNow(), -7)}'
 │
 ├── Statistics:
 │ ├── Compose_Total: length(body('Get_items')?['value'])
 │ ├── Filter_Approved → Compose_ApprovedCount
 │ ├── Filter_Rejected → Compose_RejectedCount
 │ └── Filter_Returned → Compose_ReturnedCount
 │
 ├── Select: Top 5
 │ ( AssetName )
 │
 ├── HTML :
 │
 └── :
 : "📊 - {formatDateTime(utcNow(), 'MM/dd')}"
 " {Total}
 {Approved} | {Rejected} | {Returned}
 : {Top5Table}
 : {DetailTable}"
```

### Data Consistency Auto-Fix

 Asset Inventory Service Requests

```
: 02:00
 │
 ├── Get items: Asset Inventory (Status = 'In use')
 │
 ├── Apply to each (=1):
 │ │
 │ ├── Get items: Service Requests
 │ │ Filter: AssetId eq {ID}
 │ │ and ApprovalStatus eq 'Approved'
 │ │
 │ └── : ?
 │ │
 │ └── (!):
 │ ├── Asset Inventory: Status → Available
 │ ├── : FlowRunLog
 │ └── :
 │ "⚠️ : {AssetName} In use Available
 │ : "
 │
 └── : {count}
```

### One-Click Borrow with Adaptive Card

```

: 08:30
 │
 ├── Get items: Asset Inventory (Status = 'Available')
 │
 ├── Select: Adaptive Card
 │ Map: { "title": item?['Title'], "id": item?['ID'] }
 │
 ├── Compose: Adaptive Card JSON
 │ ( + "" )
 │
 └── Teams: Adaptive Card
 → data.toolId
 → ChildFlow_BorrowTool(toolId, responderEmail)
```

---
