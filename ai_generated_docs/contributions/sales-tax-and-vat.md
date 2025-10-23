# Source: https://docs.civicrm.org/user/en/latest/contributions/sales-tax-and-vat/

---
categories: Guide
level: Intermediate
summary: Learn how to enable and set up sales tax or VAT in CiviCRM, including creating financial accounts and linking them to financial types.
section: Contributions
---

# Setting up sales tax and VAT in CiviCRM

## Enabling sales tax or VAT

If your non-profit needs to charge sales tax or VAT, you can enable this feature in CiviCRM. Go to **Administer > CiviContribute > CiviContribute Component Settings** and check the **Enable Tax and Invoicing** box. Here, you can also set your preferred tax term (for example, “VAT” or “Sales Tax”) and choose how taxes are displayed on invoices and receipts—either as part of the total, or listed separately.

## Adding a financial account for sales tax or VAT

Once tax is enabled, you need to create a financial account to track it. Go to **Administer > CiviContribute > Financial Accounts**. Scroll to the bottom and click **Add Financial Account**.

- Set **Financial Account Type** to **Liability**.
- Make sure **Enabled** and **Is Tax** are selected.
- Enter the **Tax Rate** that applies to your organization.
- If you use QuickBooks, set **Account Type Code** to **SALESTAX**.
- Enter your organization’s specific **Accounting Code**.

## Assigning the tax account to a financial type

To apply the tax to a specific type of transaction (for example, donations or event fees), go to **Administer > CiviContribute > Financial Types**. Find the relevant financial type, click **Accounts**, then **Assign Account**.

- Choose **Sales Tax Account is** for the **Financial Account Relationship**.
- Select your new sales tax account in the **Financial Account** field.
- Click **Save**.

Your sales tax account will now appear with the other financial accounts for that financial type.

## Advanced configuration

If you use accounting software like QuickBooks, involve your bookkeeper or accountant to ensure your financial types and accounts are set up correctly for your organization’s reporting needs.

---

This guide is designed for non-profit staff who are familiar with basic CiviCRM tasks but may be setting up tax features for the first time. If you are completely new to CiviCRM, consider starting with a tutorial on basic contribution setup before working with taxes. If your organization has complex tax requirements, you may want to create separate guides for different tax scenarios or integrations.