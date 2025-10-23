---
categories:
  - Tutorial  
level: Basic  
summary: This page introduces SearchKit, a tool in CiviCRM that helps users build custom searches and display results, guiding non-expert non-profit users through its basic concepts and usage.  
section: Searching and reporting  
---

# Introduction to SearchKit

## What is SearchKit?

SearchKit is a tool in CiviCRM that lets you create custom searches and decide how to show the results. It is powerful and flexible but can be a bit complex for beginners. It is mainly designed for site builders and advanced users, but with some learning, non-experts can use it to find exactly the information they need in CiviCRM.

## Who can use SearchKit?

While SearchKit is designed for experienced users, you can also use searches created by others, such as your site administrator or power users. These searches can be made available through menus or dashboards for easier access.

## Getting started with SearchKit

To open SearchKit, go to the menu and select **Search > SearchKit**. If you do not see it, your site administrator may need to enable the SearchKit extension in **Administer > System Settings > Extensions**.

## Key concepts

### Entities

An *entity* is a type of data you want to search for, such as Contacts or Contributions. When you start a search, you pick the entity you want to work with.

### Fields

You choose which pieces of information (fields) about the entity to show in your search results. You can add or remove fields easily.

### Filters (Where)

Filters let you narrow down your search results by setting conditions. For example, you can look for contacts in a specific city or contributions above a certain amount.

### Joins (With/Without)

Sometimes you want to include related information, like addresses linked to contacts. SearchKit lets you join entities using options:

- **With (required):** Only show results that have the related information.
- **With (optional):** Show all results, adding related information if it exists.
- **Without:** Show only results that do not have the related information.

### Group By

If your search returns multiple rows for one item (for example, one contact with several addresses), you can use *Group By* to combine these rows into one per item.

### Special handling of addresses, emails, and phones

CiviCRM treats primary addresses, emails, and phones specially so you can include them easily without extra joins. But if you join address data, be careful to choose the correct fields to avoid confusion.

## Permissions

SearchKit respects user permissions in CiviCRM and your website’s user roles. You can toggle whether to enforce these permissions or bypass them, but be cautious when bypassing to avoid exposing sensitive data.

## Forms and filters

SearchKit also includes *FormBuilder* to create forms for searching or data entry, with permissions controlling who can use each form.

## How SearchKit compares to other searches in CiviCRM

SearchKit replaces the older Search Builder and is more powerful than Advanced Search. However, many users still find Advanced Search or Quick Search easier for simple tasks.

## Learning more

There are many example searches and recipes in the full documentation to help you practice and build your skills with SearchKit.
