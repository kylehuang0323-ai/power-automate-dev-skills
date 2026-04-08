# Power Automate Connectors

Connectors are the bridges between Power Automate and external services. There are over 1,000 connectors available.

## Connector Categories

### Standard Connectors

Available to all users with a Microsoft 365 or Power Automate license.

| Connector | Common Use Cases |
|-----------|-----------------|
| SharePoint | List management, file operations, approvals |
| Office 365 Outlook | Send emails, manage calendar, create contacts |
| Microsoft Teams | Post messages, create meetings, manage channels |
| OneDrive for Business | File storage, create/update files |
| Microsoft Forms | Form submissions, response retrieval |
| Excel Online (Business) | Read/write Excel tables, manage workbooks |
| Approvals | Start approval processes, wait for outcomes |
| Notifications | Send mobile push notifications |
| RSS | Subscribe to RSS/Atom feeds |
| MSN Weather | Current conditions, forecasts |

### Premium Connectors

Require a Power Automate Premium, Power Apps Premium, or Microsoft 365 E3/E5 license.

| Connector | Common Use Cases |
|-----------|-----------------|
| HTTP | Call any REST API endpoint |
| SQL Server | Query and update SQL databases |
| Azure Service Bus | Asynchronous messaging |
| Azure Blob Storage | Large file and binary data storage |
| Azure Key Vault | Retrieve secrets and certificates |
| Salesforce | CRM data sync and automation |
| Dynamics 365 | ERP/CRM integration |
| Adobe Sign | E-signature workflows |
| DocuSign | E-signature workflows |
| Twilio | SMS and voice messaging |
| SendGrid | Transactional email |
| Stripe | Payment processing |

### Custom Connectors

Built by developers to connect to any REST/SOAP API not covered by built-in connectors.

**When to build a custom connector:**
- Your organization has an internal API
- A third-party service is not available as a built-in connector
- You need to wrap multiple API calls into a single action for end-users

**Requirements:**
- API must have a Swagger (OpenAPI 2.0) or OpenAPI 3.0 definition (or you can create one manually)
- API must be accessible over HTTPS (or on-premises via data gateway)
- Premium license required to use custom connectors

## Connector Authentication Types

| Auth Type | Description | When to Use |
|-----------|-------------|-------------|
| No Auth | Public endpoint, no authentication | Public read-only APIs |
| Basic | Username + password in header | Legacy APIs |
| API Key | Static key in header or query string | Most SaaS APIs |
| OAuth 2.0 | Token-based, supports refresh | Modern APIs, Microsoft services |
| Windows Auth | Integrated Windows authentication | On-premises services |
| Client Credentials (OAuth) | Service-to-service OAuth | Automated flows (no user context) |

## On-Premises Data Gateway

The on-premises data gateway allows Power Automate to connect to data sources within your organization's network.

**Supported connectors with on-premises gateway:**
- SQL Server
- Oracle Database
- File System
- SharePoint (on-premises)
- HTTP with On-Premises Data Gateway
- SAP ERP

**Setup steps:**
1. Download and install the gateway on a server inside your network
2. Register the gateway with your Azure subscription
3. In Power Automate, create a connection using the connector and select the gateway

## Connection Management

### Creating Connections

Connections store the authentication credentials for a connector. Each connector needs at least one connection.

**Best practices:**
- Use service accounts (not personal accounts) for production flows
- Name connections descriptively (e.g., "SharePoint - Production - Service Account")
- Rotate credentials regularly and update the connection
- Use Azure Key Vault connector to retrieve secrets dynamically

### Sharing Connections

- Connections are tied to the creator's identity by default
- For flows in solutions, use **connection references** to decouple the flow from specific connections
- When sharing a flow, others may need to create their own connections

## Connector Throttling and Limits

Each connector has limits on how many calls can be made per minute/day.

| Scenario | Limit |
|----------|-------|
| SharePoint Get Items | 600 calls / 60 seconds |
| Office 365 Outlook Send Email | 300 calls / 60 seconds |
| HTTP action | 100,000 calls / 24 hours (Premium plan) |
| Dataverse (per flow) | 6,000 API calls / 5 minutes |

**Handling throttling:**
- Configure retry policies on HTTP actions (exponential backoff)
- Use `Filter Query` and `Top Count` to minimize API calls
- Batch operations where supported
- Spread scheduled flows across different times

## Finding Connectors

- [Full Connector Reference](https://docs.microsoft.com/en-us/connectors/)
- Filter by: Standard vs. Premium, category, certification status
- In Power Automate Studio: Search by connector name when adding an action
