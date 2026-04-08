# Error Handling in Power Automate

Robust error handling is essential for production flows. This guide covers the tools and patterns available in Power Automate.

## Understanding Flow Run States

Each action in a flow can have one of four states:

| State | Description |
|-------|-------------|
| **Succeeded** | The action completed successfully |
| **Failed** | The action encountered an error |
| **Skipped** | The action was not run (dependency failed) |
| **TimedOut** | The action exceeded its timeout limit |

## Run After Settings

**Run After** controls when an action runs based on the state of the previous action.

### Default Behavior

By default, every action only runs if the previous action **Succeeded**. This means a single failure causes all subsequent actions to be skipped.

### Configuring Run After

Click the `...` menu on any action → **Configure run after** → Check the desired states.

```
Common Run After patterns:

✅ Only on success (default)   → is successful
✅ Error handler pattern       → has failed + has timed out + is skipped  
✅ Cleanup / always run        → is successful + has failed + has timed out + is skipped
```

## Scope Actions for Error Isolation

The **Scope** action groups related actions together and gives you a single status to check.

### Basic Error Handling Pattern

```
┌─────────────────────────────────┐
│ Scope: Main Processing           │  ← Contains all business logic
│   - Action 1                     │
│   - Action 2                     │
│   - Action 3                     │
└─────────────────────────────────┘
         ↓ Run After: Failed / TimedOut / Skipped
┌─────────────────────────────────┐
│ Scope: Error Handler             │  ← Catches failures from Main Processing
│   - Log error to SharePoint      │
│   - Send alert email             │
│   - Post to Teams                │
└─────────────────────────────────┘
```

### Accessing Error Information

Inside an error handler, access the failed scope's error using:

```
// Get error message
actions('Scope_Main_Processing')?['error']?['message']

// Get error code
actions('Scope_Main_Processing')?['error']?['code']

// Get the full error object as a string
string(actions('Scope_Main_Processing')?['error'])

// Check which specific action failed
actions('Specific_Action_Name')?['status']
```

## Retry Policies

Configure retry policies on HTTP and connector actions to handle transient failures.

### Retry Types

| Type | Description | Best For |
|------|-------------|---------|
| **None** | No retries, fail immediately | Non-retriable errors |
| **Fixed interval** | Retry N times, same delay each time | Simple retry needs |
| **Exponential** | Retry N times, delay doubles each time | HTTP API calls |

### Configuring Retries

Click the `...` menu on an action → **Settings** → **Networking** → **Retry Policy**

```json
// Exponential retry: 4 retries, starting at 7s, max 1 hour
{
  "type": "exponential",
  "count": 4,
  "interval": "PT7S",
  "minimumInterval": "PT5S",
  "maximumInterval": "PT1H"
}
```

## Terminate Action

Use the **Terminate** action to explicitly end a flow with a specific status.

```
Terminate with:
- Status: Succeeded / Failed / Cancelled
- Code: Custom error code (e.g., "VALIDATION_ERROR")
- Message: Human-readable error description
```

**Example:** Validate input at the start of a flow and terminate with a clear error if invalid:

```
Condition: Is 'email' field present?
├── Yes: Continue with flow
└── No: Terminate (Failed, "MISSING_FIELD", "Required field 'email' was not provided")
```

## Error Logging Pattern

Log errors to a persistent store for auditing and debugging.

### SharePoint Error Log List

Recommended columns:
- **Title** – Auto-generated (date + flow name)
- **FlowName** – Name of the flow
- **ErrorMessage** – Error description
- **ErrorCode** – Error code
- **InputPayload** – The data that caused the error (as JSON string)
- **Severity** – Low / Medium / High / Critical
- **Status** – Open / Investigating / Resolved

### Logging an Error

```
Create item in SharePoint (Error Log list):
├── Title:         "Flow Error - @{formatDateTime(utcNow(), 'yyyy-MM-dd HH:mm')}"
├── FlowName:      "HR - New Employee Onboarding"
├── ErrorMessage:  "@{actions('Scope_Main_Processing')?['error']?['message']}"
├── ErrorCode:     "@{actions('Scope_Main_Processing')?['error']?['code']}"
├── InputPayload:  "@{string(triggerBody())}"
└── Severity:      "High"
```

## Alert Notifications

Always notify someone when a critical flow fails.

### Teams Alert

```
Post message in Teams channel:
├── Team:    Operations Team
├── Channel: Flow Alerts
└── Message: 
    🚨 Flow Failure Alert

    Flow: HR - New Employee Onboarding
    Time: @{formatDateTime(utcNow(), 'f')}
    Error: @{actions('Scope_Main_Processing')?['error']?['message']}

    Please investigate: [Run History Link]
```

### Email Alert

```
Send an email:
├── To:      ops-team@company.com
├── Subject: ALERT: Flow Failure - HR New Employee Onboarding
└── Body:    The flow has failed. Error: [details]
```

## Common Error Patterns and Solutions

| Error | Likely Cause | Solution |
|-------|-------------|---------|
| `404 Not Found` | Resource deleted or moved | Validate resource existence before acting |
| `401 Unauthorized` | Connection expired or invalid | Reconnect / refresh token |
| `429 Too Many Requests` | API throttling | Add retry policy, reduce concurrency |
| `408 Request Timeout` | Slow API or network issue | Increase timeout, add retry with backoff |
| `InvalidTemplate` | Bad expression syntax | Check expression in the editor |
| Array is null/empty | Empty result from query | Add condition to check before looping |

## Testing Error Handling

1. **Use invalid input** to deliberately trigger failures
2. **Break a connection** temporarily to test connection errors
3. **Review run history** in Power Automate to see action states
4. **Use the "Resubmit" option** in run history to replay failed runs after fixing the issue

## Checklist: Error Handling Review

- [ ] Critical logic is wrapped in a **Scope** action
- [ ] An **Error Handler scope** with correct Run After settings exists
- [ ] Errors are **logged** to a persistent store
- [ ] An **alert notification** is sent on failure
- [ ] **Retry policies** are set on HTTP/API actions
- [ ] Input validation with **Terminate** for invalid inputs
- [ ] Flow has been **tested** with both valid and invalid inputs
