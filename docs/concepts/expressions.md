# Power Automate Expressions

Power Automate uses a subset of the **Azure Logic Apps expression language** to create dynamic values. Expressions are written inside `@{ }` delimiters.

## Expression Syntax

```
// Inline expression (entire value is the expression)
@triggerBody()?['Title']

// Embedded expression (expression within a string)
Hello, @{triggerBody()?['Name']}!

// Complex expression
@{concat('Order-', formatDateTime(utcNow(), 'yyyyMMdd'), '-', rand(100, 999))}
```

## Reference Types

### Dynamic Content vs. Expressions

| Type | How to Add | Example |
|------|-----------|---------|
| Dynamic content | Click "Add dynamic content" | `triggerBody()?['Title']` |
| Expression | Click "Add dynamic content" → "Expression" tab | `formatDateTime(utcNow(), 'yyyy-MM-dd')` |

## String Functions

```
// Concatenate strings
concat('Hello, ', triggerBody()?['Name'], '!')

// Convert to uppercase / lowercase
toUpper('hello')           // → "HELLO"
toLower('HELLO')           // → "hello"

// String length
length('hello')            // → 5

// Contains substring
contains('hello world', 'world')   // → true

// Replace substring
replace('hello world', 'world', 'there')  // → "hello there"

// Start/end with
startsWith('hello', 'he')  // → true
endsWith('hello', 'lo')    // → true

// Substring extraction
substring('hello world', 6, 5)  // → "world"

// Split string into array
split('a,b,c', ',')        // → ["a", "b", "c"]

// Trim whitespace
trim('  hello  ')          // → "hello"

// Format a number
formatNumber(12345.678, 'C2', 'en-US')  // → "$12,345.68"
```

## Date and Time Functions

```
// Current UTC time
utcNow()                   // → "2024-01-15T10:30:00.0000000Z"

// Format a date
formatDateTime(utcNow(), 'yyyy-MM-dd')           // → "2024-01-15"
formatDateTime(utcNow(), 'MMMM d, yyyy')         // → "January 15, 2024"
formatDateTime(utcNow(), 'MM/dd/yyyy HH:mm')     // → "01/15/2024 10:30"
formatDateTime(utcNow(), 'dddd, MMMM d yyyy')    // → "Monday, January 15 2024"

// Add/subtract time
addDays(utcNow(), 7)       // Add 7 days
addHours(utcNow(), -1)     // Subtract 1 hour
addMinutes(utcNow(), 30)   // Add 30 minutes
addSeconds(utcNow(), 10)

// Convert time zones
convertTimeZone(utcNow(), 'UTC', 'Eastern Standard Time')
convertTimeZone(utcNow(), 'UTC', 'Pacific Standard Time')

// Parse a date string
parseDateTime('2024-01-15T10:30:00Z')

// Get specific date parts
dayOfMonth(utcNow())       // → 15
dayOfWeek(utcNow())        // → 1 (0=Sunday)
month(utcNow())            // → 1
year(utcNow())             // → 2024
```

## Logical / Comparison Functions

```
// Equals
equals('hello', 'hello')   // → true

// Not equals
not(equals('a', 'b'))      // → true

// Greater / less than
greater(10, 5)             // → true
greaterOrEquals(10, 10)    // → true
less(5, 10)                // → true
lessOrEquals(5, 5)         // → true

// Logical AND / OR / NOT
and(true, true)            // → true
or(false, true)            // → true
not(false)                 // → true

// If / else (ternary)
if(equals(variables('status'), 'Active'), 'green', 'red')

// Null checks
empty('')                  // → true
empty(null)                // → true
null()                     // returns null value
```

## Array Functions

```
// Create an array
createArray('a', 'b', 'c')

// Get array length
length(body('Get_items')?['value'])

// First / last element
first(body('Get_items')?['value'])
last(body('Get_items')?['value'])

// Access by index
body('Get_items')?['value']?[0]

// Join array into string
join(createArray('a', 'b', 'c'), ', ')  // → "a, b, c"

// Check if array contains value
contains(variables('myArray'), 'targetValue')

// Combine arrays
union(variables('array1'), variables('array2'))

// Intersect arrays (items in both)
intersection(variables('array1'), variables('array2'))
```

## Math Functions

```
add(1, 2)                  // → 3
sub(10, 3)                 // → 7
mul(4, 5)                  // → 20
div(10, 4)                 // → 2 (integer division)
mod(10, 3)                 // → 1
rand(1, 100)               // Random integer between 1 and 100
min(5, 3, 8)               // → 3
max(5, 3, 8)               // → 8
```

## Conversion Functions

```
// Convert types
int('42')                  // → 42 (string to integer)
float('3.14')              // → 3.14
string(42)                 // → "42"
bool('true')               // → true

// JSON
json('{"key": "value"}')   // Parse JSON string to object
string(body('action'))     // Serialize object to JSON string

// Base64
base64('hello')            // → "aGVsbG8="
base64ToString('aGVsbG8=') // → "hello"

// URL encoding
encodeUriComponent('hello world')   // → "hello%20world"
decodeUriComponent('hello%20world') // → "hello world"
```

## Accessing Dynamic Content

```
// Trigger body
triggerBody()?['FieldName']
triggerBody()?['nested']?['field']

// Action output body
body('Action_Name')?['FieldName']

// Action output (full)
outputs('Action_Name')

// Loop item (inside Apply to each)
items('Apply_to_each')?['FieldName']

// Variables
variables('myVariableName')

// Parameters
parameters('$connections')

// Null-safe access (use ?[] to avoid errors on null)
triggerBody()?['OptionalField']    // Returns null if field missing
triggerBody()['RequiredField']     // Throws error if field missing
```

## Common Expression Patterns

```
// Generate a unique ID
guid()                     // → "b651f0b5-5deb-4ae9-9bc2-c90a2028bbf8"

// Build a formatted ticket number  
concat('TKT-', formatDateTime(utcNow(), 'yyyyMMdd'), '-', rand(1000, 9999))

// Check if a value is in a list
contains(createArray('Admin', 'Manager', 'Owner'), triggerBody()?['Role'])

// Build a conditional message
if(greater(variables('errorCount'), 0), 
   concat(string(variables('errorCount')), ' errors occurred'),
   'All items processed successfully')

// Get day name for scheduling logic
equals(dayOfWeek(utcNow()), 1)  // true on Monday
```

## Tips

- Use the **Expression** tab in the dynamic content pane to write expressions
- Use `?['FieldName']` (null-safe) instead of `['FieldName']` to prevent errors on missing fields
- Test expressions in the **Expression editor** using the "peek code" view
- Complex expressions are easier to build and debug using **Compose** actions
