---
categories: Guide
level: Basic
summary: Learn how to manually register one or more participants for an event in CiviCRM, including handling payments and importing registrations.
section: Events > Event registration
---

# Manual event registration

Manual event registration lets you and your team register people for events directly in CiviCRM, which is helpful if someone calls your office, sends an email, or registers in person.

## Registering a participant manually

Follow these steps to register someone for an event:

1. Enter the person's name in the Quick search box at the top of CiviCRM.
2. Select the correct contact from the search results.
3. On their contact record, click the **Events** tab.
4. Click **Add Event Registration** if the person will pay later (by check or at the event), or **Submit Credit Card Event Registration** if you are taking their credit card payment now (this option appears only if your CiviCRM is set up with a payment processor).
5. Fill out the registration form. The fields may change depending on your choices (for example, if the event has custom questions or fees).
6. If the event has a fee, you can record a payment by checking **Record Payment** and filling in the payment details. This links the event registration with a financial transaction in CiviCRM.
7. Click **Save** to finish.

**Tip:** If you do not record a payment, only the registration will be saved. You can always add a payment later.

**Note:** Event registrations and payments are kept as separate records in CiviCRM. This means you can register someone without recording a payment, which is useful if you are waiving fees for a VIP or speaker.

## Registering a participant with a deposit (partial payment)

You can accept a deposit or partial payment when registering someone:

1. In the **Payment Information** section, enter the amount paid (less than the full event fee).
2. Set the **Participant Status** to **Partially paid**.
3. Save the registration.

To add more payments later:

1. Go to the participant’s contact record.
2. Click the **Events** tab.
3. Click **more** next to the event, then choose **Record Payment** or **Submit Credit Card payment**.
4. Enter the new payment details.

When the full fee is paid, the participant’s status will automatically update to **Registered**, and the payment status will show as **Completed**.

**Tip:** You can view all payments made by clicking **view payments** under the Total Paid amount on the registration, or by expanding the Contribution record at the bottom.

## Mass registrations

You can register several people for the same event at once:

1. Search for the group of contacts you want to register (for example, by going to **Search > Find Participants**).
2. On the search results page, select the people you want to register.
3. From the **Actions** menu, choose **Register participants for event** and click **Go**.
4. Choose the event and fill out the registration form. All selected contacts will get the same participant status and options.
5. Click **Save**.

**Limitations:**
- All selected contacts get the same status and options.
- You cannot mass-register for past events.
- You cannot record payments (such as pay-later or credit card) for multiple people at once. Mass registration works best for free events or when you do not need to record payment now. You can add payments individually later.

## Importing registrations

If you have many registrations in a spreadsheet, you can import them:

### Preparing your data

- Make sure all participants already exist as contacts in CiviCRM. If not, import contacts first.
- Your CSV file should include at least:
  - One field to match the contact (Contact ID, Email, or External Identifier)
  - Event ID
  - Participant Status

### Import steps

1. Go to **Events > Import Participants**.
2. Select your CSV file.
3. Choose the correct contact type, date format, and other options, then click **Continue**.
4. Match the columns in your file to CiviCRM fields.
5. (Optional) Save the field mapping for future imports.
6. Preview and complete the import.

# comment: Source: https://docs.civicrm.org/user/en/latest/events/manual-event-registration/
# comment: Suggestion: This page is a Guide, as it gives step-by-step instructions for specific tasks (manual, mass, and imported event registration) rather than teaching concepts (Explanation), providing a hands-on lesson (Tutorial), or listing exhaustive options (Reference). The level is Basic, as it is aimed at new or non-expert users. If needed, the "Importing registrations" section could be split into its own Guide for clarity.