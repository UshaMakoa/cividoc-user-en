---
categories:
  - Tutorial
level: Intermediate
summary: Learn how to test and troubleshoot common CiviMail delivery issues to make sure your emails reach supporters reliably.
section: Email and communications
---

# Testing and troubleshooting email delivery

Even properly configured systems may face delivery problems.

This guide helps identify and resolve email delivery issues.

## Step 1: Send a test message

- Send to internal addresses.  
- Check From details, images, and tokens.  
- Confirm unsubscribe footer works.  

## Step 2: Common delivery issues

If the message is missing or delayed:

- **Check spam folder**  
- Verify **sender domain** matches organisation  
- Review **Scheduled and Sent Mailings** queue  

## Step 3: Confirm domain authentication

Work with admins to validate **SPF/DKIM** DNS records.

These confirm your authority to send on your domain’s behalf.

## Step 4: Check message content

Avoid spam triggers:

- “FREE”, “Act now”, excessive caps  
- Unverified external links  

## Step 5: Review bounce data

Review mailing reports to identify invalid addresses or blocked messages.

Clean invalid contacts to maintain reputation.

## Step 6: Fix resubscription issues

- Verify **Do Not Email** isn’t falsely active.  
- Ensure unsubscribe/resubscribe works properly.  

## Step 7: Tracking

Confirm:

- Open/click tracking is active  
- Links resolve correctly  
- Changes to the web server didn’t block analytics  

## Step 8: When to ask for help

If issues persist, contact your admin with logs and bounce codes.

## Best practice

- Test systems monthly.  
- Clean lists regularly.  
- Send gradually to new audiences.  
- Monitor results for early warnings.
