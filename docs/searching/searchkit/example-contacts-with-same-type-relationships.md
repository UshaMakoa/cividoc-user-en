---
categories:
  - Guide
level: Intermediate
summary: Learn how to create a list of contacts who share the same relationship type in CiviCRM using Search Kit, ideal for non-profit staff wanting to identify families or groups with multiple connections.
section: Searching and reporting > Search Kit > Examples
---

# Listing contacts who have relationships of the same type

## Introduction

Sometimes your organisation may need a list of contacts who have more than one of the same relationship type. For example, a summer camp might want to find families with multiple children, so you can reach out to them about special offers or events.

This guide will show you how to use CiviCRM's Search Kit to create such a list.

## Steps to create your search

### Step 1: Start a new search

- Go to **Administer > Search > Search Kit** in your CiviCRM dashboard.

- Click **New Search**.

- Make sure **Contacts** is selected as the main entity you want to search for.

### Step 2: Set up relationship criteria

- Click **With (required)** and choose **Contact Related Contacts** as a new entity.

- Click the **+Group By** button.

- Group by both **Contact ID** and **Relationship Type**. This lets you see contacts grouped by their relationships.

### Step 3: Add relationship columns

- Under the criteria section, click the **+Add** button.

- Select **Contact Related Contacts: Relationship**.

- Optionally, add **Contact Related Contacts: Relationship from contact** to show the relationship type for each contact. This helps if you have several types of relationships.

### Step 4: Transform the relationship column

- Find the **Field Transformations** section below the **Having** dropdown.

- Set the transformation for **Relationship** to **Count**. This counts how many relationships each contact has.

### Step 5: Filter for contacts with multiple relationships

- In the **Having** section, select **(Count) Contact Related Contact: Relationship** from the dropdown.

- Choose the **greater than (>)** symbol and enter **1** in the field next to it. This will show contacts with more than one relationship of the same type.

### Step 6: Run and save your search

- Click **Search** to view your results.

- Name and save your search so you can use it again later.

## Tips

- You can turn your search results into a mailing list or export them for further use.

- If you want to focus on a specific relationship type (like parent
-child), adjust your criteria accordingly.

<!--
This page is a Guide because it helps users achieve a specific goal (listing contacts with the same relationship type) using step
-by-step actions, but does not teach general concepts or provide exhaustive reference information[3][4]. -->

<!--
The level is Intermediate, as it requires some familiarity with Search Kit and relationships in CiviCRM.
 -->

<!--
If the page included more background on relationships or a reference list of all relationship types, those parts could be split into Explanation or Reference pages for clarity.
 -->
