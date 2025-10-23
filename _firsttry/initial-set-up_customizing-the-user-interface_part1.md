# Source: https://docs.civicrm.org/user/en/latest/initial-set-up/customizing-the-user-interface/

---
categories: Guide  
level: Basic  
summary: Learn how to customize CiviCRM’s user interface to make it easier and faster for your team to use the system.  
section: Initial set up  
---

# Customizing the user interface

CiviCRM is flexible and lets you change how it looks and works to fit your organization’s needs. This guide will help you adjust dropdown menus, display options, search settings, navigation menus, and more — all without needing to be a technical expert.

## Changing dropdown options

Dropdown menus let you choose options like gender, phone types, or location types when entering or editing contacts. You can add, rename, disable, or remove these options to match the words your organization uses.

To update dropdown options:

- Go to **Administer > Customize Data and Screens > Dropdown Options**.
- Choose the dropdown list you want to change (for example, Gender or Phone Types).
- Add new options, rename existing ones, or disable options you don’t use.

You can also change the choices for Preferred Communication Methods (like Phone, Email, SMS) at **Administer > Communications > Preferred Communications Methods**.

*Note:* Changing dropdowns that define data categories (like Activity Types or Contribution Status) is covered in other guides about organizing your data.

## Changing display preferences

If your organization doesn’t use certain features or types of data, you can hide those fields and tabs to make the interface simpler for your users.

To change what shows up:

- Go to **Administer > Customize Data and Screens > Display Preferences**.
- Under **Viewing Contacts**, check or uncheck boxes to show or hide tabs when viewing contact records.
- Under **Editing Contacts**, check or uncheck boxes to show or hide blocks of information when editing contacts.

Hiding tabs or fields does not delete any data — it just hides it from view. You can always show them again later.

## Disabling popup forms

CiviCRM often uses popup windows to quickly view or edit information. If your team prefers traditional page loads instead, you can turn off popup forms.

- Go to **Administer > Customize Data and Screens > Display Preferences**.
- Uncheck **Enable Popup Forms**.

*Note:* Disabling popups will slow down navigation because each form will load as a full page.

## Disabling activity assignee notifications

By default, when an activity is assigned, CiviCRM sends email notifications to the people assigned. You can turn off these notifications if you want.

- Go to **Administer > Customize Data and Screens > Display Preferences**.
- Uncheck **Notify Activity Assignees** to stop all notifications.
- Or choose specific activity types to disable notifications for.

## Customizing search preferences

You can change how CiviCRM’s search works to make it faster or more tailored to your needs.

Go to **Administer > Customize Data and Screens > Search Preferences** to adjust options like:

- **Automatic Wildcard:** Automatically add wildcards before and after search terms for broader matches.
- **Include Email or Nickname:** Include these fields when searching by name.
- **Alphabetical Pager:** Show an A-Z bar to jump to contacts by first letter.
- **Autocomplete fields:** Choose which contact details appear when typing in the Quick Search box.
- **Maximum autocomplete results:** Limit how many results show when searching.

If your database is large and searches are slow, try turning off some of these options.

You can also customize which fields appear on the **Find Contacts** and **Advanced Search** screens under **Display Preferences > Contact Search settings**.

## Customizing date preferences

You can set how dates display and the date ranges users can enter.

- Default date formats are set at **Administer > Localization > Date Formats**.
- To adjust allowed date ranges for specific fields (like activity dates), go to **Administer > Customize Data and Screens > Date Preferences**.
- For example, you can allow users to enter activities from more than 20 years ago by expanding the date range.

## Customizing the navigation menu

Make the menu easier to use by adding, removing, renaming, or moving items.

To customize the menu:

- Go to **Administer > Customize Data and Screens > Navigation Menu**.
- The menu items appear in a folder tree.
- Right-click an item to **Delete** or **Rename** it.
- Drag and drop items to move them.
- Click **Add Menu Item** to create a new menu link:
  - Enter the title and URL.
  - Choose where it appears in the menu.
  - Optionally add a separator line below it.

Use this to simplify the menu or add quick links to forms or external websites.

## Making custom data entry forms

If your team often enters similar contact information, you can create a custom form called a Profile that only shows the fields they need.

To create a data entry form:

- Go to **Administer > Customize Data and Screens > Profiles** and click **Add Profile**.
- Give your form a clear name (for example, "Volunteer Contact Form").
- Check **Standalone Form or Directory** under **Used For**.
- Add helpful instructions in the **Pre-form Help** and **Post-form Help** fields.
- Save and then add fields by selecting the contact type and the fields you want.
- Mark fields as **Required** if needed.
- Arrange the order of fields using the **Order** number.
- Preview the form and copy its link to share or add to the navigation menu.

## Customizing search views

You can create custom search result views to show only the information you want.

To do this:

- Create or edit a Profile and set it as **Used for Search Views**.
- When adding fields, set their visibility to **Public Pages** and check **Results Column**.
- When running an advanced search, select your profile from the **Search Views** dropdown to see your custom columns.

## Using word replacement to change terminology

If your organization uses different words than CiviCRM’s defaults, you can replace them everywhere in the system.

To set up word replacements:

- Go to **Administer > Customize Data and Screens > Word Replacements**.
- Enter the original word or phrase and your replacement.
- Choose whether to match exactly or replace all variations.
- Enable each replacement by checking the box.
- Save your changes.

For example, replace "Contribution" with "Donation" to match your organization’s language.

*Note:* Word replacements only work when the original text is in English, even if you use CiviCRM in another language.

---

If you want to learn more about customizing data fields or organizing your data, see the guides on **Organizing your data** and the specific sections for components like **Events** or **Membership**.