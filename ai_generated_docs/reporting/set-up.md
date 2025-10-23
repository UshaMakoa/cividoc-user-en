# Source: https://docs.civicrm.org/user/en/latest/reporting/set-up/

---
categories: Guide  
level: Basic  
summary: This guide explains how to create, customize, and manage reports in CiviCRM using the built-in report templates, helping non-profit users generate useful data insights without needing expert knowledge.  
section: Reporting / Set-up  
---

# Set up CiviReports

## Introduction

This guide will help you create and manage reports in CiviCRM using the report templates provided. You will learn how to select the data you want to see, customize your reports, and make them available to your users. This guide assumes you have a basic idea of why reports are useful and that the report you need can be made with the existing templates.

If you need a report that is not available as a template, you might need help from a developer to create a custom report.

## Report templates

Report templates are pre-made report formats grouped by CiviCRM components (like contributions, memberships, or events). You start by choosing a template that fits your needs. You can find these templates under **Administer > CiviReport** in the menu.

If reports already exist from a template, you can view or edit them. To create a new report, click on the template name to start configuring it.

## Selecting report criteria

When creating a report, you will set what information it shows by choosing options on tabs. The tabs you see depend on the template but usually include:

- **Columns**: Choose which data fields to display in the report. Some fields are required and cannot be removed.
- **Grouping**: (Optional) Summarize data by categories, like donations per year. You can use more than one grouping, but some combinations may not work together.
- **Sorting**: (Optional) Arrange the order of the report rows.
- **Filters**: Select which records to include, such as members who joined in a specific date range.

### Using the date range filter

Most reports let you filter records by date. You can choose:

- An absolute date range (e.g., January 1 to July 31, 2023)
- A relative date range (e.g., last 12 months, previous year)

Relative date ranges are helpful for reports you run regularly because they update automatically.

After setting your criteria, click **Preview Report** to see the results. You can adjust the settings if needed.

## Defining report settings

Once you are happy with the data shown, you need to save the report so it can be used again.

- On the **Title and Format** tab, give your report a clear name and description, like "Members joined this year."
- You can customize the report header and footer using simple HTML, including adding your logo.
- The **Email Delivery** tab lets you schedule the report to be emailed regularly to yourself or others. To use this, make sure the scheduled job for sending reports is enabled.
- On the **Access** tab, decide if the report should appear in the menu and who can see or edit it. You can restrict access based on user permissions or roles to keep sensitive data secure.
- You can also allow users to add the report to their personal dashboard if they have permission.

When everything is set, click **Create Report**. Your report will now be listed under **Reports > All Reports** and in any menu location you chose.

## Editing or copying reports

To change an existing report, open it, make your changes, and click **Update Report**.

If you want similar reports with different filters (for example, one for all events and another only for fundraising events), you can open a report, change the filters, and click **Save a Copy**. Give the new report a different title and description.

## CiviReport permissions

There are four key permissions related to reports:

- **Access CiviReport**: View the report menu and reports you have permission for.
- **Access Report Criteria**: Change the search filters in reports.
- **Administer Reserved Reports**: Edit reports marked as reserved (usually for admins).
- **Administer Reports**: Manage report templates and settings.

Setting these permissions helps control who can see and modify reports in your organization.

---

This guide helps you get started with CiviReports by using the built-in templates to create useful reports tailored to your non-profit’s needs. As you become more comfortable, you can explore more advanced options or custom reports with developer help.