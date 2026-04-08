---
applyTo: "docs/04-expressions.md,docs/11-expert-patterns.md"
---

# Expression Writing Rules

When writing or reviewing Power Automate expressions:

- Always use `?[]` for safe property access at every nesting level
- Use `coalesce()` for default values on optional fields
- Use `string()` or `int()` for explicit type conversion before comparisons
- Cache repeated expressions in a `Compose` action — reference with `outputs('Compose_Name')`
- SharePoint Choice columns require `?['Value']` suffix
- SharePoint People columns require Claims format: `concat('i:0#.f|membership|', email)`
- Test complex expressions with a `Compose` action before using in conditions
