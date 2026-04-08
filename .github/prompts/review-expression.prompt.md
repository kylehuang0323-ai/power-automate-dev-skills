---
description: Validate, fix, or optimize Power Automate expressions
---

# Review Power Automate Expression

Please review and improve this Power Automate expression:

```
{{expression}}
```

## Context

- **Where it's used**: {{action_or_context}}
- **Expected behavior**: {{expected_result}}
- **Actual behavior**: {{actual_result}}

## Review checklist

1. **Null safety** — Does every property access use `?[]` syntax?
2. **Type correctness** — Are comparisons between matching types? (string vs number, etc.)
3. **Edge cases** — What happens if a field is null, empty string, or missing?
4. **Readability** — Can the expression be simplified without losing functionality?
5. **Performance** — Is the same sub-expression repeated? Should it be cached in a `Compose`?

## Common fixes

```
# ❌ Unsafe
triggerBody()['Status']['Value']

# ✅ Safe
triggerBody()?['Status']?['Value']

# ❌ Type mismatch
equals(triggerBody()?['ID'], '42')

# ✅ Explicit conversion
equals(triggerBody()?['ID'], 42)
# or: equals(string(triggerBody()?['ID']), '42')

# ❌ No fallback
triggerBody()?['OptionalField']

# ✅ With fallback
coalesce(triggerBody()?['OptionalField'], 'default')
```

Reference `docs/04-expressions.md` for the complete function reference.
