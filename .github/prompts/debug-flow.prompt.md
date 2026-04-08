---
description: Diagnose and fix Power Automate flow failures or unexpected behavior
---

# Debug a Power Automate Flow

I need help debugging a Power Automate flow issue:

{{issue_description}}

## Diagnostic steps to follow

1. **Identify the failure point** — Which action failed? What is the error code and message?
2. **Check the input/output** — Examine the failing action's inputs and outputs in run history
3. **Common root causes**:
   - Null reference: missing `?[]` safe access in expressions
   - Type mismatch: comparing string to number without `string()` or `int()` conversion
   - Stale trigger data: using `triggerBody()` when item was modified by a parallel run
   - DLP block: connector group conflict preventing flow from running
   - Permission: connection account lacks access to the resource
   - Throttling (429): too many API calls, needs retry policy or delay
4. **Expression validation** — Test suspect expressions with `Compose` to isolate the issue
5. **Fix and verify** — Provide corrected expression or action configuration

## Quick checks

```
# Is value null?
coalesce(triggerBody()?['Field'], 'FIELD_IS_NULL')

# What type is it?
string(triggerBody()?['Field'])

# Is the field a Choice column (needs ?['Value'])?
triggerBody()?['Status']?['Value']

# People column needs Claims format?
concat('i:0#.f|membership|', body('Get_user')?['Mail'])
```

Reference `docs/09-debugging.md` and `docs/13-troubleshooting.md` for detailed guidance.
