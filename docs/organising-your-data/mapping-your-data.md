---
categories:
  - Explanation
level: Basic
summary: This page explains how to organize and map your organisation’s existing data into CiviCRM, helping you understand where different types of information fit and how to avoid common mistakes.
section: Organising your data
---

# Mapping your data

## What does “mapping your data” mean?

Mapping your data means taking information your organisation already has—whether in spreadsheets, paper files, or staff memory—and deciding where it belongs in CiviCRM. This step is important because putting information in the right place helps you use CiviCRM’s features fully and avoids confusion later.

For example, if you put membership expiration dates in a custom field instead of using the built-in membership module, you might miss out on automatic reminders and reporting. Try to use CiviCRM’s existing features before creating new fields, as this keeps your data clean and easy to manage.

## How CiviCRM helps you organise information

CiviCRM is designed for non-profits and offers flexible ways to store information about your supporters, donors, members, and partners. Instead of keeping everything in “flat” spreadsheets, CiviCRM uses relationships and categories to connect data, giving you a fuller picture of your community.

Below are the main types of information you’ll map into CiviCRM:

### Basic information about your constituents

CiviCRM has built-in fields for names, addresses, phone numbers, emails, and notes. Contacts are divided into three types:

- **Individuals**: People your organisation interacts with.
- **Organisations**: Other non-profits, companies, chapters, or committees.
- **Households**: Families or groups sharing a physical address.

Each contact type has different fields—like gender for individuals, but not for organisations or households.

### Information specific to your organisation (custom fields)

If you need to track details unique to your mission (like allergies or service areas), you can create custom fields in CiviCRM. Before adding custom fields, decide if the information applies to an individual, organisation, or household, and check if there is already a suitable field.

### Relationships between constituents

Relationships record how two contacts are connected, such as “parent–child” or “employer–employee.” You can create your own relationship types to match your organisation’s needs. Relationships help you track connections, such as family members or past employers, and can be used to group people who share an address (households).

### Activities

Activities record interactions with your constituents, such as phone calls, meetings, or emails. CiviCRM automatically creates activities for things like contributions, event attendance, and membership renewals. You can also add your own activity types (e.g., training or support).

### Events (CiviEvents)

CiviCRM manages events like webinars, performances, and meetings. You can record registrations, track attendance, and analyse participation. Event types help you distinguish between different kinds of events and see which are most popular.

### Memberships

Memberships let people join your organisation for a set period and receive benefits. CiviCRM tracks membership levels, start dates, dues paid, and renewals. Before importing membership data, review your current structure and simplify where possible. Avoid creating too many membership types.

### Contributions

Contributions include money, goods, or services received. CiviCRM records the amount, date, type, and payment method. Decide which contributions to import, focusing on those that are most relevant for your organisation.

### Campaigns

Campaigns group activities and contributions around a common goal, such as a fundraising drive. Use campaigns to track how different efforts support your objectives.

### Grouping and tagging constituents

Groups and tags help you organise contacts for communications, invitations, and reporting. Groups are useful for mailing lists or identifying people with something in common. Tags are keywords you can quickly add or remove. Smart Groups automatically update based on criteria you set.

### Profiles

Profiles are sets of fields used for editing or displaying contact information. They help staff collect and view the right data for different tasks.

## Where next?

This page gives an overview of how to map your data into CiviCRM. For more details on each component, see the chapters on CiviEvent, CiviMember, CiviMail, CiviContribute, CiviCase, CiviCampaign, and CiviGrant. These sections will help you streamline tasks like event management, membership, communications, fundraising, and more.

<!--
Source: https://docs.civicrm.org/some/page/
 -->

<!--
This content is best classified as an Explanation, as it provides conceptual background and practical context for mapping organisational data into CiviCRM, rather than step
-by-step instructions or exhaustive technical details. It is suitable for basic-level users who are new to CiviCRM and need to understand how their data fits into the system. If desired, more detailed Guides or Tutorials could be created for specific data import tasks, while Reference material could list all possible fields and data structures. -->
