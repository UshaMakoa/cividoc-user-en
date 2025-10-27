---
categories: Guide
level: Basic
summary: Learn how to adjust dropdown options, display settings, search preferences, navigation menus, and terminology in CiviCRM to make the system easier for your organisation to use.
section: Initial set up / Customizing the user interface
---

# Customizing the user interface

CiviCRM lets you tailor the user interface so it matches your organisation’s needs and makes everyday tasks easier for your team. This guide shows you how to adjust dropdown menus, display settings, search preferences, navigation menus, data entry forms, and system terminology.

## Change dropdown options

You can add, rename, disable, or remove options from dropdown fields (like gender, prefixes, phone types, and more) to match your organisation’s language and needs.

- Go to **Administer > Customize Data and Screens > Dropdown Options**.
- Choose the dropdown you want to edit (such as Gender, Individual Prefixes, Phone Types, etc.).
- Add, rename, disable, or remove options as needed.

For "Preferred Communication Methods" (like Phone, Email, SMS):

- Go to **Administer > Communications > Preferred Communication Methods** and adjust the options.

*Note: Some dropdowns that define core data (like Activity Type or Contribution Status) are managed elsewhere. See the Organising Your Data section for those.*

## Change display preferences

You can hide fields or tabs that your organisation doesn’t use, making the interface simpler for your users.

- Go to **Administer > Customize Data and Screens > Display Preferences**.

To hide or show tabs when viewing contacts:
- Check or uncheck the boxes next to each tab under "Viewing Contacts".

To hide or show sections when editing contacts:
- Check or uncheck the boxes under "Editing Contacts".

*Any data in hidden fields or tabs stays in your database and will reappear if you show the fields again.*

## Disable popup forms

If you prefer not to use popup windows for editing or viewing data:

- Go to **Administer > Customize Data and Screens > Display Preferences**.
- Uncheck **Enable Popup Forms**.

*Disabling popups may slow down the interface, as each form will load as a full page.*

## Disable activity assignee notifications

By default, CiviCRM emails all activity assignees when an activity is created. To turn this off:

- Go to **Administer > Customize Data and Screens > Display Preferences**.
- Uncheck **Notify Activity Assignees**.
- You can also disable notifications for specific activity types below this option.

## Customize search preferences

Adjust how searches work to suit your organisation’s needs and improve speed, especially for large databases.

- Go to **Administer > Customize Data and Screens > Search Preferences**.

Available options include:
- **Automatic Wildcard**: Choose if searches should match parts of names or just the start.
- **Include Email/Nickname**: Decide if these fields are included in name searches.
- **Include Alphabetical Pager**: Show an A–Z bar for browsing results.
- **Include Order By Clause**: Choose if results are ordered.
- **Smart group cache timeout**: Set how often smart group results are refreshed.
- **Autocomplete Contact Search**: Choose which fields show up in quick search results.
- **Contact Reference Options**: Set which fields appear in autocomplete for contact reference fields.
- **Autocomplete Results**: Set the maximum number of results shown.

You can also adjust which fields appear on the main search screens:
- Go to **Administer > Customize Data and Screens > Display Preferences** and use the "Contact Search" section.

## Customize date preferences

Set how dates are displayed and what date ranges are allowed.

- To set the default date format: **Administer > Localization > Date Formats**.
- To set allowed date ranges for specific fields: **Administer > Customize Data and Screens > Date Preferences**.

For example, you can allow activity dates from 25 years ago if your organisation needs to track older events.

## Customize the navigation menu

You can add, remove, rename, or move items in the CiviCRM navigation menu to match your workflows.

- Go to **Administer > Customize Data and Screens > Navigation Menu**.
- To delete or rename a menu item, right-click it and select the option.
- To move an item, drag and drop it where you want.
- To add a new item:
  - Click **Add Menu Item**.
  - Fill in the title and URL.
  - Choose where it should appear in the menu.
  - Optionally, add a separator line below it.

## Make custom data entry forms

If your team enters lots of similar contacts, create a custom Profile form with just the fields you need.

- Go to **Administer > Customize Data and Screens > Profiles** and click **Add Profile**.
- Name your Profile (e.g., "Volunteer Data Entry Form").
- Choose **Standalone Form or Directory** in the "Used For" field.
- Add help text as needed.
- Click **Save** to add fields.
- For each field:
  - Select the contact type (Individual, Organization, etc.).
  - Choose the field.
  - Edit the label if needed.
  - Mark as required if necessary.
  - Add help text if useful.
  - Set the order for display.
- Click **Save and New** to add more fields, or **Save** when done.
- Preview your form and copy its link to add to your navigation menu if desired.

## Customize search views

You can control which fields show up in search results by creating a Profile for search views.

- Create or open a Profile and set it as used for "Search Views".
- When adding fields, set their visibility to "Public Pages" and check the "Results Column" box.
- When running an advanced search, choose your Profile from the "Search Views" dropdown.

## Use word replacement to change terminology

Replace words across CiviCRM to match your organisation’s language (for example, change "Contribution" to "Donation").

- Go to **Administer > Customize Data and Screens > Word Replacements**.
- Enter the original word and your replacement.
- Check "Exact Match" if you only want to replace exact matches.
- Check "Enabled" to activate the replacement.
- Add more rows as needed and click **Save**.

*Note: Word replacements only work if you enter the English word, even if your CiviCRM is in another language.*

---

# comment: Source: https://docs.civicrm.org/user/en/latest/initial-set-up/customizing-the-user-interface/
# comment: This page is a Guide, as it gives step-by-step instructions for achieving specific configuration tasks, but does not serve as a tutorial for first-time users nor as a reference listing all options. Level is Basic, as it assumes little prior knowledge. If the page grows, some sections (like dropdown option lists or date format settings) could be split into Reference pages for easier lookup.