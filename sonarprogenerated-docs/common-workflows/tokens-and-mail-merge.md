---
categories: Reference
level: Basic
summary: Learn how to use tokens in CiviCRM to personalize emails and printed letters for your contacts.
section: Common workflows
---

# Tokens and mail merge

## What are tokens?

**Tokens** are special codes you can add to emails or letters in CiviCRM to automatically insert information from your database, such as a contact’s name, your organisation’s address, or custom fields. When you send a message, CiviCRM replaces each token with the correct information for each recipient.

## Where can you use tokens?

You can use tokens in:
- **Emails** (including mass mailings with CiviMail)
- **Printed letters and mailing labels**
- **PDF letters and receipts**

Most contact fields, including custom fields you’ve created, are available as tokens.

## How to insert tokens

1. When writing an email or letter in CiviCRM, look for the **Insert Tokens** button (usually at the top right of the editor).
2. Click it to open a list of available tokens.
3. Find the token you want (for example, “First name”) and select it.
4. The token (like `{contact.first_name}`) will appear in your message.
5. When you send your message, CiviCRM will replace the token with the correct value for each recipient.

*Tip: Browse the Insert Tokens pop-up to see all available tokens, including your custom fields.*

## Common types of tokens

- **Contact tokens**: Personalize with fields like first name, last name, or custom data (`{contact.first_name}`, `{contact.custom_1}`).
- **Organizational tokens**: Include your organisation’s address, email, or phone (`{domain.address}`, `{domain.email}`).
- **Action tokens**: Add links for recipients to unsubscribe, opt-out, or resubscribe (`{action.unsubscribeUrl}`, `{action.optOutUrl}`).
- **Special tokens for emails**: Some tokens create links (URLs). When using these, make sure to place the token in the URL field of the link, not just as plain text, so it becomes clickable for the recipient.

## Required tokens for mass emails

Every mass email sent with CiviMail must include:
- An **opt-out** or **unsubscribe** link (`{action.optOutUrl}` or `{action.unsubscribeUrl}`)
- Your organisation’s **address** (`{domain.address}`)

You can put these directly in your message, or include them in a standard footer or header for all mailings.

*Tip: Clickable unsubscribe and opt-out links are more user-friendly than asking people to reply by email. You can include both options if you wish.*

## Using checksum tokens for personalized links

The **checksum token** (`{contact.checksum}`) lets you send contacts special links to forms (like donation pages or event sign-ups) that are pre-filled with their information. This saves time for your contacts and helps keep your data up to date.

- **Security note:** Checksum links only work for seven days after the email is sent (this can be changed in your settings).
- **Tracking note:** Links with checksums are not tracked in CiviMail reports, as they are unique to each recipient.

### Examples of checksum links

Replace `IDNUMBER` with your page’s ID:
- **Contribution page:**  
  `http://example.org/civicrm/contribute/transact?reset=1&id=IDNUMBER&{contact.checksum}&cid={contact.contact_id}`
- **Membership renewal:**  
  `http://example.org/civicrm/contribute/transact?reset=1&id=IDNUMBER&{contact.checksum}&cid={contact.contact_id}&mid={membership.id}`
- **Profile update:**  
  `http://example.org/civicrm/profile/edit?reset=1&gid=IDNUMBER&{contact.checksum}&id={contact.contact_id}`
- **Event registration:**  
  `http://example.org/civicrm/event/register?reset=1&id=IDNUMBER&{contact.checksum}&cid={contact.contact_id}`
- **Petition signature:**  
  `http://example.org/civicrm/petition/sign?reset=1&sid=IDNUMBER&{contact.checksum}&cid={contact.contact_id}`
- **View mailing in browser:**  
  `http://example.org/civicrm/mailing/view?reset=1&id={mailing.key}&cid={contact.contact_id}&{contact.checksum}`

*Adjust the URL format for your CMS (Drupal, Joomla!, WordPress) as needed.*

## Site tokens

**Site tokens** are reusable snippets (like a message header or logo) that administrators can define and insert into emails and templates. For example, `{site.message_header}` is automatically added to the top of every message template, but you can customize its content.

Administrators can manage site tokens at:  
**Administer > Communications > Site Tokens**

## Custom tokens

Developers can create custom tokens to display special information, such as a contact’s total donations. (See the Developer Guide for details.)

## Date tokens

Tokens like `{event.start_date}` or `{domain.now}` can display dates and times, automatically formatted based on your organisation’s settings. You can also customize date formats using the `|crmDate` filter.

**Examples:**
- `{domain.now|crmDate:"Full"}` → September 19th, 2022
- `{domain.now|crmDate:"%B %Y"}` → September 2022

*For a full list of date formatting codes, see the PHP Manual for strftime().*

## Using Smarty in mail templates

CiviCRM mail templates use **Smarty**, a template language, to add logic or display variables. For example, you can use `{if}` statements or the `{capture}` function to include tokens in conditional text.

**Example:**
```smarty
{capture assign=first_name}{contact.first_name}{/capture}
{if $first_name}
  Hello, {$first_name}, how are you?
{/if}
```
*System administrator access is required to enable Smarty in your CiviCRM settings.*

## Click tracking for token links in CiviMail

CiviMail can track how many people click links in your emails, even if those links include tokens (for example, personalized donation links). However, tokens must be in the **query part** of the URL (after the `?`). Tokens in the domain or path will not be tracked.

**Allowed:**  
`https://example.org/page?magic={some.token}`

**Not allowed:**  
`https://{some.token}.org/` or `https://example.org/{some.token}`

*Make sure your tokens only insert safe data into URLs (for example, use IDs or codes, not names with spaces or special characters).*

## List of available tokens

Below are some commonly used tokens and their purposes:

| Token                     | Purpose                                                   | Example use                                  |
|---------------------------|-----------------------------------------------------------|----------------------------------------------|
| `{action.optOutUrl}`      | Opt-out link for recipient                                | `<a href="{action.optOutUrl}">opt-out</a>`   |
| `{action.unsubscribeUrl}` | Unsubscribe link for recipient                            | `<a href="{action.unsubscribeUrl}">unsubscribe</a>` |
| `{domain.address}`        | Your organisation’s postal address                        | `Mailing Address: {domain.address}`          |
| `{contact.first_name}`    | Recipient’s first name                                   | `Dear {contact.first_name},`                 |
| `{mailing.viewUrl}`       | View mailing in browser link                             | `<a href="{mailing.viewUrl}">View in Browser</a>` |
| `{contact.custom_nn}`     | Custom field value for contact                           | `Your interest: {contact.custom_1}`          |
| `{site.message_header}`   | Custom message header (set by admin)                     | Appears at top of message templates          |

*For a full list of tokens, use the Insert Tokens tool when editing your message.*

---

# comment: Source: https://docs.civicrm.org/user/en/latest/common-workflows/tokens-and-mail-merge/
# comment: This page is best categorized as Reference, as it systematically lists facts about tokens, their usage, and available options, with minimal procedural or explanatory content. The audience is non-expert, so the level is Basic. The logical section is "Common workflows" as per the CiviCRM User Guide structure. If desired, a separate Tutorial or Guide could be created for "How to use tokens in a CiviMail mailing" or "How to create a mail merge letter," but this page itself is Reference.