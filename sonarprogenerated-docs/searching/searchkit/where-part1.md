---
categories: Guide
level: Basic
summary: Learn how to use the "Where" clause in CiviCRM to filter data effectively, making it easier to manage and analyze your contacts and other data.
section: Searching and reporting
---

# Using the "where" clause in civicrm

The "Where" clause in CiviCRM is a powerful tool used to filter data from your database before it is returned to SearchKit. This helps you narrow down your search results to only the most relevant information. Here's how you can use it effectively:

## Components of the "where" clause

1. **Element**: This is the field you want to compare. For example, it could be a contact's email address or their primary address.
2. **Operator**: These are similar to arithmetic or SQL operators. Common operators include "Is Like," "Contains," and "Matches Pattern."
3. **Value or Field**: This is what you compare the element against. It can be a specific value or another field.
4. **Comparison Type**: You can compare against a value or a field.

## Tips for using operators

- **Matches Pattern**: Use this to match a regular expression pattern.
- **Is Like**: This matches a complete field. Use it with wildcards (e.g., `%search term%`) to find parts of a field.
- **Contains**: Useful for searching in serialized fields, but it only matches full values.
- **Negated Operators**: Be careful with operators like "Not Like" or "Doesn't Contain," as they won't match NULL fields. To include NULL fields, use a combination like `!= searchterm OR Is Empty`.

## Examples

### Example 1: Filtering Contacts by Email

To find all contacts whose email address contains `.gov`, you can use the "Contains" operator with the value `.gov`.

### Example 2: Comparing Primary and Billing Addresses

To find contacts whose primary address is not the same as their billing address, use the "!=" operator.

# comment: Source: https://docs.civicrm.org/some/page/
# comment: Suggestion: Consider breaking this into a tutorial if it's intended for first-time users, focusing on step-by-step instructions for using the "Where" clause. 

---