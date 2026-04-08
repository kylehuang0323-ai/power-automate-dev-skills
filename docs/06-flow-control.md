## Flow Control

### Condition
```
: Status Value == "Available"
 ├── (If yes): ...
 └── (If no): ...
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
 └── Default:
```

> 💡 3+ Switch Condition
> Use Switch over nested Conditions when you have 3+ branches

### Apply to each
Iterate over each element in an array:
```
Apply to each: body('Get_items')?['value']
 └── : items('Apply_to_each')
```

**Concurrency setting**: (50)
Default is sequential; can set parallelism (max 50)

### Do until
Loop until condition is met:
```
Do until: variables('retryCount') >= 3
 ├── A
 └── retryCount
```

> ⚠️ 60
> Set loop limit (default 60, adjustable) to prevent infinite loops

### Scope
Group multiple steps together:
- Flow / Collapse for cleanliness
- Unified error handling
- Configurable "run after" conditions

### Terminate
 Flow / Immediately end Flow with a status:
- Succeeded
- Failed —
- Cancelled

### Delay
Pause for specified duration:
- (Delay): //// Fixed duration
- (Delay until): / Until specific datetime

### Parallel Branch
Create multiple parallel execution paths; all branches complete before the next step.

```
 │
 ├──┬── A: (2)
 │ │
 │ ├── B: (3)
 │ │
 │ └── C: (1)
 │
 ▼ (Continue after all complete)
 ≈ 3 ( 6)
 Total ≈ 3s (not 6s sequential)
```

**How to create:**
1. **+** → Add a parallel branch

> ⚠️ Compose
> Cannot use the same variable in parallel branches (race condition); use Compose instead

> 💡 **Parallel branches vs Apply to each**: Parallel branches = fixed number of different operations; Apply to each concurrency = same operation on multiple items() 
---
