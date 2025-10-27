---
categories: Guide
level: Basic
summary: Learn how to find and work with contacts and data in CiviCRM using quick, advanced, and component searches, plus tips for customizing results and using search actions.
section: Searching and reporting
---

# Introduction to searching and reporting

## Overview

CiviCRM offers several ways for your organisation to find and use information stored in your database. You can start with simple searches and move to more advanced techniques as you get comfortable. This guide covers:

- How to quickly find contacts using Quick search.
- Using Advanced search for more detailed searches.
- Searching text across all fields with Full-text search.
- Finding data in specific areas like events or memberships with Component searches.
- Using custom searches from CiviCRM core or extensions.
- What you can do with search results, such as sending emails or exporting data.
- How to use wildcards and understand case sensitivity in searches.
- Adjusting the number of results shown.
- An introduction to SearchKit for advanced users.

## Why search?

You might search in CiviCRM to:

- Find a specific contact by name, email, or other details.
- Take action on a group of contacts, such as sending reminders or invitations.
- Create ad-hoc reports for quick insights.

For more complex reports, CiviReport offers additional options.

## Quick search

Quick search is the easiest way to find a contact. Use the search box at the top left of your screen. You can search by name, email, or other criteria. To adjust what Quick search looks for, go to **Administer > Customize Data and Screens > Search Preferences**.

- Start typing in the Quick search box; matching contacts appear below.
- You don’t need to type the full name—just a few letters often works.
- If you don’t see the contact, type more characters or press Return to switch to Advanced search.
- By default, Quick search shows up to 10 results; you can change this in Search Preferences.
- Nicknames are included in searches (e.g., “Joe” finds “Joseph”). You can turn this on or off in Search Preferences.

**Tip:** When searching by phone, enter only the digits, with no spaces or symbols.

**Pitfall:** If searching by name, use the format “Lastname, Firstname” (e.g., “Peterson, Mary”).

## Advanced search

Advanced search lets you find contacts using many criteria, such as location, group membership, or activities. Access it from **Search > Advanced Search** in the menu.

- Criteria are grouped into sections (called accordions); click to expand and set your search options.
- For example, to find people aged 16–18, open the Demographics section and set the birth date range.
- You can combine multiple criteria to narrow your results.

## Customizing results

- By default, search results show contact details like name and address.
- You can display other types of records (e.g., memberships) by choosing from the “Display Results As” dropdown.
- To change which columns appear, create a Profile with the “Search Views” option. Make sure fields are set to be visible for listings and marked as Results Columns.

**Tip:** Combine with “Batch Update via Profile” to quickly update multiple records.

## Search settings

- The Search Operator controls whether criteria are combined with AND (all must match) or OR (any can match).
- You can search for deleted contacts in the Trash if you have permission.

## Date range filter

- Many searches let you filter by date, either with exact dates or relative ranges (like “Last week”).
- Relative date ranges help create Smart Groups (auto-updating groups based on criteria).
- You can set which day is the start of the week in **Administer > Localization > Date Format**.

## Combining criteria

- Criteria are usually combined with AND (all must match), but you can change to OR in Search Settings.
- Within a group of checkboxes, options are also combined with AND.
- Dropdown lists combine selected values with OR.

**Tip:** To remove a criteria group from your search, click the cross on the section header.

## Limitations

Advanced search works well for most needs, but there are some limits (e.g., filtering activities by case type is not always accurate).

## Full-text search

Full-text search looks for words in all text fields. Use it if you remember a word or phrase but not where you saved it.

## Component searches

Each CiviCRM component (like Contributions, Memberships, Events) has its own search form. These work like Advanced search but focus on that component’s data.

- Each component search has its own list of actions you can take on results.

## Search results actions

After searching, you can select records and choose actions such as:

- Add contacts to a group
- Export contacts
- Map contacts (requires setup)
- Print mailing labels
- Send emails

Actions are listed above your results.

## Contact summary pop-up

Hover over a contact icon in your results to see a pop-up with more details. You can customize which fields appear in this view by editing the “Summary Overlay” profile.

## Using wildcards (%)

A wildcard (%) stands for any character(s) in your search. For example, “Mich%” finds “Michael”, “Michelle”, and similar names.

- Use % before, after, or within words to broaden your search.
- To find records with any data in a field, use “%_%”.
- Using just % can sometimes return empty values.

## Case sensitivity

Searches are not case-sensitive. For example, searching for “brooklyn” finds “Brooklyn” and “BROOKLYN”.

## Default number of rows

By default, Advanced search and reports show 50 rows. Administrators can change this in **Search Preferences**. Higher numbers may slow down loading.

## SearchKit

SearchKit is a powerful tool for advanced users, allowing more complex searches and reports. See the SearchKit section for details.

# comment: Source: https://docs.civicrm.org/user/en/latest/searching/reporting/introduction/
# comment: This page is a Guide: it shows users how to accomplish specific tasks (finding and working with data), with actionable steps and tips, but does not teach concepts or provide reference details. The content is basic, aimed at non-experts learning how to perform searches and related actions. It belongs in the "Searching and reporting" section. If desired, the Quick search and Advanced search portions could be split into separate Tutorials for first-time users, but the current content is best served as a Guide.