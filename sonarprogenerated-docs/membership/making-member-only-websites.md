---
categories: Guide
level: Basic
summary: Learn how to set up a members-only section of your website using CiviCRM and your CMS.
section: Membership
---

# Making member only websites

## Overview

If your non-profit wants to offer special content, events, or directories just for members, you can use CiviCRM’s membership features together with your website’s content management system (CMS) to create a members-only area. This guide walks you through the basic steps to make this happen, focusing on what you need to do—not the technical “why” behind it.

## What you’ll need

- A working CiviCRM installation integrated with your CMS (like Drupal, WordPress, or Joomla).
- The CiviMember extension enabled in CiviCRM.
- A CMS module or plugin that supports membership access control (for example, CiviCRM Drupal Integration, CiviCRM WordPress Member Sync, or similar for your CMS).

## Step-by-step how-to

**1. Set up membership types in CiviCRM**  
Go to CiviCRM > Administer > CiviMember > Membership Types. Create the membership types that match your organisation’s needs (for example, “Standard Member,” “Lifetime Member”). Make sure the status is active so people can join.

**2. Create a membership sign-up page**  
Use CiviCRM’s online contribution pages to let people sign up and pay for memberships online. When setting up the page, include the membership option. This way, when someone joins, they become a member in CiviCRM.

**3. Integrate with your CMS**  
Each CMS has its own way to connect CiviCRM memberships with website access. For example:
- **Drupal:** Use the CiviCRM Drupal Integration module to sync membership status with Drupal user roles.
- **WordPress:** Use the CiviCRM WordPress Member Sync plugin to connect CiviCRM memberships with WordPress user roles.
- **Joomla:** Check for extensions that link Joomla user groups with CiviCRM memberships.

Follow the instructions for your specific CMS module or plugin to complete the setup.

**4. Create member-only content**  
In your CMS, create the pages, posts, or directories you want to reserve for members. Use your CMS’s access control features to restrict this content so only users with the right role (synced from CiviCRM) can see it.

**5. Test the workflow**  
Have someone sign up as a member through your CiviCRM page, then log in to your website. Check that they can access the member-only content and that non-members cannot.

## Troubleshooting tips

- **Members can’t access content:** Double-check that the CMS user role is correctly synced with the CiviCRM membership status.
- **Sign-up page issues:** Make sure your contribution page includes the membership option and that payments are processing correctly.
- **Need more help:** Refer to your CMS’s integration documentation or ask the CiviCRM community for support.

## Next steps

Once your members-only area is working, you can add more features, like a private member directory or special event listings, by using CiviCRM’s tools to display member data on your site.

---

# comment: Source: https://docs.civicrm.org/some/page/
# comment: This page is a How-to Guide because it focuses on solving the specific problem of creating a members-only website section, with clear, actionable steps. It does not teach a broad concept (Tutorial), list technical details (Reference), or explain underlying principles (Explanation). The content is practical and task-oriented, ideal for non-expert users who need to accomplish this goal. If the page included detailed technical configuration for each CMS, those sections could be split into separate Reference pages for clarity.