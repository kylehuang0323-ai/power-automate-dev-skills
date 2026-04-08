# Power Automate Actions

Actions are the steps your flow performs after the trigger fires. Each action typically maps to an operation in a connector.

## Built-in Actions (No Connector Required)

These actions are always available and don't count against API quota.

### Control Actions

| Action | Description |
|--------|-------------|
| **Condition** | If/else branching based on a condition |
| **Switch** | Multi-case branching (like a switch/case statement) |
| **Apply to each** | Loop over every item in an array |
| **Do until** | Loop until a condition is true |
| **Scope** | Group actions for error handling or organization |
| **Terminate** | End the flow with Succeeded/Failed/Cancelled status |

### Data Operations

| Action | Description |
|--------|-------------|
| **Compose** | Evaluate and store an expression or value |
| **Parse JSON** | Parse a JSON string into a typed object |
| **Select** | Transform each item in an array |
| **Filter array** | Remove items from an array based on a condition |
| **Create HTML table** | Convert an array into an HTML table |
| **Create CSV table** | Convert an array into CSV format |
| **Join** | Join array elements into a single string |

### Variable Actions

| Action | Description |
|--------|-------------|
| **Initialize variable** | Declare a new variable |
| **Set variable** | Update a variable's value |
| **Increment variable** | Add to an integer variable |
| **Decrement variable** | Subtract from an integer variable |
| **Append to string variable** | Concatenate a value to a string variable |
| **Append to array variable** | Add an item to an array variable |

### Date/Time Actions

| Action | Description |
|--------|-------------|
| **Current time** | Returns the current UTC time |
| **Convert time zone** | Converts a timestamp between time zones |
| **Add to time** | Adds an interval to a timestamp |
| **Subtract from time** | Subtracts an interval from a timestamp |
| **Get future time** | Returns a future time relative to now |
| **Get past time** | Returns a past time relative to now |

## Key Action Concepts

### Dynamic Content

Every action produces outputs that can be referenced in subsequent actions. In the action input fields, click **Add dynamic content** to browse available outputs.

```
// Examples of dynamic content references
triggerBody()?['Subject']          // Email subject from trigger
body('Get_items')?['value']        // Array from SharePoint Get items
outputs('Compose')?['body']        // Output from a Compose action
```

### Action Configuration

Most actions have two sections:
- **Required fields** – Must be filled in
- **Advanced parameters** – Optional fields, click "Show advanced options" to expand

### Timeout Settings

Long-running actions can time out. Configure timeouts in **Settings** → **General** → **Timeout**:

```
// ISO 8601 duration format
PT30S   = 30 seconds
PT5M    = 5 minutes
PT1H    = 1 hour
P1D     = 1 day
```

Maximum timeout is **30 days** for approval actions, **30 minutes** for most other actions.

### Concurrency and Parallelism

- **Apply to each** – Enable concurrency in Settings to process items in parallel (max 50)
- **Parallel branches** – Add a branch at the same level to run actions simultaneously

## Common Action Patterns

### Condition Pattern

```
Condition: Is status equal to 'Approved'?
├── Yes (True branch):
│   └── Send approval email
└── No (False branch):
    └── Send rejection email
```

### Loop with Early Exit

```
Initialize variable: blnStopLoop = false

Do until: blnStopLoop equals true
├── Get next batch of items
├── Apply to each item:
│   └── Process item
└── Condition: Is there another page?
    ├── Yes: Continue loop (get next page token)
    └── No: Set blnStopLoop = true
```

### Parallel Processing Pattern

```
// Sequential (slow): ~60 seconds total
Action A (20s) → Action B (20s) → Action C (20s)

// Parallel (fast): ~20 seconds total
├── Branch 1: Action A (20s)
├── Branch 2: Action B (20s)
└── Branch 3: Action C (20s)
         ↓ (all complete)
    Final action
```

### Data Transformation Pattern

```
Get items (SharePoint)
    ↓
Filter array (status = 'Active')
    ↓
Select (extract only id, name, email)
    ↓
Create HTML table
    ↓
Send email with table in body
```

## Compose Action Deep Dive

`Compose` is one of the most versatile actions. Use it to:

1. **Evaluate and store complex expressions**

   ```
   Compose: concat('Hello, ', triggerBody()?['Name'], '!')
   ```

2. **Build JSON objects**

   ```json
   {
     "requestId": "@{guid()}",
     "timestamp": "@{utcNow()}",
     "submittedBy": "@{triggerBody()?['Author']?['DisplayName']}",
     "data": "@{body('Parse_JSON')}"
   }
   ```

3. **Debug/inspect values during development**

   ```
   Compose: @{body('Get_items')?['value']}
   // Inspect in run history to see the actual value
   ```

4. **Create reusable computed values**

   ```
   // Compute once, use the Compose output multiple times downstream
   Compose: formatDateTime(utcNow(), 'yyyy-MM-dd')
   ```

## Parse JSON Action

Parse a JSON string into a structured object so its fields appear as dynamic content.

```
// 1. Provide a JSON sample to generate the schema
{
  "id": 123,
  "name": "Sample Product",
  "price": 9.99,
  "inStock": true
}

// 2. Power Automate generates the schema:
{
  "type": "object",
  "properties": {
    "id":      { "type": "integer" },
    "name":    { "type": "string" },
    "price":   { "type": "number" },
    "inStock": { "type": "boolean" }
  }
}

// 3. After parsing, use dynamic content:
body('Parse_JSON')?['name']   // → "Sample Product"
body('Parse_JSON')?['price']  // → 9.99
```

## Select Action

Transform each item in an array (like `Array.map()` in JavaScript).

```
// Input array:
[
  { "firstName": "Alice", "lastName": "Smith", "dept": "HR" },
  { "firstName": "Bob",   "lastName": "Jones", "dept": "IT" }
]

// Select map:
{
  "fullName": "@{concat(item()?['firstName'], ' ', item()?['lastName'])}",
  "department": "@{item()?['dept']}"
}

// Output array:
[
  { "fullName": "Alice Smith", "department": "HR" },
  { "fullName": "Bob Jones",   "department": "IT" }
]
```

## Filter Array Action

Remove items from an array based on a condition (like `Array.filter()` in JavaScript).

```
// Input: array of orders
// Condition: Status equals 'Pending'
// Output: only orders where Status = 'Pending'

From: body('Get_orders')?['value']
Filter: item()?['Status'] is equal to 'Pending'
```
