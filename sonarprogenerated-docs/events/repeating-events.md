---
categories: Guide
level: Basic
summary: Learn how to set up an event in CiviCRM that repeats on a schedule, including how to choose dates, set exclusions, and manage reminders.
section: Events
---

# Repeating events

## How to set up a repeating event

You can create an event in CiviCRM that repeats on a regular schedule, such as weekly or monthly. This is helpful if your organisation runs the same event multiple times.

Follow these steps to set up a repeating event:

1. Go to **Manage Events** in your CiviCRM dashboard.

2. Find the event you want to repeat. Under the **Configure** menu, select **Repeat**.

3. On the **Repeat Event** screen, fill in these details:
   - **Repeating intervals**: Choose how often the event repeats (for example, every week, month, or year).
   - **Event end date**: Set when the event itself ends (for example, the time the meeting finishes each day).
   - **Occurrence end date**: Set the last date the event should repeat.
   - **Repetition start date**: When the first event in the series should happen.
   - **Excluded dates**: Add any dates you want to skip (for example, holidays).

4. If you want to send reminders for each event, make sure you have set up **Scheduled Reminders** on the event before repeating it. You can edit reminders later if needed. It's best to set reminders to go out a certain number of days before each event, not on specific dates.

5. When you have finished, click **Save**.

6. A popup window will appear. Confirm your choices to finish creating the repeating event.

You have now set up a repeating event. Each occurrence will appear in your events list, and reminders will be sent as you have configured.

# comment: Source: https://docs.civicrm.org/user/en/latest/events/repeating-events/
# comment: Suggestion: This page is a Guide because it helps users achieve a specific goal (setting up a repeating event), with clear, actionable steps and no background or conceptual explanation. The task is basic, as it is a common need for non-profit users managing events. If more background on "why use repeating events" or technical reference about all recurrence options were needed, those would belong in separate Explanation or Reference pages.