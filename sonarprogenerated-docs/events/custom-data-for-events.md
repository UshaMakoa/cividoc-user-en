---
categories: Explanation
level: Basic
summary: Learn where and how to add custom data for events and participants in CiviCRM, so your organisation collects the right information in the right place.
section: Events
---

# Custom data for events

## What is custom data in CiviCRM events?

Custom data lets your organisation collect extra information about events and participants beyond the standard fields in CiviCRM. You can use custom fields to track details important to your work, such as dietary preferences, session choices, or topics covered in workshops.

## Where should you add custom data?

Choosing the right place to store custom data is important for keeping your records accurate and useful. In CiviCRM, you can add custom data to three main places:

- **Participant record:** Use this for information specific to a person's involvement in a particular event (for example, which session they want to attend).
- **Contact record:** Use this for information about the person that stays the same across events (for example, dietary preferences).
- **Event record:** Use this for information about the event itself, not about the people attending (for example, topics covered in a training workshop).

Adding custom data in the wrong place can make it difficult to manage or report on later. For example, if you add dietary preferences to the participant record, you’ll have to re-enter the same information every time someone attends an event, instead of storing it once on their contact record.

## Examples to help you decide

- *Dietary preference:* Add to the contact record, since it’s unlikely to change between events.
- *Session preference:* Add to the participant record, since it’s only relevant for a specific event.
- *Workshop topics covered:* Add to the event record, since it describes the event itself.

## Types of custom data for participants

When adding custom data to participants, you have several options:

- **Participants:** The custom field appears for all participant records. Use this for information you want to collect from everyone attending any event.
- **Participants (Event Name):** The custom field is linked to a specific event. Use this for complex registration data unique to one event.
- **Participants (Role):** The custom field is only shown for certain types of participants (for example, speakers). Use this for details you need from specific roles.

## How to add custom data

To add custom data, you need administrator permission. You can add custom fields by going to:

- **Administer > Customize Data and Screens > Custom Data**

Here, you choose the record type (participant, contact, or event) and then create your custom fields.

You can also create custom fields during the event creation process if you need them quickly.

# comment: Source: https://docs.civicrm.org/some/page/
# comment: This page is best categorized as Explanation, because it helps users understand the reasoning and context for where to add custom data, with examples and guidance rather than step-by-step instructions or a factual reference. For a complete Diátaxis structure, step-by-step tutorials for adding custom fields and a reference list of field options should be split into separate pages.