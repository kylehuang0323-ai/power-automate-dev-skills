# ALM for Power Automate (Application Lifecycle Management)

Application Lifecycle Management (ALM) ensures your Power Automate flows can be developed, tested, and deployed reliably across environments.

## Environment Strategy

Use separate environments for each stage of development.

```
Development  →  Test/QA  →  Production
     ↑                           ↑
  Makers build              End users run
```

| Environment | Purpose | Who Can Access |
|-------------|---------|----------------|
| Development | Makers create and test flows | Developers only |
| Test / UAT | User acceptance testing | Testers + select users |
| Production | Live flows used by the business | All users |

## Solutions

Always build flows inside a **Solution** for proper ALM support.

### Why Use Solutions?

- Solutions bundle flows, connectors, environment variables, and more into a single deployable package
- Enables version control and deployment automation
- Supports connection references (environment-agnostic connections)
- Required for managed deployments and DLP governance

### Creating a Solution

1. Go to Power Automate → **Solutions** → **New solution**
2. Fill in: Display name, Publisher, Version
3. Add existing flows or create new ones inside the solution

### Solution Components

| Component Type | Description |
|---------------|-------------|
| Cloud flow | The flow itself |
| Connection reference | Abstract pointer to a connection |
| Environment variable | Environment-specific configuration value |
| Custom connector | Custom API connector |
| Canvas app | Power Apps app (if related) |
| Table | Dataverse table definition |

## Environment Variables

Use environment variables instead of hardcoded values so the same solution works across environments.

```
// Types of environment variables
- Text           → Site URLs, email addresses, team names
- Number         → Numeric thresholds and configuration
- Boolean        → Feature flags
- Secret (JSON)  → Sensitive configuration (requires Key Vault integration)
- Data source    → SharePoint list or Dataverse table references
```

**Usage in expressions:**
```
parameters('EnvVar_SharePoint_SiteURL')
```

### Setting Environment Variable Values

- In **Development**: Set values directly
- In **Test/Production**: Set values when deploying the solution, or use a deployment pipeline

## Connection References

Connection references decouple a flow from a specific user's connection.

```
Flow → Connection Reference → Actual Connection
                ↑
        Swappable per environment
```

**How to use:**
1. Create a connection reference in your solution
2. Select the connection reference when building the flow action
3. When deploying to a new environment, map the connection reference to a connection in that environment

## Exporting and Importing Solutions

### Manual Export

1. Solutions → Select solution → **Export**
2. Choose **Managed** (for production) or **Unmanaged** (for dev)
3. Download the `.zip` file

### Manual Import

1. Target environment → Solutions → **Import solution**
2. Upload the `.zip` file
3. Map connection references and environment variables
4. Import

### Managed vs. Unmanaged Solutions

| Type | When to Use | Edit the Flow? |
|------|-------------|----------------|
| Unmanaged | Development environment | Yes |
| Managed | Test and Production | No (read-only) |

## Power Platform CLI (pac)

Automate solution operations from the command line.

```bash
# Install the CLI
npm install -g @microsoft/powerplatform-cli

# Authenticate
pac auth create --url https://yourenv.crm.dynamics.com

# Export a solution
pac solution export --name MySolution --path ./solutions/MySolution.zip

# Import a solution
pac solution import --path ./solutions/MySolution.zip

# Check solution differences
pac solution diff --solution1 ./MySolution_old.zip --solution2 ./MySolution_new.zip
```

## CI/CD with GitHub Actions

Automate deployments using the Power Platform GitHub Actions.

```yaml
# .github/workflows/deploy.yml
name: Deploy to Production

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Install Power Platform CLI
        uses: microsoft/powerplatform-actions/actions-install@v1

      - name: Import solution to Production
        uses: microsoft/powerplatform-actions/import-solution@v1
        with:
          environment-url: ${{ secrets.PROD_ENVIRONMENT_URL }}
          app-id: ${{ secrets.APP_ID }}
          client-secret: ${{ secrets.CLIENT_SECRET }}
          tenant-id: ${{ secrets.TENANT_ID }}
          solution-file: solutions/MySolution_managed.zip
          force-overwrite: true
```

## Version Control for Solutions

Store exported solution files in Git for version history.

```
repository/
├── solutions/
│   ├── MySolution/
│   │   ├── MySolution_unmanaged.zip     # For import to dev
│   │   └── MySolution_managed.zip       # For import to test/prod
│   └── README.md
├── docs/
└── README.md
```

## Governance Checklist

Before promoting a solution to production:

- [ ] All flows use connection references (not direct connections)
- [ ] All hardcoded values replaced with environment variables
- [ ] Flows tested in the Test/UAT environment
- [ ] Error handling and alerting configured on all critical flows
- [ ] DLP policy reviewed and compliant
- [ ] Service account connections used (not personal accounts)
- [ ] Flow owners and co-owners assigned (not just one person)
- [ ] Run history monitored for at least 1 week in test

## Resources

- [Power Platform CLI Documentation](https://docs.microsoft.com/en-us/power-platform/developer/cli/introduction)
- [Power Platform GitHub Actions](https://github.com/microsoft/powerplatform-actions)
- [ALM Accelerator for Power Platform](https://github.com/microsoft/coe-starter-kit)
- [Environment Strategy Guide](https://docs.microsoft.com/en-us/power-platform/guidance/adoption/environment-strategy)
