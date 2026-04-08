---
applyTo: "docs/03-connectors.md,docs/12-dlp-policies.md"
---

# SharePoint & DLP Rules

When working with SharePoint connectors and DLP policies:

- Use OData `$filter` with delegable operators (`eq`, `ne`, `gt`, `lt`, `startswith`) for large lists
- Always use indexed columns in filter queries for lists with >5,000 items
- Use `$select` to return only needed columns — reduces payload and improves performance
- Use `$expand` to resolve lookup/person columns in a single request
- SharePoint "Send an HTTP request to SharePoint" is part of the SharePoint connector (Business DLP group)
- The standalone HTTP connector is blocked in most enterprise environments
- All connectors in a flow must be in the same DLP group — Business or Non-Business
