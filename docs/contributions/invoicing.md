---
categories:
  - Guide
level: Basic
summary: Learn how to enable, create, send, and customize invoices for contributions in CiviCRM, step by step, using simple instructions.
section: Contributions > Invoicing
---

# Invoicing in CiviCRM

## Enable invoicing

To use invoicing for your organisation’s contributions, you first need to turn on the feature.

- Go to **Administer > CiviContribute > CiviContribute Component Settings**.

- Tick the box labeled **Enable Tax and Invoicing**.

- On this screen, you can also:

- Add a prefix for invoices and credit notes (for example, “INV
-”).

- Set how many days, weeks, or years until an invoice is due.

- Add standard notes or terms to appear on all invoices.

## Create and send an invoice

Once invoicing is enabled, you can create and send invoices for any completed or pending contribution.

- Go to the **Contact’s Contribution** tab.

- Find and view the contribution record you want to invoice.

- Choose **Print Invoice** to download a PDF, or **Email Invoice** for email options.

### Emailing invoices

- When you choose **Email Invoice**, you can:

- Select the “From” email address.

- Type an additional message.

- Note: You cannot add CC or BCC when emailing invoices by default. If you need this, ask your administrator about the “invoicehelper” extension.

## Customize invoices

You can change how invoices look and what information they show.

- The organisation’s name, address, and website (shown on invoices) come from **Administer Console > Configuration Checklist > Organization Address and Contact Info**.

- To change the invoice template or image:

- Go to **Administer > Communications > Message Templates > System Workflow Messages > Contributions
-Invoice**.

- Edit the template code as needed, for example, to swap out the logo image.

For advanced accounting integration (like with QuickBooks), work with your bookkeeper to set up financial types and accounts. See the “Accounting Integration” section for more details.

<!--
Source: https://docs.civicrm.org/user/en/latest/contributions/invoicing/
 -->

<!--
Suggestion: The original page is a step
-by-step guide focused on enabling and using invoicing, with some brief reference material about customization. According to Diátaxis, this is best classified as a "Guide" (problem-oriented how-to). The customization and integration details could be split into a separate Reference or Tutorial page for advanced users if needed. -->
