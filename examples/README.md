# 📦 Importable Flow Examples

Ready-to-use Power Automate flow definitions that you can import directly into your environment.

## Available Examples

| Example | Scenario | Patterns Demonstrated |
|---------|----------|----------------------|
| [SharePoint Approval](sharepoint-approval/) | Item selection → lock → approval → rollback | Concurrency control, Scope error handling, Saga rollback |
| [Error Handling Saga](error-handling-saga/) | Multi-step operation with compensation | Try-Catch-Finally, Saga compensation pattern |
| [Teams Adaptive Card](teams-adaptive-card/) | Approval via Teams rich card | Adaptive Cards, Approvals connector, conditional update |

## How to Import

### Option 1: Dataverse Solution Import (Recommended)

1. Open [Power Automate](https://make.powerautomate.com)
2. Left menu → **Solutions**
3. **Import solution** → Browse → Select `*_solution.zip`
4. Configure connections when prompted → **Import**
5. Open the solution → Turn on each flow

### Option 2: Paste JSON Definition

1. Create a new flow of the matching type (Instant / Automated)
2. In the designer, switch to **Code View** (`</>`)
3. Replace content with the `flow-definition.json` content
4. Switch back to Designer → Configure connections → **Save**

## ⚠️ After Import Checklist

- [ ] Update **Site Address** to your SharePoint site URL
- [ ] Update **List Name** to match your actual list names
- [ ] Verify column **internal names** match (use REST API to check)
- [ ] Select your **SharePoint connection** for each step
- [ ] For approval flows: update the **Assigned To** email
- [ ] Test with a sample item before enabling for production

## Customization

Each example includes a `README.md` explaining:
- The business scenario
- Flow architecture diagram
- Which parameters to customize
- Common modifications
