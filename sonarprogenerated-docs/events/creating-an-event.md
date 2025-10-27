---
categories: Guide
level: Basic
summary: Learn how to create a new event in CiviCRM, step by step, including key settings for non-profit organisations.
section: Events > Event creation
---

# Creating an event

This page shows you how to create a new event in CiviCRM, guiding you through each step so your organisation can start managing events easily.

## Start a new event

- Go to **Events > New Event** in the CiviCRM menu.
- If you do not see the Events menu, check that the Events component is enabled in **Administer > System Settings > Components**.

## Enter event information

- Fill in the **Event Title**. This is the name that will appear on event pages and listings.
- Add a short **Event Summary** and a more detailed **Complete Description**. Use the editor to include images or formatting if you wish.
- Set the **Start date/time** and **End date/time** for your event.
- Choose an **Event Type** to help organise your events.
- If your organisation uses campaigns, you can link the event to a campaign.
- Decide the **default participant role** (such as attendee, speaker, or staff). This sets what role people get when they register.
- Set a **Maximum number of participants** if you want to limit attendance, and add a message for when the event is full.
- Choose if this is a **Public Event** (shows up in listings and feeds).
- Decide if you want to **Allow sharing through social media**.
- You can make the event **active** (visible) or **inactive** (hidden until ready).
- If you want people to download calendar invites, enable **Show Calendar Links** (test this if your participants are in different time zones).

When you are done, click **Continue** to move to the next step, or **Save and Done** to finish later. To return to your event, go to **Events > Manage Events** and click **Configure**.

## Set the event location

- Enter the event’s address and contact details.
- If you have run events at this location before, you can select **Use existing location** to reuse details.
- You can add phone numbers and email addresses for organisers.
- Choose whether to show the location on event and registration pages.
- If you want to display a map, set up mapping in **Administer > System Settings > Mapping and Geocoding**.

## Set event fees

- If the event is free, select **No** for Paid Event and skip to online registration.
- If the event has a fee, select **Yes**. Choose the **Contribution Type** (usually “Event Fee”).
- If you want to accept credit cards, a payment processor must be set up first.
- Enable **Pay Later** if you want to allow payment by cheque, cash, or other methods, and add instructions.
- Set up **Regular Fees** (like “Individual - $50”, “Family - $100”) or use more complex price sets if needed.

## Enable online registration (optional)

- If you want people to register online, check **Allow Online Registration**.
- For more details on setting up online registration, see the Online event registration page.

## Set up scheduled reminders (optional)

- Use **Scheduled Reminders** to send automatic emails before or after the event (such as reminders or feedback requests).
- Go to the **Scheduled Reminders** tab for your event and click **Add Reminder**.
- Choose who should get the reminder (by status or role) and when it should be sent.

## Enable Tell-A-Friend (optional)

- Allow participants to share the event with their friends by enabling **Tell-A-Friend**.
- Customise the message and links that will be sent.
- Each time someone uses this, the action is tracked, and new contacts are added to CiviCRM.

## Registration confirmation and receipts

- Automated confirmation and receipt emails can be sent to all registrants.
- These emails use templates, which you can edit in **Administer > Communications > Message Templates** under the **System Workflow Message** tab.
- Edit the “Events - Registration Confirmation and Receipt” template for your event.
- Be careful not to change the program logic in these templates. Test your changes to make sure everything works.

# comment: Source: https://docs.civicrm.org/user/en/latest/events/creating-an-event/
# comment: Suggestion: This content is a step-by-step guide for non-expert users to achieve a specific goal (creating an event), matching the Diátaxis definition of a "Guide" [3][4]. It is not a Tutorial (no first-time, hands-on walkthrough), Reference (not exhaustive/systematic), or Explanation (no conceptual background). If splitting, details about each field could be moved to Reference, and a separate Tutorial could walk through a basic event creation for the first time.