---
categories:
  - Guide  
level: Basic  
summary: This guide explains how to use the "Group By" feature in CiviCRM Search Kit to organize and analyze your data by common fields, helping non-expert users better understand patterns and relationships in their data.  
section: Searching and reporting  
---

# Group by

## What is group by?

The **Group By** feature in CiviCRM lets you organize your search results by one or more shared fields. Instead of seeing every record listed individually, results are combined into groups based on the values in the fields you choose.

For example, if you search contacts, you can group results by country or contact type. This means you will see one row per country or contact type, with counts or summaries for each group.

## Why use group by?

Grouping your data helps you analyze patterns and relationships more easily. You can:

- Count how many contacts are in each country  
- Total contributions by payment method  
- Average donation amounts by membership type  

This makes it easier to understand your data and make informed decisions.

## How to use group by

1. **Start a search** in CiviCRM Search Kit for the entity you want to analyze (e.g., Contacts, Contributions).  
2. **Select one or more fields** to group by. For example, choose "Country" or "Contribution Date."  
3. Click **Search**. Your results will show one row for each unique value in the group by fields.  
4. You can **drag columns** left or right to reorder them. If you change the order, click **Search** again to update the display.  

If you select multiple group by fields, results will show one row for each combination of those fields. For example, grouping by Country and State will show rows for each state within each country.

## Tips for effective grouping

- Use grouping to summarize large datasets and spot trends.  
- Combine grouping with filters to focus on specific data subsets.  
- Remember that grouping works best with fields that have meaningful categories or values.  

## Example use case

If you want to see how many contacts live in each country, group your contact search results by the "Country" field. The results will show one row per country with the count of contacts in that country.

If you add "State/Province" as a second group by field, you will see rows for each state within each country, helping you drill down further.

## Summary

The **Group By** feature is a simple but powerful way to organize your data by common elements, making it easier to analyze and understand your contacts, contributions, events, and more.
