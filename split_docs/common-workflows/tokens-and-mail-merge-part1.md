# Source: https://docs.civicrm.org/user/en/latest/common-workflows/tokens-and-mail-merge/

---
categories: Guide  
level: Basic  
summary: This guide explains how non-expert users of CiviCRM can use tokens to personalize emails and printed materials, and how to set up mail merges to save time and improve communication.  
section: Common workflows  
---

# Tokens and mail merge

## Overview

In CiviCRM, you can personalize your emails and printed letters by using **tokens**. Tokens are placeholders that automatically fill in information from your database, like a contact’s first name or your organization’s address. This helps you create mail merges that feel personal and save you time.

## Using basic contact data tokens

To greet someone by their first name in an email, type your greeting (for example, "Dear") and then click **Insert Tokens** above the message box. Search for "First name" and select the token `{firstname}`. When the email is sent, each person will see their own first name in the greeting.

You can explore the Insert Tokens popup to find many other tokens, including any custom fields your organization has added.

## Adding organizational tokens

You can also include your organization’s details, such as the postal address or phone number, using tokens like `{domain.address}`. These pull information from your organization’s settings, so your mailings always have the correct contact info.

## Special tokens for emails

Some tokens add special functions to your emails:

- **Action tokens** like `{action.optOutUrl}` and `{action.unsubscribeUrl}` add links that allow recipients to opt out or unsubscribe from mailings, which is required by law for mass emails.

- **Checksum tokens** create personalized links that let recipients update their information or register for events without filling in their details again. These links are secure and expire after seven days.

## Required tokens for mass emails

Every mass email sent through CiviMail must include:

- An **opt-out** or **unsubscribe** link token (`{action.optOutUrl}` or `{action.unsubscribeUrl}`)

- Your organization's address token (`{domain.address}`)

You can add these tokens directly in your email or include them in a standard footer so you don’t have to add them every time.

## Using checksum tokens for personalized links

Checksum tokens let you send links to forms or pages that are already filled with the recipient’s information. This makes it easier for people to donate, renew memberships, register for events, or sign petitions.

Here are examples of how to build these links for different platforms (replace `IDNUMBER` with your page or event ID):

| Platform | Contribution page link example |
|---|---|
| Drupal | `http://example.org/civicrm/contribute/transact?reset=1&id=IDNUMBER&{contact.checksum}&cid={contact.contact_id}` |
| Joomla! | `http://example.org/index.php?option=com_civicrm&task=civicrm/contribute/transact&reset=1&id=IDNUMBER&{contact.checksum}&cid={contact.contact_id}` |
| WordPress (Clean URLs) | `http://example.org/civicrm/contribute/transact?reset=1&id=IDNUMBER&{contact.checksum}&cid={contact.contact_id}` |
| WordPress (No Clean URLs) | `http://example.org/?civiwp=CiviCRM&q=civicrm/contribute/transact&reset=1&id=IDNUMBER&{contact.checksum}&cid={contact.contact_id}` |

Similar links exist for membership renewals, profiles, event registrations, petitions, and viewing mailings in a browser.

## Site tokens

Starting with CiviCRM 5.76, administrators can create **Site Tokens**—predefined snippets like logos or standard messages—that can be inserted automatically into emails or other communications. These tokens help keep your messages consistent and branded.

## Custom tokens

Developers or site administrators can create **custom tokens** to include special information, like total contributions from a contact. This requires some technical setup but can make your mail merges even more personalized.

## Date tokens

Tokens that show dates and times, such as `{event.start_date}` or `{domain.now}`, automatically format according to your site’s date preferences. You can customize how these dates appear using formatting options.

## Using Smarty in mail templates

CiviCRM mail templates use the **Smarty** template language to add logic and conditions to your messages. For example, you can show different text based on whether a membership is a gift. Enabling Smarty requires a small change to your system settings and some basic coding knowledge.

## Tracking links with tokens in emails

From CiviCRM version 5.35 onward, links containing tokens in their query parameters can be tracked in CiviMail reports. This means you can see how many people clicked personalized links like donation pages. Tokens must be placed in the URL query part (after `?`) to be tracked correctly.

## Available tokens summary

Here are some common tokens you can use in your mailings:

| Token | Purpose | Example use |
|---|---|---|
| `{action.optOutUrl}` | Link for recipients to opt out | *You can <a href="{action.optOutUrl}">opt-out</a> anytime.* |
| `{action.unsubscribeUrl}` | Unsubscribe link | *Click here to <a href="{action.unsubscribeUrl}">unsubscribe</a>.* |
| `{domain.address}` | Organization's postal address | *Mailing address: {domain.address}* |
| `{contact.custom_nn}` | Custom contact field content | *Thanks for your interest in {contact.custom_1}.* |
| `{mailing.viewUrl}` | Link to view email in browser | *Can't see this email? <a href="{mailing.viewUrl}">View in browser</a>* |

---

If you want to explore more advanced uses of tokens or set up custom tokens, consider creating separate pages for those topics to keep this guide focused and easy to follow.