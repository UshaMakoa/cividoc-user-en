---
categories:
  - Guide  
level: Basic  
summary: This guide explains how non-profit users can set up and manage online event registration in CiviCRM, including configuring registration forms, managing participants, and using optional features like waitlists and participant approval.  
section: Events  
---

# Online event registration

## Introduction

Online event registration lets your supporters sign up for events at their convenience, saving your organization time and effort. This guide walks you through the steps to set up and manage online registration in CiviCRM, so you can offer a smooth registration experience for your participants.

## Setting up online registration

To enable online registration for an event:

- When creating or editing an event, go to the **Online Registration** tab.
- Check **Allow Online Registration** to activate this feature.
- Customize the link text that appears on the event page, such as “Register Now.”
- Set the registration start and end dates. The end date can be before the event date to allow time for preparation.
- Optionally, enable **Register multiple participants** to let one person register several attendees in one transaction.
- Decide if you want to allow multiple registrations using the same email address by enabling **Allow same email and multiple registrations**.
- Set a time limit (in hours) for how long registrations with a pending status remain before expiring.
- Choose whether to allow participants to cancel or transfer their registration themselves and set any time limits for this.

## Collecting participant information with profiles

Profiles are forms that collect information from registrants. You can:

- Use the default profile “Your Registration Info” which collects first name, last name, and email.
- Modify this profile or create new ones with custom fields to fit your event’s needs.
- Add one profile above the fees section and additional profiles below fees and payment details.
- Be careful when editing existing profiles, as changes affect all places where the profile is used. It’s safer to copy and rename profiles for specific events.
- Include features like adding registrants to groups, requiring CMS user accounts, or adding CAPTCHA to prevent spam.

## Registration confirmation and emails

- Customize the text shown on the **Confirmation** and **Thank you** pages.
- For paid events, payment is processed after the confirmation page.
- Enable **Send Confirmation Email** to automatically email registrants a receipt or confirmation.
- Ensure the “Confirm From Email” address is valid and monitored.
- Avoid using HTML tags in confirmation email text to ensure compatibility.

## Email alerts for event registrations

- Add staff email addresses to **CC Confirmation To** or **BCC Confirmation To** fields to receive real-time notifications of new registrations.
- Use caution with these addresses to avoid bounce issues that could affect your contacts’ email statuses.

## Optional event registration features

### Waitlists

- Set a maximum number of participants for your event.
- When full, new registrants can join a waitlist.
- As spots open, waitlisted participants receive an email with a link to complete registration.
- Manage waitlist timing with the **Pending participant expiration** setting.
- Enable related participant statuses and scheduled jobs to automate waitlist processing.

### Participant approval

- Use this feature to approve registrations before they are confirmed.
- Enable participant statuses like **Awaiting approval** and **Pending from approval**.
- Customize messages for approval and set expiration times for completing registration after approval.
- Review and approve participants via the participant management interface.
- Scheduled jobs automate status updates.

### Personal Campaign Pages (PCPs)

- Allow registrants to create personalized pages to promote the event or fundraising.
- This is an optional feature enabled at the end of event setup.

## Contact matching and duplicate management

- CiviCRM uses duplicate matching rules to prevent creating duplicate contact records during registration.
- You can choose which duplicate matching rule applies for each event.
- Ensure your profiles collect enough information to allow effective matching.
- Be aware that requiring login for registration reduces duplicates but may lower registrations.

## Registration permissions

- To allow anonymous users to register, assign these permissions to the anonymous role:
  - Access all custom data (if collecting custom fields)
  - Profile create (if using profiles)
  - Register for events
  - View event info
  - View event participants (optional)
- Use Access Control Lists (ACLs) if you need more fine-grained permission control.

## Testing the registration process

Before making your event public:

- Use the **Test-drive** link in the event management screen to try registering.
- This uses sandbox payment settings and marks test participants for easy cleanup.
- Test both logged-in and anonymous user registrations.
- Adjust settings as needed based on your test results.

## Next steps

Once you have tested and are happy with your event registration setup, you can integrate your event with your website and start promoting it.
