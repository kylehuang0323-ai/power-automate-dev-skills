---
name: power-automate
description: >
  Expert-level Power Automate development skill covering flow design,
  expressions, error handling, DLP compliance, CI/CD pipelines, and
  enterprise architecture patterns.
---

# Power Automate Developer Skill

This skill provides comprehensive Power Automate cloud flow development expertise,
from fundamentals through enterprise-grade architecture patterns.

## When to use this skill

- Building or debugging Power Automate cloud flows
- Writing or reviewing expressions (string, date, logic, collection functions)
- Implementing error handling patterns (Try-Catch-Finally, Saga compensation, retry with backoff)
- Checking DLP (Data Loss Prevention) policy compliance for connector usage
- Setting up CI/CD pipelines with PAC CLI and Azure DevOps / GitHub Actions
- Optimizing SharePoint queries, loop performance, and API call efficiency
- Designing multi-flow architectures with child flows and Solution packaging
- Integrating with Teams (Adaptive Cards), Power Apps, AI Builder, or Dataverse

## Skill structure

The knowledge base is organized into focused modules under `docs/`:

| Module | File | Description |
|--------|------|-------------|
| Fundamentals | `docs/01-fundamentals.md` | Flow types, core concepts, run modes |
| Triggers | `docs/02-triggers.md` | SharePoint triggers, conditions, concurrency |
| Connectors | `docs/03-connectors.md` | SharePoint, Approvals, Outlook, HTTP actions |
| Expressions | `docs/04-expressions.md` | Complete function reference (string, date, logic, collection, type) |
| Variables | `docs/05-variables.md` | Variable types, data operations, Compose patterns |
| Flow Control | `docs/06-flow-control.md` | Conditions, Switch, loops, Scope, parallel branches |
| Error Handling | `docs/07-error-handling.md` | Try-Catch, retry policies, Saga compensation |
| Performance | `docs/08-performance.md` | Runtime limits, quotas, optimization strategies |
| Debugging | `docs/09-debugging.md` | Run history, Compose debugging, trigger diagnostics |
| Best Practices | `docs/10-best-practices.md` | Naming, architecture, security, maintenance |
| Expert Patterns | `docs/11-expert-patterns.md` | Child flows, Solutions, CI/CD, JSON, monitoring, design patterns |
| DLP Policies | `docs/12-dlp-policies.md` | Connector groups, policy stacking, compliance strategies |
| Troubleshooting | `docs/13-troubleshooting.md` | Common errors and solutions FAQ |
| Ecosystem | `docs/14-ecosystem.md` | AI Builder, Teams Adaptive Cards, Power Apps, RPA, Dataverse |
| Cookbook | `docs/appendix-cookbook.md` | Ready-to-use recipe patterns |

## Key patterns

- **Try-Catch-Finally**: `Scope_Try` → `Scope_Catch` (run after: failed) → `Scope_Finally` (run after: all)
- **Saga Compensation**: Each forward step has a compensating rollback action
- **Circuit Breaker**: Stop calling after N failures, probe periodically
- **State Machine**: SharePoint Choice column as state, trigger conditions as transitions
- **Queue Processing**: SharePoint list as message queue with LockedBy/Status fields
- **Sync-to-Async Bridge**: Azure Function wrapping async agent calls for synchronous HTTP

## Prompt templates

Pre-built prompt templates are available in `.github/prompts/`:

- `build-flow.prompt.md` — Design and build a new flow
- `debug-flow.prompt.md` — Diagnose and fix flow issues
- `review-expression.prompt.md` — Validate and optimize expressions
- `dlp-check.prompt.md` — Check DLP compliance for a flow design
