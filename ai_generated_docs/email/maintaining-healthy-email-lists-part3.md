---
categories: Guide
level: Intermediate
summary: Learn how to configure CiviMail to handle bounced emails and manage unsubscribe preferences automatically.
section: Email and communications
---

# Configuring bounce and unsubscribe handling

CiviMail can process bounced messages and handle unsubscribe requests automatically.

## Why it matters

Automatic bounce/unsubscribe handling ensures:

- Compliance with mailing laws  
- Clean lists and good sender reputation.  

## Setting up bounce handling

Admins should:

1. Create a specific mailbox for bounces.  
2. Add mail server credentials in **Admin → Mail Settings**.  
3. Test message retrieval.  

When active, CiviCRM updates contact records automatically.

## Unsubscribe options

Each mailing must include:

- `{action.unsubscribe}` and `{action.resubscribe}` tokens  
- Your organisation’s contact address  

This ensures compliance with GDPR and anti-spam laws.

## Testing unsubscribe links

Before live mailing, confirm:

- The link loads correctly  
- The contact record updates  
- Contact receives no more bulk mailings  

## Managing unsubscribed and bounced contacts

- Excluded automatically from future mailings  
- You can check **On Hold / Do Not Email** flags in records  

## Best practice

- Use dedicated inboxes for bounce handling.  
- Always include unsubscribe links.  
- Audit bounce and unsubscribe reports after every campaign.
