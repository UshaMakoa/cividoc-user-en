---
categories:
  - Uncategorized
  - Tutorial
level: Basic
summary: This guide explains how to link users from your CMS (Drupal, Joomla, or WordPress) to their corresponding contact records in CiviCRM.
section: Users contacts
---

# Linking users to contacts in CiviCRM

When you use CiviCRM with a Content Management System (CMS) like Drupal, Joomla, or WordPress, it's important to understand how user accounts and contact records are connected. This guide will help you learn how to link users to their contact records in CiviCRM, making it easier to manage your organization's data.

## Understanding users and contacts

In CiviCRM, "contacts" refer to individuals, organizations, or households that you manage. "Users," on the other hand, are people who have a username and password to log into CiviCRM through your CMS. Not every contact will have a corresponding user account.

## How linking works in different CMSs

### Drupal behavior

When a new user registers on your Drupal site, CiviCRM checks if there is an existing contact with the same email address:

- **If a match is found:** The new user is linked to the existing CiviCRM contact.
- **If no match is found:** A new CiviCRM contact is created using the user’s primary email address.

When an existing user logs in, CiviCRM performs a similar check to link them to their contact record. If no link exists, it will either link them to an existing contact or create a new one.

### Joomla behavior

CiviCRM does not automatically link Joomla users to contact records during registration or login. Instead, this linking occurs when a user interacts with CiviCRM, such as by editing a profile or making a contribution. To ensure users are linked, they must engage with CiviCRM after creating their Joomla account.

### WordPress behavior

In WordPress, CiviCRM listens for user registration and profile updates. When a user registers or updates their profile, CiviCRM synchronizes their account with the corresponding contact record, primarily using the email address.

## Synchronizing users to contacts

To link existing users to their CiviCRM contact records, you can use the "Synchronize Users to Contacts" feature. This is especially useful if you are adding CiviCRM to an existing Drupal or Joomla site. Here’s how to do it:

1. Go to **Administer CiviCRM**.
2. In the **Users and Permissions** section, select **Synchronize Users to Contacts**.
3. CiviCRM will check each user record for a corresponding contact record. If a match is not found, a new contact will be created.
4. Click **OK** to proceed with the synchronization.

Once the process is complete, you will see a summary message indicating how many user records were checked, how many matches were found, and how many new contact records were created.

## Conclusion

Linking users to contacts in CiviCRM is a crucial step in managing your organization's data effectively. By understanding how this process works in different CMSs and utilizing the synchronization feature, you can ensure that your user and contact records are properly connected. If you have questions or need further assistance, don’t hesitate to reach out for help!
