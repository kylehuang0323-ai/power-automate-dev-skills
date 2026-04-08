## Trigger Types

### SharePoint Triggers

| Trigger | | Description |
|---|---|---|
| When an item is created | `When_an_item_is_created` | Fires when a new item is added |
| When an item is modified | `When_an_existing_item_is_modified` | Fires when an item is modified |
| For a selected item | `manual` (selected item) | User selects an item and triggers manually |
| When an item is created or modified | `When_an_item_is_created_or_modified` | Fires on both create and modify |

### Trigger Conditions

Add condition expressions in trigger settings — **Flow only runs when condition is true**.

```
# Single condition
@equals(triggerBody?['Status']?['Value'], 'Available')

# Multiple conditions (AND logic)
@equals(triggerBody?['ApprovalStatus']?['Value'], 'Returned')
@equals(triggerBody?['ActualReturnDate'], null)

# Not empty check
@not(empty(triggerBody?['Title']))

# Contains keyword
@contains(triggerBody?['Title'], 'Urgent')
```

> ⚠️ **AND** true
> Multiple trigger conditions are **AND** — all must be true to fire

### Concurrency Control

Configure in trigger **Settings → Concurrency Control**:

- **Parallelism = 1**: Only one instance at a time (prevents race conditions)
- **Parallelism = N**: Allow N instances concurrently

> Asset management scenario **must be 1** to prevent double-lending

---
