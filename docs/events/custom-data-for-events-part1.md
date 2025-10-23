---
categories:
  - Uncategorized
  - Guide
level: Intermediate
summary: Learn how to collect and manage extra information for your events and participants using custom data in CiviCRM.
section: Events
---

# Custom Data for Events

## What Custom Data Is and Why It Matters

Custom data lets you collect information beyond the standard fields in CiviCRM, helping you tailor your event management to your organisation’s needs. For example, you might want to track dietary preferences, session choices, or workshop topics. Using custom data effectively makes your events more organised and your reporting more useful.

## Where to Add Custom Data

You can add custom data in three main places in CiviCRM:

- **Participant record:** For information specific to a person’s participation in a particular event (e.g., session preference).
- **Contact record:** For information that applies to the person across all events (e.g., dietary requirements).
- **Event record:** For information about the event itself (e.g., workshop topics offered).

**Choosing the right place is important.** Adding custom data in the wrong place can cause confusion and make reporting harder. Here are some guidelines:

- **Add to the contact record** if the information is about the person and unlikely to change between events.
- **Add to the participant record** if the information is only relevant to a specific event.
- **Add to the event record** if the information is about the event itself, not the participants.

## Examples

- **Dietary preference:** Add to the contact record, since it’s about the person and not the event.
- **Session preference:** Add to the participant record, since it’s about their choices for this event.
- **Workshop topics:** Add to the event record if you want to track which topics are offered at each workshop.

## How to Add Custom Data

**You need administrator permissions to add custom data.** Here’s how to get started:

1. **Go to Administer > Customize Data and Screens > Custom Data.**
2. **Choose the record type** (Participant, Contact, or Event).
3. **Create a new custom field set** (a group of related fields).
4. **Add your custom fields** (e.g., text, checkbox, dropdown).
5. **Set where the field appears** (for all participants, a specific event, or a participant role).

You can also add custom fields while creating an event—look for the option during event setup.

## Tips for Success

- **Keep it simple:** Only collect the information you really need.
- **Name fields clearly** so everyone understands what to enter.
- **Review your choices** to make sure you’re adding data in the right place.
- **Test your setup** by registering for an event to see how the custom data fields work in practice.

## When to Split This Topic

If your organisation has complex event needs—such as many custom fields, different roles, or advanced reporting—consider splitting this into separate guides:

- **Basic:** How to add a simple custom field to an event or participant.
- **Intermediate:** Managing multiple custom fields and understanding where to place them.
- **Advanced:** Using custom data for reporting, integrating with other CiviCRM features, or handling large-scale events.
