# Source: https://docs.civicrm.org/user/en/latest/initial-set-up/dates/

---
categories: Guide
level: Basic
summary: This guide provides an overview of how to manage dates in CiviCRM, including localization, display formats, input fields, and preferences.
section: Initial set up
---

# Understanding dates in CiviCRM

In this guide, we will explore how to manage dates in CiviCRM effectively. Understanding how to set up and customize date formats is essential for ensuring that your organization’s data is accurate and easily interpretable.

## Date localization

Date and time conventions can vary significantly depending on your location and language. To ensure that CiviCRM reflects the correct date formats for your needs, navigate to **Administer > Localization > Date Formats**. Here, you can configure the date settings to match your locale.

## Date display

Dates can appear differently based on the context in which they are used. For example, an accounting report may display dates in a compact format (like 09/19/22) to save space, while an event registration form might use a more detailed format (like September 19th, 2022) for clarity.

CiviCRM offers several common date formats, which you can adjust to fit your local preferences. Here are some examples:

| Format Name               | Example Configuration        | Example Value                  |
|---------------------------|------------------------------|--------------------------------|
| Complete Date and Time    | %B %E%f, %Y %l:%M %P        | September 18th, 2022 11:58 PM |
| Complete Date             | %B %E%f, %Y                 | September 19th, 2022          |
| Short Date                | %m/%d/%Y                    | 09/18/2022                     |
| Month and Year            | %B %Y                        | September 2022                 |
| Time Only                 | %l:%M %P                     | 1:34 PM                       |
| Year Only                 | %Y                           | 2022                           |
| Financial Batch           | %m/%d/%Y                    | 09/19/2022                     |

For a complete list of formatting codes, please refer to the PHP Manual: strftime().

## Date input fields

When using forms in CiviCRM, you may need to enter dates or times. The **Date Input Format** and **Time Input Format** settings will adjust how these fields appear on your data-entry screens. Make sure these settings align with your organization's needs.

## Calendar settings

You can customize your calendar settings by specifying the first day of the week and the month and day that mark the beginning of your fiscal year. This helps ensure that your organization’s scheduling aligns with your operational practices.

## Date preferences

By default, CiviCRM allows for a specific range of dates for certain fields. For example, the default range for activity dates is set from 20 years prior to the current year to 10 years into the future. If you need to track activities from further back in time, you can adjust this range. To do so, go to **Administer > Customize Data and Screens > Date Preferences**. 

If you leave the settings at their default values and attempt to enter a date outside of the allowed range, you may encounter an error message like: "Please enter a date between 01/01/1994 and 12/31/2024."

By understanding and customizing these date settings, you can ensure that CiviCRM meets the specific needs of your organization and enhances your data management capabilities.