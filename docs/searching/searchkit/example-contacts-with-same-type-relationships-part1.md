---
categories:
  - Guide
level: Basic
summary: Learn how to find contacts in CiviCRM who have more than one relationship of the same type, for example, families with multiple children.
section: Searching and reporting
---

# Finding contacts with multiple relationships of the same type

## Why use this guide

This guide is for non-profit staff who are new to CiviCRM and want to create useful lists for outreach, such as identifying families with more than one child. You’ll learn how to use Search Kit to build a list based on relationship types, which can help with targeted communications like special offers or event invitations.

## Step 1: Start a new search

Go to **Administer > Search > Search Kit** and click **New Search**.  
Make sure **Contacts** is selected as the main entity to search.  
Choose **With (required)** and select **Contact Related Contacts** to include relationships in your search.  
Click the **+Group By** button and group by both **Contact ID** and **Relationship Type**. This helps organize your results by each contact and the type of relationship they have.

## Step 2: Add relationship details

Below the search criteria, click **+Add** and select **Contact Related Contacts: Relationship**.  
For extra clarity—especially if you’re searching for multiple relationship types—you can also add **Contact Related Contacts: Relationship from contact**. This shows the specific type of relationship for each result.

## Step 3: Count the relationships

In the **Field Transformations** section, choose **Count** as the transformation for the **Relationship** field. This tells CiviCRM to count how many times each relationship type appears for each contact.

## Step 4: Filter for multiple relationships

Under the **Having** section, select **(Count) Contact Related Contact: Relationship** from the dropdown.  
Set the filter to **greater than ( > )** and enter **1** in the value field.  
Click **Search** to see your results.  
Don’t forget to **name and save your search** for future use.

## Tips for success

- **Double-check your relationship types** to make sure you’re counting the right ones.
- **Name your search clearly** so you and your team can find it again.
- **Export your results** to use in mailings or reports.

## Next steps

Now that you have your list, you can use it for mailings, event invitations, or reporting. If you want to learn more about creating searches or using Search Kit, try our beginner tutorials or explore other guides in the Searching and Reporting section.
