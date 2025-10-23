---
categories:
  - Uncategorized
  - Tutorial
level: Basic
summary: This tutorial guides non-profit users through the process of setting up and customizing reports in CiviCRM using report templates.
section: Set-up
---

# Setting up reports in CiviCRM

Creating and customizing reports in CiviCRM can help your organization track important information and make informed decisions. This tutorial will walk you through the steps to set up reports using the available templates in CiviCRM.

## Understanding report templates

Report templates are pre-defined formats that you can customize to create specific reports. To access the report templates, go to the **Administer > CiviReport** menu. Here, you will find a list of available templates grouped by component, along with descriptions of their intended use.

## Creating a new report

To create a new report from a template, follow these steps:

1. **Select a report template**: Click on the name of the template you want to use. This will bring up a configuration screen.
2. **Choose your report criteria**: Decide what information you want to display in your report. You will see tabs that allow you to define the following:
   - **Columns**: Select the data to display for each record.
   - **Grouping**: (if applicable) Choose how to summarize data.
   - **Sorting**: (if applicable) Determine the order of records.
   - **Filters**: Specify which records to include in the report.

## Selecting report criteria

When configuring your report, you will have options to set criteria based on the template chosen. Here are some key points:

- **Columns**: At least one display column is required. For example, in a membership detail report, you must include fields like "Contact Name" and "Membership Type."
- **Grouping**: This feature allows you to summarize data. You can compare different types of data, such as donations by year.
- **Sorting**: Useful for organizing detailed reports.
- **Filters**: Filters help you narrow down the records included in your report. For example, you can filter to show members who joined last year.

### Using date range filters

Most reports include a date range filter, which can be set in two ways:

- **Absolute date range**: Specify exact dates, like "1st Jan 2010" to "31st July 2010."
- **Relative date range**: Use options like "This year" or "Last 12 months" for ongoing reports.

Once you have selected your criteria, click **Preview Report** to see how it looks.

## Defining report settings

After previewing your report and ensuring the criteria are correct, you need to save it:

1. **Title and Format**: Give your report a clear title and description.
2. **Email Delivery**: Set up email delivery options if you want the report sent regularly.
3. **Access Control**: Decide who can view or edit the report. You can limit access based on user roles.
4. **Navigation Menu**: Choose if and where the report will appear in the navigation menu.

Once everything is set, click **Create Report**. Your report will now be available in **Reports > All Reports**.

## Editing or copying an existing report

If you need to change an existing report, open it, make your adjustments, and click **Update Report** to save. If you want to create a similar report with different filters, you can click **Save a Copy...** and give it a new title.

## Understanding CiviReport permissions

There are specific permissions related to reports in CiviCRM:

- **Access CiviReport**: View the CiviReport menu.
- **Access Report Criteria**: Change report search criteria.
- **Administer Reserved Reports**: Edit all reserved reports.
- **Administer Reports**: Manage report templates.

By following these steps, you'll be able to set up and customize reports in CiviCRM effectively, helping your non-profit organization make data-driven decisions. If you have further questions or need assistance, feel free to reach out to the CiviCRM community for support.
