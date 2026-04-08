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
| | 8,192 | Max expression length() |
| SharePoint Get items() | 5,000 | Max items returned |

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
