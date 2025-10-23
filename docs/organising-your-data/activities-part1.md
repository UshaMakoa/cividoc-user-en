---
categories:
  - Uncategorized
  - Explanation
level: Basic
summary: Activities in CiviCRM are a central way to record and track interactions with your contacts, helping you keep a clear history of your organization’s work with supporters, clients, and partners.
section: Organising your data
---

# Activities in CiviCRM

## What are activities?

Activities are the building blocks for tracking your organization’s day-to-day interactions with contacts—people like donors, volunteers, clients, or partners. Every time your team meets with someone, makes a phone call, sends an email, or processes a donation, you can record it as an activity. This creates a unified history that’s easy to review and report on.

Activities always happen at a specific date and time, involve at least one contact, and can be assigned to staff or volunteers. You can also link multiple contacts to a single activity, making it easy to see who was involved in group meetings or collaborative projects.

## Why use activities?

Recording activities helps your team stay organized and accountable. Instead of relying on memory or scattered notes, you have a clear record of who did what, when, and with whom. This is especially helpful for reporting, evaluating your work, and planning future outreach.

For example, if you send a membership packet to a contact, you could simply add them to a “received membership packet” group. But recording this as an activity lets you note when it was sent, who sent it, and any special requests—making your records much more useful.

## Activity attributes

Every activity in CiviCRM includes:

- **Date and time**: When the interaction happened.
- **Duration**: How long it took (optional, but helpful for tracking time spent).
- **Status**: Such as Scheduled, Completed, or Cancelled.
- **Added by**: Who recorded the activity.
- **Assigned to**: Who is responsible for completing the activity (usually a staff member or volunteer).
- **With contact(s)**: The people in your database involved in the activity.

## Activities vs. events

It’s important to understand the difference between activities and events. An event is something a contact attends, like a workshop, fundraiser, or meeting. An activity is any interaction your organization has with a contact, whether it’s a phone call, email, donation, or meeting. Events are a type of activity, but not all activities are events.

## Activity status options

By default, activities can have these statuses:

- Scheduled
- Completed
- Cancelled
- Left Message
- Unreachable
- Not Required

You can add more statuses if your organization needs them, but remember that all statuses appear for every activity type.

## Repeating activities

If you have regular meetings or tasks, you can set an activity to repeat—for example, a weekly check-in call. When you create a repeating activity, CiviCRM will make a new activity record for each occurrence. You can edit or delete individual instances, or make changes that apply to all future repeats.

## Customizing activities

CiviCRM comes with several standard activity types (like Meeting, Phone Call, and Email), but you can create your own to match your organization’s work. For example, you might add “Training Session” or “Interview” as activity types. You can also add custom fields to collect extra information, like which project or funder is related to the activity.

To add a new activity type, go to **Administer > Customize Data and Screens > Activity Types** and click **Add Activity Type**. Assign it to the “Contact” component to make it available from a contact’s record, or to “CiviCase” if it’s only for case management.

## Custom field sets for activities

You can create custom fields to collect information that’s specific to your organization’s needs. When setting up a custom field set, choose “Activity” as the type. You can even link custom fields to specific activity types, so you only see relevant fields when recording that kind of activity.

## Creating new activity statuses

If the default statuses aren’t enough, you can add more by going to **Administer > System Settings > Option Groups**. Be mindful—every status you add will appear for all activity types, so keep your list clear and practical.
