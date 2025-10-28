---
categories:
  - Reference
level: Basic
summary: Message templates in CiviCRM let your organisation create, manage, and personalise reusable email messages for mass mailings and automated system communications.
section: Email > Message templates
---

# Message templates overview

Message templates help your organisation send consistent, professional communications by letting you reuse entire emails or parts of emails for both mass mailings and individual messages. There are two main types of message templates in CiviCRM:

- **User-driven message templates**: Created by your staff for regular communications, such as thank-you letters or meeting announcements.
- **System workflow message templates**: Pre-configured templates used by CiviCRM for automated messages, such as receipts or event confirmations.

Message templates are available even if CiviMail is disabled.

## Creating user-driven templates

You can create a new message template by ticking the "Save as New Template" box when sending an email or mass mailing. To manage templates directly, go to **Mailings > Message Templates** or **Administer > Communications > Message Templates**.

To create a new template:

- Click **Add Message Template**.

- Enter a **Message Title** and **Message Subject**. You can use tokens to personalise the subject.

- Create your template in the **HTML Format** section using the WYSIWYG editor. If you want to paste or edit HTML code directly, switch to "Source" view.

- Save your template.

## Tips for creating templates

When designing HTML email templates, remember:

- Use tables for layout and inline CSS; avoid background images.

- Keep the email width under 600 pixels for compatibility.

- Images must be online and sized appropriately.

- Use the WYSIWYG editor provided by CiviCRM, or select another editor via **Administer > Customize Data and Screens > Display Preferences**.

## Plain text and HTML formats

Messages can be sent in both plain text and HTML. To ensure everyone can read your emails:

- Leave the text version blank (recommended); CiviCRM will generate it from your HTML.

- Or, manually enter a text version, but keep it updated to avoid sending incomplete information.

To create a plain text version:

- Copy the text from the HTML Format field (not the Source view) into the Plain Text Format field.

- Copy URLs for links into the text version.

- Adjust layout for readability if your HTML used tables.

## Modifying system workflow message templates

System workflow templates are used for automated communications and include logic to display relevant data. You can view and edit these by going to **Administer > Communication > Message Templates** and clicking the **System Workflow Message** tab.

**Be careful when editing these templates:**

- Customising them means future CiviCRM upgrades won’t update your changes automatically, so you may miss new features.

- Avoid changing program logic; test emails after making changes.

- You can revert to the default template if needed.

For branding, use the `{site.message_header}` site token instead of editing templates directly.

## Variables and tokens in workflow message templates

Workflow templates use both tokens (e.g. `{contribution.tax_amount}`) and Smarty variables (e.g. `{$taxAmount}`). Tokens are consistent across screens, while available Smarty variables depend on the template and are less predictable.

Common Smarty variables in contribution templates include:

| Variable              | Meaning                                  | Example usage                |
|
-----------------------|------------------------------------------|------------------------------|
| `$isShowLineItems`    | Is the contribution using a price set?   | `{if $isShowLineItems}...{/if}` |
| `$isShowTax`          | Is sales tax enabled for the site?       | `{if $isShowTax}...{/if}`        |
| `$taxRateBreakDown`   | Array of tax rate breakdowns             | `{foreach from=$taxRateBreakDown item=taxDetail key=taxRate}{$taxDetail.percentage}%{/foreach}` |
| `$lineItem`           | Array of line items for contributions    | See template code example    |

## Configuring message templates

To configure message templates:

- Go to **Administer CiviCRM > Communications > Message Templates**.

- You can add, edit, preview, disable, or delete templates.

**Creating a new template:**

- Click **New Message Template**.

- Enter a title, subject, and HTML message (using tokens as needed).

- Leave the text message blank unless you need to customise it.

- Enable the template and save.

**Managing existing templates:**

- Edit: Change content or enable/disable the template.

- Disable: Temporarily turn off the template.

- Delete: Remove the template permanently.

<!--
Source: https://docs.civicrm.org/some/page/
 -->

<!--
This page systematically describes the features and options for message templates, with factual details and configuration steps, matching the Diátaxis "Reference" category. It is basic
-level, suitable for new non-profit users. For clarity, step-by-step creation could be split into a Tutorial, and troubleshooting could be added as a Guide if needed. -->
