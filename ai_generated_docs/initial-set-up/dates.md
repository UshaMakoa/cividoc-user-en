# Source: https://docs.civicrm.org/user/en/latest/initial-set-up/dates/

---
categories: Guide
level: Basic
summary: This guide helps non-profit users understand how to manage dates in CiviCRM, including localization, display formats, input fields, and preferences.
section: Initial set up
---

# Managing dates in CiviCRM

## Understanding date localization

In CiviCRM, date and time formats can vary based on your country and language preferences. To set up the appropriate date conventions for your organization, navigate to **Administer > Localization > Date Formats**. This ensures that dates are displayed correctly for your users.

## Date display formats

CiviCRM offers several ways to display dates depending on the context. For example, a report may show dates in a short format (like 09/19/22) to save space, while an event registration form might use a longer format (like September 19th, 2022) for clarity. Here are some common date formats you can customize:

| Format Name               | Example Configuration         | Example Value                   |
|---------------------------|-------------------------------|---------------------------------|
| Complete Date and Time    | %B %E%f, %Y %l:%M %P         | September 18th, 2022 11:58 PM  |
| Complete Date             | %B %E%f, %Y                  | September 19th, 2022           |
| Short Date                | %m/%d/%Y                     | 09/18/2022                      |
| Month and Year            | %B %Y                        | September 2022                  |
| Time Only                 | %l:%M %P                     | 1:34 PM                         |
| Year Only                 | %Y                           | 2022                            |
| Financial Batch           | %m/%d/%Y                     | 09/19/2022                      |

For a complete list of formatting codes, refer to the PHP Manual: strftime().

## Date input fields

When users need to enter dates or times in CiviCRM forms, the **Date Input Format** and **Time Input Format** settings determine how these fields appear. Make sure these formats are user-friendly to facilitate easy data entry.

## Calendar settings

You can customize the calendar settings in CiviCRM by specifying the first day of the week and the month and day that mark the start of your fiscal year. This helps align the system with your organization's operational calendar.

## Adjusting date preferences

By default, CiviCRM allows date entries within a specific range. For instance, the default range for activity dates is set from 20 years before the current year to 10 years after. If your organization needs to track activities from further back, you can adjust this range. To do so, go to **Administer > Customize Data and Screens > Date Preferences**. If you don’t update these settings, users may encounter errors like, "Please enter a date between 01/01/1994 and 12/31/2024."

By understanding and managing these date settings, you can ensure that your CiviCRM system meets the unique needs of your organization and its users.