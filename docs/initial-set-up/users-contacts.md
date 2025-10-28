---
categories:
  - Explanation
level: Basic
summary: Learn how CiviCRM connects user accounts in your content management system (Drupal, Joomla, or WordPress) with contact records in CiviCRM.
section: Initial set up
---

# Understanding user accounts and contact records

When you use CiviCRM, it works alongside your website platform—whether that's Drupal, Joomla, or WordPress. These platforms handle who can log into your site (users), while CiviCRM manages information about all the people and organizations you work with (contacts). Understanding how these two systems connect is important for managing your data effectively.

## The difference between users and contacts

**Users** are people who have login credentials for your website. They have a username and password that lets them access certain features. Typically, only staff members, volunteers, or board members need user accounts.

**Contacts** are everyone in your CiviCRM database—donors, members, volunteers, partner organizations, and anyone else your organization interacts with. Most contacts will not have user accounts.

When someone needs both—for example, a staff member who is also a donor—CiviCRM links their user account to their contact record so all their information stays connected.

## How the connection works in different platforms

The way CiviCRM creates these connections varies depending on which content management system you use.

### Drupal

Drupal automatically creates connections between users and contacts. When someone registers for a new account on your site, CiviCRM immediately checks whether a contact with that email address already exists. If it finds a matching contact, it links the new user account to that existing record. If no match exists, CiviCRM creates a brand new contact record.

The same process happens when existing users log in—CiviCRM checks for a linked contact and either connects to an existing one or creates a new record.

### Joomla

Joomla works differently. Simply creating a user account or logging in doesn't automatically trigger a connection to CiviCRM. Instead, the connection happens the first time that logged-in user does something in CiviCRM—like updating their profile, making a donation, or registering for an event.

This means if you manually added someone to CiviCRM and they later create a Joomla account with the same email address, those records won't connect until that person logs in and interacts with a CiviCRM feature on your site. You can work around this by using a CiviCRM profile form for your registration page instead of Joomla's default form.

### WordPress

WordPress uses a middle-ground approach. CiviCRM listens for two events: when a new user registers and when an existing user updates their profile. In both cases, CiviCRM automatically synchronizes the WordPress user account with the corresponding contact record, matching them by email address.

## When to synchronize users to contacts

If you're adding CiviCRM to a website that already has user accounts, those existing users won't automatically have CiviCRM contact records. The synchronization tool solves this problem by checking all your existing user accounts and creating matching contact records where needed.

You'll typically run this synchronization once, right after installing CiviCRM on an existing site. After that, the automatic processes described above handle new users.

### Running the synchronization

To synchronize your existing users with CiviCRM contacts, go to **Administer CiviCRM**, then find **Synchronize Users to Contacts** in the Users and Permissions section.

The tool will examine each user account in your system. For every user without a linked contact record, it will create one using the information from their user account. When it finishes, you'll see a summary showing how many user records were checked, how many already had matching contacts, and how many new contact records were created.

After synchronization completes, you can find the newly created contacts using Advanced Search. In the **Change Log** section, enter the date range that includes when you ran the synchronization.

## Why this matters for your organization

Understanding this connection helps you avoid creating duplicate records and ensures your data stays organized. When you know someone needs a user account, you can check whether they already exist as a contact first. When someone makes a donation before creating an account, you'll understand why their records might not connect automatically in some systems.

This knowledge also helps when troubleshooting. If a volunteer says they can't see their donation history after logging in, you'll know to check whether their user account is properly linked to their contact record.

<!--
Source: https://docs.civicrm.org/user/en/latest/initial
-set-up/users-contacts/ -->

<!--
This page is primarily an Explanation because it clarifies the concept of how users relate to contacts across different CMS platforms, addressing "why" these connections matter and providing background context. However, the "Synchronize Users
-to-Contacts" section contains procedural how-to content that could be split into a separate Guide if needed for clarity. The conceptual understanding is most valuable for non-expert users to grasp before they attempt synchronization. -->
