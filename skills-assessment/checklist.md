# Power Automate Skills Assessment Checklist

Use this checklist to assess your Power Automate development skills. Mark each item as you achieve proficiency.

---

## 🟢 Beginner Level

### Flow Basics
- [ ] Create a flow from a template in Power Automate
- [ ] Create a flow from scratch with a trigger and at least two actions
- [ ] Save, test, and view the run history of a flow
- [ ] Enable and disable a flow
- [ ] Turn on/off a flow and understand its impact
- [ ] Share a flow with another user as a co-owner or run-only user
- [ ] Copy a flow

### Triggers
- [ ] Create a flow with an automated trigger (e.g., SharePoint item created)
- [ ] Create a flow with a scheduled/recurrence trigger
- [ ] Create a flow with a manual trigger (button / Power Apps trigger)
- [ ] Use trigger conditions to filter when a flow runs

### Actions
- [ ] Send an email using the Office 365 Outlook connector
- [ ] Post a message to a Microsoft Teams channel
- [ ] Create, update, and get items from a SharePoint list
- [ ] Use dynamic content to reference trigger and action outputs in inputs

### Conditions
- [ ] Use the **Condition** action (if/else)
- [ ] Create a nested condition (condition within a condition)
- [ ] Use **Switch** for multi-case conditions

### Debugging
- [ ] View a flow run's history
- [ ] Inspect inputs and outputs of individual actions in a run
- [ ] Re-run a failed flow from the run history
- [ ] Use the **Test** function to test a flow manually

---

## 🟡 Intermediate Level

### Data & Variables
- [ ] Initialize variables of all types (String, Integer, Boolean, Array, Object, Float)
- [ ] Set and update a variable inside a flow
- [ ] Use `Append to array variable` to build a list during a loop
- [ ] Use `Increment variable` for counters

### Loops & Arrays
- [ ] Use **Apply to each** to loop over an array of items
- [ ] Enable concurrency on `Apply to each` for parallel processing
- [ ] Use **Filter array** to subset an array based on a condition
- [ ] Use **Select** to transform/reshape an array
- [ ] Use **Do until** for loops with a dynamic exit condition
- [ ] Break a loop using `Configure run after` or a boolean flag

### Expressions
- [ ] Write a string expression using `concat()`, `toUpper()`, `substring()`
- [ ] Write a date expression using `utcNow()`, `formatDateTime()`, `addDays()`
- [ ] Write a conditional expression using `if()` and `equals()`
- [ ] Write an array expression using `length()`, `first()`, `join()`
- [ ] Use null-safe access (`?['FieldName']`) to prevent expression errors
- [ ] Use `Compose` actions to build and test complex expressions

### Approvals
- [ ] Create an approval flow using the **Approvals** connector
- [ ] Handle approval responses (Approved / Rejected) with conditions
- [ ] Send approval notifications via email or Teams
- [ ] Implement a multi-stage approval (sequential approvers)
- [ ] Implement parallel approvals (multiple approvers, any/all must respond)

### HTTP & APIs
- [ ] Use the **HTTP** action to make a GET or POST request to a REST API
- [ ] Set request headers and authentication on an HTTP action
- [ ] Use **Parse JSON** to extract fields from an API response
- [ ] Use the **HTTP Request trigger** to expose a flow as a webhook endpoint
- [ ] Return a response from a triggered flow using the **Response** action

### Error Handling
- [ ] Configure **Run After** settings to handle failed actions
- [ ] Use a **Scope** action to group related steps
- [ ] Create an error handler scope that runs when the main scope fails
- [ ] Access error information from a failed scope using expressions
- [ ] Configure **Retry Policy** on an HTTP or connector action

---

## 🔴 Advanced Level

### Custom Connectors
- [ ] Create a custom connector from scratch (or from an OpenAPI file)
- [ ] Configure OAuth 2.0 or API key authentication for a custom connector
- [ ] Define GET and POST operations with parameters and response schemas
- [ ] Add `x-ms-summary` and `x-ms-visibility` extensions for better UI
- [ ] Test a custom connector operation in the connector wizard
- [ ] Use a custom connector in a flow

### Child Flows
- [ ] Create a child flow that can be called from a parent flow
- [ ] Pass input parameters from a parent to a child flow
- [ ] Return output from a child flow to the parent flow
- [ ] Use child flows to modularize and reuse common logic

### Performance Optimization
- [ ] Use `Filter Query` on SharePoint/Dataverse to reduce retrieved items
- [ ] Use `Select` and `Filter array` instead of filtering inside a loop
- [ ] Enable `Apply to each` concurrency for parallel processing
- [ ] Use parallel branches to run independent actions simultaneously
- [ ] Use `Compose` to pre-build objects and avoid recalculation in loops

### ALM (Application Lifecycle Management)
- [ ] Create flows inside a **Solution** (not My Flows)
- [ ] Use **Connection References** instead of direct connections
- [ ] Use **Environment Variables** for environment-specific configuration
- [ ] Export a solution (managed and unmanaged)
- [ ] Import a solution into another environment
- [ ] Use **Power Platform CLI** to script solution export/import
- [ ] Set up a basic CI/CD pipeline for automated deployments (GitHub Actions, Azure DevOps)

### Security & Governance
- [ ] Understand and configure **DLP (Data Loss Prevention)** policies
- [ ] Use **Azure Key Vault** connector to retrieve secrets
- [ ] Use service accounts instead of personal accounts for production connections
- [ ] Restrict HTTP trigger access by IP or SAS token
- [ ] Set appropriate flow permissions (owner vs. run-only)
- [ ] Monitor flows using **Power Platform Admin Center**

### Azure Integration
- [ ] Use **Azure Service Bus** for reliable asynchronous messaging
- [ ] Call an **Azure Function** from a flow via HTTP
- [ ] Use **Azure Blob Storage** for file handling
- [ ] Integrate with **Azure Monitor** or **Application Insights** for observability
- [ ] Use **Azure AD** (via Graph API) to manage users and groups

### Power Platform Integration
- [ ] Call a flow from a **Power Apps** canvas app
- [ ] Use **Dataverse** as a data store for flows
- [ ] Trigger a flow from a **Power BI** alert
- [ ] Use **AI Builder** models within a flow (e.g., form processing, sentiment analysis)

---

## Skills Score

Count your checked items:

| Range | Level |
|-------|-------|
| 0 – 15 | 🟢 Beginner – Keep building! |
| 16 – 35 | 🟡 Intermediate – Good progress! |
| 36 – 55 | 🔴 Advanced – Power user! |
| 56+ | ⭐ Expert – Consider sharing your knowledge! |

---

## Learning Resources

| Resource | URL |
|----------|-----|
| Official Documentation | https://docs.microsoft.com/en-us/power-automate/ |
| Learning Paths (Microsoft Learn) | https://docs.microsoft.com/en-us/learn/browse/?products=power-automate |
| Power Automate Community | https://powerusers.microsoft.com/t5/Microsoft-Power-Automate/ct-p/MPACommunity |
| YouTube: Power Automate channel | https://www.youtube.com/c/PowerAutomate |
| Certification: PL-900 (Fundamentals) | https://docs.microsoft.com/en-us/learn/certifications/power-platform-fundamentals/ |
| Certification: PL-500 (RPA Developer) | https://docs.microsoft.com/en-us/learn/certifications/power-automate-rpa-developer-associate/ |
