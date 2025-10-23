---
categories:
  - Uncategorized
  - Guide  
level: Basic  
summary: This guide explains how to set up and configure the CiviCase component in CiviCRM to help non-profit users manage cases effectively.  
section: Set-up  
---

# Set up CiviCase in CiviCRM

## Enable the CiviCase component

To start using case management in CiviCRM, you first need to enable the CiviCase component:

- Go to **Administer > System Settings > Components**.
- Find and select **CiviCase**.
- Click **Save**.

After this, you will see **Cases** appear in your main navigation menu.

## Define case types

Case types help you organize different kinds of cases you manage. You can create one or more case types to fit your needs.

To add a case type:

- Go to **Administer > CiviCase > Case Types**.
- Click **New Case Type**.
- Enter a **Title** (this is what users will see) and an optional **Description**.
- The system will auto-fill a **Name** field for internal use; leave it as is unless you are an advanced user.
- Optionally, restrict who can be assigned to case activities by groups or website users.
- Select or create **Case Roles** — these are the people involved in the case (e.g., client, case manager).
  - You can assign roles automatically to the case creator.
  - Mark one role as the **Manager** to highlight that person in case lists.
- Choose **Activity Types** that users can add quickly when working on a case (e.g., Phone Call, Email).
  - You can create new custom activity types if needed.
  - Set limits on how many times an activity can be used per case if you want.
- Define **Timelines** and **Sequences** to set standard workflows for your cases.
  - Timelines schedule activities relative to case start or other activities.
  - Sequences define the order of activities, creating the next only after the previous is done.
  - Each case type must have a **Standard Timeline** starting with the "Open Case" activity.

## Create custom fields for cases and activities

Custom fields let you collect specific information relevant to your cases or activities.

To create custom fields:

- Go to **Administer > Customize Data and Screens > Custom Fields**.
- Click **Add a Set of Custom Fields**.
- Choose if the fields are for **Cases** or **Activities**.
- Select the specific case or activity types these fields apply to.
- Add helpful instructions for users if needed.
- Save and then add individual custom fields.
- Organize large numbers of fields into logical groups to keep forms user-friendly.

## Filing emails on cases

You can keep case-related emails attached to cases for easy reference.

- Send emails directly from the **Manage Case** screen to have them filed automatically.
- If you use the Email Processor, replies to case emails will also be filed automatically.
- Alternatively, include “[case #123]” in the email subject to file it to case ID 123.

## Set up user permissions for CiviCase

To control who can see and manage cases:

- Create contact records for all staff or service providers using CiviCase.
- Ensure they have user accounts in your CMS (Drupal, Joomla!, or WordPress).
- Assign appropriate permissions based on their roles:

| Permission                  | What it allows                                   | Notes                                                                                         |
|
