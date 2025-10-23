---
categories:
  - Uncategorized
  - Tutorial
level: Basic
summary: This guide explains how to manage permissions and access control in CiviCRM, ensuring users can effectively use the system while keeping data secure.
section: Permissions and access control
---

# Managing permissions and access control in CiviCRM

In CiviCRM, permissions and access control are essential for ensuring that users can perform their tasks while protecting sensitive data. This guide will help you understand how to set up and manage permissions effectively.

## Understanding permissions and access control

Permissions are rules that determine what users can see and do within CiviCRM. By creating roles, assigning permissions to those roles, and then assigning users to these roles, you can control access to various areas of the system.

### Why are permissions important?

Properly configured permissions help maintain the security of your data. If permissions are set incorrectly, sensitive information may be exposed. It's crucial to understand the implications of each permission before assigning it.

## The difference between CMS permissions and CiviCRM ACLs

Permissions in CiviCRM are managed separately from your content management system (CMS). While CMS permissions control access to entire sections of CiviCRM, CiviCRM's Access Control Lists (ACLs) allow for more detailed control over specific records and actions.

### When to use CMS permissions

For many organizations, CMS permissions are sufficient. They allow you to grant or restrict access to broad sections of CiviCRM, like CiviMail or CiviEvent. However, if you need more granular control, you should consider using CiviCRM ACLs.

### When to use CiviCRM ACLs

CiviCRM ACLs are useful when you need to restrict access to specific groups of contacts or particular data fields. For example, if a regional office should only access its local contacts, you would use ACLs to enforce this restriction.

## Setting up CMS permissions

Each CMS has its own method for managing permissions. Here’s a brief overview of how to set permissions in popular CMS platforms:

### In Drupal

1. Go to the **People** menu.
2. Click on the **Permissions** tab.
3. Review the list of actions and check the boxes for the roles you want to grant access.

### In Joomla!

1. Log into the Joomla! administrative portal.
2. Navigate to **Components > CiviCRM > Administer > User and Permissions > Permissions**.
3. Adjust the permissions for each user group as needed.

### In WordPress

1. Go to **Administer > User and Permissions > Permissions** in CiviCRM.
2. Select the **WordPress Access Control** link to adjust settings for predefined user roles.

## Managing access for anonymous and authenticated users

CiviCRM distinguishes between anonymous users (those who haven't logged in) and authenticated users (logged-in users). By default, both roles have similar permissions, but you can customize these as needed.

### Common scenarios

- **Taking online contributions**: If you want only logged-in users to make contributions, remove the permission from the anonymous role.
- **Viewing events**: If you want to restrict event registration, use ACLs to control who can view or register for specific events.

## Using CiviCRM ACLs for more granular control

CiviCRM ACLs provide a more advanced way to manage user access. Here’s how to set them up:

### Step 1: Manage roles

1. Go to **Administer > User and Permissions > Permissions**.
2. Click on **Manage Roles** to create new roles as needed.

### Step 2: Assign users to roles

1. Create a contact group for users who need similar access.
2. Assign this group to the appropriate ACL role.

### Step 3: Create ACLs

1. Return to the **Permissions** screen and click on **Manage ACLs**.
2. Click **Add ACL** and fill in the required fields, including role, operation, and type of data.

## Conclusion

Understanding and managing permissions in CiviCRM is crucial for maintaining data security while allowing users to perform their tasks efficiently. Start with CMS permissions for broader access control, and use CiviCRM ACLs when you need more specific restrictions. With careful management, you can create a secure and effective environment for your organization's needs.
