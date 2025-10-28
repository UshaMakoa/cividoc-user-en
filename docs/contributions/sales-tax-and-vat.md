---
categories:
  - Guide
level: Basic
summary: Learn how to enable and set up sales tax or VAT in CiviCRM so your organisation can properly track and display tax on contributions.
section: Contributions > Sales tax and VAT
---

# Sales tax and VAT setup

If your organisation needs to charge **sales tax** or **VAT** on contributions, you can enable and configure this feature in CiviCRM. This guide will walk you through each step.

## Enable sales tax/VAT

1. Go to **Administer > CiviContribute > CiviContribute Component Settings**.

2. Find and check the box for **Enable Tax and Invoicing**.

3. On this screen, you can adjust the following settings:
   - **Tax term**: Enter the name you want to use for your tax (e.g., "VAT", "Sales Tax").
   - **Tax display settings**: Choose how you want tax to appear on invoices and receipts:

- No breakdown, total only

- Show as inclusive price (e.g., $120 includes $20 tax)

- Show as exclusive price (e.g., $100 + $20 tax)

## Add a financial account for sales tax/VAT

1. Go to **Administer > CiviContribute > Financial Account**.

2. Scroll down and click **Add Financial Account**.

3. Fill in the details:

   - **Financial Account Type**: Set this to **Liability**.

- Check **Enabled** and **Is Tax**.

- Set the **Tax Rate** (e.g., 20 for 20%).

- If using QuickBooks, set **Account Type Code** to **SALESTAX**.

- Use your organisation’s accounting codes for the **Accounting Code** field.

## Assign the tax account to a financial type

1. Go to **Administer > CiviContribute > Financial Types**.

2. Find the financial type (like "Donations" or "Event Fees") that should include tax, and click **Accounts**.

3. Click **Assign Account**.

4. For **Financial Account Relationship**, choose **Sales Tax Account is**.

5. In the **Financial Account** field, select the tax account you just created.

6. Click **Save**.

You will now see the sales tax financial account listed with other accounts for that financial type.

*Tip: For advanced accounting integration (for example, with QuickBooks), involve your bookkeeper or accountant to make sure your setup matches your organisation’s needs.*

<!--
Source: https://docs.civicrm.org/user/en/latest/contributions/sales
-tax-and-vat/ -->

<!--
Suggestion: This page is a Guide (step
-by-step, problem-oriented: "How do I enable and configure sales tax/VAT in CiviCRM?"). It is not a Tutorial (not a first-time, hands-on lesson), not Reference (not exhaustive options/config), and not Explanation (no background/why). Level is Basic, as it is aimed at non-experts performing a common admin task. For best clarity, the "Adding a Financial Account for Sales Tax/VAT" section could be split into its own page if more detail or troubleshooting is needed, but for most users, a single guide is sufficient. -->
