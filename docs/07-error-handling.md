## Error Handling & Reliability

### Configure Run After

Configure when an action runs based on the outcome of a previous action:

| Condition | Description |
|---|---|
| ✅ (is successful) | Default, run after success |
| ❌ (has failed) | Run after failure |
| ⏩ (is skipped) | Run after skip |
| ⏱️ (has timed out) | Run after timeout |

### Scope + Run After = Try-Catch Pattern

```
Scope_Try (Main operations):
 ├── A
 ├── B
 └── C

Scope_Catch (Run after: "has failed" only):
 ├── : result('Scope_Try')
 └──
```

**Get error details from Scope:**
```
# Get all action results
result('Scope_Try')

# Filter failed actions
@body('Filter_array')
 From: result('Scope_Try')
 Where: @equals(item?['status'], 'Failed')
```

### Retry Policy
Configure in action settings:

| Policy | Description |
|---|---|
| Default | 4 retries, exponential backoff |
| None | No retry |
| Fixed interval | Fixed interval retry |
| Exponential interval | Exponential backoff retry |

### Error Handling in Asset Management Scenario

```
Scope_BorrowActions:
 ├── : Status → "In use"
 └── : Service Requests

Scope_Rollback ( BorrowActions ):
 └── : Status → "Available"
```

> This ensures the tool won't get stuck in "In use" if creating the request fails

---
