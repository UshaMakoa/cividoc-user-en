---
categories:
  - Uncategorized
  - Explanation
level: Basic
summary: Understand the difference between custom data on contacts, participants, and events in CiviCRM.
section: Events
---

# Understanding Where to Put Custom Data

## Contact, Participant, or Event?

When you collect extra information in CiviCRM, it’s important to choose the right place for your custom data. Here’s a simple way to think about it:

- **Contact record:** Use this for information about the person that doesn’t change much, like dietary needs or accessibility requirements. This data stays with the contact, no matter which events they attend.
- **Participant record:** Use this for information that’s only relevant to a specific event, like session preferences or workshop feedback. This data is tied to the person’s registration for that event.
- **Event record:** Use this for information about the event itself, like workshop topics or location details. This data is about the event, not the people attending.

## Why Does It Matter?

Putting custom data in the right place makes your data easier to manage and report on. For example, if you store dietary preferences on the contact record, you can easily see them for any event the person attends. If you store session preferences on the participant record, you can report on session popularity for each event.

## Quick Reference Table

| Information Type         | Best Record Type | Example                          |
|
