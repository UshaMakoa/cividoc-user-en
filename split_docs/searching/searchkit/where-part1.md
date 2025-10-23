# Source: https://docs.civicrm.org/user/en/latest/searching/searchkit/where/

---
categories: Guide  
level: Basic  
summary: This page explains how to use the "Where" filter in CiviCRM Search Kit to narrow down search results by setting conditions on data fields before the search runs.  
section: Searching and reporting  
---

# Where filter in Search Kit

## What is the "Where" filter?

The "Where" filter helps you **narrow down your search results** by telling CiviCRM which contacts or records to include based on specific conditions. It works by filtering data inside the database before the results are shown to you.

## Main parts of a "Where" filter

When you create a "Where" filter, you need to set four things:

- **Element**: The field or data you want to check (for example, Email or Address).  
- **Operator**: How you want to compare the data (for example, equals, contains, or not equals).  
- **Value or field**: The value or another field to compare against (for example, the text ".gov" or another address).  
- **Comparison type**: Whether you are comparing the element with a fixed value or with another field.

## Common operators and tips

- **Matches Pattern**: Use this to match a pattern using regular expressions (advanced users).  
- **Is Like**: Checks if the whole field matches, often used with wildcards like `%search term%` to find parts of a field.  
- **Contains**: Useful for fields that store multiple values together, like Contact Subtype. It matches whole values only (e.g., "Parent" but not part of a word).  
- **Negated operators** (e.g., Not Like, ≠, Doesn't Contain) do *not* match empty fields (NULL). To include empty fields, combine conditions like “≠ searchterm OR Is Empty”.

## Examples

- To find contacts whose **email contains ".gov"**, set:  
  - Element: Email  
  - Operator: Contains  
  - Value: `.gov`

- To find contacts whose **primary address is different from their billing address**, set a condition comparing the two address fields with a "not equal" operator.

## When to use "Where" vs. "Having"

- Use **Where** to filter data *before* it is returned from the database (most common).  
- Use **Having** to filter *after* the data is returned, usually for filtering aggregated or grouped data.

## Summary

The "Where" filter is a powerful way to limit your search results in CiviCRM by setting clear conditions on your data fields. It helps you find exactly the contacts or records you need by filtering data early in the search process.