---
categories:
  - Guide  
level: Intermediate  
summary:  This guide explains how to import existing memberships into CiviCRM using a spreadsheet.
section: Membership
---



# Importing memberships in bulk


This guide explains how to import existing memberships into CiviCRM using a spreadsheet.  
 You’ll learn how to prepare your data, match it to existing contacts, and check for errors before completing the import.

This process is useful when you are setting up CiviCRM for the first time, migrating from another system, or updating membership data in bulk.

## **Before you start**

Before importing memberships, make sure that:

* All the **contacts** for your members already exist in CiviCRM.

* You have created your **membership types**.

* You understand how membership **statuses** and **dates** (start, end, join) work.

If you also want to import payments or contributions linked to those memberships, you’ll handle that in a separate import after this one.

## **Step 1: Prepare your data**

Start by creating a spreadsheet that contains one row per membership.  
 Include the following columns:

* **Contact ID** or **Email Address** (to match to an existing contact)

* **Membership Type**

* **Start Date**

* **End Date**

* **Join Date**

* **Status**

* **Source** (optional, such as “Imported from legacy database”)

* **Owner Membership ID** (if importing related memberships)

Keep dates in the format `YYYY-MM-DD` (for example, `2025-03-01`).

If you have multiple memberships for one person, include each on a separate row.

Tip: Always double-check your data for typos and consistent date formats before importing.

## **Step 2: Open the import tool**

1. Go to **Memberships → Import Memberships**.

2. Choose your file and upload it.

3. Select the file type — usually **CSV** (comma-separated values).

4. If your file has a header row, tick **First row contains column headers**.

5. Click **Continue**.

## **Step 3: Map your fields**

CiviCRM will show you the column names from your spreadsheet and ask you to match each one to a CiviCRM field.

For example:

* Match **Contact ID** to *Contact ID*.

* Match **Membership Type** to *Membership Type*.

* Match **Start Date**, **End Date**, and **Join Date** to their corresponding fields.

If CiviCRM can’t find a match automatically, you can select the correct field from the dropdown list.

When you’re happy with the mapping, click **Continue**.

## **Step 4: Choose how to match contacts**

CiviCRM needs to know how to identify the contact each membership belongs to.

You can match by:

* **Contact ID** (recommended if available)

* **Email Address**

* **External Identifier** (if used in your organisation)

Make sure that the field you select exists for every contact in your import file.  
 If a match cannot be found, the membership for that row will not be imported.

## **Step 5: Review the preview**

Before the import is finalised, CiviCRM will show you a preview of the first few rows and how they will be matched.

Check that:

* Membership types match correctly.

* Dates and statuses are showing as expected.

* Each row links to the right contact.

If something looks wrong, cancel and fix your spreadsheet before trying again.

## **Step 6: Run the import**

Once everything looks right, click **Import Now**.

CiviCRM will process your file and confirm how many memberships were successfully imported and how many, if any, had issues.  
 If there are errors, download the error file provided and review what went wrong.

Common issues include:

* Membership type names that don’t exactly match existing ones.

* Dates in the wrong format.

* Contacts that can’t be matched.

Fix these and re-import only the affected rows.

## **Step 7: Verify your imported data**

After the import completes, spot-check a few contacts:

1. Open a contact record and check the **Memberships** tab.

2. Confirm that the correct membership type, dates, and status appear.

3. Run the **Find Memberships** search to confirm the total number imported matches your expectations.

If everything looks correct, your import is complete.

## **Tips and best practices**

* Always back up your database before running large imports.

* Test with a small file (five to ten records) before importing everything.

* Use consistent membership type names — they must match exactly.

* Save your import mapping if you plan to reuse it later.

* Keep a copy of your original import file for audit purposes.

* After importing, consider setting up renewal reminders or Smart Groups to manage your new members effectively.

## **What’s next**

Once your membership data is imported, you can:

* Import related contributions to link payments to memberships.

* Set up dashboards and reports to track totals and renewal rates.

* Use CiviRules to automate communications with your newly imported members.
