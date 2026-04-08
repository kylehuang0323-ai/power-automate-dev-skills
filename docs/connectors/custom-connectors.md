# Building Custom Connectors

Custom connectors allow you to connect Power Automate to any REST API or SOAP service not available as a built-in connector.

## When to Build a Custom Connector

- Your organization has an internal API
- A needed third-party service lacks a built-in connector
- You want to wrap complex API logic into simple, reusable actions for makers

## Prerequisites

- Power Automate Premium license
- An API with HTTPS support
- An OpenAPI (Swagger) definition for the API (or you can create one manually)
- Developer access to register an OAuth2 app (if OAuth is used)

## Creating a Custom Connector

### Step 1: Navigate to Custom Connectors

Power Automate → **Data** → **Custom connectors** → **New custom connector** → **Create from blank**

### Step 2: General Information

```
Connector name: My Company API
Description:    Connects to the My Company internal REST API
Host:           api.mycompany.com
Base URL:       /v1
```

### Step 3: Authentication

Choose the authentication type your API uses:

#### No Authentication (public APIs)
- No configuration needed

#### API Key
```
Parameter label:  API Key
Parameter name:   X-API-Key
Parameter location: Header
```

#### OAuth 2.0
```
Identity provider: Generic OAuth 2
Client ID:         [Your app client ID]
Client secret:     [Your app client secret]
Authorization URL: https://login.microsoftonline.com/{tenant}/oauth2/v2.0/authorize
Token URL:         https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token
Refresh URL:       https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token
Scope:             https://api.mycompany.com/.default
```

### Step 4: Define Actions (Operations)

Each operation corresponds to an API endpoint.

#### Example: GET operation

```
Summary:         Get all products
Description:     Returns a list of products, optionally filtered by category
Operation ID:    GetProducts
Visibility:      important

Request:
  Verb:    GET
  URL:     /products
  
  Query parameters:
    - Name: category  | Type: string | Required: No | Description: Filter by category
    - Name: pageSize  | Type: integer | Required: No | Default: 50
    - Name: page      | Type: integer | Required: No | Default: 1
```

#### Example: POST operation

```
Summary:         Create a product
Description:     Creates a new product in the catalog
Operation ID:    CreateProduct
Visibility:      important

Request:
  Verb:    POST
  URL:     /products
  
  Body (JSON schema):
  {
    "type": "object",
    "properties": {
      "name":     { "type": "string", "x-ms-summary": "Product Name" },
      "price":    { "type": "number", "x-ms-summary": "Price" },
      "category": { "type": "string", "x-ms-summary": "Category" },
      "sku":      { "type": "string", "x-ms-summary": "SKU" }
    },
    "required": ["name", "price"]
  }
```

### Step 5: Response Schema

Define the response schema to make output properties available as dynamic content.

```json
{
  "type": "object",
  "properties": {
    "id":       { "type": "string", "x-ms-summary": "Product ID" },
    "name":     { "type": "string", "x-ms-summary": "Product Name" },
    "price":    { "type": "number", "x-ms-summary": "Price" },
    "category": { "type": "string", "x-ms-summary": "Category" },
    "createdAt": { "type": "string", "format": "date-time", "x-ms-summary": "Created At" }
  }
}
```

### Step 6: Test the Connector

1. In the connector wizard, go to **Test** tab
2. Create a new connection
3. Test each operation with real values
4. Verify the response is parsed correctly

## OpenAPI Extensions (`x-ms-*`)

These extensions enhance the connector experience in Power Automate:

| Extension | Purpose |
|-----------|---------|
| `x-ms-summary` | Display name for the field in the UI |
| `x-ms-visibility` | `important` / `advanced` / `internal` – controls visibility |
| `x-ms-dynamic-values` | Populates a dropdown from an API call |
| `x-ms-dynamic-schema` | Dynamic response schema based on inputs |
| `x-ms-url-encoding` | Controls URL encoding behavior |

## Importing an OpenAPI Definition

If your API has an existing OpenAPI spec:

1. **New custom connector** → **Import an OpenAPI file** or **Import from URL**
2. Review and edit the imported definition
3. Add `x-ms-*` extensions to improve usability
4. Test all operations

## Using a Custom Connector in a Flow

1. Add an action in your flow
2. Search for your custom connector by name
3. Select the operation
4. Create a new connection (enter API key / authenticate via OAuth)
5. Fill in the required parameters

## Custom Connector Lifecycle

### Versioning

```
// Bump the version when making breaking changes
v1.0 → v1.1   Minor: added optional parameters
v1.0 → v2.0   Major: breaking change (renamed/removed parameters)
```

To version:
1. Export the connector definition as a file
2. Create a new connector with the new version
3. Migrate flows to the new version before deprecating the old one

### Certification

Consider submitting to Microsoft for certification if:
- The API is a popular third-party service
- You want it available to all Power Automate users globally

[Certification guide](https://docs.microsoft.com/en-us/connectors/custom-connectors/certification-submission)

## Sharing Custom Connectors

| Sharing Method | Audience |
|----------------|---------|
| Share with specific users | Small team, dev testing |
| Share via Solution | Environment-wide deployment |
| Submit for certification | All Power Automate users |
| Share via GitHub | Open source / community |

## Custom Connector Best Practices

- Use descriptive `x-ms-summary` labels for all parameters and response properties
- Mark rarely-used parameters as `advanced` visibility to keep the UI clean
- Provide default values for optional parameters
- Test error responses as well as success responses
- Document the connector setup steps (authentication, required permissions, etc.)
- Version your connector properly to avoid breaking existing flows
- Store the OpenAPI definition in source control

## Troubleshooting

| Issue | Solution |
|-------|---------|
| Connection fails to authenticate | Verify client ID, secret, and scope in OAuth settings |
| Operation returns 401 | Check the API key header name matches exactly |
| Dynamic content not showing | Verify response schema is correctly defined |
| Parameters not mapping | Check parameter names in the OpenAPI definition |
| SSL certificate error | Ensure API uses a valid, trusted certificate |
