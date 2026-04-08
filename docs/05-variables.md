## Variables & Data Operations

### Variable Types

| Type | Description | Init Example |
|---|---|---|
| String | Text | `""` `"default value"` |
| Integer | Whole number | `0` |
| Float | Decimal | `0.0` |
| Boolean | True/False | `false` |
| Array | List | `[]` |
| Object | Key-value | `{}` |

### Variable Actions

| Action | Description |
|---|---|
| (Initialize variable) | Declare at top level |
| (Set variable) | Overwrite variable value |
| (Append to string variable) | Append text |
| (Append to array variable) | Append element |
| (Increment variable) | Add to number |
| (Decrement variable) | Subtract from number |

> ⚠️ **Top-level only**: Initialize variable must be at top level, not inside conditions, loops, or scopes

### Data Operations

| Action | Purpose |
|---|---|
| (Compose) | Build any value, works as temp variable |
| JSON (Parse JSON) | Parse JSON string into dynamic content |
| CSV (Create CSV table) | Array to CSV |
| HTML (Create HTML table) | Array to HTML table |
| (Filter array) | Filter array by condition |
| (Select) | Map array fields |
| (Join) | Join array to string() |

> 💡 **Tip**: `Compose` is more flexible than variables — no top-level restriction, works as a lightweight temp variable

---
