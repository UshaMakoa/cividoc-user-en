---
categories:
  - Guide  
level: Basic  
summary: This guide explains what smart groups are in CiviCRM, how to create and manage them, and practical ways non-expert users in non-profits can use smart groups to organize contacts automatically based on criteria.  
section: Organising your data  
---

# Smart groups

## What are smart groups?

Smart groups in CiviCRM are saved searches that automatically collect contacts matching specific criteria you set. Instead of manually adding contacts to a group, a smart group updates itself whenever you view it, showing only contacts who meet your conditions at that time. This makes managing and communicating with specific sets of contacts easier and more accurate.

## When might I use a smart group?

Smart groups are helpful in many situations. For example:

- **Membership directories:** You can create a smart group of all current members and use it with a profile to display an up-to-date member list on your website. When someone becomes a member, they automatically appear in the directory.

- **Mailing lists for events:** Create a smart group of all people who have registered for or attended events. Use this group as a mailing list for newsletters about upcoming events. As people register or attend, they are automatically added to the group and can receive your communications.

## How to create a smart group

1. Go to **Search > Find Contacts > Advanced Search** in CiviCRM.  
2. Set your search criteria to find the contacts you want in your group. For example, find all donors who have not yet received a thank-you letter by selecting the appropriate options under Contributions.  
3. Click **Search** to see the results.  
4. Select all contacts from the search results.  
5. From the **Actions** dropdown, choose **Group - create smart group**.  
6. Give your smart group a clear name and description. Optionally, mark it as a mailing list or assign it a parent group.  
7. Click **Save Smart Group**.

You can also create smart groups from SearchKit by clicking **+Add** after a contact search and selecting **Smart Group**.

## Changing smart group criteria

To update the conditions that define your smart group:

1. Go to **Contacts > Manage Groups**.  
2. Find your smart group and click **Settings** next to it.  
3. Click **Edit Smart Group Criteria** at the bottom left.  
4. Adjust the search criteria as needed.  
5. Select all contacts from the updated results.  
6. From the **Actions** dropdown, choose **Update Smart Group**.

Your smart group will now include contacts matching the new criteria.

## Manually adding or removing contacts

Smart groups usually update automatically based on their criteria, but you can manually add or remove contacts if needed:

- To **add** contacts, use the same process as adding to a regular group.  
- To **remove** contacts, go to **Contacts > Manage Groups**, select your smart group, click **Contacts** on the right, check the contacts to remove, then select **Group - remove contacts** from the Actions dropdown. Confirm the removal.

Manually removed contacts will stay out of the smart group even if they meet the criteria, until you delete their smart group record on their contact page.

## Smart group caching

For faster performance, CiviCRM may cache smart groups, meaning it saves the list of contacts temporarily instead of recalculating every time. By default, this cache lasts about 5 minutes. This means changes in contacts might not appear immediately in the smart group.

You can adjust or disable this cache timeout in **Administer > Customize Data and Screens > Search Preferences** if you want smart groups to update instantly.
