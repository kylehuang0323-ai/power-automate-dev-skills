## Common Connectors

### SharePoint

| Action | Purpose | Key Parameters |
|---|---|---|
| (Get item) | Read a single item | Site, List, Id |
| (Get items) | Query multiple items() | Site, List, Filter Query, Top Count |
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
