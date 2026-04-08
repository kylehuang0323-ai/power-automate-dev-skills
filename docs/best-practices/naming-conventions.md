# Power Automate Naming Conventions

Consistent naming makes flows easier to understand, maintain, and troubleshoot. Follow these conventions for professional Power Automate development.

## Flow Names

**Pattern:** `[Team/Project] - [Description] - [Environment]`

```
Good:
✅ HR - New Employee Onboarding - Production
✅ IT - Helpdesk Ticket Escalation - Dev
✅ Finance - Monthly Budget Report - Production

Avoid:
❌ My Flow
❌ Test Flow 1
❌ Copy of Copy of Approval
```

## Action Names

Always rename actions from their defaults to descriptive names. Use present-tense verbs.

**Pattern:** `[Verb] [Object] - [Context/Purpose]`

```
Good:
✅ Get SharePoint items - Pending approvals
✅ Send email - Notify requester of approval decision
✅ Update SharePoint item - Set status to Approved
✅ Parse JSON - Extract order details from API response
✅ Condition - Is priority High or Critical?
✅ Initialize variable - Request counter

Avoid:
❌ Get items
❌ Send an email
❌ Update item 2
❌ Condition
❌ Initialize variable
```

## Variable Names

Use camelCase for variable names. Prefix with type for clarity.

**Pattern:** `[type prefix][DescriptiveName]`

```
// String variables
varRequestId
varCustomerName
varStatusMessage

// Integer variables
intCounter
intSuccessCount
intPageNumber

// Boolean variables
blnIsApproved
blnHasErrors
blnProcessComplete

// Array variables
arrPendingItems
arrErrorLog
arrApprovers

// Object variables  
objRequestPayload
objApiResponse
```

## Scope Names

Scopes group related actions. Name them to describe the logical phase.

```
✅ Scope - Initialize and validate inputs
✅ Scope - Main processing
✅ Scope - Error handler
✅ Scope - Send notifications
✅ Scope - Cleanup and finalize

❌ Scope
❌ Scope 1
❌ Do stuff
```

## Condition Names

Name conditions as questions with clear yes/no answers.

```
✅ Condition - Is the request status Pending?
✅ Condition - Does the approver email exist?
✅ Condition - Were any errors logged?
✅ Condition - Is the item count greater than zero?

❌ Condition
❌ Check
❌ If true
```

## Loop Names (Apply to each)

Describe what is being iterated.

```
✅ Apply to each - SharePoint list item
✅ Apply to each - Pending approval request
✅ Apply to each - Customer email address

❌ Apply to each
❌ For each
```

## Connection Names

Use a consistent pattern to identify the environment and account.

**Pattern:** `[Service] - [Environment] - [Account Type]`

```
✅ SharePoint - Production - Service Account
✅ Office 365 - Dev - svc-automate@company.com
✅ SQL Server - Production - Read-Only Service Account

❌ SharePoint Connection
❌ My Connection
```

## Environment Variable Names

**Pattern:** `[Scope]_[Category]_[Name]`

```
✅ App_SharePoint_SiteURL
✅ App_Email_SupportAddress
✅ Env_Database_ConnectionString
✅ Env_API_BaseURL

❌ siteurl
❌ My Email
❌ URL
```

## Solution Names

**Pattern:** `[Organization/Team] [Product/Project] [optional version]`

```
✅ Contoso HR Automation v2
✅ IT ServiceDesk Flows
✅ Finance Reporting Suite

❌ My Solution
❌ Flows
❌ Test
```

## Tips

1. **Rename immediately** – When you add an action, rename it before moving on
2. **Be verbose** – A slightly longer but clear name is always better than a short cryptic one
3. **Use consistent verbs** – Pick a verb style and stick to it (Get, Send, Update, Create, etc.)
4. **Add context** – Include what the action operates on and why (e.g., "for approval notification")
5. **Avoid abbreviations** – Write out words in full (e.g., "SharePoint" not "SP", "Notification" not "Notif")
