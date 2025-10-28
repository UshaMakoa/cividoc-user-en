---
categories:
  - Guide
level: Intermediate
summary: Learn how to use the "Having" feature in CiviCRM's Search Kit to filter displayed search results based on specific conditions.
section: Searching and reporting
---

# Using the "having" feature in search kit

## Introduction to Having

The "Having" feature in CiviCRM's Search Kit allows you to filter the results displayed in a table after they have been retrieved from the database. This is particularly useful for filtering aggregate data or transforming field values. Unlike the "Where" clause, which filters data before it is retrieved, "Having" operates on the results set.

## How to Use Having

1. **Access the Filter Conditions Tab**: You can find both "Where" and "Having" options in the "Filter Conditions" tab on the left side of the Search Kit interface.

2. **Select Fields for Filtering**: With "Having," you can only select fields that are already included in the results set. This means you need to ensure that the fields you want to filter are part of your initial search criteria.

3. **Choose Operators and Comparison Values**: Once you've selected a field, you need to choose an operator (e.g., equals, greater than, matches pattern) and set a comparison value. The operators available are similar to those in SQL.

4. **Tips for Using Operators**:
   - **Matches Pattern**: Use regular expressions to match complex patterns.
   - **Is Like**: Use with wildcards to find parts of a field (e.g., `%searchterm%`).
   - **Contains**: Useful for searching serialized fields (e.g., Contact Subtype).

5. **Handling NULL Fields**: When using negated operators like "Not Like" or "Doesn't Contain," remember that these won't match NULL fields. To include NULL fields, you can search for `!=searchterm` or "Is Empty."

## Example Use Cases

- **Filtering Phone Numbers**: Use regular expressions to filter phone numbers that match a specific format. You can reverse this to find records where the phone number needs correction.
- **Comparing Fields**: Display rows where two fields have the same value, such as the display name and email address.

<!--
Source: https://docs.civicrm.org/some/page/
 -->

<!--
Suggestion: This page could be part of a larger guide on using Search Kit in CiviCRM. Consider adding more examples or scenarios to illustrate the flexibility of the "Having" feature.
 -->
