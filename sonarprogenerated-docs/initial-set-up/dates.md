---
categories: Reference
level: Basic
summary: This page describes how dates and times are displayed, entered, and configured in CiviCRM, helping your organisation set up date formats and preferences to match your needs.
section: Initial set up
---

# Dates in CiviCRM

## Date localization

You can set up how dates and times appear in CiviCRM to match your country and language. To do this, go to **Administer > Localization > Date Formats**. This helps your organisation ensure that everyone sees dates in a familiar format.

## Date display

Dates can look different depending on where they appear in CiviCRM. For example:

- In reports, dates might use a short format like **09/19/22** to save space.
- On event registration forms, dates might use a long format like **September 19th, 2022** for clarity.

CiviCRM provides several common date and time formats, including:

| Format name             | Example configuration     | Example value                |
|-------------------------|--------------------------|------------------------------|
| Complete date and time  | %B %E%f, %Y %l:%M %P     | September 18th, 2022 11:58 PM|
| Complete date           | %B %E%f, %Y              | September 19th, 2022         |
| Short date              | %m/%d/%Y                 | 09/18/2022                   |
| Month and year          | %B %Y                    | September 2022               |
| Time only               | %l:%M %P                 | 1:34 PM                      |
| Year only               | %Y                       | 2022                         |
| Financial batch         | %m/%d/%Y                 | 09/19/2022                   |

You can adjust each format to match your organisation’s preferences.

## Date input fields

When filling out forms in CiviCRM, you may need to enter dates or times. The **Date Input Format** and **Time Input Format** settings control how these fields look and work, making it easier for users to enter information correctly.

## Calendar settings

You can choose which day starts the week in your organisation’s calendar, and set the starting month and day for your fiscal year. These options help your organisation track activities and finances in a way that matches your internal processes.

## Date preferences

By default, CiviCRM sets a range of years for date fields. For example, activity dates might be allowed from 20 years ago up to 10 years in the future. If you need to record dates outside this range (such as activities from 25 years ago), you can change the settings by going to **Administer > Customize Data and Screens > Date Preferences**.

If you try to enter a date outside the allowed range, you will see an error message, such as: *Please enter a date between 01/01/1994 and 12/31/2024.*

# comment: Source: https://docs.civicrm.org/user/en/latest/initial-set-up/dates/
# comment: This page is a Reference: it provides systematic, factual information about date handling in CiviCRM, not step-by-step instructions or conceptual background.
