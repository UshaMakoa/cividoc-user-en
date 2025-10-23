# Source: https://docs.civicrm.org/user/en/latest/organising-your-data/groups-and-tags/

---
categories: Guide  
level: Basic  
summary: This guide explains how to use groups and tags in CiviCRM to organize your contacts and data effectively, helping non-profit users segment and manage their information easily.  
section: Organising your data  
---

# Groups and tags

## What are groups and tags?

Groups and tags are two important ways to organize your data in CiviCRM. They help you sort your contacts and other records so you can find and use them more easily. While both help categorize your data, they work in different ways and serve different purposes.

- **Groups** are collections of contacts that you manage as a unit. You can use groups to send emails, control access, or organize people who share something in common.
- **Tags** are labels you apply to contacts, activities, or cases to describe them with keywords or categories.

Understanding the difference helps you decide when to use a group or a tag.

## When to use groups or tags?

Think of **tags** as descriptive labels. For example, you might tag contacts as "volunteer," "musician," or "vegetarian" to describe who they are.

Think of **groups** as sets of people you want to treat as a unit. For example, you might have a "Volunteer Committee" group or a "Board of Directors" group to manage communications or permissions.

## Types of groups

There are two main types of groups:

- **Regular groups:** You add and remove contacts manually. For example, you add your board members to a "Board of Directors" group.
- **Smart groups:** These groups update automatically based on rules you set. For example, a smart group might include all contacts who donated in the last year and live in your state.

## Managing groups

- Give each group a clear name and description so everyone understands its purpose.
- Groups can be set as mailing lists if you want to send emails to them.
- In some systems like Drupal, groups can control access permissions.
- You can create parent groups that include several child groups, making it easier to send mailings to a large set of contacts.

## Group visibility

You can control who can join or leave a group:

- **User and admin only:** Only authorized users can add or remove contacts.
- **Public pages:** Contacts can join or leave groups themselves through forms on your website.

## Group membership history

When you remove someone from a group, CiviCRM keeps a record of when and who removed them. This helps track changes over time. You can also delete contacts from groups, which removes all history of their membership.

## Working with tags

- Tags are easy to create and apply.
- You can assign tags to contacts, activities, or cases.
- Tags can be grouped into **tag sets**, which organize related tags together and make it easier to find and apply them.
- Tags are flexible but do not support some features groups have, like controlling visibility or access permissions.

## Benefits and limitations

| Aspect           | Tags                                   | Groups                                  |
|------------------|--------------------------------------|----------------------------------------|
| **Use case**     | Describing contacts or activities    | Organizing contacts for communication or access control |
| **Setup**        | Easy to create and apply              | More flexible but requires management  |
| **Automation**   | Cannot auto-add contacts              | Smart groups update automatically      |
| **Visibility**   | Cannot restrict visibility            | Can control visibility and permissions |
| **Search**       | Easy to combine with other criteria   | Supports complex segmentation          |
| **Data export**  | Tags export as a list in one field    | Groups export as a list in one field   |

## How to add contacts to groups or tags

You can add contacts to groups or tags in several ways:

- From the contact’s edit screen or the Groups tab.
- By selecting multiple contacts after a search and using the batch action to add them.
- By managing group members directly from the Manage Groups page.
- Contacts can also be added to groups by filling out profile or registration forms if configured.

## Finding and managing groups

- Go to **Contacts > Manage Groups** to see all your groups.
- Use filters to find groups by name, type, or visibility.
- From here, you can add or remove contacts, edit group settings, disable, or delete groups.
- You can also search for contacts within a group by name, email, or status (added, removed, pending).

## Summary

Groups and tags help you organize your contacts and data in CiviCRM. Use **groups** when you want to manage collections of contacts for communications or permissions, and use **tags** to label and describe contacts or activities flexibly. Understanding how to use both will help you keep your database organized and make your work more efficient.