---
categories:
  - Guide
level: Basic
summary: Learn how to set up and manage online event registration in CiviCRM so people can easily sign up for your events through your website.
section: Events > Online event registration
---

# Online event registration

## What is online event registration?

Online event registration in CiviCRM lets people sign up for your events directly from your website, making it easier for your organisation and your participants. This reduces your administrative work and allows participants to register at their convenience.

The typical registration process includes:

- Viewing event information (date, location, details)

- Completing the registration form (including fees and participant info)

- Confirming registration and payment (if required)

- Receiving a thank you message and confirmation email

## How to set up online registration

1. **Enable online registration**

- When creating or editing an event, check the “Allow Online Registration” box in the Online Registration section.

- Set the link text (e.g., "Register Now") that appears on the event page.

- Choose the registration start and end dates. The end date can be before the event starts, allowing you time for preparations.

2. **Allow multiple registrations (optional)**

- Enable “Register multiple participants” if you want people to register more than one person at a time, such as a group from an organisation or a family.

- By default, each registrant must have a unique name and email. If you want to allow the same email for multiple registrations, check the “Allow same email and multiple registrations?” option.

3. **Pending participant expiration**

- Set how long (in hours) a registration can remain “pending” before it is automatically cancelled if not completed. This helps manage incomplete registrations, especially when using “pay later” options.

4. **Self
-service cancellation or transfer**

- Allow participants to cancel or transfer their registration themselves via a link in their confirmation email.

- Set a time limit (in hours) before the event start after which cancellations or transfers are no longer allowed.

## Collecting participant information with profiles

- Use CiviCRM “profiles” to collect information from registrants, such as name, email, or custom questions.

- You can add one profile at the top of the registration form (often called “Your Registration Info”) and more profiles after fee/payment sections if needed.

- By default, the top profile collects first name, last name, and email. You can customise this or create a new profile with the fields you need.

- If you don’t want to collect email addresses, make sure to turn off confirmation emails.

**Tip:** If you edit a profile that is used elsewhere, changes will affect all forms where it appears. To avoid this, copy and rename the profile before editing.

- You can create profiles and custom fields directly from the registration setup page.

- Each profile appears as a section with a heading (the “Public Title” or profile name).

**Advanced options:**

- Add registrants to a group (e.g., for follow
-up emails).

- Require or offer website user account creation during registration.

- Add a CAPTCHA to prevent spam registrations.

## Registration confirmation and emails

- Set up the text for the confirmation page, thank
-you page, and confirmation/receipt emails.

- For free events, the confirmation step is skipped.

- For paid events, payment is processed between the confirmation and thank
-you pages.

- Enable “Send Confirmation Email” so registrants get an email receipt (required for paid events).

- The “From” email address must be valid on your mail server.

- Avoid using HTML tags in the text field, as the message is sent in both plain text and HTML formats.

## Email alerts for event registrations

- Add staff email addresses in the “CC Confirmation To” or “BCC Confirmation To” fields to receive real
-time notifications of new registrations.

- Enter email addresses separated by commas.

- Make sure these email addresses are correct and active. If emails bounce, CiviCRM may mark the registrant’s email as “On Hold,” preventing future emails.

## Optional event registration features

### Waitlists

- Set a maximum number of registrants for your event.

- When the event is full, people can add themselves to a waitlist.

- As spaces become available (e.g., cancellations), people on the waitlist are invited by email to complete their registration.

- The time allowed for waitlisted participants to register is set by the “Pending participant expiration (hours)” field.

- To use waitlists, enable the “On waitlist” and “Pending from waitlist” statuses in Administer > CiviEvent > Participant statuses, and turn on “Offer Waitlist” in your event settings.

- Make sure the “Update Participant Statuses” scheduled job is running.

### Participant approval

- For invitation
-only events, enable “Require participant approval.”

- Registrants are placed in “Awaiting Approval” status until you review and approve them.

- Approved participants receive an email to complete registration and payment.

- Set how long (in hours) approved participants have to finish registration.

- Enable the necessary statuses in Administer > CiviEvent > Participant statuses, and ensure the “Update Participant Statuses” scheduled job is active.

### Personal Campaign Pages (PCPs)

- Allow registrants to create a personal fundraising or promotion page for the event.

- For more details, see the section on Personal Campaign Pages in the Contributions chapter.

## Contact matching and duplicate management

- CiviCRM checks for duplicate contacts when someone registers.

- By default, the “Unsupervised” duplicate rule is used, but you can select a different rule for each event.

- The system checks if the registration form collects enough information to match existing contacts. Warnings will appear if there is not enough data to avoid duplicates.

- For more about managing duplicates, see the Deduping and Merging chapter.

## Registration permissions

- Check your website’s user permissions to allow the right people to register for events.

- Most organisations allow “anonymous” users (not logged in) to register. Assign these permissions:

  - access all custom data (if collecting custom fields)
  - profile create (if using profiles)
  - register for events
  - view event info
  - view event participants (if you want to show a list of registrants)

- If you want only logged
-in users to register, assign permissions to the “authenticated user” role.

- CiviCRM’s Access Control Lists (ACLs) can further restrict access to specific events or groups.

- See the Permissions and Access Control chapter for more information.

## Testing the registration process

- Always test your event registration before making it public:

- Go to Events > Manage Events.

- Use the “Test
-drive” link to try the registration form. This uses test payment options and marks the record as a test.

- Complete the registration process and check the participant record in Events > Find Participants (check “Find Test Participants”).

- Adjust event settings as needed and retest.

- If anonymous registration is allowed, test while logged out as well.

Once you are satisfied, you can display your event registration form on your website.

---

<!--
Source: https://docs.civicrm.org/user/en/latest/events/online
-event-registration/ -->

<!--
This content is a practical, step
-by-step "how-to" for setting up and managing online event registration in CiviCRM. It is not a tutorial for first-time users, nor is it a reference or explanation. The page is best categorised as a Guide, with a Basic level, and belongs in the Events > Online event registration section. -->
