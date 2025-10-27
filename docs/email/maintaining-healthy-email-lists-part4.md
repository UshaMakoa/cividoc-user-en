---
categories:
  - Guide
level: Intermediate
summary: Learn how to test and maintain your CiviMail setup to ensure reliable delivery and accurate tracking over time.
section: Email and communications
---

# Testing and maintaining your CiviMail setup

Once configured, CiviMail should be tested regularly to ensure reliable communication.

## Testing setup

1. Create and send a test message internally.  
2. Confirm delivery and display.  
3. Review **opens/clicks** tracking.  
4. Verify unsubscribe and bounce handling.  

## Checking deliverability

If emails land in spam:

- Confirm SPF/DKIM records are valid.  
- Keep consistent “From” domain.  
- Avoid spammy subject lines.  

## Monitoring bounces/unsubscribes

Regularly check reports:

- High bounce = bad data  
- High unsubscribes = content or frequency issue  

## Maintaining setup

- Verify configuration annually.  
- Review templates after updates.  
- Remove outdated senders and test accounts.  

## Best practice

- Always test before large sends.  
- Keep reports reviewed.  
- Document your configuration steps.
