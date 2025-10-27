---
categories: Guide
level: Intermediate
summary: Learn how to set up and manage automatic email or SMS reminders for contacts, events, memberships, activities, and contributions in CiviCRM.
section: Email > Scheduled reminders
---

# Scheduled reminders

## What are scheduled reminders?

Scheduled reminders let your organisation automatically send emails or SMS messages to contacts when certain conditions are met, such as before an event, when a membership is about to expire, or after a donation is made. You can use reminders for:

- Contacts (e.g., birthdays or anniversaries)
- Activities (e.g., interviews or meetings)
- Memberships (e.g., renewals or engagement)
- Events (e.g., attendance reminders)
- Contributions (e.g., donation follow-ups)

You can create and manage reminders at **Administer > Communications > Schedule Reminders**. For events, reminders can also be set up directly on the event configuration pages.

## Personalising reminders with tokens

You can use *tokens* in your reminder messages to automatically include details like event location, membership expiry date, or the recipient’s name. Tokens help you create one template that works for multiple situations. The *checksum* token allows contacts to access specific pages without logging in, with forms pre-filled for them.

## Creating and managing reminders

To set up a scheduled reminder:

- Give your reminder a clear name.
- Select the type of record (Entity) the reminder is for (e.g., event, membership).
- Choose the specific options for your reminder (multi-select is available).
- Decide when to send the reminder (e.g., a set date, or a number of days before or after an event).
- If you want the reminder to repeat, check the Repeat box and set the interval.
- If you want to track who received the reminder, check Record activity for automated email.
- Specify the sender’s name and email if different from the site default.
- Limit or add to your recipient list as needed.
- Choose whether to send by email, SMS, or both (SMS requires an SMS gateway).
- Write your message, or use a template.
- Click Save.

You can edit, disable, or delete reminders from the same administration page.

**Important:** Your system administrator must ensure the "Send Scheduled Reminders" scheduled job is enabled and runs at least once a day. If this job is not running, reminders will not be sent.

## Using reminders for different CiviCRM components

### Contacts

Set reminders for dates like birthdays, anniversaries, or custom date fields. You can send reminders every year (for recurring events) or only once (for non-repeating events). By default, all contacts with the relevant date will receive the reminder, but you can limit recipients (e.g., only children).

### Activities

Send reminders based on activity type and status (e.g., scheduled, completed, cancelled). You can target assignees, activity targets, or sources. Examples include:

- Reminding staff about upcoming interviews
- Notifying donors or executives about completed calls
- Sending thank-you notes after meetings

### Contributions

Send emails to donors based on the donation page or financial type, and filter by contribution status.

### Memberships

Send reminders based on membership type and status, such as renewal reminders before expiry, engagement emails after joining, or follow-ups for pending payments.

#### Example: Renewal reminders

To send a renewal reminder 5 days before membership expires:

- Set Entity Type to Membership
- Select Membership Types
- Exclude auto-renewing memberships if needed
- Set When to 5 days before Membership End Date
- Do not repeat
- Choose Email and select a template

#### Example: Chasing pending membership payments

- Create a smart group for contacts with pending membership status
- Set Entity Type to Activity, Membership Signup, Completed
- Restrict recipients to the pending smart group

### Events

Set reminders for specific events or event types, and filter by participant status or role. Examples include:

- Reminding volunteers before an event
- Sending feedback requests after events
- Thanking speakers or hosts
- Following up with no-shows

Reminders set for a specific date are sent only on that date. Reminders set relative to event start or end are sent to all who registered before the event ends.

## Limiting or adding recipients

You can limit recipients by group, participant role, or manually selected contacts. Use the "Limit to" option to restrict recipients, or "Also include" to add extra contacts who do not meet the general criteria. For example, you can include your office manager in event reminders even if they are not registered.

## Troubleshooting: Why reminders might not be sent

If reminders are not being sent, check for:

- Contact is deleted or marked as deceased
- Privacy options like "Do not email" or email address is on hold
- Membership status override is enabled (for renewal reminders)
- "Send Scheduled Reminders" job is not enabled or not running
- Reminder is disabled or criteria not met
- Recipient is not included in the "Limit to" option
- Reminder trigger date has passed or not met

You can check reminder activity by searching for "Reminder Sent" or "Membership Renewal Reminder" activities.

## Privacy options

Scheduled reminders are sent even to contacts who have opted out of bulk emails, unless they have "Do not email" or their email is on hold. To exclude contacts who opted out of bulk emails, create a smart group of contacts without these privacy options and use it as your recipient group.

# comment: Source: https://docs.civicrm.org/some/page/
# comment: Suggestion: This page is best classified as a Guide, as it provides step-by-step instructions for achieving specific goals (setting up and managing scheduled reminders), with practical examples and troubleshooting. Some sections (like tokens and privacy) could be split off into Reference or Explanation for advanced users. Level is Intermediate because users need some familiarity with CiviCRM administration.