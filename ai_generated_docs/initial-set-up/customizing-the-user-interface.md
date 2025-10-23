# Source: https://docs.civicrm.org/user/en/latest/initial-set-up/customizing-the-user-interface/

---
categories: Tutorial
level: Basic
summary: This guide provides step-by-step instructions on how to customize the user interface in CiviCRM to better suit the needs of your organization and its users.
section: Customizing the user interface
---

# Customizing the user interface in CiviCRM

CiviCRM is a powerful tool that can be tailored to fit the specific needs of your organization. This guide will help you understand how to customize the user interface so that it is user-friendly and efficient for your team. 

## Changing dropdown options

You can modify the options in dropdown fields on contact entry and editing forms. To do this, navigate to **Administer > Customize Data and Screens > Dropdown Options**. Here are some examples of dropdowns you can customize:

- **Gender**: Add or modify gender options.
- **Phone types**: Change labels for phone types like Mobile or Pager.
- **Website types**: Adjust the categories for websites such as Work or Social Media.

Feel free to add, rename, disable, or remove options to better reflect your organization’s needs.

## Changing display preferences

If there are fields or categories of data that your organization does not track, you can hide these from users to simplify their experience. To adjust display preferences, go to **Administer > Customize Data and Screens > Display Preferences**. Here’s how:

- Uncheck tabs for categories you don’t use, such as Cases or Grants.
- Streamline the editing screen by hiding fields that aren’t relevant to your work.

Remember, hidden information remains in your database, so you can always re-display it later.

## Disabling popup forms

CiviCRM uses popup forms for quick data viewing and editing. If you prefer a traditional browsing experience, you can disable these popups. Go to **Administer > Customize Data and Screens > Display Preferences** and uncheck **Enable Popup Forms**. Keep in mind that this may slow down your interface as every form will require a full page load.

## Disabling activity assignee notifications

By default, CiviCRM sends notifications to all activity assignees when an activity is created. If you want to turn this off, go to **Administer > Customize Data and Screens > Display Preferences** and uncheck **Notify Activity Assignees**. You can also selectively disable notifications for specific activity types.

## Customizing search preferences

You can adjust how searches function in CiviCRM by going to **Administer > Customize Data and Screens > Search Preferences**. Here are some options you can modify:

- **Automatic Wildcard**: Choose whether to automatically add wildcards to search terms.
- **Include Email**: Decide if email addresses should be included in name searches.
- **Smart group cache timeout**: Control how often the smart group cache refreshes.

These adjustments can help speed up searches, especially in larger databases.

## Customizing date preferences

To change how dates are displayed or to set allowed date ranges, navigate to **Administer > Localization > Date Formats** and **Administer > Customize Data and Screens > Date Preferences**. This is particularly useful if you need to log activities from specific time periods.

## Customizing the navigation menu

You can personalize the navigation menu to better fit your organization’s workflows. Go to **Administer > Customize Data and Screens > Navigation Menu** to:

- Add or remove menu items.
- Rename items to use terminology familiar to your users.
- Move items to improve workflow efficiency.

## Making custom data entry forms

If you have staff or volunteers who frequently enter similar data, consider creating a Profile with only the necessary fields. This can streamline the data entry process. To create a Profile, go to **Administer > Customize Data and Screens > Profiles** and follow the prompts to set it up.

## Customizing search views

You can create search views to make finding specific data easier. When creating a Profile, mark it for Search Views and set the visibility for the fields you want to include. 

## Using word replacement to change terminology

CiviCRM allows you to replace existing terminology with terms that better suit your organization. To set this up, go to **Administer > Customize Data and Screens > Word Replacements**. Enter the original text and the replacement text, and check the **Enabled** box to activate it.

By customizing the user interface in CiviCRM, you can create a more efficient and user-friendly experience for your team. Take the time to explore these options and tailor the system to meet your organization’s unique needs.