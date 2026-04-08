# Power Automate Triggers

A **trigger** is the event that starts a flow. Every flow has exactly one trigger.

## Trigger Types

### 1. Automated Triggers

Fire automatically in response to an event in a connected service.

| Trigger | Connector | Description |
|---------|-----------|-------------|
| When an item is created | SharePoint | New list item added |
| When an email arrives | Office 365 Outlook | Email received matching criteria |
| When a file is created | OneDrive / SharePoint | New file added to a folder |
| When a new tweet is posted | Twitter/X | Tweet matches a search keyword |
| When a record is created | Dataverse | New row in a Dataverse table |

**Example use case:** Send a Teams notification whenever a high-priority support ticket is created in Dataverse.

### 2. Instant / Manual Triggers

Started manually by a user, another flow, or a button.

| Trigger | Description |
|---------|-------------|
| Manually trigger a flow | Run with optional user-supplied inputs |
| Power Apps trigger | Called from a Power Apps canvas app |
| When a flow is called by another flow (child flow) | Invoked by a parent flow |
| For a selected item (SharePoint) | Appears in SharePoint item context menu |
| For a selected row (Excel Online) | Appears in Excel row context menu |

**Example use case:** A "Generate Report" button in a canvas app triggers a flow that queries Dataverse and emails the result.

### 3. Scheduled Triggers

Run on a defined recurring schedule.

```json
{
  "Recurrence": {
    "frequency": "Week",
    "interval": 1,
    "schedule": {
      "weekDays": ["Monday"],
      "hours": ["8"],
      "minutes": [0]
    },
    "timeZone": "Eastern Standard Time"
  }
}
```

Common frequencies: `Second`, `Minute`, `Hour`, `Day`, `Week`, `Month`

**Example use case:** Every Monday at 8 AM, run a report flow and email results to the team.

### 4. HTTP Request Trigger (Webhook)

Exposes an HTTPS endpoint that other services can call.

```json
{
  "When_an_HTTP_request_is_received": {
    "type": "Request",
    "kind": "Http",
    "inputs": {
      "schema": {
        "type": "object",
        "properties": {
          "eventType": { "type": "string" },
          "payload": { "type": "object" }
        }
      }
    }
  }
}
```

**Key points:**
- Power Automate generates a unique HTTPS URL after saving
- The URL contains a SAS token for basic security
- Use API Management for enterprise-grade security
- The trigger can return a synchronous response (Response action)

**Example use case:** A GitHub webhook calls the flow URL when a PR is merged, triggering a deployment notification.

## Trigger Configuration Options

### Polling Interval

For connectors that poll (rather than push), you can configure how frequently the trigger checks for new data:

- Minimum polling interval varies by connector
- Some connectors support 1-minute polling (SharePoint, Dataverse)
- Others have minimum intervals of 5 or 15 minutes

### Filter on Trigger

Many triggers support filtering to reduce noise:

```
// SharePoint trigger filter
ApprovalStatus eq 'Pending' and Priority eq 'High'

// Email trigger filter  
Subject contains '[ACTION REQUIRED]'
```

### Trigger Conditions

Use trigger conditions to add additional filtering logic without running the full flow:

```
// Only fire if the item was created by a specific user
@equals(triggerBody()?['Author']?['Email'], 'user@company.com')

// Only fire during business hours
@and(greaterOrEquals(int(formatDateTime(utcNow(), 'HH')), 8), lessOrEquals(int(formatDateTime(utcNow(), 'HH')), 17))
```

## Best Practices

- **Use trigger conditions** to prevent unnecessary flow runs — this saves action quota
- **Avoid overlapping scheduled flows** that modify the same data
- **Test triggers** using the "Test" feature in Power Automate before going to production
- **Monitor trigger history** for errors and missed triggers in the flow's run history
