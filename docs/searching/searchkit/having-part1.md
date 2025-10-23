---
categories:
  - Guide
level: Intermediate
summary: Learn how to use the "Having" filter in CiviCRM Search Kit to refine your search results by filtering on aggregated or transformed data.
section: Searching and reporting / Search Kit
---

# Using the Having Filter in CiviCRM Search Kit

## What the Having Filter Does

The **Having** filter lets you narrow down your search results after the data has been gathered, focusing on the information you actually see in your results table. This is different from the **Where** filter, which limits the data before it’s displayed. With **Having**, you can filter based on calculations, summaries, or transformed fields—things like totals, averages, or formatted values that aren’t in your original database[1].

## When to Use Having

Use **Having** when you want to filter results based on values that only exist after your search runs—for example, if you’re showing a count of donations per contact and you only want to see contacts with more than five donations. **Having** works on the fields you’ve chosen to display in your results, not on every field in your database.

## How to Apply a Having Filter

1. **Build your search**: Start by selecting your main entity (like Contacts or Contributions) and add any related entities using **With** or **Without**.
2. **Go to the Filter Conditions tab**: Here you’ll find both **Where** and **Having** options.
3. **Select a field to filter**: In **Having**, you can only choose from fields that are included in your results table.
4. **Choose an operator**: Pick how you want to compare the field—for example, “equals,” “greater than,” “contains,” or “matches pattern.”
5. **Enter your comparison value**: Type in the value you want to filter by. You can also compare one field to another field in your results.

## Tips for Effective Filtering

- **Pattern matching**: Use “Matches Pattern” for advanced filtering with regular expressions. For simpler searches, “Is Like” with wildcards (like `%search%`) works well.
- **Contains**: This is helpful for fields that store multiple values together (like Contact Subtype).
- **Negated operators**: “Not Like,” “≠,” and “Doesn’t Contain” won’t match empty (NULL) fields. To include empty fields, add a separate condition for “Is Empty.”
- **Field comparisons**: You can compare two fields in your results, for example, to find rows where the display name and email are the same.

## Example: Filtering Phone Numbers

Suppose you want to find contacts with phone numbers in a specific format. You can use a regular expression in the **Having** filter to show only those records. To find records that don’t match (perhaps to clean up your data), simply reverse the condition.

## Regular Expressions and Wildcards

While wildcards (`%` or `*`) are handy for basic searches, regular expressions offer more flexibility for complex patterns. There are many online resources to help you learn regular expressions if you’re new to them.

## Next Steps

Once you’re comfortable with **Having**, explore **Field Transformations** to further customize how your data appears. If you need to filter data before it’s displayed, use the **Where** filter instead.
