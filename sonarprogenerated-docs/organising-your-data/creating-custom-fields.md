---
categories: Guide
level: Basic
summary: Learn how to create and manage custom fields in CiviCRM to collect and organize information specific to your organisation’s needs.
section: Organising your data
---

# Creating custom fields

## What are custom fields?

Custom fields let your organisation collect and store information in CiviCRM that is not included by default. For example, you might want to track which services an organisation provides, or record a student’s subjects. Custom fields are grouped into *custom field sets*, which are containers for related fields.

## Before you start

- Think about what information you need to collect and who it applies to (e.g., individuals, organisations, events).
- Plan your custom field sets carefully. Once you set the scope (what type of record the set applies to), you cannot change it later.

## Steps to create custom fields

### 1. Create a custom field set

1. Go to **Administer > Customize Data and Screens > Custom Data**.
2. Click **Add Set of Custom Fields**.
3. Enter a **Set Name**. This will appear as the title for your group of fields.
4. Choose **Used For** to decide what type of record this set will be attached to (such as Contacts, Individuals, Events, etc.).
5. Set the **Order** if you have multiple field sets and want to control their display order.
6. Decide if this set should allow **multiple records** (for example, a person with several educational degrees).
7. Choose **Display options** (inline, tab, or tab with table) for how the set appears.
8. Set whether the field set is **Active** (visible and usable) and **Public** (shown on public pages).
9. Add any **Pre-form Help** or **Post-form Help** text to guide users filling out the fields.
10. Click **Save**.

### 2. Add custom fields to your set

1. In your new field set, click **View and Edit Custom Fields**.
2. Click **New Custom Field**.
3. Fill in the **Field Label** (the name shown to users).
4. Choose the **Type** of field (text, select, checkbox, date, etc.).
5. Set **Database Field Length** if needed (usually leave at the default).
6. Set the **Order** for display within the set.
7. Choose a **Default Value** if you want one.
8. Add **Pre-form Help** or **Post-form Help** for this field if needed.
9. Decide if the field is **Required** (must be filled in).
10. Choose whether to **Optimize for Search** (recommended for fields you’ll often search by).
11. Set whether the field is **Active** and/or **View Only**.
12. For multiple choice fields, add or select your options.
13. Click **Save** or **Save and New** to add more fields.

### 3. Manage your custom fields

- You can edit, disable, delete, or move fields within the set at any time (as long as no data has been entered, you can also change the set’s scope).
- For multiple choice fields, you can add, remove, or reorder options as needed.

## Tips for using custom fields

- Use **custom field sets** to group related information and keep screens tidy.
- Use **multiple record field sets** for information that repeats (like educational history).
- Consider whether information is better stored as a field, group, or tag. For example, use groups for mailing lists and tags for flexible categorization.
- Too many custom fields or sets can slow down your system. If you plan to add many, discuss with your system administrator.

# comment: Source: https://docs.civicrm.org/user/en/latest/organising-your-data/creating-custom-fields/
# comment: Suggestion: This page is a Guide because it provides step-by-step instructions for a specific task (creating custom fields), aimed at helping users achieve a practical goal. It is basic level, as it is for users new to custom fields. The content does not delve into background theory (Explanation), exhaustive options (Reference), or a first-time learning journey (Tutorial). If needed, the “Choosing between fields, groups and tags” section could be split into an Explanation page for deeper understanding.