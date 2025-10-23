# Source: https://docs.civicrm.org/user/en/latest/searching/searchkit/field_transformations/

### Field Transformations in CiviCRM

To re-write the "Field Transformations" page using the Diátaxis framework for an audience of non-profit users of CiviCRM who are not experts, you can structure it as follows:

---
categories: Guide
level: Basic
summary: Learn how to apply field transformations in CiviCRM to modify and enhance your search results.
section: Searching and Reporting
---

# field transformations in civicrm

## what are field transformations?
Field transformations are formulas you apply to fields in your result set. They help you display alternative fields when values are missing, round numeric values, count occurrences, sum values, and more.

## types of transformations
Field transformations are organized into four categories:
- **Comparison**: Used for comparing values.
- **Text**: For manipulating text fields.
- **Math**: For performing mathematical operations.
- **Aggregate**: Available when using Group By, for aggregating data.

## how to use transformations
To apply transformations, follow these steps:
1. **Select Transformation Type**: Choose from comparison, text, math, or aggregate transformations.
2. **Apply the Formula**: Use the appropriate formula to modify your field.
3. **Review Results**: Ensure the transformation achieves the desired outcome.

## examples
- **Example 1: Displaying Alternative Fields**: Use a transformation to show a different field if a value is missing.
- **Example 2: Rounding Numeric Values**: Apply a math transformation to round numbers to the nearest whole number.

### additional resources
For more detailed information on available transformations, refer to the MySQL documentation:
- [MySQL Built-in Functions](https://dev.mysql.com/doc/refman/8.0/en/built-in-function-reference.html)
- [MySQL Aggregate Functions](https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html)

---

If the content becomes too complex or extensive, consider splitting it into multiple pages, each focusing on a specific type of transformation or use case.

### Suggested Split:
If necessary, you can split the content into separate pages for each transformation type (e.g., Comparison, Text, Math, Aggregate) or create a page for advanced transformations and another for basic ones.