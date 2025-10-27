---
categories:
  - Guide  
level: Basic  
summary: This guide explains how non-expert users of CiviCRM can create and manage custom fields to collect additional information tailored to their organization's needs.  
section: Organising your data  
---

# Creating custom fields

## Introduction

CiviCRM lets you collect extra information about your contacts and records by creating **custom fields**. These fields help you track details that are not included by default in CiviCRM. For example, you might want to add checkboxes to track which clients an organization serves or add a field listing subjects studied by students.

Custom fields are always grouped into **custom field sets**, which act like containers holding related fields together. Creating custom data involves two steps:

1. Create a **custom field set** (the container for your fields).  
2. Add **custom fields** to that set.

## Custom field sets

A **custom field set** defines where and how the custom fields apply. For example, you might create a field set called "Nationality" that applies to all contact types, or one called "Immigration status" that applies only to individual contacts.

### Important considerations when creating a field set:

- Decide **what the fields will be used for** and which types of records they relate to (e.g., Individuals, Organizations, Events).  
- The **scope** of a field set is permanent—you cannot change it after creating the set.  
- Group related fields together for clarity. For example, split a large number of fields into smaller sets based on their topic or purpose.

### Examples of "Used For" options include:

- Contacts (all contacts or specific types like Individual or Organization)  
- Activities (e.g., meetings, phone calls)  
- Events (all events or specific event types)  
- Contributions (all contributions or specific financial types)  
- Participants (event registrations)  
- Relationships (e.g., spouse, employee)  

You create and manage custom field sets by going to:  
**Administer > Customize Data and Screens > Custom Data**

### Display options for field sets on contact records

- **Inline display:** Fields appear directly on the contact summary screen.  
- **Tab display:** Fields appear under a separate tab.  
- You can also choose to have the field set **collapsed** by default to save space.

### Multiple record field sets

Some field sets can hold **multiple records** per contact. For example, if you want to track multiple educational qualifications for a person, use a multiple record field set. This option is only available for contacts.

## Creating custom fields

After creating a custom field set, add fields to it. Each field has options to define how it behaves and appears.

### Key field settings:

- **Field label:** The name shown to users and in exports.  
- **Type:** Choose the kind of data (text, number, date, checkbox, select list, file upload, contact reference, etc.).  
- **Database field length:** Usually leave at default maximum.  
- **Order:** Controls the order fields appear in the form.  
- **Default value:** Optional preset value for the field.  
- **Help text:** Add instructions above (pre-form) or below (post-form) the field to guide users.  
- **Required:** Make the field mandatory for data entry.  
- **Optimize for search:** Index the field to speed up searches if it will be used frequently in filters or reports.  
- **Active:** Enable or disable the field's visibility.  
- **View only:** Show the field but prevent editing (useful for imported or system-managed data).  
- **Multiple choice options:** For fields like dropdowns or checkboxes, define the list of choices users can select.

### Managing multiple choice options

You can reuse option sets across multiple fields or create new ones. You can edit option labels, order, and active status later.

## Best practices and tips

- Think carefully about whether to use **custom fields, groups, or tags**. Groups and tags can be easier to manage for categories of contacts and support powerful search and mailing features.  
- Avoid creating too many custom fields or very large field sets, as this can slow down searches and reports. Consult your system administrator if unsure.  
- Preview your custom fields as you create them to check layout and usability.  
- Use clear, simple field labels and help text to make data entry easier for all users.

## Where to find custom fields

Once created, custom fields appear in contact records, event registrations, contribution records, or wherever you assigned them. You can edit or disable fields later but cannot change the field set scope after creation.
