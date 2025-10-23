# Source: https://docs.civicrm.org/user/en/latest/contributions/invoicing/

---
categories: Guide  
level: Basic  
summary: This guide explains how non-profit users can enable and create invoices in CiviCRM, customize invoice templates, and understand basic invoicing settings.  
section: Invoicing  
---

# Invoicing in CiviCRM

## What is invoicing in CiviCRM?

Invoicing lets you create, print, or email invoices for contributions in CiviCRM. It works with all financial types and contribution statuses, such as completed or pending. Before you can use invoicing, you need to enable it in your system settings.

## Enabling invoicing

To start using invoicing:

1. Go to **Administer > CiviContribute > CiviContribute Component Settings**.  
2. Check the box labeled **Enable Tax and Invoicing**.  

Here, you can also set:

- A prefix for invoice and credit note numbers (to help organize your invoices).  
- The due date interval (how many days, weeks, or years until the invoice is due).  
- Custom notes or standard terms that will appear on every invoice.

## Creating an invoice

Once invoicing is enabled, you can create invoices for contributions:

1. Open the contact’s record and go to their **Contributions** tab.  
2. Find the contribution you want to invoice.  
3. Choose to either **Print Invoice** or **Email Invoice**.  

- Printing downloads a PDF invoice.  
- Emailing opens an options screen where you can:  
  - Select the sender's email address.  
  - Add an additional message to the email.

**Note:** When emailing an invoice, you cannot add CC or BCC recipients by default. If you need this feature, there is an extension called *invoicehelper* that adds it.

## Customizing invoices

Invoices use a default template that fills in your organization’s name, address, and website from your organization’s contact information. To update this:

- Go to **Administer Console > Configuration Checklist > Organization Address and Contact Info** to change your organization details.  
- To change the look or the image on invoices, edit the template at **Administer > Communications > Message Templates > System Workflow Messages > Contributions-Invoice**.  

For example, to change the logo image, update the image source in the template code:

```html
<td><img src = "{$resourceBase}/i/civi99.png" height="34px" width="99px"></td>
```

## Advanced invoicing setup

If your organization uses accounting software like QuickBooks, you should work with your bookkeeper or accountant to set up financial types and accounts correctly in CiviCRM. For more detailed integration, see the Accounting Integration documentation and community resources.

---

This guide helps you get started with invoicing in CiviCRM, enabling you to send professional invoices to your donors or members with ease. For more detailed or technical information, see the Reference or Explanation documents in the CiviCRM documentation.