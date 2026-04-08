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
