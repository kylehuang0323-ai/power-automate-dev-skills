<div align="center">

# ⚡ Power Automate Developer Skills

**The most comprehensive GitHub Copilot skill for Power Automate development**

Give your AI assistant expert-level Power Automate knowledge —
from trigger conditions to enterprise Saga patterns.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Lint](https://github.com/kylehuang0323-ai/power-automate-dev-skills/actions/workflows/lint.yml/badge.svg)](https://github.com/kylehuang0323-ai/power-automate-dev-skills/actions/workflows/lint.yml)
[![Skill: Power Automate](https://img.shields.io/badge/Copilot_Skill-Power_Automate-0078D4)](https://github.com/kylehuang0323-ai/power-automate-dev-skills)
[![Docs: 15 modules](https://img.shields.io/badge/Docs-15_modules-green)](#knowledge-coverage)
[![Patterns: 8 designs](https://img.shields.io/badge/Patterns-8_designs-orange)](#knowledge-coverage)

🌐 [English](README.md) | [中文](README.zh-CN.md)

[Quick Start](#quick-start) · [Why This Skill?](#why-this-skill) · [Knowledge Base](#knowledge-coverage) · [Examples](#examples) · [Contributing](CONTRIBUTING.md)

</div>

---

## Why This Skill?

Building Power Automate flows with Copilot? You'll hit these walls:

| Problem | Without This Skill | With This Skill |
|---------|-------------------|-----------------|
| Trigger syntax | ❌ Generic UI advice | ✅ Generates `@equals(triggerBody()?['Status']?['Value'],'Approved')` |
| Infinite loops | ❌ No awareness of self-triggering | ✅ Adds guard conditions + flag columns automatically |
| DLP compliance | ❌ Suggests blocked HTTP connectors | ✅ Uses only Business-group connectors, offers alternatives |
| Error handling | ❌ No Scope/Try-Catch patterns | ✅ Scope_Try → Scope_Catch with Saga rollback |
| Flow JSON | ❌ Can't generate importable definitions | ✅ Full Logic Apps JSON with connection references |
| SharePoint | ❌ Wrong column names (display vs internal) | ✅ REST API discovery + correct `InternalName` usage |

## What is this?

This repository is a **reusable GitHub Copilot Skill** that gives AI assistants expert-level Power Automate knowledge. When integrated into your project, Copilot can help you:

- ✅ Build cloud flows with proper architecture patterns
- ✅ Write and debug complex expressions
- ✅ Implement enterprise error handling (Try-Catch, Saga, retry)
- ✅ Check DLP (Data Loss Prevention) compliance
- ✅ Set up CI/CD pipelines with PAC CLI
- ✅ Optimize SharePoint queries and flow performance

## Quick Start

### Option 1: Copy the skill into your project

```bash
git clone https://github.com/kylehuang0323-ai/power-automate-dev-skills.git
cp -r power-automate-dev-skills/.github/ your-project/.github/
cp -r power-automate-dev-skills/docs/ your-project/docs/
```

### Option 2: Add as a Git submodule

```bash
cd your-project
git submodule add https://github.com/kylehuang0323-ai/power-automate-dev-skills.git skills/power-automate
```

### Option 3: Reference directly in Copilot Chat

In VS Code with GitHub Copilot, use the prompt templates:

1. Open Command Palette → `Chat: Use Prompt from File`
2. Select from `.github/prompts/` (e.g., `build-flow.prompt.md`)

## Repository Structure

```
.github/
├── workflows/
│   └── lint.yml                         # CI: Markdown linting + link check
├── ISSUE_TEMPLATE/                      # Bug report & feature request forms
├── PULL_REQUEST_TEMPLATE.md             # PR checklist
├── copilot-instructions.md              # Core AI instructions (<4KB)
├── instructions/
│   ├── expressions.instructions.md      # Expression-specific rules
│   └── sharepoint.instructions.md       # SharePoint & DLP rules
├── prompts/
│   ├── build-flow.prompt.md             # "Help me build a flow"
│   ├── debug-flow.prompt.md             # "Help me debug a flow"
│   ├── review-expression.prompt.md      # "Review this expression"
│   └── dlp-check.prompt.md             # "Check DLP compliance"
└── skills/
    └── power-automate/
        └── SKILL.md                     # Skill definition & metadata

docs/                                     # Modular knowledge base (15 modules)
├── 01-fundamentals.md                   # Flow types, core concepts
├── 02-triggers.md                       # Trigger types & conditions
├── 03-connectors.md                     # Common connectors reference
├── 04-expressions.md                    # 50+ expression functions cheat sheet
├── 05-variables.md                      # Variables & data operations
├── 06-flow-control.md                   # Conditions, loops, scopes
├── 07-error-handling.md                 # Try-Catch, retry, Saga patterns
├── 08-performance.md                    # Limits, quotas, optimization
├── 09-debugging.md                      # Debugging techniques
├── 10-best-practices.md                 # Naming, architecture, security
├── 11-expert-patterns.md                # Child flows, CI/CD, 8 design patterns
├── 12-dlp-policies.md                   # DLP policies & compliance
├── 13-troubleshooting.md               # FAQ & common errors
├── 14-ecosystem.md                      # AI Builder, Teams, Power Apps, RPA
└── appendix-cookbook.md                  # Ready-to-use recipes

examples/                                 # Importable flow definitions
├── sharepoint-approval/                 # Lock → approve → rollback pattern
│   ├── README.md
│   └── flow-definition.json
├── error-handling-saga/                 # Try-Catch-Finally + Saga compensation
│   ├── README.md
│   └── flow-definition.json
└── teams-adaptive-card/                 # Teams card approval
    ├── README.md
    ├── flow-definition.json
    └── adaptive-card-template.json
```

## Prompt Templates

| Prompt | Description | Use When |
|--------|-------------|----------|
| `build-flow` | Design a complete flow from a scenario | Starting a new automation |
| `debug-flow` | Diagnose and fix flow failures | Flow is failing or behaving unexpectedly |
| `review-expression` | Validate and optimize expressions | Expression returns wrong result or errors |
| `dlp-check` | Check DLP compliance for a flow design | Before deploying to enterprise environment |

## Knowledge Coverage

| Topic | Key Content |
|-------|-------------|
| **Fundamentals** | 5 flow types, triggers, actions, connections, expressions |
| **Expressions** | 50+ functions (string, date, logic, collection, type conversion) |
| **Error Handling** | Try-Catch-Finally, Saga compensation, retry with exponential backoff |
| **DLP Policies** | 3 connector groups, policy stacking, HTTP alternatives |
| **Expert Patterns** | Child flows, Solution lifecycle, CI/CD (PAC CLI + Azure DevOps), 8 design patterns |
| **Design Patterns** | Saga, Circuit Breaker, Fan-out/Fan-in, State Machine, Queue, Observer, Idempotent Consumer |
| **Ecosystem** | AI Builder + GPT, Teams Adaptive Cards, Power Apps integration, RPA Desktop Flows, Dataverse |

## How the Skill Works

When you add this skill to your project:

1. **`.github/copilot-instructions.md`** is automatically loaded by GitHub Copilot as project-level context
2. **`.github/instructions/*.instructions.md`** provide path-specific rules when editing relevant files
3. **`.github/prompts/*.prompt.md`** offer task-specific templates you can invoke from VS Code
4. **`.github/skills/power-automate/SKILL.md`** defines the skill metadata for agent-based tools
5. **`docs/*.md`** serve as the detailed knowledge base that Copilot can reference via `@workspace`

## Examples

Importable flow definitions in the [`examples/`](examples/) directory:

| Example | Patterns | Files |
|---------|----------|-------|
| [SharePoint Approval](examples/sharepoint-approval/) | Concurrency control, Scope error handling, Saga rollback | Flow JSON |
| [Error Handling Saga](examples/error-handling-saga/) | Try-Catch-Finally, Saga compensation, audit logging | Flow JSON |
| [Teams Adaptive Card](examples/teams-adaptive-card/) | Adaptive Cards, wait for response, conditional update | Flow JSON + Card template |

Each example includes a `README.md` with architecture diagram, customization guide, and import instructions.

Want to contribute an example? See [CONTRIBUTING.md](CONTRIBUTING.md).

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Ways to contribute:**

- 📖 Fix or improve documentation
- ✨ Add new design patterns or cookbook recipes
- 🔌 Add connector references
- 📦 Submit importable flow JSON examples
- 🌐 Help with translations

## License

[MIT](LICENSE)

---

<div align="center">

Made with ⚡ by [@kylehuang0323-ai](https://github.com/kylehuang0323-ai)

If this skill helps you, consider giving it a ⭐

</div>
