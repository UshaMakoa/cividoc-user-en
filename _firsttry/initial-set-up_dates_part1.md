# Source: https://docs.civicrm.org/user/en/latest/initial-set-up/dates/

---
categories: Guide  
level: Basic  
summary: Learn how to set up and use dates in CiviCRM, including how dates display, how to enter dates, and how to adjust date settings to fit your organization's needs.  
section: Initial set up  
---

# Dates

## Introduction

Dates are important in CiviCRM because they help you track when activities happen, when events occur, and when contributions are made. This guide will help you understand how to set up and use dates in your system, so your data is clear and accurate.

## Date localization

Different countries and languages use different formats for dates and times. To make sure your CiviCRM shows dates in the way that makes sense for your organization, you can adjust the settings under **Administer > Localization > Date Formats**.

## Date display

Dates in CiviCRM can look different depending on where you see them. For example:

- In a report with many donations, dates might be short like `09/19/22` to save space.
- On an event registration form, dates might be longer like `September 19th, 2022` to be clear.

CiviCRM offers about seven common ways to format dates and times. You can customize each one to fit your local preferences. Here are some examples of date formats you might see:

| Format name           | Example format code         | Example display           |
|----------------------|-----------------------------|--------------------------|
| Complete date and time | `%B %E%f, %Y %l:%M %P`      | September 18th, 2022 11:58 PM |
| Complete date         | `%B %E%f, %Y`               | September 19th, 2022     |
| Short date            | `%m/%d/%Y`                  | 09/18/2022               |
| Month and year        | `%B %Y`                     | September 2022           |
| Time only             | `%l:%M %P`                  | 1:34 PM                  |
| Year only             | `%Y`                        | 2022                     |
| Financial batch       | `%m/%d/%Y`                  | 09/19/2022               |

If you want to learn more about how these codes work, you can look up the PHP `strftime()` manual for details.

## Date input fields

When entering dates or times in forms, CiviCRM uses settings called **Date Input Format** and **Time Input Format** to control how users type or pick dates. These settings help make sure dates are entered consistently.

## Calendar settings

You can choose which day starts the week and when your fiscal year begins. This helps CiviCRM show calendars and financial reports that match your organization's schedule. You can set these under the calendar preferences.

## Date preferences

By default, CiviCRM limits the range of dates you can enter for some fields. For example, activity dates might only allow dates from 20 years ago up to 10 years in the future. If your organization needs to track older activities or future plans outside this range, you can update these limits.

To change date ranges:

1. Go to **Administer > Customize Data and Screens > Date Preferences**.
2. Adjust the start and end years to cover the dates you need.

If the date you enter is outside the allowed range, you might see an error like:

`Please enter a date between 01/01/1994 and 12/31/2024.`

Updating the date preferences will prevent this error and let you enter the dates your organization needs.

---

If you want to learn more about working with addresses or customizing your user interface, check those guides next.