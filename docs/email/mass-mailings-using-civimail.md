---
categories:
  - Tutorial
level: Basic
summary: Learn how to create and send mass mailings in CiviMail, from selecting your audience to designing, testing, and reviewing your campaign.
section: Email and communications
---

# Sending mass mailings using CiviMail

Mass mailings are a key part of staying in touch with supporters, members, and donors.

CiviMail makes it simple to send newsletters, announcements, and updates to large groups of people while tracking who opens, clicks, or unsubscribes.

## What you'll need before you start

Before sending a mass mailing, ensure that:

- CiviMail has been set up and tested on your system.  
- You have permission to use the Mailings menu.  
- Your contact list or Smart Group is ready and updated.  
- Your organisation's sender details and unsubscribe tokens are configured.  

These steps ensure your emails work smoothly and reach your audience reliably.

## Step 1: Create a new mailing

1. Go to **Mailings → New Mailing**.  
2. Give your mailing a clear name, like “April Newsletter” or “Event Reminder”.  
3. Choose your **From Address**.  
4. Select your **recipient group** (a static list or Smart Group).  
5. Click **Continue** to begin editing.

### Tip
Double-check recipients before sending to avoid test or outdated lists.

## Step 2: Write and design your message

You can:

- Write directly in the editor, or  
- Use a saved message template for branding consistency.  

Add your subject, body text, and images. Keep your message short with a clear call to action (donation, registration, etc.).

Include personalisation tokens (like `{contact.first_name}`) for a friendly tone.

## Step 3: Add tracking and footer details

Enable tracking for opens and clicks.  
Ensure your footer has:

- Organisation contact info  
- Unsubscribe link `{action.unsubscribe}`  
- Address token `{domain.address}`  

This ensures compliance and accurate tracking.

## Step 4: Send a test message

Before full delivery:

1. Click **Send Test** and use internal addresses.  
2. Confirm links, layout, and personalisation display properly.  

If something looks off, update and retest.

## Step 5: Schedule or send

Choose to:

- **Send immediately**, or  
- **Schedule for later** (specific date/time).  

CiviCRM handles queueing and delivery automatically.

## Step 6: Monitor mailing progress

Track live under **Mailings → Scheduled and Sent Mailings**.

Reports display:

- Emails sent  
- Opens  
- Clicks  
- Bounces  
- Unsubscribes  

Use this to gauge engagement.

## Step 7: Review your results

Once complete, review detailed reports:

- High opens = good subject line  
- High clicks = engaging content  
- High bounces/unsubs = list or content issues  

## Step 8: Reuse a mailing

Repeated newsletters?  
Go to **Scheduled and Sent Mailings → Reuse Mailing**, then update details.

## Best practice

- Always test before sending.  
- Keep lists clean and current.  
- Use mobile-friendly designs.  
- Avoid large attachments.  
- Review reports regularly.
