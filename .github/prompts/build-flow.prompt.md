---
description: Design and build a Power Automate cloud flow from a scenario description
---

# Build a Power Automate Flow

Help me build a Power Automate cloud flow for the following scenario:

{{scenario}}

## Requirements

Please provide a complete flow design including:

1. **Trigger selection** — Which trigger type and configuration (include trigger conditions if applicable)
2. **Step-by-step action design** — Each action with proper naming convention (`Verb_Target_Detail`)
3. **Error handling** — Scope Try-Catch pattern with rollback if needed
4. **Expressions** — Any expressions needed for data transformation, date formatting, or conditional logic
5. **DLP considerations** — Verify all connectors belong to the same DLP group
6. **Performance notes** — Concurrency settings, pagination for large lists, caching

## Constraints

- Follow naming convention: `ProjectName_FlowDescription` for the flow name
- Use environment variables for any URLs, list names, or email addresses
- Use `Compose` instead of variables inside conditions/loops/scopes
- Set concurrency to 1 if the flow does read-then-write on shared data
- Include trigger conditions to prevent unnecessary runs

Reference the docs/ directory for expression syntax and pattern details.
