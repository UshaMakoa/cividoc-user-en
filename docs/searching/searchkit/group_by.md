---
categories:
  - Reference
level: Basic
summary: Learn how to use the "Group By" feature in CiviCRM Search Kit to organize and analyze your data by common fields.
section: Searching and reporting > Search Kit
---

# Group By

## What is "Group By"?

The **Group By** feature in CiviCRM’s Search Kit helps you organize your search results by one or more fields that your records have in common. When you use Group By, your results appear with one row for each unique value (or combination of values) in the fields you select.

For example:

- If you search for contacts and group by **Country**, you’ll see one row for each country, showing how many contacts are in each.

- If you search for contributions and group by **Payment Method**, you’ll see one row for each payment method, showing totals for each.

## Why use "Group By"?

Group By is useful for analyzing patterns in your data, such as:

- Counting how many records fall into each category (like contacts per country).

- Summing or averaging numbers (like total donations per payment method).

- Viewing related data together for easier comparison.

## How to use "Group By"

- Choose the field(s) you want to group by in your search setup.

- Run your search. The results will show one row for each unique value or combination you selected.

- If you group by more than one field (for example, **Country** and **State/Province**), you’ll see one row for each combination (like each state within each country).

## Adjusting your results

- You can drag columns left or right to change their order in the results table.

- If you change the column order, click **Search** again to refresh your results with the new layout.

<!--
Source: https://docs.civicrm.org/user/en/latest/searching/search
-kit/group-by/ -->

<!--
Suggestion: This page is systematic, factual, and describes how a feature works, matching the Diátaxis "Reference" type. It is not a step
-by-step tutorial or a problem-oriented guide, nor does it provide background explanation. The content is basic because it introduces a key feature in plain terms for new users. If more step-by-step instructions were needed (e.g., "How to create a grouped report"), that would be a Guide or Tutorial. -->
