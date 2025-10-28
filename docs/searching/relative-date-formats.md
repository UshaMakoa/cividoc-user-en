---
categories:
  - Reference
level: Basic
summary: A complete list and description of all relative date filters available in CiviCRM, to help you quickly select the right filter for your reports and searches.
section: Searching and reporting > Search Kit
---

# Relative date filters

Relative date filters in CiviCRM let you easily select time periods like “last month”, “this year”, or “next 7 days” when building searches and reports. This page lists all available filters, explains what each one means, and shows how you can add new ones if needed.

## List of relative date filters

You can use these filters in Search Kit, reports, and other search tools. Each filter name is shown as it appears in CiviCRM, with a short description of what time period it covers.

| Filter name                  | Meaning                                             | Defines         |
|------------------------------|----------------------------------------------------|-----------------|
| **current.month**            | Current calendar month to date                     | start and end   |
| **current.year**             | Current calendar year to date                      | start and end   |
| **current.quarter**          | Current quarter to date                            | start and end   |
| **current.week**             | Current week to date                               | start and end   |
| **previous_before.day**      | Day before yesterday                               | start and end   |
| **greater_previous.month**   | From end of previous calendar month                | start           |
| **greater_previous.year**    | From end of previous calendar year                 | start           |
| **greater_previous.quarter** | From end of previous quarter                       | start           |
| **greater_previous.week**    | From end of previous week                          | start           |
| **greater.month**            | From start of current calendar month               | start           |
| **greater.year**             | From start of current calendar year                | start           |
| **greater.day**              | From start of current day                          | start           |
| **greater.quarter**          | From start of current quarter                      | start           |
| **greater.week**             | From start of current week                         | start           |
| **ending.year**              | Last 12 months including today                     | start and end   |
| **ending_2.year**            | Last 2 years including today                       | start and end   |
| **ending_3.year**            | Last 3 years including today                       | start and end   |
| **ending_30.day**            | Last 30 days including today                       | start and end   |
| **ending_60.day**            | Last 60 days including today                       | start and end   |
| **ending.week**              | Last 7 days including today                        | start and end   |
| **ending_90.day**            | Last 90 days including today                       | start and end   |
| **previous_before.month**    | Month before previous calendar month               | start and end   |
| **starting.year**            | Next 12 months including today                     | start (now) and end |
| **starting.month**           | Next 30 days including today                       | start (now) and end |
| **starting_2.month**         | Next 60 days including today                       | start (now) and end |
| **starting.week**            | Next 7 days including today                        | start (now) and end |
| **starting.quarter**         | Next 90 days including today                       | start (now) and end |
| **next.month**               | Next calendar month                                | start and end   |
| **next.year**                | Next calendar year                                 | start and end   |
| **next.fiscal_year**         | Next fiscal year                                   | start and end   |
| **next.quarter**             | Next quarter                                       | start and end   |
| **next.week**                | Next week                                          | start and end   |
| **previous_2.month**         | Previous 2 calendar months                         | start and end   |
| **previous_2.year**          | Previous 2 calendar years                          | start and end   |
| **previous_2.fiscal_year**   | Previous 2 fiscal years                            | start and end   |
| **previous_2.day**           | Previous 2 days                                    | start and end   |
| **previous_2.quarter**       | Previous 2 quarters                                | start and end   |
| **previous_2.week**          | Previous 2 weeks                                   | start and end   |
| **previous.month**           | Previous calendar month                            | start and end   |
| **previous.year**            | Previous calendar year                             | start and end   |
| **previous.fiscal_year**     | Previous fiscal year                               | start and end   |
| **previous.quarter**         | Previous quarter                                   | start and end   |
| **previous.week**            | Previous week                                      | start and end   |
| **previous_before.quarter**  | Quarter before previous quarter                    | start and end   |
| **this.month**               | This calendar month                                | start and end   |
| **this.year**                | This calendar year                                 | start and end   |
| **this.fiscal_year**         | This fiscal year                                   | start and end   |
| **this.quarter**             | This quarter                                       | start and end   |
| **this.week**                | This week                                          | start and end   |
| **less.month**               | To end of current calendar month                   | end             |
| **less.year**                | To end of current calendar year                    | end             |
| **less.quarter**             | To end of current quarter                          | end             |
| **less.week**                | To end of current week                             | end             |
| **earlier.month**            | To end of previous calendar month                  | end             |
| **earlier.year**             | To end of previous calendar year                   | end             |
| **earlier.quarter**          | To end of previous quarter                         | end             |
| **earlier.week**             | To end of previous week                            | end             |
| **earlier.day**              | To end of yesterday                                | end             |
| **this.day**                 | Today                                              | start and end   |
| **starting.day**             | Tomorrow                                           | start and end   |
| **previous_before.week**     | Week before previous week                          | start and end   |
| **previous_before.year**     | Year before previous calendar year                 | start and end   |
| **previous_before.fiscal_year** | Fiscal year before previous fiscal year         | start and end   |
| **previous.day**             | Yesterday                                          | start and end   |

## Adding new relative date filters

You can add new filters (within certain limits) using the CiviCRM admin interface at `civicrm/admin/options/relative_date_filters` or by using the API.

- Some patterns, especially those with numbers (like “ending_3.day”), are flexible and let you create new filters for different time spans.

- For other patterns, adding new options may require technical changes.

## Special patterns and how they work

### The “ending” prefix

- Filters like **ending_3.day** mean “the last 3 days, including today”.

- The number can be changed to any value you need (for example, **ending_7.day** for the last 7 days).

- These filters count backwards from today.

**Examples:**

- **ending_3.day**: Last 3 days, including today
- **ending_3.week**: Last 3 weeks, including today (same as ending_21.day)
- **ending_3.month**: Last 3 months, including today
- **ending_3.quarter**: Last 3 quarters, including today (same as ending_9.month)
- **ending_3.year**: Last 3 years, including today

### The “this” prefix

- Filters like **this_3.year** cover a set of whole date units, starting from the beginning of the period.

- For example, **this_3.year** covers the last 3 full years, from January 1 of the first year to December 31 of the last year.

**Examples:**

- **this_3.day**: Last 3 days, including today (same as ending_3.day)
- **this_3.week**: From start of two weeks ago to end of this week (3 weeks total)
- **this_3.month**: From start of two months ago to end of this month (3 months total)
- **this_3.quarter**: From start of two quarters ago to end of this quarter (3 quarters total)
- **this_3.year**: From start of two years ago to end of this year (3 years total)
- **this_3.fiscal_year**: From start of two fiscal years ago to end of this fiscal year (3 fiscal years total)

---

<!--
Source: https://docs.civicrm.org/user/en/latest/searching
-and-reporting/relative-date-formats/ -->

<!--
This page is a Reference, as it provides a comprehensive, systematic list of options and their definitions, for users to consult when building searches or reports. It does not teach a process (Tutorial), solve a specific problem (Guide), or explain concepts in depth (Explanation). Basic level is appropriate, as it is meant for all users, especially those learning to use search and reporting features.
 -->
