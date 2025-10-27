---
categories: Reference
level: Intermediate
summary: This page provides a systematic overview of field transformations in CiviCRM, explaining how to apply formulas to fields in search results for tasks like displaying alternative fields or performing calculations.
section: Searching and reporting
---

# Field transformations

Field transformations in CiviCRM allow you to modify the data displayed in search results by applying formulas or functions to fields. These transformations can be used to handle missing values, perform mathematical operations, or aggregate data.

## Types of transformations

Field transformations are categorized into four types:

- **Comparison**: These transformations allow you to compare values between fields.
- **Text**: Useful for manipulating text fields, such as concatenating strings or extracting substrings.
- **Math**: Enables mathematical operations like rounding numbers or summing values.
- **Aggregate**: Available when using the "Group By" feature, these transformations help with tasks like counting occurrences or summing values across groups.

## Using transformations

To use field transformations, you need to apply them to your search results. For example, you might use a transformation to display a different field if a value is missing or to round a numeric value to the nearest whole number.

## Additional resources

For more detailed information on the available transformation functions, you can refer to the MySQL documentation, which provides a comprehensive list of built-in functions and aggregate functions.

# comment: Source: https://docs.civicrm.org/some/page/
# comment: Suggestion: This page could benefit from a companion tutorial or guide that provides step-by-step instructions on how to apply these transformations in real-world scenarios.