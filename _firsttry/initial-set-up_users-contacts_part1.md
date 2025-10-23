# Source: https://docs.civicrm.org/user/en/latest/initial-set-up/users-contacts/

---
categories: Guide  
level: Basic  
summary: This guide explains how user accounts in Drupal, Joomla, and WordPress connect to CiviCRM contact records and how to synchronize users with contacts.  
section: Initial set up  
---

# Users contacts

## Understanding users and contacts in CiviCRM

In CiviCRM, a **contact** is a record for an individual, organization, or household. A **user** is someone who can log into your website’s content management system (CMS) like Drupal, Joomla, or WordPress. Not every contact has a user account, and not every user automatically has a linked contact record.

This guide will help you understand how user accounts and contacts relate in different CMS platforms and how to make sure they are properly linked.

## How Drupal links users to contacts

When someone registers as a new user on a Drupal site with CiviCRM enabled:

- CiviCRM looks for an existing contact with the same email address.
- If it finds one, it links the user account to that contact.
- If not, it creates a new contact using the user’s email.

When an existing user logs in, CiviCRM checks if they have a linked contact record. If not, it tries to link or create one using the same email matching process.

If you are adding CiviCRM to an existing Drupal site, it’s a good idea to run the **Synchronize Users-to-Contacts** tool to link all current users to contacts.

## How Joomla links users to contacts

Joomla works a little differently because CiviCRM does not automatically check user registrations or logins.

- A Joomla user only links to a CiviCRM contact when they perform a CiviCRM action while logged in, like making a contribution or editing their profile.
- If a user registers on Joomla with the same email as an existing contact, they won’t be linked until they complete a CiviCRM transaction.
- You can replace Joomla’s registration form with a CiviCRM profile form to improve linking.

### Example process in Joomla

1. A person makes a contribution as an anonymous user, creating a contact in CiviCRM.
2. Later, they register as a Joomla user with the same email.
3. When they log in and access their profile through a menu link, Joomla links their user account to the contact record.

Developers can also create Joomla plugins to link users and contacts during user events like registration or login.

## How WordPress links users to contacts

CiviCRM listens for WordPress user registration and profile updates to keep user accounts and contacts in sync.

- When a WordPress user registers or updates their profile, CiviCRM updates the linked contact’s email address.
- Currently, only the email field is synchronized between WordPress users and CiviCRM contacts.

## Synchronize users-to-contacts tool

If you have an existing Drupal or Joomla site and are adding CiviCRM, use the **Synchronize Users-to-Contacts** tool to link all your existing users to contact records.

### How to use the tool

1. Go to **Administer CiviCRM**.
2. Under **Users and Permissions**, select **Synchronize Users to Contacts**.
3. Click **Synchronize Users-to-Contacts**.
4. Confirm the action by clicking **OK**.
5. After the process finishes, you will see a summary showing how many users were checked, how many contacts matched, and how many new contacts were created.

You can then search your contacts to review or update any new records created during synchronization.

## Summary

- Users are people who log into your website’s CMS.
- Contacts are records in CiviCRM that store detailed information.
- Drupal automatically links users and contacts by email during registration and login.
- Joomla links users and contacts when users perform CiviCRM actions while logged in.
- WordPress synchronizes user emails with contacts on registration and profile updates.
- Use the Synchronize Users-to-Contacts tool to link existing users and contacts when adding CiviCRM to your site.

This guide helps you keep your user accounts and contact records connected, so your data stays accurate and useful.