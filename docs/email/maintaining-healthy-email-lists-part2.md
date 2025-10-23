---
categories:
  - Uncategorized
  - Guide
level: Intermediate
summary: Learn how to configure bounce handling and unsubscribe links in CiviMail so your mailings stay accurate, compliant, and well maintained.
section: Email and communications
---

# Configuring bounce and unsubscribe handling

CiviMail can automatically manage bounces and unsubscribes to keep your mailing list clean and compliant.

## Why it matters

Proper setup ensures:

- Data accuracy  
- Legal compliance (GDPR, CAN-SPAM)  
- A good sender reputation  

## Setting up bounce handling

1. Create an email inbox dedicated to bounces.  
2. Add access details in **Admin → Mail Settings**.  
3. Test retrieval and tracking.  

CiviMail will log each bounce in contact records automatically.

## Adding unsubscribe and resubscribe links

Every bulk email must contain:

- `{action.unsubscribe}` – unsubscribe link  
- `{domain.address}` – contact details footer  
- `{action.resubscribe}` – optional re-opt-in link  

## Testing unsubscribe links

Before a live send:

1. Send a test email and click the unsubscribe link.  
2. Verify updates in the contact record.  

## Best practice

- Only one bounce inbox per site.  
- Always include mandatory tokens.  
- Never delete unsubscribe sections.  
- Test bounce processing regularly.
