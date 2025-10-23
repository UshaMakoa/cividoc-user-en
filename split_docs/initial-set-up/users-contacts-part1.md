# Source: https://docs.civicrm.org/user/en/latest/initial-set-up/users-contacts/

---
categories: Guide
level: Basic
summary: This guide explains how user accounts in CiviCRM are linked to contact records, specifically focusing on the behaviors of Drupal, Joomla, and WordPress systems.
section: Users contacts
---

# Understanding user contacts in CiviCRM

In CiviCRM, user accounts are linked to contact records, which represent individuals or organizations in your database. This guide will help you understand how this linking works across different content management systems (CMS) like Drupal, Joomla, and WordPress.

## How are users linked to contacts?

CiviCRM operates within a CMS that manages user authentication. Users are individuals with a username and password who log into CiviCRM, while contacts are the records of people or organizations stored in CiviCRM.

### Drupal behavior

When a new user registers on a Drupal site:

- CiviCRM checks for an existing contact with the same email address.
- If a match is found, the user is linked to that contact.
- If no match is found, a new contact is created using the user's primary email address.

When an existing user logs in, CiviCRM again checks for a linked contact record. If none exists, it follows the same logic to either link the user to an existing contact or create a new one. If you're integrating CiviCRM with an existing Drupal site, it’s recommended to run the batch synchronization utility.

### Joomla behavior

CiviCRM does not automatically use Joomla's hooks and APIs for user registration and login. Instead, the linking happens when a logged-in Joomla user interacts with CiviCRM, such as by:

- Editing a CiviCRM Profile
- Making a contribution
- Registering for a membership

If a user has previously engaged with CiviCRM as an anonymous user, they need to perform a transaction while logged in to link their Joomla account with their CiviCRM contact record.

### WordPress behavior

CiviCRM uses WordPress functions to synchronize user accounts with contact records. When a user registers or updates their profile on WordPress, CiviCRM automatically checks and syncs the email field with the corresponding contact record.

## Synchronizing users to contacts

The "Synchronize Users-to-Contacts" feature is particularly useful for organizations that are adding CiviCRM to an existing Drupal or Joomla site. This feature allows all users of the existing site to have corresponding CiviCRM contact records created automatically.

To synchronize users to contacts:

1. Go to **Administer CiviCRM**.
2. In the **Users and Permissions** section, select **Synchronize Users to Contacts**.
3. CiviCRM will check each user record for a corresponding contact record. If a contact does not exist, a new one will be created.

You will see a message confirming the synchronization process and how many records were checked, matched, or created.

After synchronization, you can search for the newly created contact records in CiviCRM to view or edit them.