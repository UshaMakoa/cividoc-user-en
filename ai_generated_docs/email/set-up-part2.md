---
categories: Guide
level: Basic
summary: Learn how to prepare your system for CiviMail by setting permissions, configuring sender addresses, and checking authentication.
section: Email and communications
---

# Preparing your system for CiviMail

Before sending newsletters or campaigns, you need to make sure CiviMail is ready to use.

This page explains how to prepare your system so that authorised users can send mailings safely and reliably.

## Why preparation matters

CiviMail is designed for bulk communication, but it relies on correct permissions and sender setup to work properly.

Setting up these elements first helps you avoid common problems such as undelivered messages, misleading sender details, or compliance issues.

## Checking user permissions

Only users with the correct permissions can create and send mailings.

Make sure your team has access to:

- Create and send mailings  
- Edit and reuse templates  
- View reports and mailing statistics  

If **Mailings** doesn’t appear in the menu, ask an administrator to review your permissions.

## Setting up sender details

Each mailing must include clear details about who it’s from.

You’ll need:

- A **From Name** — usually your organisation’s name or department  
- A **From Address** that uses your organisation’s domain (e.g. info@yourcharity.org)  
- A **Reply-To Address** that leads to an inbox that is regularly checked  

Consistency in sender details helps supporters recognise and trust your communications.

## Configuring multiple sender options

In larger organisations, you may want separate sender addresses for specific teams or campaigns:

- info@yourcharity.org for newsletters  
- membership@yourcharity.org for renewals  
- events@yourcharity.org for invitations  

Each address must belong to your domain and be authorised for sending.

## Checking email authentication

To improve deliverability, your technical staff should configure **SPF** and **DKIM** for your email domain.

Authentication records tell mail servers that CiviCRM is allowed to send messages for your organisation, reducing the risk of emails being flagged as spam.

## Testing access and sender setup

Before going live:

1. Send a test email to verify the setup.  
2. Check that the From address and name display correctly.  
3. Confirm that replies go to the right inbox.  

If something looks wrong, review the sender settings or permissions before proceeding.

## Best practice

- Keep sender details consistent.  
- Avoid sending bulk mail from personal addresses.  
- Use only your organisation’s domain.  
- Review who has mailing permission regularly.
