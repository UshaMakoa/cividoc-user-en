---
categories:
  - Explanation
level: Basic
summary: Learn the key concepts, options, and important questions about using email in CiviCRM, so your organisation can plan effective and compliant communications.
section: Email
---

# What you need to know about email in CiviCRM

## Key concepts

Email is a central part of CiviCRM, helping your organisation communicate with contacts in three main ways:
- **Sending to individuals or small groups** using the Send Email action.
- **Sending to large groups** as a mass mailing using CiviMail.
- **Sending automated emails** as part of workflows in other components (for example, event confirmations).

A key benefit of sending email through CiviCRM is that every email is recorded as an activity in each recipient’s history. This lets you track your communications and see, for example, if a donation followed a newsletter or if a volunteer was contacted about an event.

## Send Email versus CiviMail

CiviCRM offers two main options for sending email:

- **Send Email action:** Best for individuals or small groups (up to 50 recipients). Quick, simple, and works even if CiviMail is not enabled. However, it provides only basic tracking—just a record that the email was sent.
- **CiviMail:** Designed for mass mailings or scheduled emails. Offers advanced features like bounce processing, reporting, subscription management, and reply tracking. Requires more setup, but is essential for larger or more complex campaigns.

**Choosing the right method** depends on your needs:

- Use Send Email if you are contacting fewer than 50 people and do not need detailed tracking.

- Use CiviMail for larger groups, or if you want to track opens, clicks, or manage subscriptions.

## When to use each method

- **Send Email action:** Quick and easy for small numbers. You can attach files, CC/BCC contacts, and use templates. Replies are not tracked in CiviCRM, so it’s not ideal for ongoing conversations.
- **CiviMail:** Required for 50+ recipients, or when you want to gather statistics (like open rates and clicks), manage sign-ups, or handle unsubscribes automatically.

## Choosing recipients

- **Send Email:** Choose recipients directly from a contact record or from search results.
- **CiviMail:** Send to Groups marked as Mailing Lists (which you create in advance) or from search results. All CiviMail messages must include an unsubscribe link. If you use Groups, unsubscribes are managed automatically.

## Personalisation with tokens

Both Send Email and CiviMail let you personalise messages with tokens (like a contact’s name). CiviMail offers more token options than Send Email.

## From email addresses

You can send emails from your personal address, a general organisational address, or another person’s address (for example, an assistant sending on behalf of a manager).

## Headers, footers, and templates

- **Headers and footers:** Customise these for mass mailings (CiviMail only) to maintain consistent branding.
- **Templates:** Create and reuse email templates to save time and ensure consistency.

## Reporting

CiviMail provides detailed reports on mass mailings, such as how many people opened your email and which links they clicked.

## Mailing list sign-up and unsubscribing

CiviCRM can publish a sign-up form on your website. It automatically manages unsubscribes and opt-outs, ensuring compliance with privacy laws.

## Autofiling external emails

You can set up CiviCRM to record emails sent from your regular email client by BCC’ing a special address. These are automatically added to the relevant contact’s record.

## Key questions to consider

Before sending emails with CiviCRM, ask yourself:

- Do you need templates for recurring messages?

- Should every mailing include standard content (header/footer)?

- Do you want a public sign
-up page?

- Which emails should be stored in contact records?

- How many recipients are you emailing?

- Do you want to track opens and clicks?

- Have you set up Groups or Smart Groups for your recipients?

- Who should be listed as the sender?

## Interaction with other tools

Many CiviCRM components (like Events and Contributions) use email for confirmations and receipts. Check component
-specific sections to learn how to customise these emails.

## Privacy, spam, and deliverability

- Be aware of privacy laws, especially around opt
-outs and tracking.

- Mass emails can be marked as spam, which may affect future delivery—consult an expert if needed.

## Email and template design/layout

- Use well
-designed, consistent templates for branding.

- Responsive design is challenging; consider using tested free templates.

- Keep layouts simple and use tables for structure.

- Use inline CSS for consistent appearance.

- Test your emails on different devices and clients.

- Balance design and content—both are important for effective communication.

---

<!--
Source: https://docs.civicrm.org/user/en/latest/email/what
-you-need-to-know/ -->

<!--
This page is an Explanation under Diátaxis: it provides background, key concepts, and context for using email in CiviCRM, helping users understand options and make informed decisions before taking action. It does not give step
-by-step instructions (Tutorial), solve a specific problem (Guide), or list exhaustive technical details (Reference). Level is Basic, as it is aimed at new or non-expert users planning their approach. -->
