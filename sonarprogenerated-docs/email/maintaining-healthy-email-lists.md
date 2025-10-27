---
categories: Guide
level: Basic
summary: Learn how to keep your organisation’s CiviCRM email lists healthy, avoid common problems like bounces and unsubscribes, and understand what actions to take when issues arise.
section: Email > List management
---

# Maintaining healthy email lists

## Understanding email bounces

When you send bulk emails using CiviMail, some messages may not reach their recipients—this is called a “bounce.” Bounces can happen for several reasons:
- The email address was entered incorrectly.
- The email address no longer exists.
- The recipient’s inbox is full.
- The recipient has set an automatic reply (for example, they are on vacation).

CiviCRM treats bounces differently depending on their type:
- **Temporary bounces**: CiviCRM will try sending emails to these addresses again in the future.
- **Permanent bounces**: The email address may be put “on hold,” meaning no further emails will be sent until the issue is fixed.

If you notice a high rate of bounces, it may indicate a deeper issue with your contact data or list management.

## What to do if an address is put on hold

If an email address is put on hold, you have two main options:
- **Release the hold**:  
  1. Go to Advanced Search.
  2. In Basic Search Criteria, check the box to search for Emails On Hold.
  3. Select the contacts with held emails.
  4. Choose “Unhold Emails” from the dropdown list and click Go.

- **Correct or update held emails**:  
  1. Create a group for bad emails.
  2. Go to Reports and select Mail Bounce Report to see contacts whose emails have bounced.
  3. Use Report Criteria to filter by bounce type if needed.
  4. Add these contacts to your group.
  5. Use Advanced Search to find the group and select “Email on Hold” to avoid outdated records.
  6. Use “Batch Update via Profile” for contacts whose emails you can fix. Make sure your profile includes the Primary Email field.
  7. Select the profile and click Update.

## The difference between on hold emails and unsubscribes

- **On hold**: The email address is temporarily blocked due to delivery issues (like bounces).  
- **Unsubscribed**: The recipient has clicked an “unsubscribe” link in your email and will be removed from the mailing list group.

## Opting out vs. unsubscribing

- **Opting out**: Recipients click a link (using the {action.optOut} or {action.optOutUrl} token) to stop receiving any bulk emails from your organisation. You can still send individual emails using the Send Email action, and scheduled reminders may still be sent unless you exclude them.
- **Unsubscribing**: Recipients leave a specific mailing list but may still receive other emails from you.

## Privacy option: “Do not email”

If a contact’s record has “Do not email” selected:
- You cannot send them any individual or bulk emails.
- Scheduled reminders may still be sent unless you specifically exclude them.

To fully ensure a contact does not receive any emails, remove all email addresses from their record. Note: This will prevent them from logging in to your website.

# comment: Source: https://docs.civicrm.org/some/page/
# comment: This page is best classified as a Guide, as it addresses practical problems and actions for users maintaining email lists. It is written for basic-level users who are learning to manage email communications in CiviCRM. The content is action-oriented and does not provide deep background or exhaustive technical details, so it does not fit the Reference or Explanation categories. If needed, background on bounces and privacy options could be split into an Explanation page, and step-by-step instructions for releasing holds could form a Tutorial.