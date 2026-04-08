# Power Automate Dev Skills

A comprehensive reference repository for Power Automate development skills, covering beginner through advanced topics with real-world flow templates and best practices.

## Table of Contents

- [Overview](#overview)
- [Skill Levels](#skill-levels)
- [Directory Structure](#directory-structure)
- [Getting Started](#getting-started)
- [Flow Templates](#flow-templates)
- [Key Concepts](#key-concepts)
- [Best Practices](#best-practices)
- [Skills Assessment Checklist](#skills-assessment-checklist)
- [Resources](#resources)

## Overview

Microsoft Power Automate (formerly Microsoft Flow) is a cloud-based service that allows you to create automated workflows between applications and services. This repository provides structured learning materials, reusable flow templates, and best practices for Power Automate developers at all skill levels.

## Skill Levels

| Level | Description |
|-------|-------------|
| 🟢 Beginner | Creating simple flows, using triggers and basic actions |
| 🟡 Intermediate | Conditions, loops, expressions, error handling |
| 🔴 Advanced | Custom connectors, complex expressions, ALM, governance |

## Directory Structure

```
power-automate-dev-skills/
├── docs/
│   ├── concepts/          # Core Power Automate concepts
│   ├── best-practices/    # Development best practices
│   └── connectors/        # Connector reference and examples
├── flows/
│   ├── beginner/          # Simple flow templates
│   ├── intermediate/      # Mid-level flow templates
│   └── advanced/          # Advanced flow templates
└── skills-assessment/     # Skill assessment checklists
```

## Getting Started

### Prerequisites

- A Microsoft 365 or Power Apps license
- Access to [Power Automate](https://make.powerautomate.com)
- Basic understanding of APIs and JSON (helpful for intermediate/advanced)

### Importing a Flow Template

1. Navigate to [Power Automate](https://make.powerautomate.com)
2. Go to **My flows** → **Import**
3. Select the `.zip` package from this repository
4. Follow the on-screen prompts to map connections

## Flow Templates

### Beginner

| Template | Description | File |
|----------|-------------|------|
| Send Email on SharePoint Item Creation | Sends an email when a new item is added to a SharePoint list | [flows/beginner/sharepoint-email-notification.json](flows/beginner/sharepoint-email-notification.json) |
| Daily Weather Report | Sends a daily email with weather data via MSN Weather connector | [flows/beginner/daily-weather-report.json](flows/beginner/daily-weather-report.json) |
| Teams Message on Form Submission | Posts a Teams message when a Microsoft Form is submitted | [flows/beginner/forms-to-teams.json](flows/beginner/forms-to-teams.json) |

### Intermediate

| Template | Description | File |
|----------|-------------|------|
| Approval Workflow | Routes an item through a multi-stage approval process | [flows/intermediate/approval-workflow.json](flows/intermediate/approval-workflow.json) |
| HTTP Request Handler | Exposes an HTTP endpoint and processes JSON payloads | [flows/intermediate/http-request-handler.json](flows/intermediate/http-request-handler.json) |
| Scheduled Data Sync | Runs on a schedule to sync data between two systems | [flows/intermediate/scheduled-data-sync.json](flows/intermediate/scheduled-data-sync.json) |

### Advanced

| Template | Description | File |
|----------|-------------|------|
| Custom Connector Flow | Uses a custom connector to call an external REST API | [flows/advanced/custom-connector-demo.json](flows/advanced/custom-connector-demo.json) |
| Error Handling & Retry Pattern | Demonstrates robust error handling with retries and logging | [flows/advanced/error-handling-retry.json](flows/advanced/error-handling-retry.json) |
| Parallel Branch Processing | Processes multiple branches concurrently for performance | [flows/advanced/parallel-branch-processing.json](flows/advanced/parallel-branch-processing.json) |

## Key Concepts

### Triggers

Triggers are what start a flow. Common trigger types:

- **Automated** – Fires in response to an event (e.g., new email, new SharePoint item)
- **Instant / Manual** – Started by a user via a button or another flow
- **Scheduled** – Runs on a recurring schedule (hourly, daily, etc.)
- **HTTP Request** – Triggered by an incoming HTTP POST (webhook pattern)

### Actions

Actions are the steps a flow performs after being triggered. They interact with connectors such as Office 365, SharePoint, HTTP, Azure services, and more.

### Connectors

Connectors are the bridges to external services. Power Automate supports 1,000+ connectors:

- **Standard Connectors** – Available to all licensed users (SharePoint, Teams, Outlook, etc.)
- **Premium Connectors** – Require a Premium license (HTTP, SQL Server, Salesforce, etc.)
- **Custom Connectors** – Built to connect to any REST/SOAP API

### Expressions

Power Automate uses a formula language for dynamic values:

```
// String operations
concat('Hello, ', triggerBody()?['Name'])
toUpper(items('Apply_to_each')?['Title'])

// Date/time
utcNow()
formatDateTime(utcNow(), 'yyyy-MM-dd')
addDays(utcNow(), 7)

// Conditional
if(equals(variables('Status'), 'Approved'), 'green', 'red')

// Array operations
length(body('Get_items')?['value'])
first(body('Get_items')?['value'])
```

### Variables

| Type | Description | Example |
|------|-------------|---------|
| String | Text value | `Initialize variable` → `varName` = `"Hello"` |
| Integer | Whole number | `Initialize variable` → `counter` = `0` |
| Boolean | True/False | `Initialize variable` → `isApproved` = `false` |
| Array | List of values | `Initialize variable` → `items` = `[]` |
| Object | Key-value pairs | `Initialize variable` → `config` = `{}` |
| Float | Decimal number | `Initialize variable` → `price` = `9.99` |

## Best Practices

See [`docs/best-practices/`](docs/best-practices/) for detailed guides. Key highlights:

### 1. Naming Conventions

```
# Flow names
[Team/Project] - [Description] - [Environment]
Example: "HR - New Employee Onboarding - Production"

# Action names (use descriptive names, not defaults)
Good:   "Get SharePoint list items - Pending Approvals"
Avoid:  "Get items"
```

### 2. Error Handling

- Always configure **Run After** settings on critical actions
- Use **Scope** actions to group related steps and catch errors
- Add a **Send Email** or **Post to Teams** action in error scopes to alert on failures
- Log errors to a SharePoint list or Azure Table Storage for auditing

### 3. Performance

- Use **Filter Query** and **Top Count** on `Get items` actions instead of filtering in a loop
- Avoid nested `Apply to each` loops where possible — use `Select` + `Filter array` instead
- Enable **Concurrency Control** on `Apply to each` loops (up to 50 parallel branches)
- Use **Compose** actions to pre-build complex objects rather than recalculating

### 4. Security

- Store secrets in **Azure Key Vault** or **Environment Variables** (not hardcoded)
- Use **Service Accounts** for connections in production flows
- Apply **DLP (Data Loss Prevention)** policies at the environment level
- Restrict HTTP trigger flows with **SAS tokens** or check `caller IP addresses`

### 5. ALM (Application Lifecycle Management)

- Package flows in **Solutions** for portability and version control
- Use **Environment Variables** for environment-specific configuration
- Automate deployments using **Power Platform CLI** or **GitHub Actions**
- Store solution exports in source control (this repository!)

## Skills Assessment Checklist

See [`skills-assessment/`](skills-assessment/) for the full checklist. Quick summary:

### 🟢 Beginner Skills
- [ ] Create an automated flow from a template
- [ ] Create a flow from scratch with a trigger and 2+ actions
- [ ] Use conditions (if/else) in a flow
- [ ] Send an email or Teams message from a flow
- [ ] Use dynamic content in action inputs
- [ ] Test and debug a flow using run history

### 🟡 Intermediate Skills
- [ ] Initialize and update variables
- [ ] Use `Apply to each` to loop over an array
- [ ] Use `Filter array` and `Select` to transform data
- [ ] Create and use an approval flow
- [ ] Call an HTTP endpoint from a flow
- [ ] Handle errors with Scope and Run After settings
- [ ] Use expressions for string, date, and array manipulation

### 🔴 Advanced Skills
- [ ] Build a custom connector for a REST API
- [ ] Use child flows to modularize logic
- [ ] Implement retry logic and dead-letter patterns
- [ ] Deploy flows via Power Platform CLI or CI/CD pipeline
- [ ] Set up DLP policies and environment governance
- [ ] Use parallel branches to optimize performance
- [ ] Integrate with Azure services (Key Vault, Service Bus, Functions)

## Resources

- [Power Automate Documentation](https://docs.microsoft.com/en-us/power-automate/)
- [Power Automate Community](https://powerusers.microsoft.com/t5/Microsoft-Power-Automate/ct-p/MPACommunity)
- [Power Platform CLI](https://docs.microsoft.com/en-us/power-platform/developer/cli/introduction)
- [Connector Reference](https://docs.microsoft.com/en-us/connectors/)
- [Expression Reference](https://docs.microsoft.com/en-us/azure/logic-apps/workflow-definition-language-functions-reference)
- [Power Automate Blog](https://flow.microsoft.com/en-us/blog/)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-flow-template`)
3. Add your flow template or documentation
4. Submit a pull request with a clear description

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
