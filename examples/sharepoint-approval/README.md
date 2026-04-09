# SharePoint Approval Flow

## Scenario

A user selects an item in a SharePoint list → the flow locks the item (sets status to "In use") → creates a request record → if anything fails, automatically rolls back the status.

## Architecture

```
Trigger: For a selected item (SharePoint List)
         ⚙️ Concurrency: 1 (prevent race conditions)
  │
  ├── Get item (read current status)
  │
  └── Condition: Status == "Available"?
        │
        ├── Yes:
        │   ├── Scope_Try:
        │   │   ├── Update item → Status = "In use"
        │   │   └── Create item → Request record (Pending)
        │   │
        │   └── Scope_Rollback (runs only if Scope_Try fails):
        │       └── Update item → Status = "Available"
        │
        └── No:
            └── Terminate (Cancelled: "Item not available")
```

## Patterns Demonstrated

- **Concurrency Control** — Trigger parallelism set to 1 to prevent two users from borrowing the same item
- **Scope-based Error Handling** — `Scope_Try` wraps business logic, `Scope_Rollback` with `runAfter: Failed` provides compensation
- **Guard Condition** — Checks availability before modifying, prevents invalid state transitions

## Files

| File | Description |
|------|-------------|
| `flow-definition.json` | Logic Apps workflow definition (paste into Code View) |

## Customization

| Parameter | Location | What to Change |
|-----------|----------|----------------|
| Site URL | All SharePoint actions → `dataset` | Your SharePoint site URL |
| Source List | Trigger + Get/Update actions → `table` | Your inventory list name |
| Request List | Create item action → `table` | Your requests list name |
| Status Values | Condition + Update actions | Match your Choice column values |
