# Error Handling Saga Pattern

## Scenario

A multi-step business process where each step must be compensated (rolled back) if a later step fails. This implements the **Saga pattern** — each forward action has a corresponding compensation action.

Example: Create order → Reserve inventory → Charge payment. If payment fails, reverse the inventory reservation and cancel the order.

## Architecture

```
Trigger: When an item is created (Orders list)
  │
  ├── Scope_Try:
  │   ├── Step 1: Create item in OrderDetails list
  │   ├── Step 2: Update Inventory (decrement stock)
  │   └── Step 3: Send approval request
  │
  ├── Scope_Catch (runAfter: Scope_Try → Failed):
  │   ├── Compensate Step 2: Restore inventory stock
  │   ├── Compensate Step 1: Delete OrderDetails record
  │   ├── Update Order status → "Failed"
  │   └── Send failure notification email
  │
  └── Scope_Finally (runAfter: Scope_Catch → Succeeded, Failed, Skipped):
      └── Log execution result to AuditLog list
```

## Patterns Demonstrated

- **Saga Compensation** — Each forward step has a compensating reverse action
- **Try-Catch-Finally** — Three Scopes with `runAfter` configuration
- **Error Extraction** — `result('Scope_Try')` captures which step failed
- **Audit Logging** — Finally scope always runs regardless of outcome

## Files

| File | Description |
|------|-------------|
| `flow-definition.json` | Logic Apps workflow definition with Saga pattern |

## Key Configuration

### runAfter Settings

```json
"Scope_Catch": {
  "runAfter": { "Scope_Try": ["Failed", "TimedOut"] }
}
"Scope_Finally": {
  "runAfter": { "Scope_Catch": ["Succeeded", "Failed", "Skipped"] }
}
```

### Error Detail Extraction

Use this expression inside Scope_Catch to identify which action failed:

```
result('Scope_Try')
```

This returns an array of action results. Filter for failed items:

```
first(filter(result('Scope_Try'), item => item['status'] == 'Failed'))
```

## Customization

| Parameter | What to Change |
|-----------|----------------|
| Site URL | Your SharePoint site URL in all actions |
| Orders List | Your source list that triggers the flow |
| OrderDetails List | Your detail/line-item list |
| Inventory List | Your stock/inventory list |
| AuditLog List | Your audit logging list |
| Notification Email | Recipient for failure alerts |
