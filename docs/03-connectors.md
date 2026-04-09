## Common Connectors

### SharePoint

| Action | operationId | Purpose | Key Parameters |
|--------|-------------|---------|----------------|
| Get item | `GetItem` | Read a single item | Site, List, Id |
| Get items | `GetItems` | Query multiple items | Site, List, Filter Query, Top Count, Order By, Select |
| Create item | `PostItem` | Create a new item | Site, List, column fields |
| Update item | `PatchItem` | Update an item | Site, List, Id, fields to update |
| Delete item | `DeleteItem` | Delete an item | Site, List, Id |
| Send HTTP request | `HttpRequest` | Call SP REST API | Site, Method, URI, Headers, Body |

**Parameter Details:**

| Parameter | Required | Notes |
|-----------|----------|-------|
| `dataset` (Site Address) | ✅ | Full URL: `https://tenant.sharepoint.com/sites/SiteName` |
| `table` (List Name) | ✅ | Display name or GUID. If renamed, use internal name |
| `id` | ✅ (Get/Update/Delete) | Integer item ID |
| `$filter` (Filter Query) | Optional | OData filter expression |
| `$top` (Top Count) | Optional | Max items to return (default 100, max 5000) |
| `$orderby` (Order By) | Optional | `ColumnName asc` or `ColumnName desc` |
| `$select` (Select Columns) | Optional | Comma-separated column internal names — improves performance |

**SharePoint Filter Query Examples:**

```
Status eq 'Available'
AssetId eq 42
Title ne 'Test'
Status eq 'In use' and Category eq 'Electronics'
startswith(Title, 'Drill')
Modified gt '2024-01-01T00:00:00Z'
substringof('keyword', Title)
```

**Send HTTP Request to SharePoint (HTTP alternative):**

> Use this instead of the blocked HTTP connector for SharePoint API calls.

```
Site: https://tenant.sharepoint.com/sites/SiteName
Method: GET
URI: _api/web/lists/getbytitle('ListName')/items?$select=Title,Id&$filter=Status eq 'Active'&$top=50
Headers:
  Accept: application/json;odata=verbose
  Content-Type: application/json;odata=verbose
```

Common REST endpoints:

| Endpoint | Purpose |
|----------|---------|
| `_api/web/lists/getbytitle('{List}')/items` | Get/create items |
| `_api/web/lists/getbytitle('{List}')/items({Id})` | Get/update/delete single item |
| `_api/web/lists/getbytitle('{List}')/fields` | Discover column internal names |
| `_api/web/siteusers` | Get site users |
| `_api/search/query?querytext='{keyword}'` | Search site content |

### Dataverse

| Action | Purpose | Key Parameters |
|--------|---------|----------------|
| List rows | Query table rows with OData | Table name, Filter, Select, Expand, Order By, Row count |
| Get a row by ID | Read a single row | Table name, Row ID, Select columns |
| Add a new row | Create a row | Table name, column values |
| Update a row | Update existing row | Table name, Row ID, column values |
| Delete a row | Delete a row | Table name, Row ID |
| Perform a bound action | Execute table-specific actions | Table name, Action name, parameters |
| Perform an unbound action | Execute global actions | Action name, parameters |

**Dataverse vs SharePoint — When to use which:**

| Criteria | SharePoint List | Dataverse Table |
|----------|----------------|-----------------|
| Max items | 30M (but 5K threshold) | Millions (enterprise scale) |
| Relationships | Lookup columns (limited) | Full relational (1:N, N:N) |
| Calculated fields | Basic | Advanced (rollup, calculated, formula) |
| Security | List/item level | Row-level, field-level, business unit |
| File storage | Document libraries | File/Image columns |
| Use case | Team collaboration | Business applications |

### Microsoft Teams

| Action | Purpose | Key Parameters |
|--------|---------|----------------|
| Post message in a chat or channel | Send a text message | Location (Channel/Chat), Team/Channel or Recipient, Message |
| Post adaptive card in a chat or channel | Send rich interactive card | Location, Recipient, Adaptive Card JSON |
| Post adaptive card and wait for response | Send card + wait for user input | Location, Recipient, Card JSON, Update message |
| Get @mentions for a user | Get user mention token | User UPN |
| List channels | Get team channels | Team ID |

**Adaptive Card JSON (inline in Flow):**

```json
{
  "type": "AdaptiveCard",
  "version": "1.4",
  "body": [
    { "type": "TextBlock", "text": "${title}", "weight": "Bolder", "size": "Medium" },
    { "type": "FactSet", "facts": [
      { "title": "Status:", "value": "${status}" },
      { "title": "Date:", "value": "${date}" }
    ]}
  ],
  "actions": [
    { "type": "Action.Submit", "title": "Approve", "data": { "action": "approve" } },
    { "type": "Action.Submit", "title": "Reject", "data": { "action": "reject" } }
  ],
  "$schema": "http://adaptivecards.io/schemas/adaptive-card.json"
}
```

### Approvals

| Action | Purpose |
|--------|---------|
| Start and wait for an approval | Send approval request, pause until response received |
| Create an approval | Create without waiting (use with "Wait for an approval") |
| Wait for an approval | Wait for a previously created approval |

**Approval Types:**

| Type | Description |
|------|-------------|
| Basic — Approve/Reject, First to respond | Any one approver can decide |
| Basic — Approve/Reject, Everyone must approve | All approvers must approve |
| Custom Responses — Wait for one response | One response from custom options |
| Custom Responses — Wait for all responses | All must respond with custom options |

### Office 365 Outlook

| Action | Purpose | Key Parameters |
|--------|---------|----------------|
| Send an email (V2) | Send email with HTML body | To, Subject, Body, CC, BCC, Attachments |
| Get email (V2) | Read a specific email | Message ID |
| Get emails (V2) | List emails with filter | Folder, Filter, Top, Order By |
| Reply to an email (V2) | Reply to a message | Message ID, Comment, Reply All |
| Create event (V4) | Create calendar event | Subject, Start, End, Attendees |
| Send email with options | Email with voting buttons | Options, Subject, Body |

### Office 365 Users

| Action | Purpose |
|--------|---------|
| Get user profile (V2) | Get user info by UPN or email |
| Get my profile (V2) | Get current user info |
| Search for users (V2) | Search by name/email in directory |
| Get manager (V2) | Get a user's manager |
| Get direct reports (V2) | Get a user's direct reports |

### HTTP (Often Blocked by DLP)

| Action | Purpose | DLP Status |
|--------|---------|------------|
| HTTP | Call any REST API | ⛔ Often blocked |
| HTTP + Swagger | Call based on OpenAPI spec | ⛔ Often blocked |
| HTTP Webhook | Register/deregister webhook | ⛔ Often blocked |
| HTTP with Azure AD | Call API with AAD auth | ✅ Usually allowed |

**When HTTP is blocked, use these alternatives:**

| Need | Alternative |
|------|-------------|
| Call SharePoint API | SharePoint → Send an HTTP request to SharePoint |
| Call Dataverse API | Dataverse → Perform an unbound action |
| Call Graph API | Office 365 connectors OR HTTP with Azure AD |
| Call external API | Custom connector (if DLP allows) OR Azure Function relay |

---
