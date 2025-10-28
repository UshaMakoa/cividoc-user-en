---
categories:
  - Guide
level: Basic
summary: Learn how to view, create, and export membership reports in CiviCRM to understand and manage your organisation’s members.
section: Membership > Reporting
---

# Membership reports

## Viewing membership reports

CiviCRM provides several ready-made reports to help you understand your organisation’s memberships. These reports give you quick summaries and detailed information about your members, such as how many have joined each month, which memberships have lapsed, and more.

- **Membership summary report**: Shows totals and trends for your members, grouped by time periods you choose (like month, quarter, or year). This helps you see how your membership is growing or changing over time.
- **Membership detail report**: Gives detailed information for each member, based on the criteria you select. You can access this by clicking on a highlighted field in the summary report.
- **Lapsed memberships report**: Lists memberships that have ended or will end before a date you choose, so you can follow up with those members.
- **Contribution and membership details report**: Shows details about contributions and how they relate to memberships, based on your selected criteria.

You can find these reports under the Reports section in CiviCRM.

## Creating new membership reports

If the standard reports don’t meet your needs, you can create your own custom membership reports:

1. Go to **Reports > Membership Reports**.

2. Click the **New Member Report** button.

3. On the Create New Report Template screen, choose a membership report template.

4. Enter your criteria (for example, select specific membership types or date ranges).

5. Click **Preview Report** to see what your report will look like.

6. If you’re happy with it, click **Create Report**, then give your report a name and save it for future use.

This allows you to quickly return to your custom reports whenever you need them.

## Exporting membership records

You might want to export membership records to do further analysis, create mail merges, or use the data outside of CiviCRM. Here’s how:

1. Go to **Memberships > Find Members** and enter your search criteria.

2. On the search results screen, select the records you want to export.

3. In the **-actions-** dropdown, select **Export Members**.

4. Choose either **Export PRIMARY fields** (a default set of fields) or **Select fields for export** (choose the fields you want).

5. Click **Continue**.

- If you choose Export PRIMARY fields, a file called `CiviCRM_Member_Search.csv` will be created with your selected records.

- If you choose Select fields for export, select your fields, optionally save the field mapping for future use, and click **Export**. The same type of CSV file will be created.

You can now use this exported file for analysis or other tasks outside CiviCRM.

<!--
Source: https://docs.civicrm.org/user/en/latest/membership/membership
-reports/ -->

<!--
Suggestion: This page is a Guide, as it provides step
-by-step instructions for specific tasks (viewing, creating, and exporting membership reports) rather than general background, exhaustive reference, or a hands-on tutorial. The level is Basic, as it assumes no advanced knowledge and is suitable for new users. If the page included more conceptual background (e.g., why reporting is important) or exhaustive lists of all report fields, those would belong in Explanation or Reference sections, respectively. -->
