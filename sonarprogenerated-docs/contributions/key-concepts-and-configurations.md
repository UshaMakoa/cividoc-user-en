---
categories: Reference
level: Basic
summary: Understand the essential concepts and setup options for tracking and managing contributions in CiviCRM, including financial types, accounts, payment processors, and contribution data fields.
section: Contributions > Key concepts and configurations
---

# Key concepts and configurations

This page introduces the main ideas and setup options you need to manage your organisation’s contributions in CiviCRM. It covers the basic building blocks for tracking donations, membership fees, and other income, and helps you understand how to configure CiviCRM to suit your reporting and accounting needs.

## Financial types, financial accounts, and accounting codes

- **Financial types** are categories for the different kinds of income your organisation receives, such as donations, membership dues, or event fees. Each contribution in CiviCRM must be assigned a financial type.
- **Financial accounts** are linked to financial types and represent the accounts in your organisation’s chart of accounts, such as income, assets, or expenses.
- When you set up a new financial type, CiviCRM automatically creates a matching revenue account and connects it to default accounts for assets and expenses.
- You can customise financial types and accounts to match your organisation’s needs. For example, if you want to track tax appeal donations separately from general donations, you should create a separate financial type for each.
- Consult your bookkeeper or accountant before changing financial types or accounts to ensure your records stay accurate.

## Managing financial types

- To create or edit financial types, go to **Administer > CiviContribute > Financial Types**.
- When you add a new financial type, CiviCRM creates related accounts automatically, but you can adjust these by clicking “Accounts” next to the financial type.
- Use CiviCRM’s permission system to control who can access contribution data based on financial type.

## Managing financial accounts

- Edit financial accounts at **Administer > CiviContribute > Financial Accounts**.
- The required fields are **Name** and **Financial Account Type**.
- If you plan to export transactions to accounting software, fill in the accounting code accurately. For QuickBooks, you may also need the account type code.
- Changing a financial account’s name will also change the linked financial type’s name.

## Payment processors

- A **payment processor** connects your CiviCRM site to banks or credit card services, allowing you to accept online payments for donations, memberships, or event registrations.
- Set up payment processors under **Administer > CiviContribute > Payment Processors**.

## Payment methods

- Manage payment methods (such as credit card, cash, check, debit card, EFT) at **Administer > CiviContribute > Payment Methods**.
- Check with your accountant that each method is linked to the correct asset account.

## Accepted credit cards

- Define which credit cards are accepted at **Administer > CiviContribute > Accepted Credit Cards**.
- If your payment processor collects billing info on its own site, configure accepted cards there as well.

## Contribution status

Every contribution in CiviCRM has a **status** that shows its progress:

- **Pending (Pay Later):** Entered but not yet paid (e.g., awaiting a check).
- **Pending (Incomplete):** Payment started but not finished or confirmed.
- **Failed:** Payment was declined or had an error.
- **Completed:** Payment was processed successfully.
- Other statuses like **In Progress**, **Overdue**, or **Partially Paid** are used for features like partial or recurring payments.
- You can change status labels at **Administer > System Settings > Option Groups**, but adding new statuses is not recommended.

## Data needs and fields

- CiviContribute includes standard fields for tracking contributions.
- If you need to record extra information, you can add custom fields.
- Before creating custom fields, list what information you want to track and compare it to the existing fields (look at the “add contribution” screen).
- Avoid duplicating standard fields; use custom fields only for unique needs.
- For instructions on adding custom fields, see the “Creating Custom Fields” section.

# comment: Source: https://docs.civicrm.org/user/en/latest/contributions/key-concepts-and-configurations/
# comment: This page is best classified as Reference because it systematically describes key concepts, configuration options, and factual details about contributions in CiviCRM, rather than providing step-by-step instructions or background explanation. The content is introductory and suitable for basic-level users. If more detailed setup steps were included, a separate Tutorial or Guide could be created.