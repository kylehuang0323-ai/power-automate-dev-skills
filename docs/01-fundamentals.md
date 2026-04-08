## Fundamentals

### Flow Types

| Type | Description | Use Case |
|---|---|---|
| Automated cloud flow | Triggered by an event | Auto-process when SP item changes |
| Instant cloud flow | Manual trigger (button/selected item) | User clicks a button |
| Scheduled cloud flow | Runs on a schedule | Daily overdue check |
| Desktop flow | Local RPA automation | Automate local apps |
| Business process flow | Guided multi-stage process | Approval pipeline |

### Core Concepts

- **Trigger**: The event that starts a Flow; each Flow has exactly one trigger

- **Action**: Each step in a Flow (read data, send email, condition, etc.)

- **Connection**: Authenticated link between Flow and external services, stored under user account

- **Dynamic content**: Output from previous steps, referenceable in later steps

- **Expression**: Functions to process data (string concat(), date math, etc.)

### Run Modes

| Mode | Meaning |
|---|---|
| Succeeded | All steps completed normally |
| Failed | A step errored and was not caught |
| Cancelled | Stopped by Terminate action or user |
| Running | Flow is currently executing |

---
