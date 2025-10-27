---
categories:
  - Guide  
level: Basic  
summary: This guide explains how non-profit staff can manually register participants for events in CiviCRM, including single registrations, partial payments, mass registrations, and importing registrations.  
section: Events  
---

# Manual event registration

## Registering a participant manually

Sometimes people want to register for your event by phone, mail, or in person rather than online. CiviCRM lets you register these participants manually through the admin interface.

To register a participant manually:

1. Use the Quick search box to find the person’s contact record.
2. Select the contact from the search results.
3. Click the **Events** tab on their contact record.
4. Choose one of the registration options:
   - **Add Event Registration**: for participants who will pay later (e.g., by check or at the event).
   - **Submit Credit Card Event Registration**: for participants paying immediately by credit card (if your system supports this).

When you select the event and participant role, the form will load any custom fields related to the event. If the event has a fee, you will see the event fees section and an option to record payment.

**Important:** Event registrations and payments are recorded separately but linked in CiviCRM. This means you can register someone without recording a payment (for example, for VIPs or speakers who attend for free).

If the participant is paying now, check **Record Payment** and enter payment details. After saving, you can view the registration and the linked payment record on the contact’s Events tab.

## Registering a participant paying a deposit (partial payment)

You can register someone who pays part of the event fee and expects to pay the rest later.

- Enter the amount paid now in the **Payment Information** section.
- Set the **Participant Status** to **Partially paid**.

To record additional payments later:

1. Go to the participant’s contact record.
2. Click the **Events** tab.
3. Find the partially paid registration, click **more** on the right.
4. Choose **Record Payment** or **Submit Credit Card payment** to add the next payment.

Once the full fee is paid, CiviCRM automatically updates the participant status to **Registered** and the payment status to **Completed** (you can override this if needed).

You can view all payments made by clicking **view payments** on the registration or expanding the linked contribution record.

## Mass registrations

If you want to register many people at once (for example, participants from a previous event), you can use CiviCRM’s mass registration feature.

Steps for mass registration:

1. Search for the contacts you want to register (e.g., previous participants).
2. On the search results page, select all or specific contacts.
3. From the **Actions** menu above the results, select **Register participants for event** and click **Go**.
4. Choose the event and set registration options like participant status (e.g., Pending).
5. Click **Save**.

**Note:**  
- Mass registration applies the same settings to all selected contacts. To assign different statuses, run multiple mass registrations with different options.  
- You cannot mass register participants for past events.  
- You cannot record payments during mass registration; add payments individually later.

## Importing registrations

Importing registrations from a CSV file is a fast way to add many participants. Before importing, make sure:

- All participants already exist as contacts in CiviCRM. If not, import contacts first.  
- You can match participants to contacts using Contact ID, External Identifier, or a combination of first name, last name, and email.

Required fields for import include one contact matching field, Event ID, and Participant Status.

Steps to import registrations:

1. Go to **Events > Import Participants**.
2. Upload your CSV file.
3. Select contact type, date format, and other options, then click **Continue**.
4. Match CSV columns to CiviCRM fields.
5. Optionally save the field mapping for reuse.
6. Preview and save the import.
