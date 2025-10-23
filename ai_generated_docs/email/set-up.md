---
categories: Guide
level: Basic
summary: Learn how to prepare your system for CiviMail, including setting permissions and adding trusted sender addresses.
section: Email and communications
---

# Preparing your system for CiviMail

Before sending newsletters or campaign messages, you need to make sure your CiviCRM system is ready to use CiviMail.

This page explains how to confirm access permissions and set up the email addresses your organisation will use for sending.

## Why preparation matters

CiviMail is a bulk email tool that connects directly to your contact records.

Setting it up properly helps ensure that your messages:

- Are sent only by authorised users  
- Come from recognised and trusted addresses  
- Reach your audience's inboxes reliably  

## Checking user permissions

Only users with the correct permissions can use CiviMail.

If you don't see the **Mailings** menu, ask your administrator to review your access.

Typical roles might include:

- **Administrators** who configure system settings  
- **Communications staff** who create and send mailings  
- **Support staff** who view reports but cannot send  

## Setting up sender addresses

Each mailing needs a valid **From**, **Reply-To**, and optional **Bounce** address.

Your organisation should use professional, monitored email accounts—never personal ones.

When adding or reviewing sender addresses, make sure they:

- Use your organisation's domain (for example, *info@yourcharity.org*)  
- Represent your organisation clearly in the **From Name**  
- Belong to an inbox that is monitored for replies  

You can create multiple From addresses for different teams or campaigns, but they should all follow the same format and be approved for use.

## Verifying sender identity

To improve deliverability, your admin may configure SPF and DKIM.

These tell mail providers that CiviCRM is authorised to send emails on behalf of your domain.

If your emails go to spam or are rejected, ask your admin to verify these settings.

## Best practice

- Use consistent sender details.  
- Keep email addresses updated.  
- Avoid generic addresses that no one checks.  
- Test each new sender before a full send.
