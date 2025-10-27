---
categories: Guide
level: Basic
summary: Learn how to enable and configure pledges on your organisation’s online donation forms in CiviCRM, so supporters can commit to future donations and receive automated reminders.
section: Pledges > Set-up
---

# Setting up pledges on online donation forms

## Enable pledges for your donation form

You can let your supporters make **pledges**—commitments to donate in the future—using your online CiviContribute donation forms. This gives donors flexibility to choose how often and how much they want to give, such as monthly or annually.

Some payment processors do not support automated recurring payments, and some donations may arrive as cheques or other non-electronic methods. In these cases, you can manually update the pledge status from 'Pending' to 'Complete' when the payment is received. CiviCRM also helps you send automated reminders to donors about their pledges.

To enable pledges:

- Create or edit a contribution page (see the “Creating Contribution Pages” guide if you need help).
- Go to the **Amounts** tab in the page settings.
- Tick the **Pledges** option.
- Configure the pledge settings that appear.

## Configure pledge options

After enabling pledges, you can adjust these settings:

- **Supported pledge frequencies**: Let donors choose daily, weekly, monthly, or annual pledges.
- **Allow frequency intervals**: Let donors specify gaps between payments (e.g., every 5 weeks or 5 months).
- **Send payment reminder**: Set how many days before a scheduled payment a reminder is sent.
- **Send up to**: Choose the maximum number of reminders for each scheduled payment.
- **Send additional reminders**: Set the number of days between each reminder.
- **Allow other amounts**: Let donors pledge custom amounts, and set minimum and maximum limits.
- **Fixed contribution options**: Enter up to ten fixed pledge amounts, each with a label and amount, to display as radio button choices.

When you finish, save your changes. The pledge option will now appear on your online donation form.

## Monitor pledges

To view and manage current pledges:

- Go to **Contributions > Pledges > Dashboard** in CiviCRM.
- Use available reports and dashboards to track pledge status and activity.

# comment: Source: https://docs.civicrm.org/user/en/latest/pledges/set-up/
# comment: Suggestion: This page is a Guide, as it provides step-by-step actions for users to enable and configure pledges on donation forms. It does not explain background concepts or provide exhaustive technical reference. The level is Basic, since it is aimed at non-expert users performing a common setup task. The logical section is "Pledges > Set-up". The summary is tailored for non-profit staff learning to use CiviCRM pledges. If more detailed reference for each setting is needed, consider splitting those details into a Reference page.