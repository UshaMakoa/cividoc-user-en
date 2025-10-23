---
categories:
  - Uncategorized
  - Tutorial
level: Basic
summary: This tutorial explains how to use URL filtering in CiviCRM searches to efficiently bookmark and access specific search results.
section: Searching and reporting
---

# Search URL filtering in CiviCRM

In this tutorial, you will learn how to use URL filtering in CiviCRM to bookmark searches with specific parameters. This feature allows you to quickly access your most commonly used searches without having to set them up each time.

## Understanding search URL filtering

CiviCRM allows you to create parameterized URLs for advanced searches and component searches (like finding contributions). By using these URLs, you can save time and streamline your workflow.

To create a parameterized URL, follow these steps:

1. **Start with a base URL**: Ensure your URL contains `reset=1&force=1` after the question mark. This resets the search and forces the parameters to take effect.
  
2. **Add your search parameters**: Include additional supported parameters to refine your search results.

## Date and time parameters

When using date and time parameters, you can either omit the time component or specify it in full. Here’s how to format your date/time parameters:

- **Omitting time**: Use an 8-digit format like `YYYYMMDD` (e.g., `20200101`).
- **Including time**: Use a 14-digit format like `YYYYMMDDHHMMSS` (e.g., `20200101235959`).

### Example URL

Here’s an example of a URL that finds contributions made by a person named Bob, with a contribution source of "dad," made on or before January 1, 2018:

```
civicrm/contribute/search?reset=1&force=1&sort_name=bob&receive_date_high=20180101&contribution_source=dad
```

## Supported parameters for contribution searches

You can use various parameters to filter your searches. Here are some common ones:

| Field                       | Example                      | Comments                                      |
|
