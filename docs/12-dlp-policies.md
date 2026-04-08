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
│ │ │ │ │ │ │ │
│ │ │ │ │ │ │ │
│ │ ✅ Same group OK │ │ ✅ Same group OK │ │ ❌ Cannot use │ │
│ │ │ │ │ │ │ │
│ │ │ │ │ │ in any Flow │ │
│ │ ❌ Cannot mix │ │ ❌ Cannot mix │ │ │ │
│ │ Non-Biz │ │ Business │ │ │ │
│ │ │ │ │ │ │ │
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
│ Tenant-Level Policy │
│ (Covers all environments, IT admin managed) │
│ │
│ ┌─────────────────────────────────────────┐ │
│ │ Environment-Level Policy │ │
│ │ (Additional restrictions per env) │ │
│ │ │ │
│ │ Example: │ │
│ │ • Default: standard restrictions │ │
│ │ • Dev: relaxed for testing │ │
│ │ • Production: strictest policies │ │
│ └─────────────────────────────────────────┘ │
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
| SharePoint | Get items(), Get item | Delete item |
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
│ 1. Identify conflicting connectors │
│ (Check which connectors conflict) │
└───────────┬───────────────────────────┘
 │
 ▼
┌───────────────────────────────────────┐
│ 2. Check connector DLP classification │
│ (Admin Center → Data policies) │
└───────────┬───────────────────────────┘
 │
 ▼
┌───────────────────────────────────────┐
│ 3. Choose a solution: │
│ │
│ a) Replace with same-group connector │
│ (e.g., Outlook instead of SMTP) │
│ │
│ b) Split into multiple Flows │
│ (one Flow per connector group) │
│ │
│ c) Contact IT admin to adjust DLP │
│ (request policy exception) │
│ │
│ d) Request a dedicated environment │
│ (with custom DLP policies) │
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
