---
categories:
  - Guide
level: Basic
summary: Learn how to create, manage, and understand relationships between contacts in CiviCRM, including individuals, organizations, and households.
section: Organising your data
---

# Relationships in CiviCRM

## What are relationships?

Relationships in CiviCRM let you track how contacts—such as people, organizations, or households—are connected. For example, you can record that a mother and son are related, or that an individual works for an organization. These connections help you understand your community and manage communications more effectively.

## Creating relationships between contacts

To create a relationship:

- Open the contact record for one of the people or organizations you want to connect.
- Click **Add Relationship** from the **Actions** menu or the **Relationships** tab.
- Choose the **Relationship Type** (for example, “Sibling of” or “Employee of”).
- Start typing the name of the related contact. If they’re not in your database yet, you can add them now.
- Optionally, add a **Start Date**, **End Date**, **Description**, **Notes**, or set **Permissions** to control who can see or edit this relationship.
- Click **Save Relationship** when you’re done.

This process works for any type of contact—individuals, organizations, or households.

## Relationship permissions

When you set permissions on a relationship, you control what information each contact can see or edit about the other. For example, if User 1 has “View” permission for User 2, they can see User 2’s details in certain views. “View and Update” permission lets them edit those details, too. These settings help protect privacy while allowing necessary collaboration.

## Connecting employees and employers

A quick way to connect an individual to their employer (an organization) is to use the **Current Employer** field on the individual’s contact record. As you type the organization’s name, CiviCRM suggests matches. If the organization isn’t in your database, it will be created automatically, and the correct “Employee of” and “Employer of” relationships will be set up.

## Other ways to connect employees and employers

You can also connect employees and employers using the **Current Employer** field on profiles and contribution pages. When someone enters their employer’s name, CiviCRM checks for existing matches to avoid duplicates. If no match is found, a new organization contact is created, and the relationship is established.

## Adding contacts to organizations

To add multiple contacts to an organization at once:

- Select the contacts from your search results.
- Choose **Add relationship - to organization** from the **Actions** menu.
- Pick the **Relationship Type** and search for the organization.
- Select the organization and click **Add to Organization**.
- Click **Done** to return to your search results.

## Adding contacts to households

To add contacts to a household:

- Select the contacts from your search results.
- Choose **Add relationship - to household** from the **Actions** menu.
- Pick the **Relationship Type** (usually “Household Member of”).
- Search for the household by name.
- Select the household and click **Add to Household**.
- Click **Done** when finished.

## Creating new relationship types

CiviCRM comes with common relationship types, but you can create your own if you need to track something unique.

- Go to **Administer > Customize Data and Screens > Relationship Types**.
- Click **New Relationship Type**.
- Enter labels for both directions of the relationship (for example, “Partner of” might work both ways, but “Grandparent of” and “Grandchild of” are different).
- Choose which contact types can be linked.
- Add a description if needed, and click **Save**.

## Creating custom fields on relationships

If you need to store extra information about relationships, you can add custom fields. For example, you might track which department an employee works in. See the “Creating Custom Fields” guide for detailed instructions.

## Disabling or deleting relationship types

If a relationship type is no longer needed, you can **disable** it (so it’s hidden but data remains) or **delete** it (removing it completely). To do this, go to **Administer > Option Lists > Relationship Types**, find the type, and choose **Disable** or **Delete** from the **More** menu.
