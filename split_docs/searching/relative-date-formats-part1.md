# Source: https://docs.civicrm.org/user/en/latest/searching/relative-date-formats/

Here's how you can reformat the page on "Relative Date Formats" using the Diátaxis framework:

---
categories: Guide
level: Basic
summary: This page explains how to use relative date filters in CiviCRM for searching and reporting.
section: Searching and Reporting
---

# using relative date formats in civicrm
## what are relative date filters?
Relative date filters in CiviCRM allow you to search and report on data based on dynamic time ranges, such as "current month" or "last year." These filters are useful for creating reports that automatically update based on the current date.

## list of relative date filters
Below is a list of the relative date filters available in CiviCRM. You can view these filters on your site at the URL `civicrm/admin/options/relative_date_filters`.

| Filter Value | Meaning | Defines |
|--------------|---------|---------|
| `current.month` | Current calendar month to-date | Start and end |
| `current.year` | Current calendar year to-date | Start and end |
| `current.quarter` | Current quarter to-date | Start and end |
| `current.week` | Current week to-date | Start and end |
| ... | ... | ... |

## adding new filters
You can add custom filters using the API or by modifying the code. The syntax for adding filters is flexible, allowing you to create filters like `ending_3.day` for the last three days.

### examples of custom filters
- `ending_3.day`: Last 3 days, including today.
- `ending_3.week`: Last 3 weeks, including today.
- `ending_3.month`: Last 3 months, including today.

### tips for using relative date filters
- Use `ending` filters to count backwards from the current date.
- Use `this` filters to work with full date units (e.g., `this_3.year` for the last three years).

---

This page is categorized as a **Guide** because it provides practical instructions on how to use relative date filters in CiviCRM, which is suitable for users who have some familiarity with the system but need guidance on specific tasks. The level is **Basic** since it covers foundational concepts and does not require advanced knowledge of CiviCRM. 

If you find that the content is too dense or complex, consider splitting it into multiple pages, each focusing on a different aspect of using relative date filters. For example, one page could focus on the basics of relative date filters, while another could delve into advanced customizations and troubleshooting.