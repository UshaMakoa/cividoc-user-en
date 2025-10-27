---
categories:
  - Guide  
level: Basic  
summary:  This guide shows you how to manually add a membership record to someone’s contact in CiviCRM. 
section: Membership
---


# Adding memberships manually


This guide shows you how to manually add a membership record to someone’s contact in CiviCRM.  
 You’ll use this when someone joins offline (for example, by cheque, phone or in person), or if you’re adding existing members during setup.

No technical skills are needed — just access to the CiviMember component.

## **When to add a membership manually**

You might add memberships manually when:

* A member joins by post or phone.

* You import contacts but still need to record their membership dates.

* You’re testing your membership setup.

* Someone needs a complimentary or staff membership.

It’s a good idea to make sure your **membership types** are already defined before starting this process.

## **Step 1: Find the contact**

1. Go to **Search → Find Contacts**, and look up the person or organisation.

2. Click their name to open their contact record.

3. Go to the **Memberships** tab.

If the contact doesn’t exist yet, create them first.

## **Step 2: Add a new membership**

1. On the Memberships tab, click **Add Membership**.

2. Choose the **Membership organisation** (usually your own organisation).

3. Choose the **Membership type** from the list (for example, *Individual Annual*).

## **Step 3: Set membership dates**

You can enter the start date, end date, and join date.

* **Join date**: The date the person first became a member (even if renewed since).

* **Start date**: The beginning of the current membership period.

* **End date**: When this current membership expires.

Tip: If you select a membership type with fixed dates (like January to December), CiviCRM will adjust these automatically based on your settings.

## **Step 4: Record the membership status**

Choose the appropriate **status** from the list — for example *New*, *Current*, *Grace*, or *Expired*.

Usually, you’ll select *New* or *Current* for new entries.  
 CiviCRM can update statuses automatically later based on start and end dates.

## **Step 5: Link to a contribution (optional)**

If the member paid for their membership and you want to record it:

* In the **Contribution** field, select the related payment if it already exists.

* Or, after saving the membership, go to the contact’s **Contributions** tab to add a payment and link it back to the membership.

If it’s a free membership, you can leave this blank.

## **Step 6: Add notes or custom fields**

If you’ve set up **custom fields** for memberships (for example, *Source of membership* or *Region*), fill them in now.

You can also use the **Note** field to record any extra information, such as “Membership added by admin after phone call”.

## **Step 7: Save and review**

Click **Save**.

You’ll see the membership listed on the contact’s record. Check that:

* The start and end dates are correct.

* The membership type and status are what you expect.

* The payment (if linked) is shown correctly.

## **Editing or renewing a membership**

To make changes later:

* Open the contact’s **Memberships** tab.

* Click **Edit** beside the membership.

* Adjust the details or click **Renew** to extend it for another period.

CiviCRM automatically creates a new membership record when you renew, keeping a clear history of all periods.

## **Tips for accuracy**

* Be consistent with join and start dates — this helps reports stay accurate.

* Avoid creating duplicate memberships of the same type for one person.

* Use the **Search → Find Memberships** screen to check for existing records before adding new ones.

## **What’s next**

Once you’re comfortable adding memberships manually, you can:

* Import multiple memberships from a spreadsheet.

* Manage renewals and automated reminders.

* Set up online sign-up pages so members can join themselves.
