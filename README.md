# ⚡ Power Automate Developer Skills Reference

> A comprehensive, expert-level Power Automate skills reference — from fundamentals to enterprise architecture patterns.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Table of Contents

1. [Fundamentals](#1---fundamentals)
2. [Trigger Types](#2---trigger-types)
3. [Common Connectors](#3---common-connectors)
4. [Expressions & Functions Reference](#4---expressions--functions-reference)
5. [Variables & Data Operations](#5---variables--data-operations)
6. [Flow Control](#6---flow-control)
7. [Error Handling & Reliability](#7---error-handling--reliability)
8. [Performance & Limits](#8---performance--limits)
9. [Debugging Tips](#9---debugging-tips)
10. [Best Practices](#10---best-practices)
11. [Expert-Level Development](#11---expert-level-development)
12. [DLP Policies & Compliance Boundaries](#12-dlp---dlp-policies--compliance-boundaries)
13. [Troubleshooting FAQ](#13---troubleshooting-faq)
14. [Ecosystem Integration & Frontier Capabilities](#14---ecosystem-integration--frontier-capabilities)

---

## Fundamentals

### Flow Types

| Type | Description | Use Case |
|---|---|---|
| Automated cloud flow | Triggered by an event | Auto-process when SP item changes |
| Instant cloud flow | Manual trigger (button/selected item) | User clicks a button |
| Scheduled cloud flow | Runs on a schedule | Daily overdue check |
| Desktop flow | Local RPA automation | Automate local apps |
| Business process flow | Guided multi-stage process | Approval pipeline |

### Core Concepts

- **Trigger**: The event that starts a Flow; each Flow has exactly one trigger

- **Action**: Each step in a Flow (read data, send email, condition, etc.)

- **Connection**: Authenticated link between Flow and external services, stored under user account

- **Dynamic content**: Output from previous steps, referenceable in later steps

- **Expression**: Functions to process data (string concat, date math, etc.)

### Run Modes

| Mode | Meaning |
|---|---|
| Succeeded | All steps completed normally |
| Failed | A step errored and was not caught |
| Cancelled | Stopped by Terminate action or user |
| Running | Flow is currently executing |

---

## Trigger Types

### SharePoint Triggers

| Trigger | | Description |
|---|---|---|
| When an item is created | `When_an_item_is_created` | Fires when a new item is added |
| When an item is modified | `When_an_existing_item_is_modified` | Fires when an item is modified |
| For a selected item | `manual` (selected item) | User selects an item and triggers manually |
| When an item is created or modified | `When_an_item_is_created_or_modified` | Fires on both create and modify |

### Trigger Conditions

Add condition expressions in trigger settings — **Flow only runs when condition is true**.

```
# Single condition
@equals(triggerBody?['Status']?['Value'], 'Available')

# Multiple conditions (AND logic)
@equals(triggerBody?['ApprovalStatus']?['Value'], 'Returned')
@equals(triggerBody?['ActualReturnDate'], null)

# Not empty check
@not(empty(triggerBody?['Title']))

# Contains keyword
@contains(triggerBody?['Title'], 'Urgent')
```

> ⚠️ **AND** true
> Multiple trigger conditions are **AND** — all must be true to fire

### Concurrency Control

Configure in trigger **Settings → Concurrency Control**:

- **Parallelism = 1**: Only one instance at a time (prevents race conditions)
- **Parallelism = N**: Allow N instances concurrently

> Asset management scenario **must be 1** to prevent double-lending

---

## Common Connectors

### SharePoint

| Action | Purpose | Key Parameters |
|---|---|---|
| (Get item) | Read a single item | Site, List, Id |
| (Get items) | Query multiple items | Site, List, Filter Query, Top Count |
| (Create item) | Create a new item | column fields |
| (Update item) | Update an item | fields to update |
| (Delete item) | Delete an item | Site, List, Id |
| HTTP (Send an HTTP request) | Call SP REST API | Site, Method, URI, Headers, Body |

**SharePoint Filter Query Examples:**

```
Status eq 'Available'
AssetId eq 42
Title ne 'Test'
Status eq 'In use' and Category eq 'Electronics'
startswith(Title, 'Drill')
Modified gt '2024-01-01T00:00:00Z'
```

### Approvals

| Action | Purpose |
|---|---|
| (Start and wait for an approval) | Send approval, block until responded |
| (Create an approval) | Create without waiting |
| (Wait for an approval) | Wait for a created approval |

### Office 365 Outlook

| Action | Purpose |
|---|---|
| V2 (Send an email V2) | Send email notification |
| (Get email) | Read a specific email |

### Office 365 Users

| Action | Purpose |
|---|---|
| (Get user profile) | Get user info by UPN/email |
| (Get my profile) | Get current user info |
| (Search for users) | Search org users |

### HTTP

| Action | Purpose |
|---|---|
| HTTP | Call any REST API |
| HTTP + Swagger | Call based on OpenAPI spec |

---

## Expressions & Functions Reference

### String Functions

| Function | Description | Example |
|---|---|---|
| `concat(str1, str2, ...)` | Concatenate strings | `concat('Borrow - ', triggerBody ?['Title'])` → `Borrow - Drill` |
| `substring(str, start, length)` | Extract substring | `substring('Hello World', 6, 5)` → `World` |
| `replace(str, old, new)` | Replace | `replace('2024-01-01', '-', '/')` → `2024/01/01` |
| `split(str, delimiter)` | Split into array | `split('a,b,c', ',')` → `["a","b","c"]` |
| `trim(str)` | Trim whitespace | `trim(' hello ')` → `hello` |
| `toLower(str)` | To lowercase | `toLower('HELLO')` → `hello` |
| `toUpper(str)` | To uppercase | `toUpper('hello')` → `HELLO` |
| `length(str)` | String length | `length('hello')` → `5` |
| `indexOf(str, search)` | Find position | `indexOf('hello world', 'world')` → `6` |
| `startsWith(str, prefix)` | Starts with | `startsWith('Hello', 'He')` → `true` |
| `endsWith(str, suffix)` | Ends with | `endsWith('file.pdf', '.pdf')` → `true` |
| `contains(str, search)` | Contains | `contains('Hello World', 'World')` → `true` |

### Date & Time Functions

| Function | Description | Example |
|---|---|---|
| `utcNow ` | Current UTC time | `2024-03-15T08:30:00Z` |
| `utcNow('yyyy-MM-dd')` | Format current time | `2024-03-15` |
| `addDays(timestamp, days)` | Add days | `addDays(utcNow , 7)` → 7 |
| `addHours(timestamp, hours)` | Add hours | `addHours(utcNow , 8)` → 8 |
| `addMinutes(timestamp, mins)` | Add minutes | `addMinutes(utcNow , 30)` |
| `subtractFromTime(ts, interval, unit)` | Subtract time | `subtractFromTime(utcNow , 1, 'Day')` |
| `formatDateTime(ts, format)` | Format date | `formatDateTime(utcNow , 'yyyyMMdd')` |
| `convertFromUtc(ts, timezone)` | Convert from UTC | `convertFromUtc(utcNow , 'China Standard Time')` |
| `convertToUtc(ts, timezone)` | Convert to UTC | `convertToUtc('2024-03-15 16:30', 'China Standard Time')` |
| `ticks(timestamp)` | Convert to ticks | For precise comparison |
| `dateDifference(end, start)` | Time difference | `2.05:30:00` |

**Common Date Formats:**

| Format | Output |
|---|---|
| `yyyy-MM-dd` | `2024-03-15` |
| `yyyy-MM-ddTHH:mm:ssZ` | `2024-03-15T08:30:00Z` |
| `yyyyMMddHH:mm` | `2024031508:30` |
| `dddd, MMMM dd, yyyy` | `Friday, March 15, 2024` |
| `MM/dd/yyyy hh:mm tt` | `03/15/2024 08:30 AM` |

### Logical Functions

| Function | Description | Example |
|---|---|---|
| `equals(val1, val2)` | Equal check | `equals(1, 1)` → `true` |
| `not(expression)` | Negate | `not(equals(1, 2))` → `true` |
| `and(expr1, expr2)` | AND | `and(equals(a,1), equals(b,2))` |
| `or(expr1, expr2)` | OR | `or(equals(a,1), equals(a,2))` |
| `if(condition, trueVal, falseVal)` | Ternary | `if(equals(status,'Available'), 'Yes', 'No')` |
| `greater(val1, val2)` | Greater than | `greater(10, 5)` → `true` |
| `less(val1, val2)` | Less than | `less(3, 5)` → `true` |
| `greaterOrEquals(val1, val2)` | >= | `greaterOrEquals(5, 5)` → `true` |
| `lessOrEquals(val1, val2)` | <= | `lessOrEquals(3, 5)` → `true` |
| `empty(value)` | Is empty | `empty(null)` → `true`; `empty('')` → `true` |
| `coalesce(val1, val2, ...)` | First non-null | `coalesce(null, '', 'default')` → `''` |

### Collection & Array Functions

| Function | Description | Example |
|---|---|---|
| `length(array)` | Array length | `length(body('Get_items')?['value'])` |
| `first(array)` | First element | `first(variables('myArray'))` |
| `last(array)` | Last element | `last(variables('myArray'))` |
| `contains(array, item)` | Array contains | `contains(createArray('a','b'), 'a')` → `true` |
| `union(arr1, arr2)` | Union | `union(createArray(1,2), createArray(2,3))` → `[1,2,3]` |
| `intersection(arr1, arr2)` | Intersection | `intersection(createArray(1,2,3), createArray(2,3,4))` → `[2,3]` |
| `createArray(v1, v2, ...)` | Create array | `createArray('a', 'b', 'c')` |
| `join(array, delimiter)` | Join | `join(createArray('a','b'), ', ')` → `a, b` |

### Type Conversion Functions

| Function | Description |
|---|---|
| `int(value)` | To integer |
| `float(value)` | To float |
| `string(value)` | To string |
| `bool(value)` | To boolean |
| `json(value)` | To JSON object |
| `base64(value)` | Base64 encode |
| `base64ToString(value)` | Base64 decode |
| `decodeUriComponent(str)` | URI decode |
| `encodeUriComponent(str)` | URI encode |

### Reference Functions

| Function | Description |
|---|---|
| `triggerBody ` | Trigger output body |
| `triggerOutputs ` | Trigger full outputs |
| `body('actionName')` | Specific action output body |
| `outputs('actionName')` | Specific action full outputs |
| `actions('actionName')` | Action info including status |
| `result('scopeName')` | Array of all action results in scope |
| `items('Apply_to_each')` | Current item in loop |
| `variables('varName')` | Get variable value |
| `workflow ` | Current Flow metadata |
| `parameters('paramName')` | Flow parameter value |

### SharePoint People Column Claims Format

```
# Standard format
i:0#.f|membership|user@domain.com

# Build in expression
concat('i:0#.f|membership|', triggerBody?['headers']?['x-ms-user-email'])
```

---

## Variables & Data Operations

### Variable Types

| Type | Description | Init Example |
|---|---|---|
| String | Text | `""` `"default value"` |
| Integer | Whole number | `0` |
| Float | Decimal | `0.0` |
| Boolean | True/False | `false` |
| Array | List | `[]` |
| Object | Key-value | `{}` |

### Variable Actions

| Action | Description |
|---|---|
| (Initialize variable) | Declare at top level |
| (Set variable) | Overwrite variable value |
| (Append to string variable) | Append text |
| (Append to array variable) | Append element |
| (Increment variable) | Add to number |
| (Decrement variable) | Subtract from number |

> ⚠️ ** Flow **//Scope
> Initialize variable must be at top level, not inside conditions/loops/scopes

### Data Operations

| Action | Purpose |
|---|---|
| (Compose) | Build any value, works as temp variable |
| JSON (Parse JSON) | Parse JSON string into dynamic content |
| CSV (Create CSV table) | Array to CSV |
| HTML (Create HTML table) | Array to HTML table |
| (Filter array) | Filter array by condition |
| (Select) | Map array fields |
| (Join) | Join array to string |

> 💡 `Compose` ""
> **Tip**: `Compose` is more flexible than variables — no top-level restriction

---

## Flow Control

### Condition
```
: Status Value == "Available"
 ├── (If yes): ...
 └── (If no): ...
```

 / Use expressions for complex logic:
```
@and(
 equals(triggerBody?['Status']?['Value'], 'Available'),
 greater(triggerBody?['Quantity'], 0)
)
```

### Switch

```
Switch: ApprovalStatus Value
 ├── Case "Approved": ...
 ├── Case "Rejected": ...
 ├── Case "Returned": ...
 └── Default:
```

> 💡 3+ Switch Condition
> Use Switch over nested Conditions when you have 3+ branches

### Apply to each

 / Iterate over each element in an array:
```
Apply to each: body('Get_items')?['value']
 └── : items('Apply_to_each')
```

**Concurrency setting**: (50)
Default is sequential; can set parallelism (max 50)

### Do until

 / Loop until condition is met:
```
Do until: variables('retryCount') >= 3
 ├── A
 └── retryCount
```

> ⚠️ 60
> Set loop limit (default 60, adjustable) to prevent infinite loops

### Scope

 / Group multiple steps together:
- Flow / Collapse for cleanliness
- Unified error handling
- Configurable "run after" conditions

### Terminate
 Flow / Immediately end Flow with a status:
- Succeeded
- Failed —
- Cancelled

### Delay
 / Pause for specified duration:
- (Delay): //// Fixed duration
- (Delay until): / Until specific datetime

### Parallel Branch
Create multiple parallel execution paths; all branches complete before the next step.

```
 │
 ├──┬── A: (2)
 │ │
 │ ├── B: (3)
 │ │
 │ └── C: (1)
 │
 ▼ ( / Continue after all complete)
 ≈ 3 ( 6)
 Total ≈ 3s (not 6s sequential)
```

**How to create:**
1. **+** → Add a parallel branch

> ⚠️ Compose
> Cannot use the same variable in parallel branches (race condition); use Compose instead

> 💡 **Parallel branches vs Apply to each**: Parallel branches = fixed number of different operations; Apply to each concurrency = same operation on multiple items

---

## Error Handling & Reliability

### Configure Run After

Configure when an action runs based on the outcome of a previous action:

| Condition | Description |
|---|---|
| ✅ (is successful) | Default, run after success |
| ❌ (has failed) | Run after failure |
| ⏩ (is skipped) | Run after skip |
| ⏱️ (has timed out) | Run after timeout |

### Scope + Run After = Try-Catch Pattern

```
Scope_Try ( / Main operations):
 ├── A
 ├── B
 └── C

Scope_Catch (: "" / Run after: "has failed" only):
 ├── : result('Scope_Try')
 └──
```

** Scope / Get error details from Scope:**
```
# Get all action results
result('Scope_Try')

# Filter failed actions
@body('Filter_array')
 From: result('Scope_Try')
 Where: @equals(item?['status'], 'Failed')
```

### Retry Policy
 / Configure in action settings:

| Policy | Description |
|---|---|
| Default | 4 retries, exponential backoff |
| None | No retry |
| Fixed interval | Fixed interval retry |
| Exponential interval | Exponential backoff retry |

### Error Handling in Asset Management Scenario

```
Scope_BorrowActions:
 ├── : Status → "In use"
 └── : Service Requests

Scope_Rollback ( BorrowActions ):
 └── : Status → "Available"
```

> This ensures the tool won't get stuck in "In use" if creating the request fails

---

## Performance & Limits

### Runtime Limits

| Limit | Value | Description |
|---|---|---|
| Flow duration | 30 min | Max single run duration |
| | 100,000/ | Max actions per run |
| | 5,000 (60) | Apply to each / Do until / Max loop iterations |
| Apply to each | 50 | Max parallelism |
| | 500 | Concurrent outbound requests |
| | 104 MB | Max data size per action |
| | 8,192 | Max expression length |
| SharePoint Get items | 5,000 | Max items returned |

### SharePoint Delegation Limits

| Action | Default | Max |
|---|---|---|
| Get items (Top Count) | 100 | 5,000 |
| Filter Query | Limited delegation | Depends on column type |

**Delegable Filter Operators:**
- `eq`, `ne`, `gt`, `ge`, `lt`, `le` — ✅
- `startswith` — ✅
- `substringof`, `contains` — ❌ 2000

> For large lists (>5000 items), always use delegable filters

### API Call Quotas

| License | Per 24h |
|---|---|
| Power Automate Free | 750 |
| Per User Plan | 40,000 |
| Per Flow Plan | 250,000 |

### License Model Comparison

| Feature | Free / | Microsoft 365 | Per User Plan | Per Flow Plan |
|---|---|---|---|---|
| Standard connectors | ✅ | ✅ | ✅ | ✅ |
| Premium connectors | ❌ | ❌ | ✅ | ✅ |
| Custom connectors | ❌ | ❌ | ✅ | ✅ |
| Desktop flows | ❌ | ❌ | ✅ | ✅ |
| AI Builder credits | ❌ | ❌ | 5K/ | 5K/ |
| Dataverse storage | ❌ | ❌ | 250 MB | 50 MB |
| Child flows | ❌ | ❌ | ✅ | ✅ |
| Business process flows | ❌ | ❌ | ✅ | ✅ |
| Solution management | ❌ | ❌ | ✅ | ✅ |

> ⚠️ Actual capabilities depend on your organization's license tier, IT admin configuration, and DLP policies.
> Check with your admin for available connectors and features.

> 💡 **Standard vs Premium**: SharePoint, Outlook, Teams = Standard;
> Dataverse, SQL Server, HTTP with Microsoft Entra ID, Adobe Sign = Premium.

---

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
| | Click trigger to see full triggerBody |
| | Use **Test** → **Manually** to run in real-time |
| **Peek code** | View underlying JSON definition |

### Condition Debugging Tips

 / When conditions behave unexpectedly:

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

## Best Practices

### Naming Convention

```
# Flow naming
AssetMgmt_CreateRequest
AssetMgmt_RejectedRollback
AssetMgmt_ReturnedRollback
AssetMgmt_Approval

# Action naming (rename each step)
[]_[]_[]
Get_ToolInventory_ById
Update_ToolStatus_ToInUse
Create_BorrowRequest
Check_ToolAvailability
Send_RejectionEmail
```

> Always rename actions — defaults like "Get item 2" are hard to debug

### Architecture Design

1. Single responsibility per Flow
 - ✅ Flow
 - ❌ Flow

 Enable concurrency control (parallelism=1) for read-then-write scenarios

 Add trigger conditions to exclude self-modifications when using "on modified" triggers

 Design for idempotency — operations should be safe to repeat

### Security & Compliance

 Flow connections run with the creator's permissions
- **DLP **:
 Ensure all connectors are in the same DLP group
 Use "Secure Inputs/Outputs" to hide sensitive data in steps
 Use environment variables for URLs, emails, and other config

### Maintenance Tips

- Regularly check run history for failure rates
- Flow / Set up failure notifications for critical Flows
- Flow / Export Flow definitions as backups
- Flow / Document business logic and dependencies

---

## Expert-Level Development

> 🔥 JSON Solution CI/CD
>
> 🔥 This chapter covers advanced architecture patterns, complex expression techniques, child flow orchestration, JSON manipulation, Solution management, CI/CD, and enterprise production practices.

### Child Flows & Modular Architecture

#### Why Child Flows

| Problem | Child Flow Solution |
|---|---|
| Flow 500 | Split into child flows, each ≤100 actions |
| Flow | Extract to shared child flow, maintain once |
| | Parent orchestrates, children execute |
| | Different teams own their child flows |

#### Creating a Child Flow

```
 Child Flow Requirements:
1. Solution: Must be created inside a Solution
2. : "" (Manually trigger a flow)
3. : " Power App Flow" (Respond to a PowerApp or flow)
4. / Parent & child must be in the same environment
```

**Defining Input Parameters:**

```json
// Trigger → Add an input
{
 "type": "object",
 "properties": {
 "AssetId": { "type": "integer", "description": " ID" },
 "AssetName": { "type": "string", "description": "" },
 "RequesterEmail": { "type": "string", "description": "" },
 "Action": { "type": "string", "description": ": Borrow |Return|Reject" }
 },
 "required": ["AssetId", "Action"]
}
```

**Defining Output (Respond action):**

```json
// Define in Respond action
{
 "Status": "Success", // "Failed"
 "Message": "",
 "RequestId": 42
}
```

#### Parent Calling Child Flow

```
 Parent Flow:
 ├──
 ├──
 ├── (Run a Child Flow)
 │ : AssetId=123, Action="Borrow", RequesterEmail="user@contoso.com"
 │ ← : Status, Message, RequestId
 ├── : Status == "Success"?
 │ ├── :
 │ └── :
 └──
```

> Child flows run in the caller's connection context, sharing the parent's permissions.

#### Modular Refactoring Example

```
 Current (Monolithic):
 Flow 1: CreateRequest ( Flow )

 Refactored (Modular):
 Flow_Main: CreateRequest_Orchestrator
 ├── → ChildFlow_ValidateTool
 ├── → ChildFlow_LockTool
 ├── → ChildFlow_CreateRecord
 └── → ChildFlow_SendNotification
 ↑ Flow 2A, 2B
```

### Solution Lifecycle Management

#### Solution Basics

Solution Power Platform Flow Solution
Solutions are the **packaging & deployment unit** for Power Platform; all enterprise Flows should be created inside Solutions.

```
Solution: Solution Structure:
 MySolution/
 ├── Cloud flows/
 │ ├── AssetMgmt_CreateRequest
 │ ├── AssetMgmt_RejectedRollback
 │ ├── AssetMgmt_ReturnedRollback
 │ └── AssetMgmt_Approval
 ├── Connection references/
 │ ├── SharePoint_Connection
 │ └── Outlook_Connection
 ├── Environment variables/
 │ ├── SiteUrl (ContosoTeam URL)
 │ ├── AdminEmail (admin@contoso.com)
 │ └── ListName_Inventory ("Asset Inventory")
 └── Tables (if using Dataverse)/
```

#### Environment Variables

Replace hardcoded values with environment variables for cross-environment deployment.

```
# Definition ( Solution ):
: SiteUrl
: (Text)
: https://contoso.sharepoint.com/teams/ContosoTeam
: different per environment)

# Reference in Flow:
@{parameters('SiteUrl')}

# Good candidates for env vars:
- URL / Site URLs
- / List names
- / Admin emails
- / Approval timeouts
- / Feature flags
```

#### Connection References

```
# Create in Solution:
Connection Reference: SharePoint_ContosoTeam
Type: SharePoint
Description: Contoso team SharePoint connection

# When deploying to new environment:
Update connection reference to point to new SharePoint connection
```

#### Export & Import

| Export Type | Purpose | Characteristics |
|---|---|---|
| **Managed** | Production deployment | Cannot edit in target environment |
| **Unmanaged** | Dev/test environments | Editable, for continued development |

```
 Recommended Workflow:
 Dev → → Test → → Prod
 Dev (unmanaged) → export managed → import Test → verify → import Prod
```

### Advanced JSON Manipulation

#### Parse JSON Schema Generation

```
 Method:
1. Flow JSON / Run Flow once, get actual JSON output
2. Parse JSON "" (Generate from sample)
3. JSON → Schema

 Schema: Manual Schema Tuning:
{
 "type": "object",
 "properties": {
 "AssetId": { "type": "integer" },
 "Status": {
 "type": "object",
 "properties": {
 "Value": { "type": "string" }
 }
 },
 "Title": { "type": ["string", "null"] } // null / Allow null
 },
 "required": ["AssetId"] // / Only mark truly required fields
}
```

> ⚠️ Schema required null Parse JSON
> **Common pitfall**: Schema defaults all properties to required; if a field can be null, Parse JSON fails.

#### Dynamically Build Complex JSON

```
# Method 1: Compose + expressions
Compose :
{
 "request": {
 "toolId": @{triggerBody?['ID']},
 "toolName": "@{body('Get_item')?['Title']}",
 "requester": "@{triggerBody?['headers']?['x-ms-user-email']}",
 "timestamp": "@{utcNow}",
 "metadata": {
 "flowRunId": "@{workflow?['run']?['name']}",
 "environment": "@{parameters('EnvironmentName')}"
 }
 }
}

# Method 2: json from string
json(concat(
 '{"toolId":', string(triggerBody?['ID']),
 ',"status":"', body('Get_item')?['Status']?['Value'],
 '","timestamp":"', utcNow, '"}'
))
```

#### XPath for XML Processing

```
# When processing XML data:
xpath(xml(body('HTTP_Response')), '//tool[@status="available"]/name/text')

# XML to JSON:
json(xml(body('HTTP_Response')))
```

#### Advanced Array Operations

```
# project array
Select:
 From: body('Get_items')?['value']
 Map: { "id": @{item?['ID']}, "name": @{item?['Title']} }
 → : [{"id":1,"name":"Drill"}, {"id":2,"name":"Saw"}]

# Complex filtering
Filter array:
 From: body('Get_items')?['value']
 Where: @and(
 equals(item?['Status']?['Value'], 'Available'),
 greater(item?['Quantity'], 0),
 not(contains(item?['Title'], 'RESERVED'))
 )

# Deduplicate
union(variables('myArray'), variables('myArray'))

# 4. — Select + sortBy (Office Script Compose )
# Power Automate sort:
# a) Office Script
# b) SharePoint Get items OData orderby
# c) Select + + sort

# Array aggregation — sum
# Use Apply to each + increment variable
length(body('Filter_array')) // / Count
```

### Advanced Expression Patterns

#### Nested Conditional Expressions

```
# Multi-level if (switch-like)
if(
 equals(triggerBody?['Status']?['Value'], 'Available'),
 'green',
 if(
 equals(triggerBody?['Status']?['Value'], 'In use'),
 'red',
 if(
 equals(triggerBody?['Status']?['Value'], 'Maintenance'),
 'yellow',
 'gray'
 )
 )
)
```

#### Safe Property Access Chain

```
# Deep nested safe access
# ?[] null
triggerBody?['d']?['results']?[0]?['Status']?['Value']

# Safe access with default
coalesce(
 triggerBody?['OptionalField']?['Value'],
 'DefaultValue'
)

# Multi-level fallback
coalesce(
 body('Get_item')?['PreferredEmail'],
 body('Get_item')?['Email'],
 body('Get_item')?['Created By']?['Email'],
 'unknown@contoso.com'
)
```

#### Regex Alternatives

PA expressions don't support regex directly, but you can combine functions:

```
# Check email format (simplified)
and(
 contains(variables('email'), '@'),
 contains(variables('email'), '.'),
 greater(indexOf(variables('email'), '@'), 0)
)

# Extract domain
# user@contoso.com → microsoft.com
substring(
 variables('email'),
 add(indexOf(variables('email'), '@'), 1),
 sub(
 length(variables('email')),
 add(indexOf(variables('email'), '@'), 1)
 )
)

# Office Script Azure Function
# For complex regex needs, use Office Script or Azure Function
```

#### Dynamic Property Access

```
# When property name is in a variable
# body('step')?[variables('fieldName')]
# PA doesn't support variable as property index

# Serialize → string extraction
Compose_JSON: string(body('Get_item'))
Compose_Value:
 substring(
 outputs('Compose_JSON'),
 add(indexOf(outputs('Compose_JSON'), concat('"', variables('fieldName'), '":"')),
 add(length(variables('fieldName')), 4)),
 indexOf(
 substring(outputs('Compose_JSON'),
 add(indexOf(outputs('Compose_JSON'), concat('"', variables('fieldName'), '":"')),
 add(length(variables('fieldName')), 4))),
 '"')
 )

# Use Select + predefined mapping
# Pre-build mapping object
Compose_FieldMap:
{
 "Status": "@{body('Get_item')?['Status']?['Value']}",
 "Category": "@{body('Get_item')?['Category']?['Value']}",
 "Priority": "@{body('Get_item')?['Priority']?['Value']}"
}
# json
# Then parse with json and access by variable
json(outputs('Compose_FieldMap'))?[variables('fieldName')]

# xpath extraction (most universal)
# JSON XML xpath
xpath(
 xml(json(concat('{"root":', string(body('Get_item')), '}'))),
 concat('//root/', variables('fieldName'), '/text')
)
```

### Advanced Error Handling Patterns

#### Global Try-Catch-Finally Pattern

```
Flow: Flow structure:
 │
 ├── Initialize: var_FlowStatus = "Running"
 ├── Initialize: var_ErrorMessage = ""
 │
 ├── Scope_TRY:
 │ ├── All business logic
 │ └── Set var_FlowStatus = "Succeeded"
 │
 ├── Scope_CATCH (Run after: failed):
 │ ├── Set var_FlowStatus = "Failed"
 │ ├── Set var_ErrorMessage =
 │ │ string(result('Scope_TRY'))
 │ ├── Log error
 │ └── Send alert
 │
 └── Scope_FINALLY (Run after: succeeded, failed, skipped):
 ├── Cleanup temp data
 ├── Write audit log
 └── : var_FlowStatus == "Failed"?
 └── : Terminate (Failed)
```

#### Retry Wrapper Pattern

```
Initialize: retryCount = 0
Initialize: maxRetries = 3
Initialize: operationSuccess = false

Do until: or(variables('operationSuccess'), greaterOrEquals(variables('retryCount'), variables('maxRetries')))
 │
 ├── Scope_Attempt:
 │ ├── Execute operation
 │ └── Set operationSuccess = true
 │
 ├── Scope_RetryHandler (Run after: Scope_Attempt failed):
 │ ├── Increment retryCount
 │ ├── Delay: mul(variables('retryCount'), 30) // / Incremental delay
 │ └── Log: concat(' #', string(variables('retryCount')))
 │
 └── ( / Loop continues)

Condition: operationSuccess == false
 └── : Terminate (Failed, " 3 ")
```

#### Error Classification & Tiered Response

```
Scope_CATCH:
 │
 ├── Compose: result('Scope_TRY') /
 │
 ├── Filter_FailedActions:
 │ From: outputs('Compose')
 │ Where: equals(item?['status'], 'Failed')
 │
 ├── Apply to each: body('Filter_FailedActions')
 │ │
 │ └── Switch: items('Apply_to_each')?['code']
 │ ├── "429" ( / Throttled):
 │ │ → / Delay and retry
 │ ├── "404" ( / Not found):
 │ │ → / Log and skip
 │ ├── "401/403" ( / Permission):
 │ │ → / Alert admin immediately
 │ └── Default:
 │ → / Generic error handling
```

### Advanced Trigger Patterns

#### Polling Optimization — Incremental Query

```
# SharePoint "" +
# "Get items" + status flag to avoid reprocessing

 Scheduled trigger (every 5 min):
 │
 ├── Get items:
 │ Filter: ProcessingStatus eq 'Pending'
 │ Order: Created asc
 │ Top: 50
 │
 ├── Apply to each:
 │ ├── Processing Mark as Processing immediately
 │ ├── Execute business logic
 │ └── Completed / Mark as Completed
 │
 └── Condition: 50 ?
 └── : HTTP
 Trigger self again to process remaining
```

#### Queue-Based Processing Pattern

```
# SharePoint
# Use SharePoint list as a message queue

Queue: Queue list design:
 - Title:
 - Payload: JSON
 - Status: Queued → Processing → Completed → Failed
 - LockedBy: Flow Run ID
 - LockedAt:
 - RetryCount:
 - MaxRetries:
 - ErrorMessage:

 Processing flow:
 ├── Status=Queued (LockedBy LockedAt 30 )
 ├── : LockedBy = workflow?['run']?['name'], Status = Processing
 ├── Parse JSON: Payload
 ├── : Status = Completed
 └── : RetryCount++,
 if RetryCount < MaxRetries → Status = Queued
 else → Status = Failed
```

#### Event-Driven Orchestration

```
# Flow SharePoint
# Multiple Flows orchestrated via status field changes (loosely coupled)

 SharePoint List
 (State Machine)
 ┌────────────────────┐
 │ Status │
 ┌──────────────┤ Flow ├──────────────┐
 │ └────────┬───────────┘ │
 │ │ │
 ▼ ▼ ▼
 Flow A Flow B Flow C
 : : :
 Status= Status= Status=
 "Step1_Done" "Step2_Done" "Step3_Done"
 │ │ │
 └→ └→ └→
 Status= Status=
 "Step2_Done" "Step3_Done"
```

### Advanced Performance Optimization

#### Concurrency Optimization

```
# Apply to each concurrency

 1: → = 20-50
 Scenario 1: Independent operations (e.g., notifications) → Parallelism 20-50

 Scenario 2: Shared resources (e.g., updating same list) → Parallelism 1

 3: API→ = 5-10
 Scenario 3: External API with throttling → Parallelism 5-10, add delay
```

#### Batch Operations Instead of Loops

```
# Inefficient: Create one-by-one in loop
Apply to each (100 items):
 └── Create item (SharePoint) ← 100 API calls

# Efficient: Use SP batch API
SharePoint " HTTP ":
 Method: POST
 URI: _api/$batch
 Headers: { "Content-Type": "multipart/mixed; boundary=batch_xxx" }
 Body: ( / Batch request body)
 ← 1 API call for 100 items

# ✅ : Compose + Select
# Alternative: Preprocess with Compose + Select, minimize in-loop actions
```

#### SharePoint Query Optimization

```
# Reduce response data

# Return only needed columns
SharePoint " HTTP ":
 GET _api/web/lists/getbytitle('Asset Inventory')/items?$select=ID,Title,Status&$top=100

# Reduce extra requests with $expand
 GET ...?$select=ID,Title,Requester/EMail&$expand=Requester

# Indexed columns + filter
# Ensure filtered columns are indexed (List settings → Indexed columns)

# Paginate large lists
Do until: empty(body('Get_items')?['value'])
 ├── Get items (Top: 5000, Skip Token: variables('skipToken'))
 ├── Process current batch
 └── Set skipToken = body('Get_items')?['odata.nextLink']
```

#### Caching Strategy

```
# Cache repeatedly used values with Compose

# Recalculated each time
 1: ... formatDateTime(utcNow, 'yyyy-MM-dd') ...
 2: ... formatDateTime(utcNow, 'yyyy-MM-dd') ... ←
 3: ... formatDateTime(utcNow, 'yyyy-MM-dd') ...

# Compute once, reference many times
Compose_TodayDate: formatDateTime(utcNow, 'yyyy-MM-dd')
 1: ... outputs('Compose_TodayDate') ...
 2: ... outputs('Compose_TodayDate') ... ←
 3: ... outputs('Compose_TodayDate') ...
```

### Flow Definition Language

#### Understanding the Underlying JSON

 Flow JSON
Every Flow is a JSON definition file underneath. Understanding it enables:

- Flow / Batch-modify Flow configurations
- / Flow / Copy/templatize Flows
- (Git) / Version control (Git)
- Automated deployment

```json
// Flow JSON structure overview
{
 "definition": {
 "$schema": "https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#",
 "triggers": {
 "When_an_item_is_created": {
 "type": "ApiConnection",
 "inputs": {
 "host": { "connection": { "name": "@parameters('$connections')['shared_sharepointonline']['connectionId']" }},
 "method": "get",
 "path": "/datasets/@{encodeURIComponent('https://contoso.sharepoint.com/teams/ContosoTeam')}/tables/@{encodeURIComponent('Service Requests')}/onnewitems"
 },
 "recurrence": { "frequency": "Minute", "interval": 1 }
 }
 },
 "actions": {
 "Get_item": {
 "type": "ApiConnection",
 "inputs": { ... },
 "runAfter": {}
 },
 "Condition": {
 "type": "If",
 "expression": { "@equals": ["@body('Get_item')?['Status']?['Value']", "Available"] },
 "actions": { ... },
 "else": { "actions": { ... } },
 "runAfter": { "Get_item": ["Succeeded"] }
 }
 }
 },
 "parameters": {
 "$connections": { ... }
 }
}
```

#### Peek Code & Debugging

```
 How to use:
1. Flow "..."
2. "Peek code"

 Common uses:
- ( Status Status/Value)
```

### 11.9 CI/CD ALM / CI/CD & Application Lifecycle Management

#### Deployment Pipeline

```
┌─────────────┐ ┌──────────────┐ ┌──────────────┐
│ Dev │───→│ Test │───→│ Prod │
│ │ │ │ │ │
│ │ │ │ │ │
│ & │ │ UAT │ │ │
│ │ │ │ │ │
└──────┬──────┘ └──────┬───────┘ └──────────────┘
 │ │
 ▼ ▼
 Export unmanaged
 Export managed
```

#### Using Power Platform CLI

```powershell
# Install PAC CLI
dotnet tool install --global Microsoft.PowerApps.CLI.Tool

# Authenticate
pac auth create --url https://org.crm.dynamics.com

# Export Solution
pac solution export --path ./exports/AssetMgmt_1_0_0.zip --name AssetMgmtSolution --managed false

# Unpack to source code (Git-friendly)
pac solution unpack --zipfile ./exports/AssetMgmt_1_0_0.zip --folder ./src/AssetMgmtSolution --packagetype Both

# Repack
pac solution pack --folder ./src/AssetMgmtSolution --zipfile ./builds/AssetMgmt_managed.zip --packagetype Managed

# Import to target environment
pac solution import --path ./builds/AssetMgmt_managed.zip --activate-plugins
```

#### Azure DevOps / GitHub Actions / Pipeline Integration

```yaml
# Azure DevOps Pipeline example
trigger:
 branches: [main]
 paths:
 include: ['src/AssetMgmtSolution/**']

stages:
 - stage: Build
 jobs:
 - job: PackSolution
 steps:
 - task: PowerPlatformToolInstaller@2
 - task: PowerPlatformPackSolution@2
 inputs:
 SolutionSourceFolder: src/AssetMgmtSolution
 SolutionOutputFile: $(Build.ArtifactStagingDirectory)/AssetMgmt_managed.zip
 SolutionType: Managed

 - stage: DeployTest
 dependsOn: Build
 jobs:
 - deployment: DeployToTest
 environment: PowerPlatform-Test
 strategy:
 runOnce:
 deploy:
 steps:
 - task: PowerPlatformImportSolution@2
 inputs:
 Environment: $(TestEnvironmentUrl)
 SolutionInputFile: $(Pipeline.Workspace)/AssetMgmt_managed.zip
 ActivatePlugins: true

 - stage: DeployProd
 dependsOn: DeployTest
 condition: succeeded
 jobs:
 - deployment: DeployToProd
 environment: PowerPlatform-Prod
 strategy:
 runOnce:
 deploy:
 steps:
 - task: PowerPlatformImportSolution@2
 inputs:
 Environment: $(ProdEnvironmentUrl)
 SolutionInputFile: $(Pipeline.Workspace)/AssetMgmt_managed.zip
```

### Monitoring & Observability

#### Run Status Dashboard

```
# SharePoint Flow
# Use SharePoint list to log Flow run history

FlowRunLog: FlowRunLog list design:
 - FlowName: Text (Flow )
 - RunId: Text (workflow?['run']?['name'])
 - Status: Choice (Started / Succeeded / Failed)
 - StartTime: DateTime (utcNow at start)
 - EndTime: DateTime (utcNow at end)
 - Duration: Number (dateDifference )
 - ErrorMessage: Multiple lines
 - InputSummary: Multiple lines

# Add logging steps at the start and end of every Flow

# Power BI
# Then connect Power BI to this list for dashboards
```

#### Alerting Strategy

```
 Alert Levels:

🔴 P0 - / Critical:
 - Flow (CreateRequest) 3
 → Teams + / Immediate Teams + Email

🟡 P1 - / Warning:
 - Flow
 → / Email admin

🟢 P2 - / Info:
 → / Daily summary email
```

#### Flow Analytics API / Flow API

```
# Power Automate Management Connector
# Get run analytics via PA Management Connector

# Power Platform Admin Center:
# → → Power Automate
# Admin → Analytics → Power Automate

 Key Metrics:
 - // / Daily/weekly/monthly run count
 - / Success rate
 - / Average run duration
 - / Most frequently failing steps
 - API / API call consumption
```

### Security Hardening

#### Principle of Least Privilege

```
# Connection account permissions

 Using admin account for Flow connections

 Create dedicated service account with minimal permissions

 Permission Matrix:
┌────────────────────────┬──────────────────┬──────────────────┐
│ / List │ Flow │ │
├────────────────────────┼──────────────────┼──────────────────┤
│ Asset Inventory │ + │ │
│ Service Requests │ + + │ │
│ FlowRunLog │ │ │
└────────────────────────┴──────────────────┴──────────────────┘
```

#### Secure Inputs & Outputs

```
# Enable in action settings:
 → ... → → (Security)
 ☑ (Secure Inputs) —
 ☑ (Secure Outputs) —

 Use cases:
 - /Token
 - (PII)
```

#### Injection Prevention

```
# SharePoint
# Input validation in SharePoint filter queries

# Directly concatenating user input
Filter: Title eq '@{triggerBody?['UserInput']}'
 → : ' or 1 eq 1 or Title eq ' ← OData !

# ✅ encodeURIComponent
# Use encodeURIComponent or validate input
Filter: Title eq '@{replace(triggerBody?['UserInput'], '''', '''''')}'

# ✅ Get item by ID
# Or use Get item by ID (no query concatenation)
```

### Advanced Design Patterns Quick Reference

| Pattern | Use Case | Core Idea |
|---|---|---|
| **Saga ** | | Each step has a compensating action |
| **Circuit Breaker** | | Stop calling after N failures, probe periodically |
| (Fan-out/Fan-in)** | | Concurrent loop + collect results |
| **Batch** | | Scheduled + paged reads + batch updates |
| **Observer** | | Status field changes trigger independent Flows |
| **Idempotent Consumer** | | Check unique ID before processing |
| **State Machine** | | Choice column as state, trigger conditions as transitions |
| **Exponential Backoff** | API | Delay = baseDelay × 2^retryCount |

#### Saga Pattern Full Example

```
# Saga
# Asset management Saga pattern (with compensation)

Saga: Saga Steps:
 ┌─────────────────┬─────────────────────────────┐
 │ │ │
 ├─────────────────┼─────────────────────────────┤
 │ ① │ ← (Status=Available) │
 │ Status=In use │ │
 ├─────────────────┼─────────────────────────────┤
 │ ② │ ← │
 │ Service Requests │ │
 ├─────────────────┼─────────────────────────────┤
 │ ③ │ ← │
 │ │ │
 ├─────────────────┼─────────────────────────────┤
 │ ④ │ ← │
 └─────────────────┴─────────────────────────────┘

 ③ → ② ①
 If step ② fails → compensate step ①
 If step ③ fails → compensate steps ② and ① (reverse order)
```

---

## DLP Policies & Compliance Boundaries

> ⚠️ **Power Platform DLP**
>
> ⚠️ **Enterprise Power Platform environments are typically governed by DLP policies.**
> Before creating or modifying Flows, you must understand the DLP policy boundaries for your environment, or your Flow may be blocked.

### DLP Core Concepts

**DLP (Data Loss Prevention)**

| Concept | Description |
|---|---|
| **Data Policy** | Policy created in Admin Center defining connector classification rules |
| **Connector Group** | Connectors classified into 3 groups: Business, Non-Business, Blocked |
| **Policy Scope** | Policy applies to entire tenant or specific environments |
| **Policy Stacking** | When multiple policies apply, the **most restrictive** intersection wins |

### Three Connector Groups

```
┌─────────────────────────────────────────────────────────────┐
│ DLP: DLP Policy │
│ │
│ ┌──────────────┐ ┌──────────────┐ ┌──────────────────┐ │
│ │ Business │ │ Non-Business │ │ Blocked │ │
│                │ │               │ │                  │ │ │
│                │ │               │ │                  │ │ │
│ │ ✅ Same group OK │ │ ✅ Same group OK │ │ ❌ Cannot use   │ │
│                │ │               │ │                  │ │ │
│ │                │ │               │ │  in any Flow     │ │
│ │ ❌ Cannot mix  │ │ ❌ Cannot mix │ │                  │ │
│ │ Non-Biz │ │ Business │ │ │ │
│                │ │               │ │                  │ │ │
│ └──────────────┘ └──────────────┘ └──────────────────┘ │
│ │
│ / Core Rule: │
│ Flow Business │
│ Non-Business Flow │
│ All connectors in a Flow must belong to the SAME group, │
│ or the Flow is blocked. │
└─────────────────────────────────────────────────────────────┘
```

### Typical DLP Classification in Enterprise Environments

> Power Platform Admin Center
> Below is a typical enterprise classification; actual policies vary by organization.

#### Business Group

| Connector | Notes |
|---|---|
| **SharePoint** | Core connector, cannot be blocked |
| **Microsoft Teams** | Core connector |
| **Office 365 Outlook** | Core connector |
| **Office 365 Users** | Core connector |
| **OneDrive for Business** | Core connector |
| **Dataverse** | Core connector |
| **Approvals** | Approval connector |
| **Microsoft Forms** | Forms connector |
| **Planner** | Task management |
| **Power BI** | Data analytics |
| **Azure AD** | Identity management |
| **Excel Online (Business)** | Business spreadsheet |

> 💡 Microsoft 365 core connectors cannot be blocked, only moved between Business and Non-Business.

#### Non-Business Group (Default)

| Connector | Notes |
|---|---|
| **MSN Weather** | Weather |
| **RSS** | RSS feeds |
| **Notifications** | Push notifications |
| Most 3rd-party connectors | Default group for new connectors |

> ⚠️ **New connectors default to Non-Business.**
> Newly added connectors default to Non-Business. If your Flow uses Business connectors (e.g., SharePoint), you cannot mix in Non-Business connectors.

#### Blocked Group

Commonly blocked in enterprise environments:

| Connector | Reason |
|---|---|
| **HTTP** | Can send data to any external URL, high data leak risk |
| **HTTP Webhook** | Same as above |
| **HTTP with Microsoft Entra ID** | Can call any Entra-protected API |
| **Custom Connectors** | May point to unauthorized external endpoints |
| **SMTP** | Can send via any mail server |
| **FTP** | File transfer risk |
| **Azure Blob Storage** | Unmanaged storage in some environments |

> 🔴 **Key limitation**: HTTP connector is **blocked** in most enterprise environments:
> - ❌ Cannot use HTTP action to call external APIs
> - ❌ Cannot use "When an HTTP request is received" trigger for custom webhooks
> - ❌ Cannot use HTTP Webhook actions
> - ✅ CAN use SharePoint's "Send an HTTP request" action (part of SharePoint connector, not standalone HTTP)

### Policy Scope & Stacking Rules

#### Scope Hierarchy

```
┌─────────────────────────────────────────────┐
│            Tenant-Level Policy              │
│   (Covers all environments, IT admin managed) │
│                                               │
│  ┌─────────────────────────────────────────┐  │
│  │       Environment-Level Policy          │  │
│  │  (Additional restrictions per env)       │  │
│  │                                         │  │
│  │  Example:                               │  │
│  │  • Default: standard restrictions       │  │
│  │  • Dev: relaxed for testing             │  │
│  │  • Production: strictest policies       │  │
│  └─────────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

#### Multi-Policy Stacking Effect

When multiple policies apply to the same environment:

| Scenario | Policy A | Policy B | Final Effect |
|---|---|---|---|
| Business + Blocked | Business | Blocked | **Blocked** ❌ |
| Business + Non-Business | Business | Non-Business | Cannot mix with either group |
| Business + Business | Business | Business | **Business** ✅ |

> ⚠️ **Most Restrictive Wins**: The most restrictive classification always wins. Blocked in ANY policy = Blocked.

### Connector Action-Level Control

> New in 2024-2025: Admins can control specific actions within a connector, not just the whole connector.

#### Action-Level DLP Examples

| Connector | Allowed Actions | Blocked Actions |
|---|---|---|
| SQL Server | Select | Delete, Drop Table |
| SharePoint | Get items, Get item | Delete item |
| SMTP | — | Send email |
| Office 365 Outlook | Send email (V2) | Forward email |

#### Endpoint Filtering (Preview)

Admins can restrict connectors to specific endpoints:

```
# Example: Only allow organization API
HTTP Connector endpoint rules:
  ✅ Allow: https://*.contoso.com/*
  ✅ Allow: https://*.sharepoint.com/*
  ❌ Deny: * (all others)

# Note:
# Endpoint filtering only applies to statically configured URLs at design time
# Dynamically generated URLs at runtime are NOT filtered (security gap)
```

### DLP Policy Management

#### View DLP Policies for Current Environment

**Method 1: Admin Center (Recommended)**

1. https://admin.powerplatform.microsoft.com
2. → **Policies** → **Data policies**
3. Click policy name to see connector classification

**Method 2: PowerShell**

```powershell
# Install admin module
Install-Module -Name Microsoft.PowerApps.Administration.PowerShell

# Login
Add-PowerAppsAccount

# List all DLP policies
Get-DlpPolicy

# View specific policy details
Get-DlpPolicy -PolicyName "<policy-guid>"
```

#### When Blocked by DLP

```
Error when saving or running Flow:
"Blocked by Data Loss Prevention policy"
        │
        ▼
┌───────────────────────────────────────┐
│ 1. Identify conflicting connectors    │
│    (Check which connectors conflict)  │
└───────────┬───────────────────────────┘
            │
            ▼
┌───────────────────────────────────────┐
│ 2. Check connector DLP classification │
│    (Admin Center → Data policies)     │
└───────────┬───────────────────────────┘
            │
            ▼
┌───────────────────────────────────────┐
│ 3. Choose a solution:                 │
│                                       │
│  a) Replace with same-group connector │
│     (e.g., Outlook instead of SMTP)   │
│                                       │
│  b) Split into multiple Flows         │
│     (one Flow per connector group)    │
│                                       │
│  c) Contact IT admin to adjust DLP    │
│     (request policy exception)        │
│                                       │
│  d) Request a dedicated environment   │
│     (with custom DLP policies)        │
└───────────────────────────────────────┘
```

### DLP Best Practices

1. **Check before build**: Verify connector DLP groups before building a Flow

2. **Prefer Business group connectors**: SharePoint + Outlook + Teams + Approvals covers most scenarios

3. **Avoid HTTP connector**: Commonly blocked in enterprise environments; use SharePoint REST API or native connectors instead

4. **SP "Send HTTP request" is a safe alternative**: This action is part of the SharePoint connector (Business group), can call SP REST API, unaffected by HTTP block

5. **Review new connectors**: Check DLP group for every new connector; default Non-Business may cause conflicts

6. **Environment isolation**: Request separate environments with dedicated DLP policies for projects needing special connectors

7. **Document connector usage**: Record all connectors and their DLP groups in Flow design docs

8. **Monitor policy changes**: DLP policies may be updated by IT admin at any time; existing Flows may break due to policy changes

### Advanced Connector Policies (2025+)

> **Advanced Connector Policies**

| Change | Description |
|---|---|
| **Simplified Groups** | Simplified to Allow and Block |
| **Default Block** | New connectors blocked by default until admin review |
| **Action Granular** | Per-trigger/action control |
| **Policy Coexistence** | Advanced policies coexist with standard DLP |

---

## Troubleshooting FAQ

### People column write fails

**Cause**: SharePoint People columns require Claims format
**Solution**:
```
# Claims format
concat('i:0#.f|membership|', <email>)

# If new SP supports Email directly
# Just use email address
```

### Value casing in trigger conditions

**Symptom**: Flow trigger condition not working
**Solution**: Try `Value` (uppercase) first, then `value` (lowercase), or use in-flow conditions instead

### Can't access loop variable

**Solution**: `items('Apply_to_each')?['fieldName']`

### Old instances still running after modification

**Solution**: Go to Flow → Turn off → Cancel all running instances → Turn on again

### "Item or list not found" error

**Investigation**:
1. Check site URL spelling
2. Check list name (use internal column name)
3. Verify ID value is valid
4. Check connection account permissions

### Expression returns null

**Common causes**:
```
# Wrong property path
triggerBody?['Status']?['Value'] # ✅ ?['Value']
triggerBody?['Status'] # ❌

# Null-safe access
triggerBody?['Field'] # ✅ ?[] null
triggerBody['Field'] # ❌ Field

# Dynamic content vs Expression
```

### How to handle concurrency conflicts

**Scenario**: Multiple Flow instances updating the same item simultaneously
**Solution**:
1. Set trigger concurrency to 1
2. Re-read status before update (optimistic lock)
3. Use SP list versioning

### How to test auto-triggered Flows

1. Convert to instant flow to test logic first
2. Create dedicated test data
3. Expand trigger in run history
4. **Add debug Compose**: Add Compose actions at key points to output variable values

### Flow blocked by DLP policy

**Symptom**: "Blocked by Data Loss Prevention policy" error
**Cause**: Flow uses connectors from different DLP groups
**Solution**:
1. Check error details for conflicting connectors
2. Replace with same-group connector (e.g., Outlook instead of SMTP)
3. Or split into multiple Flows per group
4. Contact IT admin (`Power Platform Admin Center → Data policies`)

### HTTP connector blocked

**Symptom**: Cannot save or run Flow using HTTP connector
**Solution**:
```
# Alternative priority:
1. Use SharePoint "Send an HTTP request" action — calls SP REST API ✅
2. Use Dataverse or SQL Server native connector ✅
3. Request DLP exception from IT admin ⚠️
4. Request dedicated environment with custom DLP ⚠️
```

---

## Ecosystem Integration & Frontier Capabilities

> 🚀 This chapter covers deep integration with AI/Copilot, Teams Adaptive Cards, Power Apps,
> Dataverse, Desktop Flows (RPA), Custom Connectors, and governance toolkits.

### AI Builder & Copilot Integration

#### Copilot in Power Automate

```
Use Cases:
1. Create Flow from natural language
   e.g., "When a SharePoint item is created, send approval"
   → Copilot generates: trigger + condition + approval + notification

2. Edit existing Flow with Copilot
   → Copilot adds Outlook Send email action

3. Ask Copilot questions about your Flow

Entry:
  make.powerautomate.com → Open Flow → Click Copilot icon
```

#### AI Builder Models

| Model | Purpose | Asset Management Scenario |
|---|---|---|
| **Document Processing** | Extract data from PDF/images | Auto-import from scanned inventory forms |
| **Text Classification** | Categorize text | Auto-classify request types |
| **Sentiment Analysis** | Analyze sentiment | Analyze user feedback |
| **Entity Extraction** | Extract entities from text | Extract tool name + requester from email |
| **GPT (Create text with GPT)** | Generate text | Auto-generate confirmation messages |
| **Object Detection** | Detect objects in images | Photo-verify return condition |

#### Using AI Builder in Flows

```
# Example: Generate personalized notification with GPT

Flow structure:
  ├── Trigger: Service Requests (new item)
  ├── Get item details
  ├── AI Builder: Create text with GPT
  │   Input: Item title, requester name, date
  │   ← Output: AI-generated message
  └── Send email (V2): Include AI-generated content
```

> ⚠️ **AI Builder Credits**
> AI Builder requires credits — monthly quota, additional credits cost extra.

### Teams + Adaptive Cards Patterns

#### Adaptive Cards Basics

Adaptive Cards are cross-platform UI cards enabling **rich interactions** in Teams (buttons, forms, selectors).

```json
// Asset management approval card example
{
 "type": "AdaptiveCard",
 "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
 "version": "1.4",
 "body": [
 {
 "type": "TextBlock",
 "text": "🔧 ",
 "weight": "Bolder",
 "size": "Large"
 },
 {
 "type": "FactSet",
 "facts": [
 { "title": "", "value": "${AssetName}" },
 { "title": "", "value": "${RequesterName}" },
 { "title": "", "value": "${RequestDate}" }
 ]
 },
 {
 "type": "TextBlock",
 "text": "",
 "wrap": true
 }
 ],
 "actions": [
 {
 "type": "Action.Submit",
 "title": "✅ ",
 "style": "positive",
 "data": { "action": "approve", "requestId": "${RequestId}" }
 },
 {
 "type": "Action.Submit",
 "title": "❌ ",
 "style": "destructive",
 "data": { "action": "reject", "requestId": "${RequestId}" }
 }
 ]
}
```

#### Sending Adaptive Cards in Flow

```
# 1: " Adaptive Card "
# Post adaptive card and wait for a response

Teams → Adaptive Card
 Team: Contoso
 Channel:
 Card: ( JSON)
 : " @{body('Post_adaptive_card')?['responderDisplayName']} "
 ← : body('Post_adaptive_card')?['data']?['action']

# 2: " Adaptive Card"
# Post card without waiting

# 3: "Post Adaptive Card to a Teams user and wait"
# Send to specific user and wait
```

#### Teams @Mention / @

```
# @mention a user in Teams message
<at></at>

# HTML :
<at>admin</at>
```

#### Teams Notification Best Practices

```
✅ :
 - Adaptive Card
 - "Post and wait"

❌ :
 - Flow Teams
 - debug
```

### Power Apps ↔ Power Automate Integration

#### Triggering Flow from Power Apps

```
# 1. Flow "Power Apps (V2)"
# 3. ( "Respond to a PowerApp or flow" )
# 4. Power Apps : → Power Automate → Flow

Power Apps: Button formula example:
 // Flow
 Set(varResult,
 AssetMgmt_CreateRequest.Run(
 ThisItem.ID, // AssetId
 User.Email // RequesterEmail
 )
 );
 If(varResult.Status = "Success",
 Notify("!", NotificationType.Success),
 Notify(varResult.Message, NotificationType.Error)
 );
```

#### Flow Operating Power Apps Data

```
# Power Apps Dataverse SharePoint

: Power Apps → SharePoint ← Flow
 ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
 │ Power Apps │─────→│ SharePoint │←─────│ Power Automate│
 │ │ │ │ │ │
 │ │ │ Service Requests │ │ │
 └──────────────┘ └──────────────┘ └──────────────┘
```

### Custom Connector Development

#### When to Build Custom Connectors

```
 - REST API
 - SaaS
 - Flow API

 - → HTTP DLP
```

#### Creating a Custom Connector

```
 1: OpenAPI/Swagger
 make.powerautomate.com → → → OpenAPI
 swagger.json →

 1. : URL
 2. : API Key / OAuth 2.0 / Basic Auth
 3. : API endpoint

 Authentication Types:
 ┌─────────────────┬──────────────────────────────┐
 │ / Method │ / Use Case │
 ├─────────────────┼──────────────────────────────┤
 │ No Auth │ API │
 │ API Key │ API │
 │ Basic Auth │ │
 │ OAuth 2.0 │ Microsoft GraphGoogle │
 │ Microsoft Entra │ API │
 └─────────────────┴──────────────────────────────┘
```

> Custom connectors may be blocked by DLP policies. Check your environment policies first.

### RPA / Desktop Flows & RPA

#### Desktop Flows Overview

Desktop flows automate **local desktop application** operations — traditional RPA.

```
 Run Modes:
 ┌────────────────┬─────────────────────────────────┐
 │ │ │
 │ Attended │ Runs while user is logged in │
 ├────────────────┼─────────────────────────────────┤
 │ │ │
 │ Unattended │ Runs in background (dedicated VM) │
 └────────────────┴─────────────────────────────────┘

  Toolchain:
  Power Automate Desktop (PAD)
```

#### RPA Scenario Examples

```
  ├── OCR scan (PAD OCR)
  ├── Extract to Excel
  ├── Upload to SharePoint

  ├── Generate report → PDF
  ├── PAD Excel → SharePoint upload
  └── Archive PDF → SharePoint

  ├── PAD data scraping (via API)
  ├── Export to CSV
  └── Upload CSV → SharePoint
```

### Dataverse Integration Patterns

#### When to Migrate from SP to Dataverse

| Dimension | SharePoint Lists | Dataverse |
|---|---|---|
| Capacity | ≤ 30M items, <5000 view threshold | Unlimited rows |
| Relational | Lookup columns only | Full relational model |
| Transactions | No native support | Built-in transactions |
| Security | Site + list permissions | Row-level security (RLS) |
| Throttling | 5000 items API limit | Higher throughput |
| Offline | No | Power Apps offline |
| License | M365 included | Automate Premium required |

#### Dataverse Triggers

```
# "When a row is added, modified, or deleted" trigger
# More reliable than SharePoint webhook triggers

  Table: Asset Inventory
  Change type: Added, Modified, Deleted
  Scope: Organization / Business Unit / User
  Filter rows: Status eq 'Available'
  Select columns: toolid, title, status
```

### Governance & CoE Toolkit

#### Center of Excellence (CoE) Starter Kit

 Power Platform Flow/App
Microsoft's official governance toolkit for Power Platform — discover, clean up, and audit.

```
CoE: Core Components:
 ┌────────────────────────────┐
 │ 1. (Core) │ → Flow/App
 ├────────────────────────────┤
 │ 2. (Governance) │ → Flow DLP
 ├────────────────────────────┤
 │ 3. (Nurture) │ → Maker
 ├────────────────────────────┤
 │ 4. (Audit) │ → Flow
 └────────────────────────────┘

: https://aka.ms/CoEStarterKit
```

#### Power Automate Management Connector

```
# Flow Flow —
# Manage Flows with Flows — meta-programming

 Available Actions:
 - (List My Flows)
 - (Get Flow)
 - (Get Flow Runs)
 - (Create Flow)
 - (Edit Flow)
 - / (Enable/Disable Flow)
 - (Delete Flow)

# Example: Daily check for failing Flows and alert

 ( 9:00):
 ├── → Flow
 ├── Apply to each:
 │ ├── (24, Status=Failed)
 │ └── : > 3?
 │ └── : failedFlows
 └── : failedFlows ?
 └── : (Teams/Email)
```

#### Environment Strategy

```
 Recommended Environment Structure:
 ┌──────────────────────────────────────────┐
 │ Default ( DLP) │
 │ → │
 │ → │
 ├──────────────────────────────────────────┤
 │ Project-Dev │
 │ → Lab Manager │
 │ → & │
 ├──────────────────────────────────────────┤
 │ Project-Prod │
 │ → │
 │ → │
 └──────────────────────────────────────────┘
```

---

## Appendix C: Cookbook Recipes

### Approval Auto-Escalation

**Scenario**: Approval not responded within 24h, auto-escalate to manager.

```
: Service Requests
 │
 ├── (Create an approval) —
 │ :
 │
 ├── Do until: or( isResponded, escalationCount >= 2)
 │ │
 │ ├── 24
 │ │
 │ ├── (Wait for an approval, timeout 1)
 │ │
 │ └── : ?
 │ ├── : Set isResponded = true
 │ └── :
 │ ├── escalationCount++
 │ ├── (O365 Users → Get manager)
 │ ├──
 │ └── Teams : ""
 │
 └── ApprovalStatus
```

### Daily Overdue Tool Reminder

```
: 09:00
 │
 ├── Get items (Service Requests):
 │ Filter: ApprovalStatus eq 'Approved'
 │
 ├── Filter array:
 │ Where: StartDate < addDays(utcNow, -7)
 │ ← 7
 │
 ├── : ?
 │ │
 │ └── :
 │ ├── Apply to each :
 │ │ └── :
 │ │ " {AssetName} 7 "
 │ │
 │ └── HTML →
 │ " {length} ..."
 │
 └── (: )
```

### Weekly Asset Management Statistics

```
: 09:00
 │
 ├── 7 Service Requests
 │ Filter: Created gt '@{addDays(utcNow, -7)}'
 │
 ├── Statistics:
 │ ├── Compose_Total: length(body('Get_items')?['value'])
 │ ├── Filter_Approved → Compose_ApprovedCount
 │ ├── Filter_Rejected → Compose_RejectedCount
 │ └── Filter_Returned → Compose_ReturnedCount
 │
 ├── Select: Top 5
 │ ( AssetName )
 │
 ├── HTML :
 │
 └── :
 : "📊 - {formatDateTime(utcNow, 'MM/dd')}"
 " {Total}
 {Approved} | {Rejected} | {Returned}
 : {Top5Table}
 : {DetailTable}"
```

### Data Consistency Auto-Fix

 Asset Inventory Service Requests

```
: 02:00
 │
 ├── Get items: Asset Inventory (Status = 'In use')
 │
 ├── Apply to each (=1):
 │ │
 │ ├── Get items: Service Requests
 │ │ Filter: AssetId eq {ID}
 │ │ and ApprovalStatus eq 'Approved'
 │ │
 │ └── : ?
 │ │
 │ └── (!):
 │ ├── Asset Inventory: Status → Available
 │ ├── : FlowRunLog
 │ └── :
 │ "⚠️ : {AssetName} In use Available
 │ : "
 │
 └── : {count}
```

### One-Click Borrow with Adaptive Card

```

: 08:30
 │
 ├── Get items: Asset Inventory (Status = 'Available')
 │
 ├── Select: Adaptive Card
 │ Map: { "title": item?['Title'], "id": item?['ID'] }
 │
 ├── Compose: Adaptive Card JSON
 │ ( + "" )
 │
 └── Teams: Adaptive Card
 → data.toolId
 → ChildFlow_BorrowTool(toolId, responderEmail)
```

---

## Appendix B: Quick Reference Card

### Common Expression Cheat Sheet

```
# Current time
utcNow

# Local time (example: Pacific Standard Time)
convertFromUtc(utcNow(), 'Pacific Standard Time')

# 7 days later
addDays(utcNow, 7)

# Concat title
concat('Borrow - ', triggerBody?['Title'])

# Conditional value
if(equals(body('Get_item')?['Status']?['Value'], 'Available'), 'Yes', 'No')

# People column Claims
concat('i:0#.f|membership|', triggerBody?['headers']?['x-ms-user-email'])

# Null check
coalesce(triggerBody?['Description'], ' / No description')

# Array length
length(body('Get_items')?['value'])

# Format date
formatDateTime(utcNow, 'yyyy-MM-dd HH:mm:ss')
```

---

> ✏️ Maintainer: kylehuang0323-ai
