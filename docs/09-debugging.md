## Debugging Tips

### View Run History

1. Go to https://make.powerautomate.com
2. Navigate to **My flows**
3. Select a Flow → **Run history** tab
4. Click any run to see step-by-step I/O

### Common Debug Methods

| Method | Description |
|---|---|
| **Compose** | Use Compose to output variable values |
| | Outputs JSON / Expand each step to see I/O JSON |
| | Click trigger to see full triggerBody() |
| | Use **Test** → **Manually** to run in real-time |
| **Peek code** | View underlying JSON definition |

### Condition Debugging Tips
When conditions behave unexpectedly:

```
# Output actual value with Compose
Compose: triggerBody?['Status']?['Value']

# Compare expected value
Compose: equals(triggerBody?['Status']?['Value'], 'Available')

# Check type -
# Numbers and strings won't auto-convert
Compose: equals(string(triggerBody?['AssetId']), '42')
```

### Trigger Debugging

 Flow / If Flow is not triggering:

1. Remove all trigger conditions temporarily
2. SharePoint Verify SP connection is valid
3. Verify list read permissions
4. ** Value **: `Value` `value` / Try uppercase `Value` first
5. "Test → Manually" / Use manual test to isolate trigger issues

### Performance Debugging

| Issue | Investigation |
|---|---|
| Slow Flow | Check per-step timing in run history |
| Slow Apply to each | Enable concurrency or pre-filter |
| Slow SharePoint | Reduce fields, index columns |
| Throttled (429) | Check API quotas, add delays |

---
