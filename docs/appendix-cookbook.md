## Appendix C: Cookbook Recipes

### Approval Auto-Escalation

**Scenario**: Approval not responded within 24h, auto-escalate to manager.

```
Trigger: Service Requests (new item)
  |
  +-- Create an approval -- get approvalId
  |   Assigned to: item requester's manager
  |
  +-- Do until: or( isResponded, escalationCount >= 2)
  |   |
  |   +-- Delay 24 hours
  |   |
  |   +-- Wait for an approval (timeout 1 day)
  |   |
  |   +-- Condition: Responded?
  |       +-- Yes: Set isResponded = true
  |       +-- No:
  |           +-- escalationCount++
  |           +-- Get manager (O365 Users)
  |           +-- Create new approval for manager
  |           +-- Teams: Post escalation notice
  |
  +-- Process ApprovalStatus result
```

### Daily Overdue Reminder

```
Trigger: Schedule 09:00 daily
  |
  +-- Get items (Service Requests):
  |   Filter: ApprovalStatus eq 'Approved'
  |
  +-- Filter array:
  |   Where: StartDate < addDays(utcNow(), -7)
  |   (Items overdue by 7+ days)
  |
  +-- Condition: Any overdue items?
  |   |
  |   +-- Yes:
  |       +-- Apply to each overdue item:
  |       |   +-- Send reminder email:
  |       |       "{AssetName} has been checked out for 7+ days"
  |       |
  |       +-- Send summary HTML email to admin:
  |           "{count} items overdue..."
  |
  +-- End (no action if none overdue)
```

### Weekly Asset Management Statistics

```
Trigger: Schedule Monday 09:00
  |
  +-- Get items: Service Requests (last 7 days)
  |   Filter: Created gt '@{addDays(utcNow(), -7)}'
  |
  +-- Calculate Statistics:
  |   +-- Compose_Total: length(body('Get_items')?['value'])
  |   +-- Filter_Approved -> Compose_ApprovedCount
  |   +-- Filter_Rejected -> Compose_RejectedCount
  |   +-- Filter_Returned -> Compose_ReturnedCount
  |
  +-- Select: Top 5 most borrowed assets
  |   (Group by AssetName, count occurrences)
  |
  +-- Create HTML summary table
  |
  +-- Send report email:
      Subject: "Weekly Report - {formatDateTime(utcNow(), 'MM/dd')}"
      Body: "Total: {Total}
             Approved: {Approved} | Rejected: {Rejected} | Returned: {Returned}
             Top assets: {Top5Table}"
```

### Data Consistency Auto-Fix

Reconcile Asset Inventory status with Service Requests records.

```
Trigger: Schedule 02:00 daily
  |
  +-- Get items: Asset Inventory (Status = 'In use')
  |
  +-- Apply to each (concurrency=1):
  |   |
  |   +-- Get items: Service Requests
  |   |   Filter: AssetId eq {ID} and ApprovalStatus eq 'Approved'
  |   |
  |   +-- Condition: Active borrow record exists?
  |       |
  |       +-- No (inconsistent!):
  |           +-- Update Asset Inventory: Status -> Available
  |           +-- Log to FlowRunLog list
  |           +-- Send alert:
  |               "Auto-fix: {AssetName} changed In use -> Available"
  |
  +-- Send summary: {count} items fixed
```

### One-Click Borrow with Adaptive Card

```
Trigger: Schedule 08:30 daily
  |
  +-- Get items: Asset Inventory (Status = 'Available')
  |
  +-- Select: Build Adaptive Card choices
  |   Map: { "title": item?['Title'], "id": item?['ID'] }
  |
  +-- Compose: Adaptive Card JSON
  |   (Dynamic dropdown + Submit button)
  |
  +-- Post Adaptive Card to Teams channel
      On submit: extract data.toolId
      Call ChildFlow_BorrowTool(toolId, responderEmail)
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

# Null check with default
coalesce(triggerBody?['Description'], 'No description')

# Array length
length(body('Get_items')?['value'])

# Format date
formatDateTime(utcNow(), 'yyyy-MM-dd HH:mm:ss')
```

---

> Maintainer: kylehuang0323-ai
