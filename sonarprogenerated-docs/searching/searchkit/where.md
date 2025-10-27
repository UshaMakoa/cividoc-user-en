---
categories: Reference
level: Basic
summary: Learn how to use the "Where" filter in CiviCRM SearchKit to select and narrow down your data based on specific conditions.
section: Search Kit
---

# Where filter

## What is the Where filter?

The **Where filter** in SearchKit lets you choose which records to include in your search results by setting specific conditions. It filters data directly in the database before showing results in SearchKit. If you want to filter results after they are loaded, use the "Having" filter instead.

## How does the Where filter work?

The Where filter has four main parts:

- **Element to compare:** The field or data you want to filter (for example, "Email" or "Contact Type").
- **Operator:** The rule for comparison, such as equals, not equals, contains, or matches pattern.
- **Value (or field) to compare against:** The specific value or another field you want to use for comparison.
- **Type of comparison:** Whether you are comparing to a value you enter or to another field.

## Tips for using operators

- **Matches Pattern:** Use this to match a regular expression pattern.
- **Is Like:** Matches the whole field. Use wildcards (like `%search term%`) to find part of a value.
- **Contains:** Useful for fields with multiple values (like Contact Subtype). It matches only a full value (e.g., "Parent"), not part of it.
- **Negated operators (Not Like, ≠, Doesn't Contain):** These do not match fields that are empty (NULL). They only match records where the field has a value that does not meet your condition. If you want to include empty fields too, combine "≠ searchterm" with "Is Empty" using OR.

## Examples

- To find contacts whose email address contains ".gov", set:
  - Element: Email
  - Operator: Contains
  - Value: .gov

- To find contacts whose primary address is not the same as their billing address, set:
  - Element: Primary Address
  - Operator: ≠
  - Value: Billing Address

# comment: Source: https://docs.civicrm.org/user/en/latest/searching-and-reporting/search-kit/where/
# comment: This page is best classified as Reference because it systematically describes the parts and usage of the "Where" filter, lists options, and provides factual details for users to look up while working. It is not a step-by-step tutorial or a problem-oriented guide, nor does it explain the background or architecture. Level is Basic, as it introduces core concepts for everyday users.