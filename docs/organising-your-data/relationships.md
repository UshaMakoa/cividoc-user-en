---
categories:
  - Guide
level: Basic
summary: Learn how to create, manage, and customize relationships between contacts in CiviCRM to accurately reflect connections in your organisation's database.
section: Organising your data
---

# Managing relationships between contacts

CiviCRM helps your organisation keep track of connections between people and organisations, such as family members, staff, volunteers, and employers. This guide walks you through the main tasks involved in working with relationships.

## Creating a relationship between two contacts

To link two contacts (for example, to show that two people are siblings or that a person works for an organisation):

1. Go to the contact record for one of the people or organisations you want to link.

2. Click **Actions** and choose **Add Relationship** (you can also find this under the Relationships tab).

3. Select the **Relationship Type** (such as "Sibling of", "Employee of", etc.).

4. Start typing the name of the other contact. If they are not yet in your database, you can add them from this screen.

5. Optionally, fill in:
   - **Start Date** and **End Date** if the relationship is time-limited.
   - **Description** for a short summary.
   - **Notes** for more detailed information.
   - **Permissions** to allow another user to view or update the related contact.
   - **Enabled** to show the relationship is active.

6. Click **Save Relationship**.

## Understanding relationship permissions

When you create a relationship, you can set permissions so that one user can view or update the other contact’s details. For example, if you allow "View" access, the related user can see the contact’s information; with "View and Update", they can also make changes. You can extend this with the Related Permissions extension if needed.

## Connecting employees and employers

To quickly connect an individual to their employer:

1. Open the individual’s contact record.

2. Click **Edit**.

3. In the **Current Employer** field, start typing the organisation’s name.

- If the organisation exists, select it from the list.

- If not, type the full name to create a new organisation contact.

4. Click **Save**.

- This automatically creates an "Employee of" relationship from the individual to the organisation, and an "Employer of" relationship from the organisation to the individual.

5. You can view these relationships under the Relationships tab.

## Other ways to connect employees and employers

- The **Current Employer** field is also available on CiviCRM Profiles and Contribution Pages.

- When users fill in this field, CiviCRM tries to match the name to an existing organisation to avoid duplicates, using deduplication rules.

- If no match is found, a new organisation is created and linked to the individual.

## Adding contacts to organisations

To add several people to an organisation at once:

1. Select the contacts you want from your search results.

2. Choose **Add relationship
 - to organization** from the Actions menu.

3. On the next screen, select the **Relationship Type**.

4. Enter part of the organisation’s name in the **Find Target Organization** field and click **Search**.

5. Select the correct organisation from the results and click **Add to Organization**.

6. You’ll see a message confirming the contacts have been added.

7. Click **Done** to return to your search results.

## Adding contacts to households

To add people to a household:

1. Select the contacts from your search results.

2. Choose **Add relationship - to household** from the Actions menu.

3. Select the **Relationship Type** (usually "Household Member of" is best).

4. Enter part of the household’s name in the **Find Target Household** field and click **Search**.

5. Select the household and click **Add to Household**.

6. You’ll see a confirmation message.

7. Click **Done**.

*Tip: Only one contact should be set as "Head of Household" per household to avoid confusion. Use "Household Member of" for other members.*

## Creating new relationship types

If your organisation needs to track a type of relationship that isn’t already available:

1. Go to **Administer > Customize Data and Screens > Relationship Types**.

2. Check the list to avoid creating duplicates.

3. Click **New Relationship Type**.

4. Enter clear labels for both directions (e.g. "Mentor of" and "Mentee of").

- If the relationship is the same both ways, you only need to fill in one label.

5. Select which contact types can be linked.

6. Optionally, add a description.

7. Leave **Enabled** checked unless you want to create it for future use only.

8. Click **Save**.

## Creating custom fields on relationships

You can add custom fields to relationships to record extra details (like department, start date, or special notes) without creating lots of new relationship types. Custom fields can be added for all relationships or just for certain types. See the "Creating custom fields" guide for step
-by-step instructions.

## Disabling or deleting relationship types

If you no longer need a relationship type:

1. Go to **Administer > Option Lists > Relationship Types**.

2. Click **More** next to the type you want to change.

3. Choose **Disable** or **Delete**.
   - **Disable** keeps existing data and lets you re-enable the type later.
   - **Delete** removes the type and all related data from new entries.

4. Confirm your choice.

Disabled types appear in red and can be re-enabled at any time.

---

<!--
Source: https://docs.civicrm.org/user/en/latest/organising
-your-data/relationships/ -->

<!--
This page is a Guide because it provides step
-by-step instructions for specific tasks users want to perform, such as creating, managing, and customizing relationships. It does not provide background theory (Explanation), exhaustive technical detail (Reference), or a hands-on, first-time learning experience (Tutorial). The level is Basic, as it is aimed at non-expert users learning core features. -->
