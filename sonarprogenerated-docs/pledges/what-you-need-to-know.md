---
categories: Guide
level: Basic
summary: Learn the essential steps and options for managing pledges in CiviCRM, including creating new pledges, sending reminders, enabling self-service payments, and finding existing pledges.
section: Pledges
---

# What you need to know about pledges

## Enabling pledges in your CiviCRM

Before you can use pledges, you need to enable the CiviPledge component in your system.

- Go to **Administer > System Settings > Enable CiviCRM Components**.
- Check the box for **CiviPledge**.
- Click **Save**.

## Creating a new pledge

To record a new pledge for a supporter:

- Go to **Contributions > Pledges > New Pledge**.
- Select the contact making the pledge (type their name or create a new contact if needed).
- Enter the **total pledge amount**.
- Specify how the pledge will be paid (number of instalments and the time period).
- Choose the **day payments are due** (for example, the 2nd of each month).
- Set the **date the pledge was made** and the **date payments start**.
- If you want to send an email acknowledgment, check **Send Acknowledgment?** (the contact must have a valid email and outgoing mail must be set up).
- The **Acknowledgement Date** will be filled automatically if an email is sent.
- Choose the **Financial Type** (such as Donation or Event Fee) to show what the pledge is for.
- If you use campaigns, you can assign the pledge to a **Campaign**.
- To let donors pay online, select a **Self-service Payments Page** (an online contribution form).
- If the donor wants to dedicate their pledge, you can add **Honoree information**.
- Set up **payment reminders** if you want the donor to receive emails before each payment is due.

## Setting up payment reminders

You can email one or more reminders to the donor before each scheduled payment.

- Make sure the **Process Pledges** scheduled job is enabled. This updates payment statuses and sends reminders.
- The donor must have a valid email address and must not be marked as "Do Not Email".
- When creating a pledge, you can set:
  - **Send Initial Reminder**: how many days before the payment date the first reminder is sent.
  - **Send up to**: the maximum number of reminders for each payment.
  - **Send additional reminders**: how many days between reminders.

If you select a **Self-service Payments Page**, the reminder email will include a link for the donor to pay online.

## Allowing self-service payments

Donors can pay their pledge instalments online if you have a contribution page with a payment processor.

- When creating a pledge, choose the relevant **Self-service Payments Page**.
- If reminders are enabled, the email will include a payment link.

## Finding and managing pledges

To search for existing pledges:

- Go to **Contributions > Pledges > Find Pledges**.
- Search by name, email, or pledge details (such as payment start date or status).
- The results show a summary of pledges, with options to **View**, **Edit**, or **Delete** each one.
- If a pledge is "In Progress" or "Pending", you can also **Cancel** it.

## Viewing the pledges dashboard

To see recent pledges and summary tables for the current month and past year:

- Go to **Contributions > Pledges > Dashboard**.

This dashboard helps you keep track of all pledge activity in your organisation.

---

# comment: Source: https://docs.civicrm.org/user/en/latest/pledges/what-you-need-to-know/
# comment: This page is a Guide because it provides step-by-step instructions for specific tasks (enabling, creating, managing pledges), but does not cover deep background or comprehensive reference details. It is suitable for users new to pledges, so the level is Basic. If the original page contained detailed field-by-field definitions or conceptual background, those would be split into Reference or Explanation pages for best clarity.