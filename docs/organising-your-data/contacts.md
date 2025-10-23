---
categories:
  - Uncategorized
  - Guide  
level: Basic  
summary: This guide introduces CiviCRM contacts, explaining how to find, add, edit, and delete contacts, and how to understand and customize contact information for non-expert nonprofit users.  
section: Organising your data  
---

# Contacts

## Introduction to contacts

Contacts are the foundation of CiviCRM. They represent the people, organizations, or households you work with. In CiviCRM, there are three main contact types:

- **Individuals** (people)
- **Organizations** (companies or nonprofits)
- **Households** (families or groups sharing an address)

Each contact has core information like names, addresses, phone numbers, email addresses, and communication preferences. Contacts connect to all other parts of CiviCRM, such as relationships, activities, contributions, and events.

## Viewing contacts

When you open a contact record, information is organized into tabs for easy navigation. The first tab, **Summary**, shows basic details like names and contact information. Other tabs display related information such as relationships, activities, contributions, memberships, events, groups, notes, and tags.

Some tabs appear only if certain CiviCRM features are enabled or if you have the right permissions.

## Contact actions

Above the tabs, the **Actions** button lets you quickly perform tasks related to the contact, such as adding notes or recording contributions and activities.

## Understanding the summary tab

The summary tab shows:

- Names (with parts like prefix, first name, last name, nickname)
- Addresses (home, work, billing, etc.)
- Phone numbers (work, mobile, fax)
- Email addresses (one can be marked for bulk mailings)
- Communication preferences (how the contact prefers to be contacted)
- Greetings and addressee fields (used in letters and emails)
- Demographic details (birth date, gender, deceased status)

## Managing addresses

You can add multiple addresses for different purposes (e.g., home, work). One address can be marked as primary for mailings. Addresses can be shared between contacts, such as a person and their employer. When shared, updates to the address affect all linked contacts.

If your system has mapping enabled, you can view addresses on a map.

## Phone numbers and emails

Store multiple phone numbers with types (mobile, landline, fax). Mobile numbers can be used for SMS messaging.

Store multiple email addresses and designate one for bulk emails. Emails that bounce during mailings are automatically marked to avoid future mailings.

## Communication preferences and privacy

Contacts can specify how they want to be contacted or if they prefer not to be contacted by phone, email, mail, or SMS. These preferences are respected during mailings and communications.

Privacy options include:

- Do not phone
- Do not email
- Do not mail
- Do not SMS
- Do not trade (no sharing of info with others)
- No bulk emails (opt-out from mass mailings)

## Greetings and addressee formats

CiviCRM automatically creates greetings (like "Dear Jenny") based on contact names. You can customize these globally or for individual contacts.

## Relationships tab

Relationships connect contacts to each other with named connections (e.g., "parent of," "employee of"). A contact can have many relationships.

## Activities tab

This tab lists all interactions with the contact, such as emails, meetings, phone calls, event attendance, and contributions. You can also add new activities here.

## Contributions tab

Shows all financial contributions made by the contact, with options to add offline contributions or credit card payments on their behalf.

## Memberships tab

Displays memberships the contact holds, with options to add, renew, or delete memberships.

## Events tab

Lists events the contact has registered for or attended. You can register the contact for new events and manage their event status.

## Groups tab

Shows groups the contact belongs to, which can be used for mailing lists or permissions. You can add or remove contacts from groups here.

## Notes tab

Use this tab to record informal or additional information about a contact. Notes can be private (visible only to the author) or shared.

## Tags tab

Tags categorize contacts and can be used for searching or creating smart groups.

## Change log tab

Shows basic information about when and who last edited the contact record.

## Adding contacts

To add a new contact:

1. Go to **Contacts > New Individual** (or select other contact types).
2. Fill in the basic information like name and email.
3. Use **Check for Matching Contacts** to avoid duplicates.
4. Add addresses, phone numbers, emails, tags, and groups as needed.
5. Choose **Save** to finish or **Save and New** to add another contact.

Required fields:

- Individuals: first name and last name OR email address
- Organizations/Households: organization or household name

## Editing contacts

You can edit contact information directly on the summary screen by clicking **Edit Info** in each section or open the full edit screen for more detailed changes.

If two users edit the same contact simultaneously, the second user will be notified and can merge changes manually.

## Deleting contacts

Contacts are not permanently deleted immediately; they move to the trash and can be restored later.

- To delete a single contact, open their record and click **Delete Contact**.
- To delete multiple contacts, use advanced search, select contacts, and choose **Delete Contacts** from the actions menu.

## Contact subtypes

You can create custom contact subtypes based on the main types to better organize contacts (e.g., "Student" subtype of Individual). Subtypes allow you to collect specific custom data for different groups.

Contacts can have multiple subtypes but only one main type (Individual, Organization, or Household).

Manage subtypes at **Administer > Customize Data and Screens > Contact Types**.

## Customizing contact views

You can hide or rearrange fields and sections to simplify the contact screen for your needs:

- To hide demographics or change field order: **Administer > Customize Data and Screens > Display Preferences**
- To customize address fields: **Administer > Localization > Address Settings**
- To enable or disable tabs: **Administer > Customize Data and Screens > Display Preferences**

Tabs depend on enabled components and user permissions.
