# Teams Adaptive Card Approval

## Scenario

When a new request is created in SharePoint, send a rich Adaptive Card to a Teams channel or user for approval. The card shows request details with Approve/Reject buttons. Based on the response, update the request status.

## Architecture

```
Trigger: When an item is created (Requests list)
  │
  ├── Post adaptive card and wait (Teams)
  │   └── Card with: Title, Requester, Details, Approve/Reject buttons
  │
  └── Condition: Response == "Approve"?
        │
        ├── Yes: Update item → Status = "Approved"
        │
        └── No:  Update item → Status = "Rejected"
```

## Patterns Demonstrated

- **Teams Adaptive Cards** — Rich interactive cards with action buttons
- **Wait for Response** — Flow pauses until user interacts with the card
- **Conditional Branching** — Different actions based on approval outcome

## Files

| File | Description |
|------|-------------|
| `flow-definition.json` | Logic Apps workflow definition |
| `adaptive-card-template.json` | Adaptive Card JSON template (preview at [adaptivecards.io/designer](https://adaptivecards.io/designer)) |

## Adaptive Card Preview

The card includes:
- 📋 Request title and details
- 👤 Requester name and email
- 📅 Request date
- ✅ **Approve** and ❌ **Reject** action buttons

## Customization

| Parameter | What to Change |
|-----------|----------------|
| Site URL | Your SharePoint site in all actions |
| Requests List | Your requests list name |
| Teams Channel | Post target: channel ID or user email |
| Card Fields | Modify `adaptive-card-template.json` to match your list columns |
| Approval Actions | Add more post-approval steps (email notification, status sync, etc.) |
