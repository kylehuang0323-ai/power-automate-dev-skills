## Troubleshooting FAQ

### People column write fails

**Cause**: SharePoint People columns require Claims format
**Solution**:
```
# Claims format
concat('i:0#.f|membership|', <email>)

# If new SP supports Email directly
# Just use email address
```

### Value casing in trigger conditions

**Symptom**: Flow trigger condition not working
**Solution**: Try `Value` (uppercase) first(), then `value` (lowercase), or use in-flow conditions instead

### Can't access loop variable

**Solution**: `items('Apply_to_each')?['fieldName']`

### Old instances still running after modification

**Solution**: Go to Flow → Turn off → Cancel all running instances → Turn on again

### "Item or list not found" error

**Investigation**:
1. Check site URL spelling
2. Check list name (use internal column name)
3. Verify ID value is valid
4. Check connection account permissions

### Expression returns null

**Common causes**:
```
# Wrong property path
triggerBody?['Status']?['Value'] # ✅ ?['Value']
triggerBody?['Status'] # ❌

# Null-safe access
triggerBody?['Field'] # ✅ ?[] null
triggerBody['Field'] # ❌ Field

# Dynamic content vs Expression
```

### How to handle concurrency conflicts

**Scenario**: Multiple Flow instances updating the same item simultaneously
**Solution**:
1. Set trigger concurrency to 1
2. Re-read status before update (optimistic lock)
3. Use SP list versioning

### How to test auto-triggered Flows

1. Convert to instant flow to test logic first
2. Create dedicated test data
3. Expand trigger in run history
4. **Add debug Compose**: Add Compose actions at key points to output variable values

### Flow blocked by DLP policy

**Symptom**: "Blocked by Data Loss Prevention policy" error
**Cause**: Flow uses connectors from different DLP groups
**Solution**:
1. Check error details for conflicting connectors
2. Replace with same-group connector (e.g., Outlook instead of SMTP)
3. Or split into multiple Flows per group
4. Contact IT admin (`Power Platform Admin Center → Data policies`)

### HTTP connector blocked

**Symptom**: Cannot save or run Flow using HTTP connector
**Solution**:
```
# Alternative priority:
1. Use SharePoint "Send an HTTP request" action — calls SP REST API ✅
2. Use Dataverse or SQL Server native connector ✅
3. Request DLP exception from IT admin ⚠️
4. Request dedicated environment with custom DLP ⚠️
```

---
