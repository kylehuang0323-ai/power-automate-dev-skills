## Flow Control

### Condition
```
Condition: Status Value == "Available"
  ├── If yes: ...
  └── If no: ...
```
Use expressions for complex logic:
```
@and(
  equals(triggerBody?['Status']?['Value'], 'Available'),
  greater(triggerBody?['Quantity'], 0)
)
```

### Switch

```
Switch: ApprovalStatus Value
  ├── Case "Approved": ...
  ├── Case "Rejected": ...
  ├── Case "Returned": ...
  └── Default: ...
```

> 💡 **Use Switch over nested Conditions** when you have 3+ branches

### Apply to each
Iterate over each element in an array:
```
Apply to each: body('Get_items')?['value']
  └── Current item: items('Apply_to_each')
```

**Concurrency setting**: Default is sequential; can set parallelism (max 50)

### Do until
Loop until condition is met:
```
Do until: variables('retryCount') >= 3
  ├── Perform action
  └── Increment retryCount
```

> ⚠️ **Loop limit**: Set a loop limit (default 60, adjustable) to prevent infinite loops

### Scope
Group multiple steps together:
- Collapse actions for visual cleanliness
- Unified error handling
- Configurable "run after" conditions

### Terminate
Immediately end Flow with a status:
- Succeeded
- Failed
- Cancelled

### Delay
Pause for a specified duration:
- **Delay**: Fixed time duration (hours/minutes/seconds)
- **Delay until**: Wait until a specific datetime

### Parallel Branch
Create multiple parallel execution paths; all branches complete before the next step.

```
  │
  ├──┬── Branch A: (2s)
  │  │
  │  ├── Branch B: (3s)
  │  │
  │  └── Branch C: (1s)
  │
  ▼ (Continue after all complete)
  Total ≈ 3s (not 6s sequential)
```

**How to create:**
1. **+** → Add a parallel branch

> ⚠️ Cannot use the same variable in parallel branches (race condition); use Compose instead

> 💡 **Parallel branches vs Apply to each**: Parallel branches = fixed number of different operations; Apply to each concurrency = same operation on multiple items

---
