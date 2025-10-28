---
categories:
  - Guide
level: Intermediate
summary: Step-by-step instructions for setting up CiviCase so your organisation can manage cases, roles, activities, and permissions in CiviCRM.
section: Case management > Set-up
---

# Set up CiviCase

## Enable the CiviCase component

To start using CiviCase, you first need to enable it in your CiviCRM system.

1. Go to **Administer > System Settings > Components**.

2. Find and select **CiviCase**.

3. Click **Save**.

You should now see **Cases** in your main navigation menu.

## Define case types

Case types help you organise the different kinds of cases your organisation manages (for example, "Employment Counselling" or "Support Request").

To add a new case type:

1. Go to **Administer > CiviCase > Case Types**.

2. Click **New Case Type**.

3. Enter a **Title** (what users will see) and an optional **Description**.

4. The **Name** field is filled in automatically for internal use. Advanced users can change this, but it should not be changed after the case type is created.

### Restrict activity assignment (optional)

- By default, any contact can be assigned to activities in a case.

- You can choose to limit this to certain groups or to users with website accounts.

### Include case roles

- Roles are the types of people involved in a case (like "Case Manager" or "Client").

- Use the **Add role** drop
-down to select or create roles for this case type.

- To create a new role, type its name and select it when it appears underlined in blue.

- For each role, you can set:

  - **Assign to Creator**: Automatically assigns the role to the person who creates the case.
  - **Is Manager**: Marks the role as a manager, which will be shown in listings and reports.

**Note:** Roles created here are for individual-to-individual relationships. To set up individual-to-organisation roles, edit them later at **Administer > Customize Data and Screens > Relationship Types**.

### Include activities

- Activities are the actions or steps that happen in a case (like phone calls, emails, or meetings).

- Choose which activity types users can add to this case type using the **Add activity type** drop
-down.

- To add a new activity type, type its name and select it when it appears underlined in blue.

- For each activity type, you can set a maximum number of times it can be used in a case.

- You can edit activity types later at **Administer > Customize Data and Screens > Activity Types**.

### Set up timelines and sequences

- **Timelines** are groups of activities scheduled relative to when the case is opened or to another activity.

- The **Standard Timeline** is required and is added automatically when a case is opened.

- You can add more timelines or a **Sequence** (a set of activities where each one appears only after the previous is completed).

- To add activities to a timeline:

1. Select or create an activity.

2. Set its status (default is Scheduled).

3. Choose a reference activity (often "Open Case").

4. Enter an offset in days (when the activity should happen).

5. Use the "Select" option if there are multiple reference activities to choose from.

- You can rename timelines or sequences in the **Advanced** section.

- Reorder activities using the drag
-and-drop handles.

**Tip:** Sample case types are included when you enable CiviCase. Use these as examples or starting points.

## Add custom fields

Custom fields let you collect extra information specific to your cases or activities.

To add custom fields:

1. Go to **Administer > Customize Data and Screens > Custom Fields**.

2. Click **Add a Set of Custom Fields**.

3. Under **Used For**, select **Activities** or **Cases**.

4. Choose the specific activity or case types these fields are for.

5. Add any help text for your users.

6. Click **Save**.

7. Add your custom fields to the set.

**Tip:** If you need many fields, group them into sets that make sense to users to avoid overwhelming forms.

## File emails on cases

You can keep emails related to a case in CiviCase.

- You can send emails directly from the **Manage Case** screen.

- If you use the Email Processor, replies to emails sent from CiviCase are filed automatically.

- To file an email or activity to a case manually, add `[case #123]` (replace 123 with the case ID) at the start of the subject line.

## Set CiviCase permissions

To manage who can access and work with cases:

- Each staff member or provider needs a contact record in CiviCRM and a user account on your website (Drupal, Joomla!, or WordPress).

- In Joomla! and WordPress, users must have administrator access to use CiviCase.

- Add contact records for external providers who need to be assigned roles but will not log in.

- Assign permissions in your CMS to control access:

  - **Access my cases and activities**: User can create and manage their own cases and activities, but not see others'.
  - **Access all cases and activities**: User can create, view, and manage any case.
  - **Delete in CiviCase**: User can mark cases and activities as deleted (they are hidden, not removed).
  - **Administer CiviCase**: User can create/edit case types, set case statuses, and define rules for redacting case data.

---

<!--
Source: https://docs.civicrm.org/user/en/latest/case
-management/set-up/ -->

<!--
This page is a Guide, as it provides step
-by-step instructions for configuring CiviCase, aimed at users who need to achieve a specific setup goal. It is not a Tutorial (not a first-time learning exercise), nor Reference (not exhaustive options), nor Explanation (not background/why). The level is Intermediate, as it expects users to be familiar with basic CiviCRM navigation and concepts. -->
