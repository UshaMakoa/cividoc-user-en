---
categories: Guide
level: Intermediate
summary: Learn how to create new activity types, add custom fields, and manage activity statuses in CiviCRM.
section: Organising your data
---

# How to administer activities

## Creating new activity types

1. Go to **Administer > Customize Data and Screens > Activity Types**.
2. Click **Add Activity Type**.
3. Enter a name and assign it to a component:
   - Use “Contact” if you want it available for all contacts.
   - Use “CiviCase” if it’s only for case management.
4. Save your new activity type.

## Adding custom fields to activities

1. Go to **Administer > Customize Data and Screens > Custom Fields**.
2. Click **Add Set of Custom Fields**.
3. Set the “Used For” option to **Activity**.
4. If you want, specify which activity types the custom fields apply to.
5. Add your custom fields (for example, project name, funder, meeting type).

Custom fields let you collect extra information relevant to your organisation’s work.

## Creating new activity statuses

1. Go to **Administer > System Settings > Option Groups**.
2. Find and select the **activity status** option group.
3. Add your new status option.

Be careful not to add too many statuses, since all statuses appear for all activity types.

# comment: Source: https://docs.civicrm.org/user/en/latest/organising-your-data/activities/
# comment: This section is a Guide, as it gives step-by-step instructions for common administrative tasks related to Activities.

---

# Suggestion

If the original page included both conceptual explanation and step-by-step instructions, consider splitting the conceptual overview (Explanation) from the administrative tasks (Guide), as done above, for clarity and to match the Diátaxis framework[1][2][3][4].