---
categories:
  - Explanation
level: Intermediate
summary: Understand how permissions and access control work in CiviCRM, including the difference between CMS and CiviCRM ACLs, to help you keep your data secure and organized.
section: Initial set up
---

# Permissions and access control in CiviCRM

## What are permissions and access control?

Permissions and access control lists (ACLs) are rules that determine who can see and do what in your CiviCRM system. You create roles (like “Event Coordinator” or “Fundraiser”), assign permissions to those roles, and then assign people to the roles. This helps you make sure staff and volunteers only access the information and features they need for their jobs, keeping your data safe and organized[1].

## Why is this important?

Setting up permissions correctly is crucial for security. If permissions are too loose, sensitive information could be seen by the wrong people. If they’re too tight, your team might not be able to do their work. It’s easy to make mistakes, so take your time to understand what each permission does before you assign it.

## The difference between CMS permissions and CiviCRM ACLs

- **CMS permissions** are managed in your website platform (Drupal, Joomla!, or WordPress). They control access to whole sections of CiviCRM, like CiviMail or CiviEvent, and basic actions like viewing, editing, or deleting records. However, CMS permissions are “all or nothing”—you can’t, for example, let one team edit only their own contacts[1].
- **CiviCRM ACLs** (Access Control Lists) give you much more detailed control. You can limit access to specific groups of contacts, certain custom fields, particular events, or even individual profiles. This is useful when different teams or locations need access to different parts of your data[1].

**When to use which:** Start with CMS permissions. If you need more precise control—for example, letting regional offices manage only their own events or contacts—use CiviCRM ACLs.

## Common scenarios

Here are some everyday situations where permissions matter:

- **Online contributions:** If you only want logged-in users to donate, remove the “make online contributions” permission from the “anonymous” role.
- **Event registration:** If you want some events to be public and others private, use CiviCRM ACLs to control who can register.
- **Editing profiles:** Only logged-in users can edit their own information in online forms, unless you use a special “checksum” link.
- **Custom data:** If you collect different information from different groups (like volunteers vs. donors), use CiviCRM ACLs to control who can see or edit which custom fields.
- **Uploaded files:** If you want the public to see photos or documents on your site, give the “anonymous” role permission to “access uploaded files.”
- **Contact dashboard:** Let logged-in users see their own contributions, memberships, and event registrations by enabling the “access contact dashboard” permission for the “authenticated” role.

## How to manage permissions

**In Drupal:** Go to People > Permissions. Here you can see all possible actions and assign them to roles. You can also create new roles and assign them to users through their contact record or user profile.

**In Joomla!:** Go to Components > CiviCRM > Administer > User and Permissions > Permissions (Access Control). User groups inherit permissions from parent groups, so plan your structure carefully.

**In WordPress:** Go to Administer > User and Permissions > Permissions (Access Control) and adjust settings for each WordPress user role.

**Financial type permissions:** For even more control over who can see or edit different types of donations, enable “Access Control by Financial Type” in CiviContribute settings.

## Native CiviCRM ACLs: A closer look

If you need very specific control, use CiviCRM’s own ACL system:

1. **Create ACL roles** (like “Regional Fundraiser”).
2. **Assign users to these roles** by first creating a contact group, then linking the group to the role.
3. **Define exactly what each role can do**—view, edit, delete, etc.—and on which data (groups, profiles, custom fields, or events).

This system lets you, for example, allow staff in one office to manage only their local donors, while headquarters can see everything.

## Tips for success

- **Start simple:** Use CMS permissions for most needs. Only use CiviCRM ACLs when you need more detail.
- **Test as you go:** After changing permissions, log in as a test user to make sure everything works as expected.
- **Document your setup:** Keep a record of which roles have which permissions, especially if your team changes over time.
- **Review regularly:** As your organization grows, revisit your permissions to make sure they still fit your needs.

## Summary table: Key permissions for anonymous and authenticated users

| Permission                        | Anonymous Role | Authenticated Role | Purpose                                                                 |
|------------------------------------|:--------------:|:------------------:|-------------------------------------------------------------------------|
| Access all custom data             |       ✔️       |         ✔️         | View/edit all custom fields in forms                                    |
| Access uploaded files              |       ✔️       |         ✔️         | View/download files and images                                          |
| Profile create                     |       ✔️       |         ✔️         | Add data via online forms                                               |
| Profile edit                       |       ✔️       |         ✔️         | Edit data in standalone profiles (with checksum for anonymous)          |
| Profile view                       |       ✔️       |         ✔️         | View data in profiles                                                   |
| Register for events                |       ✔️       |         ✔️         | Sign up for events                                                      |
| View event info                    |       ✔️       |         ✔️         | See event details                                                       |
| View event participants            |       ✔️       |         ✔️         | See who’s registered                                                    |
| Make online contributions          |       ✔️       |         ✔️         | Donate or pay online                                                    |
| Access CiviMail subscribe pages    |       ✔️       |         ✔️         | Join/leave mailing lists                                                |
| View public CiviMail content       |       ✔️       |         ✔️         | See mailings on your site                                               |
| Sign CiviCRM Petition              |       ✔️       |         ✔️         | Sign petitions (if CiviCampaign is enabled)                             |
| Access contact dashboard           |       ❌       |         ✔️         | See own contributions, memberships, event registrations                 |

## When to ask for help

If you’re not sure how to set up a particular permission, or if something isn’t working as expected, ask your CiviCRM administrator or consult the community. Permissions can be complex, but getting them right is worth the effort for your organization’s security and efficiency.

<!--
Source: https://docs.civicrm.org/user/en/latest/initial
-set-up/permissions-and-access-control/ -->

<!--
This page is best categorized as an Explanation because it provides background, context, and rationale for permissions and access control in CiviCRM, rather than step
-by-step instructions or a quick reference. It helps non-expert users understand “why” and “how” permissions work, which is essential for making good decisions about securing their data[2][3]. If you need specific “how-to” steps for your CMS, those should be split into separate Guide pages. -->
