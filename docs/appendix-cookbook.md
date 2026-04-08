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

## Appendix B: Quick Reference Card

### Common Expression Cheat Sheet

```
# Current time
utcNow() 
# Local time (example: Pacific Standard Time)
convertFromUtc(utcNow(), 'Pacific Standard Time')

# 7 days later
addDays(utcNow(), 7)

# Concat title
concat('Borrow - ', triggerBody?['Title'])

# Conditional value
if(equals(body('Get_item')?['Status']?['Value'], 'Available'), 'Yes', 'No')

# People column Claims
concat('i:0#.f|membership|', triggerBody?['headers']?['x-ms-user-email'])

# Null check
coalesce(triggerBody?['Description'], ' / No description')

# Array length
length(body('Get_items')?['value'])

# Format date
formatDateTime(utcNow(), 'yyyy-MM-dd HH:mm:ss')
```

---

> ✏️ Maintainer: kylehuang0323-ai
