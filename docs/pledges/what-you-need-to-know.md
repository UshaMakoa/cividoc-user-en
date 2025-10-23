---
categories:
  - Guide
level: Basic
summary: This guide provides step-by-step instructions on how to manage pledges in CiviCRM, including creating new pledges, setting up payment reminders, and finding existing pledges.
section: Pledges
---

# managing pledges in civicrm
## creating a new pledge
To create a new pledge on behalf of a constituent, follow these steps:

1. **Enable CiviPledge**: Go to Administer > System Settings > Enable CiviCRM Components, and check the box for CiviPledge.
2. **Navigate to Pledges**: Go to Contributions > Pledges > New Pledge.
3. **Select Contact**: Type the name of an existing contact or create a new one.
4. **Enter Pledge Details**:
   - Total Pledge Amount
   - Payment Schedule (number of instalments and time period)
   - Payment Due Date
   - Pledge Made Date
   - Payments Start Date
   - Send Acknowledgment Email (if configured)
   - Financial Type
   - Campaign (if applicable)
   - Self-service Payments Page (if applicable)
   - Honoree Information (if applicable)

## setting up payment reminders
To set up payment reminders, follow these steps:

1. **Enable Scheduled Job**: Ensure the Process Pledges (process_pledge) scheduled job is enabled.
2. **Configure Reminders**: Set the reminder schedule when creating a new pledge.
   - Send Initial Reminder: Number of days before the payment date.
   - Send Up To: Maximum number of reminders.
   - Send Additional Reminders: Interval period between reminders.

## self-service payments
To allow donors to make payments online:

1. **Select Contribution Page**: Choose a Contribution Page with a Payment Processor when creating a new pledge.
2. **Include Link in Reminders**: If reminders are enabled, a link to the payment page will be included in the emails.

## finding pledges
To search for existing pledges:

1. **Navigate to Find Pledges**: Go to Contributions > Pledges > Find Pledges.
2. **Search Criteria**: Search by Pledger Name, Email Address, or other discrete features.
3. **Manage Pledges**: View, Edit, or Delete pledges from the search results.

## pledges dashboard
View a summary of recent and past pledges on the Pledges Dashboard, accessible through the Contributions menu.
