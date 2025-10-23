---
categories:
  - Uncategorized
  - Guide
level: Basic
summary: This guide explains how to use the With (Optional), With (Required), and Without options when creating searches in CiviCRM.
section: Searching and Reporting
---

# creating searches with optional, required, or without entities

## Introduction

When creating a new search in CiviCRM, you often need to include additional entities to get the data you want. You can choose to include these entities in three ways: With (Optional), With (Required), or Without. Each option affects how the search results are returned.

## Understanding the Options

- **With (Optional):** This option treats the new entity as optional. Even if there is no match, the rows from the earlier entity will still be returned in the results. For example, if you search for Contacts With (optional) Contact Addresses, you will get a row for a Contact even if they have no addresses.

- **With (Required):** This option only returns rows if there is a match between the earlier entity and the new entity. For instance, Contacts With (required) Contact Addresses will not return any rows for Contacts without addresses.

- **Without:** This option returns rows only if there is no match between the earlier entity and the new entity. For example, Contacts Without Contact Addresses will return a row for each Contact that has no Contact Address.

## Applying the Options

When you add an entity to your search, you are essentially joining it to the existing entities. Your choice of With (Optional), With (Required), or Without determines whether rows are added or removed from your search results.

### Example Use Cases

- **Filtering Contacts:** You might want to find all Contacts who have bought tickets for an event. You could start with the Contacts entity and join it With (required) to the Event Participation entity to ensure only Contacts with event participation are returned.

- **Finding Contacts Without Addresses:** If you want to identify Contacts who do not have any addresses, you can use the Without option to exclude any Contacts with addresses.
