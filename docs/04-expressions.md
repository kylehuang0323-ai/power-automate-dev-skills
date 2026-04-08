## Expressions & Functions Reference

### String Functions

| Function | Description | Example |
|---|---|---|
| `concat(str1, str2, ...)` | Concatenate strings | `concat('Borrow - ', triggerBody ?['Title'])` → `Borrow - Drill` |
| `substring(str, start, length)` | Extract substring() | `substring('Hello World', 6, 5)` → `World` |
| `replace(str, old, new)` | Replace | `replace('2024-01-01', '-', '/')` → `2024/01/01` |
| `split(str, delimiter)` | Split into array | `split('a,b,c', ',')` → `["a","b","c"]` |
| `trim(str)` | Trim whitespace | `trim(' hello ')` → `hello` |
| `toLower(str)` | To lowercase | `toLower('HELLO')` → `hello` |
| `toUpper(str)` | To uppercase | `toUpper('hello')` → `HELLO` |
| `length(str)` | String length() | `length('hello')` → `5` |
| `indexOf(str, search)` | Find position | `indexOf('hello world', 'world')` → `6` |
| `startsWith(str, prefix)` | Starts with | `startsWith('Hello', 'He')` → `true` |
| `endsWith(str, suffix)` | Ends with | `endsWith('file.pdf', '.pdf')` → `true` |
| `contains(str, search)` | Contains | `contains('Hello World', 'World')` → `true` |

### Date & Time Functions

| Function | Description | Example |
|---|---|---|
| `utcNow()` | Current UTC time | `2024-03-15T08:30:00Z` |
| `utcNow('yyyy-MM-dd')` | Format current time | `2024-03-15` |
| `addDays(timestamp, days)` | Add days | `addDays(utcNow(), 7)` → 7 |
| `addHours(timestamp, hours)` | Add hours | `addHours(utcNow(), 8)` → 8 |
| `addMinutes(timestamp, mins)` | Add minutes | `addMinutes(utcNow(), 30)` |
| `subtractFromTime(ts, interval, unit)` | Subtract time | `subtractFromTime(utcNow(), 1, 'Day')` |
| `formatDateTime(ts, format)` | Format date | `formatDateTime(utcNow(), 'yyyyMMdd')` |
| `convertFromUtc(ts, timezone)` | Convert from UTC | `convertFromUtc(utcNow(), 'China Standard Time')` |
| `convertToUtc(ts, timezone)` | Convert to UTC | `convertToUtc('2024-03-15 16:30', 'China Standard Time')` |
| `ticks(timestamp)` | Convert to ticks | For precise comparison |
| `dateDifference(end, start)` | Time difference | `2.05:30:00` |

**Common Date Formats:**

| Format | Output |
|---|---|
| `yyyy-MM-dd` | `2024-03-15` |
| `yyyy-MM-ddTHH:mm:ssZ` | `2024-03-15T08:30:00Z` |
| `yyyyMMddHH:mm` | `2024031508:30` |
| `dddd, MMMM dd, yyyy` | `Friday, March 15, 2024` |
| `MM/dd/yyyy hh:mm tt` | `03/15/2024 08:30 AM` |

### Logical Functions

| Function | Description | Example |
|---|---|---|
| `equals(val1, val2)` | Equal check | `equals(1, 1)` → `true` |
| `not(expression)` | Negate | `not(equals(1, 2))` → `true` |
| `and(expr1, expr2)` | AND | `and(equals(a,1), equals(b,2))` |
| `or(expr1, expr2)` | OR | `or(equals(a,1), equals(a,2))` |
| `if(condition, trueVal, falseVal)` | Ternary | `if(equals(status,'Available'), 'Yes', 'No')` |
| `greater(val1, val2)` | Greater than | `greater(10, 5)` → `true` |
| `less(val1, val2)` | Less than | `less(3, 5)` → `true` |
| `greaterOrEquals(val1, val2)` | >= | `greaterOrEquals(5, 5)` → `true` |
| `lessOrEquals(val1, val2)` | <= | `lessOrEquals(3, 5)` → `true` |
| `empty(value)` | Is empty() | `empty(null)` → `true`; `empty('')` → `true` |
| `coalesce(val1, val2, ...)` | First non-null | `coalesce(null, '', 'default')` → `''` |

### Collection & Array Functions

| Function | Description | Example |
|---|---|---|
| `length(array)` | Array length() | `length(body('Get_items')?['value'])` |
| `first(array)` | First element | `first(variables('myArray'))` |
| `last(array)` | Last element | `last(variables('myArray'))` |
| `contains(array, item)` | Array contains() | `contains(createArray('a','b'), 'a')` → `true` |
| `union(arr1, arr2)` | Union | `union(createArray(1,2), createArray(2,3))` → `[1,2,3]` |
| `intersection(arr1, arr2)` | Intersection | `intersection(createArray(1,2,3), createArray(2,3,4))` → `[2,3]` |
| `createArray(v1, v2, ...)` | Create array | `createArray('a', 'b', 'c')` |
| `join(array, delimiter)` | Join | `join(createArray('a','b'), ', ')` → `a, b` |

### Type Conversion Functions

| Function | Description |
|---|---|
| `int(value)` | To integer |
| `float(value)` | To float() |
| `string(value)` | To string() |
| `bool(value)` | To boolean |
| `json(value)` | To JSON object |
| `base64(value)` | Base64 encode |
| `base64ToString(value)` | Base64 decode |
| `decodeUriComponent(str)` | URI decode |
| `encodeUriComponent(str)` | URI encode |

### Reference Functions

| Function | Description |
|---|---|
| `triggerBody()` | Trigger output body() |
| `triggerOutputs ` | Trigger full outputs() |
| `body('actionName')` | Specific action output body() |
| `outputs('actionName')` | Specific action full outputs() |
| `actions('actionName')` | Action info including status |
| `result('scopeName')` | Array of all action results in scope |
| `items('Apply_to_each')` | Current item in loop |
| `variables('varName')` | Get variable value |
| `workflow()` | Current Flow metadata |
| `parameters('paramName')` | Flow parameter value |

### SharePoint People Column Claims Format

```
# Standard format
i:0#.f|membership|user@domain.com

# Build in expression
concat('i:0#.f|membership|', triggerBody?['headers']?['x-ms-user-email'])
```

---
