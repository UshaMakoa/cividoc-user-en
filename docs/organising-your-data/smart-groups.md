---
categories:
  - Guide
level: Basic
summary: Learn how to use smart groups in CiviCRM to automatically keep track of contacts that meet specific criteria, such as members or event attendees, for tasks like directories and mailing lists.
section: Organising your data
---

# Using smart groups in CiviCRM

## What are smart groups?

Smart groups are **saved searches** that automatically include contacts who meet criteria you choose, such as “all members in Europe” or “everyone who attended an event.” This means your group updates itself—when a contact’s details change and they fit your criteria, they’re added; if they no longer match, they’re removed.

## When should you use smart groups?

Smart groups are useful whenever you want a list that updates itself based on contact information. Here are two common examples:

- **Membership directories:** You can create a smart group for all current members and use it with a profile to display a directory on your website. When someone becomes a member, they’re automatically added to the directory.
- **Mailing lists for events:** If you want to send newsletters to everyone who registered for or attended an event, create a smart group based on those criteria. As people register or attend, they’re added to the mailing list automatically. If someone unsubscribes, they’re removed.

## How to create a smart group

Follow these steps to create a smart group from a search:

1. Go to **Search > Find Contacts > Advanced Search**.

2. Set your criteria (for example, in the Contributions section, select “Thank-you date not set?” and choose “Donation” as the financial type).

3. Click **Search**.

4. Select all the records you want to include.

5. From the **Actions** drop-down, choose **Group – create smart group**.

6. Give your smart group a name and description. You can also make it a mailing list or link it to a parent group.

7. Click **Save Smart Group**.

You can also create smart groups using **SearchKit**. After running a contact search, click **+Add** on the left and select **Smart Group**.

## How smart groups update

Once you’ve created a smart group, CiviCRM will automatically update the group membership whenever contact details change. For example, if a contact no longer matches the criteria, they’ll be removed from the group. If this doesn’t happen immediately, smart group caching might be turned on (see below).

## Changing smart group criteria

If you want to change the criteria for a smart group:

1. Go to **Manage Groups**.

2. Find your smart group and click **Settings**.

3. Click **Edit Smart Group Criteria**.

4. Update your criteria and click **Search**.

5. Select all matching records and choose **Update Smart Group** from the Actions list.

Your smart group will now use the new criteria.

## Manually adding or removing contacts

Normally, smart group membership is automatic, but you can override this:

- To **add contacts manually**, use the same process as for standard groups.

- To **remove contacts manually**, go to **Contacts > Manage Groups**, select the group, and use the Actions drop
-down to remove contacts. Confirm the removal. The contact will show the group under “Past Groups,” and CiviCRM won’t re-add them unless you delete the smart group record from their contact record.

## Smart group caching

For performance, CiviCRM may “cache” smart groups, meaning the group membership list is saved for a short time (usually 5 minutes). This speeds up searches, especially for large groups, but means updates may not show instantly. You can adjust the cache timeout in **Administer > Customize Data and Screens > Search Preferences**. Setting the timeout to 0 turns caching off.

<!--
Source: https://docs.civicrm.org/user/en/latest/organising
-your-data/smart-groups/ -->

<!--
This page is a Guide, as it provides step
-by-step instructions for achieving specific tasks (creating, using, and managing smart groups) and is focused on practical actions rather than background or exhaustive reference. The level is Basic, as it is aimed at new or non-expert users. The section is "Organising your data". If the page had more technical details about smart group configuration or caching, those could be split into Reference or Explanation pages. -->
