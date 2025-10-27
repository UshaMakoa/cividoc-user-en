---
categories: Guide
level: Basic
summary: Learn how to find and view contributions in CiviCRM, understand the difference between contacts and contributions, and use the search and dashboard features to manage your organisation’s donations.
section: Contributions
---

# Finding and viewing contributions

## Viewing the contributions dashboard

The **CiviContribute dashboard** gives you a summary of all contributions made to your organisation. You can see totals for the current month, year, and all time. This dashboard helps you quickly browse donations, whether they were entered automatically (such as online donations) or manually (such as cheques or cash).

You can view your contributions in different ways:

- **Table layout:** Shows a list of recent contributions, including details like donor, amount, and date.
- **Chart layout:** Displays bar or pie charts to compare contribution totals by month or year.
- **Report dashlets:** Add custom charts or lists (like top donors or year-to-date totals) to your personal dashboard for quick access.

## Finding contributions

CiviCRM treats **contributions** (the donations themselves) and **contacts** (the people or organisations who gave) as separate things. When searching, think about whether you want to find specific donations or the donors themselves. For example, if you want to send a thank-you gift to everyone who donated last year, decide if you want to send one gift per donation or one per donor.

To search for contributions:

1. Go to **Contributions > Find Contributions** in the menu.
2. Enter your search criteria, such as:
   - **Date range** (for example: last month, last year, or a custom period)
   - **Contribution amount**
   - **Contribution status** (such as completed, pending, or cancelled)
   - **Financial type** (such as donation, membership, or event fee)

The more criteria you enter, the more specific your search results will be. For example, searching for financial type “Donation” and date range “January 1st to May 31st” will only show donations made in that period.

The results screen shows:

- Total amount for all matching contributions
- Number of contributions found
- Average contribution (mean and mode)

## Actions you can take with search results

After searching, you can select all or some contributions and choose an action from the **Actions** menu:

- **Update multiple contributions:** Change details (like thank-you date) for many contributions at once. You’ll need to set up a profile for batch updates first.
- **Delete contributions:** Permanently remove contributions. Usually, it’s better to change the status to “cancelled” for record-keeping, but deletion is possible if needed.
- **Export contributions:** Download details of contributions as a file. Each donation will be a separate row. If you want one row per donor, use the contact advanced search instead.
- **Receipts:** Print or email receipts for selected contributions.
- **Email:** Send an email to donors of selected contributions.
- **Thank-you letters:** Print or email custom thank-you letters for each contribution, with an option to update the thank-you date.
- **Record payments:** For “Pay Later” contributions that are still pending, record payment details once payment is received.

## Using advanced search

The **Advanced Search** feature usually returns contacts, but you can change the “Display Results As” field to show contributions instead. You can also combine contribution search criteria with other filters, such as finding all donations to a specific campaign made by members, or all contacts who gave more than $100 last year and live in a certain area.

# comment: Source: https://docs.civicrm.org/user/en/latest/contributions/finding-and-viewing-contributions/
# comment: This page is a Guide because it provides step-by-step actions to achieve a specific goal (finding and viewing contributions, using search and dashboard features). It is not a Tutorial (no hands-on learning sequence), not Reference (not exhaustive technical details), and not Explanation (no background or conceptual information). Level is Basic, as it is intended for users learning to perform specific, common tasks.