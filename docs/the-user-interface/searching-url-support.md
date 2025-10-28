---
categories:
  - Reference
level: Intermediate
summary: Learn how to use URL parameters to filter and bookmark advanced and component searches in CiviCRM.
section: Searching and reporting
---

# Search URL filtering

## Overview

You can filter CiviCRM searches by adding parameters to the URL, allowing you to quickly revisit specific search results by bookmarking these URLs. This feature is available for **advanced search** and **component searches** (such as "Find Contributions") starting from version 5.21.

## How to construct a search URL

To create a URL that filters search results:

- Start with the base search URL for the area you want (for example, contributions, events, or cases).

- Add `reset=1&force=1` after the question mark (`?`) in the URL.

- Add any supported parameters for the fields you want to filter by.

For example, to find contributions by someone named Bob, from the source "dad", made on or before January 1, 2018:
```
civicrm/contribute/search?reset=1&force=1&sort_name=bob&receive_date_high=20180101&contribution_source=dad
```

## Supported parameters for filtering

Below are some commonly used parameters for contribution, event, participant, and case searches:

| Field                               | Example                                  | Description                                                                                 |
|
--------------------------------------|------------------------------------------|---------------------------------------------------------------------------------------------|
| sort_name                           | sort_name=bob                            | Contact's sort name contains "bob" (matching depends on your site settings)                 |
| contribution_source                  | contribution_source=dad                  | Contribution source contains "dad"                                                          |
| cancel_reason                        | cancel_reason=dunno                      | Cancel reason contains "dunno"                                                              |
| invoice_number                       | invoice_number=xyz                       | Invoice number contains "xyz"                                                               |
| contribution_page_id                 | contribution_page_id=1                   | Contribution page ID equals 1                                                               |
| receive_date_high                    | receive_date_high=20180101132323         | Received on or before 1 Jan 2018, 1:23 pm                                                   |
| receive_date_low                     | receive_date_low=20161001                | Received on or after 1 Oct 2016                                                             |
| receive_date_relative                | receive_date_relative=this.year          | Received this year                                                                          |
| event_high                           | event_high=20190101000000                | Event end date on or before 1 Jan 2019                                                      |
| event_low                            | event_low=20190101000000                 | Event start date on or after 1 Jan 2019                                                     |
| event_relative                       | event_relative=this.year                 | Event within this year                                                                      |
| participant_registration_date_high   | participant_registration_date_high=...   | Participant registered on or before a certain date                                           |
| participant_status_id                | participant_status_id=1,2                | Participant status is Registered or Pending Pay Later                                       |
| case_start_date_high                 | case_start_date_high=20190101000000      | Case start date on or before 1 Jan 2019                                                     |
| case_type_id                         | case_type_id=1,2                         | Case type is one of the listed types                                                        |
| case_status_id                       | case_status_id=1                         | Case status is Opened                                                                       |
| case_subject                         | case_subject=test                        | Case subject contains "test"                                                                |
| case_deleted                         | case_deleted=1                           | Case is deleted                                                                             |
| case_owner                           | case_owner=2                             | Only cases owned by the specified user                                                      |
| case_tags                            | case_tags=1,2                            | Case has one of the specified tags                                                          |

## Notes on text and date fields

- **Text fields**: Whether the search looks for matches at the beginning or anywhere in the field depends on your site's "Automatic Wildcard" setting (found under *Administer CiviCRM → Customize Data and Screens → Search Preferences*). If wildcards are off, searching "dad" will match "daddy" but not "grandad".
- **Date/time fields**: Dates must be in the format `YYYYMMDD` (e.g., 20180101), or with time as `YYYYMMDDHHMMSS` (e.g., 20180101132323). If you leave out the time, it defaults to midnight.
- **Relative date fields**: Some fields accept values like `this.year` to filter by the current year.

## When to use search URL filtering

- Bookmark frequently used searches for quick access.

- Share filtered search results with colleagues by sending them the URL.

<!--
Source: https://docs.civicrm.org/user/en/latest/searching
-and-reporting/search-url-filtering/ -->

<!--
This page is best classified as Reference, as it systematically lists supported URL parameters and their usage, with no procedural steps or conceptual background. The intended audience needs to look up valid options and formats, not learn a process or underlying concept. Level is Intermediate, as some familiarity with URLs and CiviCRM search is helpful. If a step
-by-step example were added, that could be a Tutorial or Guide, but the current content is strictly Reference. -->
