---
categories:
  - Guide  
level: Intermediate  
summary:  This guide explains how to manage **related memberships** in CiviCRM — where one person or organisation’s membership automatically gives membership to another related contact.
section: Membership
---


# Managing related memberships


This guide explains how to manage **related memberships** in CiviCRM — where one person or organisation’s membership automatically gives membership to another related contact.

You’ll learn how to set up related memberships, how they behave, and how to keep them in sync when the primary membership changes.

It’s written for membership managers and administrators who manage organisational or family memberships and want to make sure related members are added and updated correctly.

## **What are related memberships**

A related membership links two or more contacts so that when one has an active membership, others automatically receive a connected membership.

This is useful when:

* An organisation joins, and all its employees are also members.

* A family membership covers multiple people in one household.

* A parent organisation’s membership grants membership to its branches.

CiviCRM uses **relationships** between contacts to determine who gets the related membership. When the main membership is added or updated, the system automatically creates or updates memberships for related contacts based on the rules you define.

## **How related memberships work**

Each related membership is defined by:

* A **membership type** that specifies which related contacts are included.

* A **relationship type** that connects the main contact to the related contact (for example, “Employee of” or “Child of”).

* The same or different **membership type** for the related contact.

For example:

* The main contact *Organisation A* has a membership type “Corporate Member”.

* Employees of *Organisation A* (linked by the “Employee of” relationship) automatically receive the “Individual Member” type.

This setup saves time and ensures consistency — you don’t need to manually add or update memberships for every related person.

## **Step 1: Setting up a relationship type**

Before defining related memberships, make sure the correct relationship types exist in your system.

1. Go to **Administer → Customize Data and Screens → Relationship Types**.

2. Check for the relationship you want to use (for example, *Employee of / Employer of*).

3. If it doesn’t exist, click **Add Relationship Type** and create one.

4. Set the relationship direction clearly — for example, *A is Employee of B* and *B is Employer of A*.

You’ll use this relationship later to link memberships.

## **Step 2: Defining the related membership rule**

1. Go to **Administer → CiviMember → Membership Types**.

2. Click **Add Membership Type** or **Edit** an existing one.

3. In the **Relationship** section, choose the relationship type that should trigger related memberships (for example, *Employee of*).

4. Choose which membership type the related contact should receive.

5. Set whether the related membership should be automatically added, updated, or removed when the main membership changes.

6. Save your changes.

You can define multiple related memberships for a single membership type if you have more than one relationship pattern (for example, both employees and volunteers receiving related membership).

## **Step 3: Creating the main membership**

When you create or import a membership for the main contact (for example, an organisation), CiviCRM will automatically generate memberships for all related contacts that match your defined rule.

To test this:

1. Create or edit a contact that has relationships set up.

2. Add a membership for the primary contact.

3. Check the related contacts — they should now each have a membership record created automatically.

If the related contact doesn’t receive a membership, check that the relationship type and membership type are correctly linked in your membership settings.

## **Step 4: Keeping memberships in sync**

CiviCRM automatically updates related memberships when:

* The main membership is renewed.

* The main membership expires.

* The relationship between contacts changes (for example, an employee leaves an organisation).

You can also update related memberships manually by editing the main membership and saving it again. This triggers a refresh of all related records.

## **Step 5: Ending a related membership**

When the main membership ends or the relationship is deleted, CiviCRM can automatically end or remove the related membership, depending on your configuration.

You can also manually remove an individual related membership if the link no longer applies. To do this, go to the related contact’s **Memberships** tab and delete the record.

## **Best practices**

* Define your relationship types clearly and avoid duplicates — this keeps your related membership rules simple and reliable.

* Name membership types consistently so it’s clear which are used for individuals and which are for organisations.

* Review your relationships periodically to ensure they’re still valid (for example, that employee lists are up to date).

* Test related membership behaviour after upgrades or configuration changes.

* Communicate clearly with organisational members about who qualifies for related membership and how updates work.

## **Common use cases**

* **Corporate memberships** – where an organisation’s employees automatically receive individual membership benefits.

* **Family memberships** – where one parent’s membership covers dependents.

* **Network memberships** – where membership at a national level includes automatic membership for local branches.

Related memberships make these models easier to manage by keeping everything connected and up to date automatically.

## **What’s next**

Once you’re comfortable with related memberships, you can:

* Combine them with **CiviRules** to trigger extra actions, such as welcome emails for new related members.

* Use **Smart Groups** to report on both main and related members together.

* Create dashboards that track total active members, including related memberships.
