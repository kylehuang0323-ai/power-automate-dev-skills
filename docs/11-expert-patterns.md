## Expert-Level Development

> 🔥 This chapter covers advanced architecture patterns, complex expression techniques, child flow orchestration, JSON manipulation, Solution management, CI/CD, and enterprise production practices.

### Child Flows & Modular Architecture

#### Why Child Flows

| Problem | Child Flow Solution |
|---|---|
| Flow exceeds 500 actions | Split into child flows, each ≤100 actions |
| Duplicate logic across Flows | Extract to shared child flow, maintain once |
| Complex orchestration | Parent orchestrates, children execute |
| Team collaboration | Different teams own their child flows |

#### Creating a Child Flow

```
Child Flow Requirements:
1. Must be created inside a Solution
2. Trigger: "Manually trigger a flow"
3. Response: "Respond to a PowerApp or flow"
4. Parent & child must be in the same environment
```

**Defining Input Parameters:**

```json
// Trigger → Add an input
{
  "type": "object",
  "properties": {
    "AssetId": { "type": "integer", "description": "Asset ID" },
    "AssetName": { "type": "string", "description": "Asset name" },
    "RequesterEmail": { "type": "string", "description": "Requester email" },
    "Action": { "type": "string", "description": "Action type: Borrow | Return | Reject" }
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
 '","timestamp":"', utcNow(), '"}'
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

# 4. Advanced sorting — Select + sortBy (use Office Script or Compose workaround)
# Power Automate sorting options:
# a) Use Office Script for complex sorting
# b) Use SharePoint Get items with OData $orderby
# c) Use Select + Compose for simple reordering

# Array aggregation — sum
# Use Apply to each + increment variable
length(body('Filter_array'))  // Count of filtered items
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
# Use ?[] operator to prevent null reference errors
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
# Build mapping object with Compose
Compose_FieldMap:
{
 "Status": "@{body('Get_item')?['Status']?['Value']}",
 "Category": "@{body('Get_item')?['Category']?['Value']}",
 "Priority": "@{body('Get_item')?['Priority']?['Value']}"
}
# Parse and access dynamically by field name
# Then parse with json and access by variable
json(outputs('Compose_FieldMap'))?[variables('fieldName')]

# xpath extraction (most universal approach)
# Convert JSON to XML, then use xpath to extract value
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
 └── (Loop continues)

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
 │ ├── "429" (Throttled):
 │ │ → / Delay and retry
 │ ├── "404" (Not found):
 │ │ → / Log and skip
 │ ├── "401/403" (Permission):
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
 Body: (Batch request body)
 ← 1 API call for 100 items() 
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
 1: ... formatDateTime(utcNow(), 'yyyy-MM-dd') ...
 2: ... formatDateTime(utcNow(), 'yyyy-MM-dd') ... ←
 3: ... formatDateTime(utcNow(), 'yyyy-MM-dd') ...

# Compute once, reference many times
Compose_TodayDate: formatDateTime(utcNow(), 'yyyy-MM-dd')
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

**Azure DevOps Pipeline:**

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

**GitHub Actions Pipeline:**

```yaml
# .github/workflows/deploy-solution.yml
name: Deploy Power Automate Solution

on:
  push:
    branches: [main]
    paths: ['src/AssetMgmtSolution/**']
  workflow_dispatch:
    inputs:
      target_env:
        description: 'Target environment'
        required: true
        default: 'test'
        type: choice
        options: ['test', 'production']

env:
  SOLUTION_NAME: AssetMgmtSolution
  SOLUTION_FOLDER: src/AssetMgmtSolution

jobs:
  build:
    name: Pack Solution
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install PAC CLI
        uses: microsoft/powerplatform-actions/install-pac@v1

      - name: Pack Solution (Managed)
        uses: microsoft/powerplatform-actions/pack-solution@v1
        with:
          solution-folder: ${{ env.SOLUTION_FOLDER }}
          solution-file: ${{ runner.temp }}/${{ env.SOLUTION_NAME }}_managed.zip
          solution-type: Managed

      - name: Upload artifact
        uses: actions/upload-artifact@v4
        with:
          name: solution-package
          path: ${{ runner.temp }}/${{ env.SOLUTION_NAME }}_managed.zip

  deploy-test:
    name: Deploy to Test
    needs: build
    runs-on: ubuntu-latest
    environment: powerplatform-test
    steps:
      - name: Download artifact
        uses: actions/download-artifact@v4
        with:
          name: solution-package

      - name: Install PAC CLI
        uses: microsoft/powerplatform-actions/install-pac@v1

      - name: Authenticate
        uses: microsoft/powerplatform-actions/who-am-i@v1
        with:
          environment-url: ${{ secrets.TEST_ENV_URL }}
          app-id: ${{ secrets.CLIENT_ID }}
          client-secret: ${{ secrets.CLIENT_SECRET }}
          tenant-id: ${{ secrets.TENANT_ID }}

      - name: Import Solution
        uses: microsoft/powerplatform-actions/import-solution@v1
        with:
          environment-url: ${{ secrets.TEST_ENV_URL }}
          app-id: ${{ secrets.CLIENT_ID }}
          client-secret: ${{ secrets.CLIENT_SECRET }}
          tenant-id: ${{ secrets.TENANT_ID }}
          solution-file: ${{ env.SOLUTION_NAME }}_managed.zip
          force-overwrite: true
          activate-plugins: true

  deploy-prod:
    name: Deploy to Production
    needs: deploy-test
    runs-on: ubuntu-latest
    environment: powerplatform-prod
    if: github.event.inputs.target_env == 'production' || github.ref == 'refs/heads/main'
    steps:
      - name: Download artifact
        uses: actions/download-artifact@v4
        with:
          name: solution-package

      - name: Install PAC CLI
        uses: microsoft/powerplatform-actions/install-pac@v1

      - name: Import Solution
        uses: microsoft/powerplatform-actions/import-solution@v1
        with:
          environment-url: ${{ secrets.PROD_ENV_URL }}
          app-id: ${{ secrets.CLIENT_ID }}
          client-secret: ${{ secrets.CLIENT_SECRET }}
          tenant-id: ${{ secrets.TENANT_ID }}
          solution-file: ${{ env.SOLUTION_NAME }}_managed.zip
          force-overwrite: true
          activate-plugins: true
```

**Required GitHub Secrets:**

| Secret | Description |
|--------|-------------|
| `CLIENT_ID` | Azure AD App Registration Client ID |
| `CLIENT_SECRET` | Azure AD App Registration Secret |
| `TENANT_ID` | Azure AD Tenant ID |
| `TEST_ENV_URL` | Test environment URL (e.g., `https://org-test.crm.dynamics.com`) |
| `PROD_ENV_URL` | Production environment URL |

**GitHub Actions — Key Actions from `microsoft/powerplatform-actions`:**

| Action | Purpose |
|--------|---------|
| `install-pac` | Install Power Platform CLI |
| `who-am-i` | Authenticate + verify connection |
| `pack-solution` | Pack solution folder to .zip |
| `import-solution` | Import solution to environment |
| `export-solution` | Export solution from environment |
| `check-solution` | Run Solution Checker (lint) |
| `deploy-package` | Deploy Package Deployer package |

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
 - Duration: Number (dateDifference() )
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
