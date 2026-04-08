## Best Practices

### Naming Convention

```
# Flow naming
AssetMgmt_CreateRequest
AssetMgmt_RejectedRollback
AssetMgmt_ReturnedRollback
AssetMgmt_Approval

# Action naming pattern: [Verb]_[Target]_[Detail]
Get_ToolInventory_ById
Update_ToolStatus_ToInUse
Create_BorrowRequest
Check_ToolAvailability
Send_RejectionEmail
```

> Always rename actions — defaults like "Get item 2" are hard to debug

### Architecture Design

1. **Single responsibility per Flow**
   - ✅ One Flow handles one business process (e.g., create request only)
   - ❌ One Flow handles create, approve, reject, return all together

2. **Concurrency control**: Enable concurrency control (parallelism=1) for read-then-write scenarios

3. **Trigger filtering**: Add trigger conditions to exclude self-modifications when using "on modified" triggers

4. **Idempotency**: Design for idempotency — operations should be safe to repeat

### Security & Compliance

- **Connection permissions**: Flow connections run with the creator's permissions
- **DLP compliance**: Ensure all connectors are in the same DLP group
- **Secure I/O**: Use "Secure Inputs/Outputs" to hide sensitive data in steps
- **Environment variables**: Use environment variables for URLs, emails, and other config

### Maintenance Tips

- Regularly check run history for failure rates
- Set up failure notifications for critical Flows
- Export Flow definitions as backups
- Document business logic and dependencies

---
