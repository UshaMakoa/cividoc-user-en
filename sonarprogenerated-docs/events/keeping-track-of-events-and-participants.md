---
categories: Guide
level: Basic
summary: Learn how to find, view, and manage your organisation’s events and participants in CiviCRM using easy-to-follow steps.
section: Events > Managing events and participants
---

# Keeping track of events and participants

## Using the events dashboard

The CiviEvent dashboard brings together details about your events and participants in one place.

- Go to **Events > Dashboard**.
- You’ll see a summary table showing up to ten scheduled or recent events.
- Click the event name to see how it looks to visitors.
- Click the participant count to view a list of people registered for that event.
- To search for more participants, click **Find more event participants** at the end of the page.
- You can also:
  - Click **Manage Events** to find and manage specific events.
  - Click **New Event** to create a new event.
  - Use the RSS and calendar icons to export event data to other applications.

## Finding and viewing events

You can access all your events from the **Manage Events** screen.

- Go to **Events > Manage Events**.
- Use the search filters at the top to find events by name, type, or date.
- For each event, you’ll see links on the right:
  - **Configure**: Change event settings like information, location, fees, registration, reminders, and sharing options.
  - **Participants**: View lists of people registered or attending, or those not attending.
  - **Event Links**: Quick access to register participants and view live event pages.

## Finding and administering participants

To manage participants for your events, follow these steps:

- Go to **Events > Dashboard**.
- Click the counted link next to an event to see all its contacts. (If the count is zero, this won’t be a link.)
- To search for participants with specific criteria:
  - Go to **Events > Find Participants**.
  - Start typing the event name and select it from the list.
  - Set any other search filters you need.
  - Click **Search**.

Once you have your results, you can select participants and perform actions such as:

- **Cancel registration** for selected participants.
- **Delete participants** from the event (this removes their event records but not their contact details; this cannot be undone).
- **Send email** to selected participants, for example, to share event updates.
- **Export participants** to a CSV file for use in spreadsheets or mail merges.
- **Add to group** or create a new group during this action.
- **Create smart group** for saved searches that update automatically.
- **Print name badges** for selected participants.
- **Print PDF letters** for participants.
- **Change participant status** (emails will be sent if you change from pending to registered/attended, or to expired/cancelled).
- **Print selected rows** to get a printout of what’s on your screen.
- **Update multiple participants** in a table grid (requires a profile set; see the Profiles chapter for more info).

## Listing participant fees

To see individual fees for participants:

- Go to **Search > Custom Searches**.
- Click on **Event Aggregate**.
- Choose your search criteria and click **Search**.

## Changing event registration selections

If you need to update a participant’s registration details (for example, change their role, adjust fees, or update session choices):

- Find the participant’s event registration (for example, via **Events > Find Participants**).
- Select **View** or **Edit** next to their event record.
- Click **Change Selections**.
- Make the necessary adjustments. CiviCRM will update the fee and status based on changes.
- For extra payments or refunds, use the **record payment** link in the registration record.

## Creating and printing event badges

You can create custom name badges for your events.

- Go to **Administer > CiviEvent > Event Badge Layout > New Badge Layout**.
- Choose your label format (Avery 5395, A6 Badge Portrait, Fattorini Name Badge, or Hanging Badge).
- Add images (top left/right), such as your logo or sponsor’s logo.
- Select up to 6 rows of information (name, organisation, country, participant role, etc.).
- Add a barcode or QR code if needed.
- Tick **Enabled** to make the badge layout available.
- Tick **Reserved** to prevent accidental deletion by admin users.

**Note:** You need at least one event and one participant registered to preview badge layouts.

To print name badges:

- Go to **Events > Find Participants**.
- Select the relevant participants.
- Choose **Print Event Name Badges** from the actions menu and click **Go**.
- Select the badge layout for your event.
- Click **Make Name Badges**.
- Download and print the PDF file on your chosen labels.

# comment: Source: https://docs.civicrm.org/some/page/
# comment: Suggestion: This page is a Guide, as it provides step-by-step instructions for specific administrative tasks (finding, viewing, and managing events and participants) without background theory or exhaustive reference details. The level is Basic, as it is intended for users new to CiviCRM event management. If needed, badge creation and printing could be split into a separate Tutorial for clarity, and fee listing could be referenced in a separate Reference page for advanced users.