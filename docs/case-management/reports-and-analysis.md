---
categories:
  - Guide
level: Basic
summary: Learn how your organisation can use CiviCRM to generate, print, and analyse case reports, search for cases, and create custom documents for case management.
section: Case management > Reports and analysis
---

# Reports and analysis

## Overview

You can use CiviCRM to report on and analyse your organisation’s casework in several ways. The case dashboard offers a quick summary of all your current cases, showing totals for each case type and status. Clicking on any number in the dashboard takes you to a list of cases matching that type and status (numbers showing zero are not clickable).

For more detailed or customised views, you can use CiviCRM’s search features and reporting tools. These options help both administrators and caseworkers track activities and outcomes.

## Running a QA audit or redacted report

To run a QA Audit or Redact report for a case:

- Go to the contact’s case management screen.

- Use the QA Audit / Redact option, which is similar to the Print Report but focuses only on activities defined in a selected timeline.

- You can choose to include all activities or exclude those marked as 'Completed'.

- If you select the option to redact client and service provider data, the report will show randomly assigned numbers instead of names. The same contact will use the same number throughout the report for consistency.

## Case reports

CiviCRM provides four main report templates for case management:

- **Case summary report**: Gives an overview of cases.
- **Case time spent report**: Shows time spent on each case.
- **Contact demographics report**: Details demographic information for contacts involved in cases.
- **Case detail report**: Offers a detailed view of individual cases.

Because cases are made up of activities, the **activity report template** is also useful. It can provide a dashboard widget (dashlet) for each user, showing all activities assigned to them. Since these activities include both case and non-case items, consider using a naming protocol to help identify case-related activities.

## Printing case reports

To print a report listing all case and activity data:

- Find the case using the Case Dashboard, the Find Cases search form, or the contact’s Cases tab.

- Click **Print Case Report** in the Case Summary section.

Your installation may have additional reports for audit or quality assurance. These will appear in the "Run QA Audit/Redact" dropdown menu.

## Searching for cases

- Use the **Find Cases** search to look up cases by type, status, client name, or email. This is helpful for quickly locating specific cases, especially if your dashboard is crowded.

- The **Advanced search** combines these options with other criteria, such as location or custom fields, allowing more refined searches.

- The **Activity Search** (found under Search > Custom Searches > Activity Search) focuses only on activities, not contacts.

## Printing and merging documents

You can create letters or documents using case tokens:

- On the case management screen, select "Export Document" next to "Print Report" to export as PDF, DOCx, ODT, or HTML.

- To print or merge documents for multiple cases, use the Find Cases search, select the cases, and choose "Print/merge Document." This creates a document for each case, combined into a single PDF.

- If exporting to DOCx, turn off spelling and grammar check for best results.

## Further analysis

If the built
-in dashboards, reports, and searches do not meet your needs, you can commission a new report or custom search for your organisation. For more details, see the sections on reporting and searching in CiviCRM.

<!--
Source: https://docs.civicrm.org/some/page/
 -->

<!--
Suggestion: This page is a Guide, as it provides step
-by-step instructions and specific actions for users to perform common reporting and analysis tasks in case management. The content is practical, problem-oriented, and does not focus on background or exhaustive technical reference, nor does it teach through a first-time tutorial. Level is Basic, as it is suitable for non-expert users learning to perform tasks. If needed, the "Further analysis" section could be split into an Explanation page about custom reporting options. -->
