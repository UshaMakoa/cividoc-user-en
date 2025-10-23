---
categories:
  - Uncategorized
  - Guide  
level: Basic  
summary: This guide explains how non-profit users can manually enter and batch enter offline contributions, memberships, or pledge payments in CiviCRM, ensuring accurate records for reporting and donor management.  
section: Contributions  
---

# Manual entry of contributions

## Introduction

When your organisation receives donations or payments offline (such as cash, checks, or EFT), you need to add these contributions manually to CiviCRM to keep your records accurate. Payments made online through CiviCRM are recorded automatically, but offline payments require manual entry.

This guide will walk you through how to enter contributions one by one and how to use batch entry for multiple payments, helping you manage your fundraising data efficiently.

## Adding contributions manually one by one

If the donor is not already in your database, first create a contact record for them. Then follow these steps to record their contribution:

1. Search for the contact using the contact search tool (e.g., *Search > Find Contacts*).
2. Open the contact’s record and select the *Contributions* tab.
3. Click **Record Contribution** (for payments like check, cash, EFT). If you have a payment processor set up, you can also select **Submit Credit Card Contribution** to process a payment immediately.
4. Fill out the *New Contribution Form*:
   - Choose the **Financial Type** (e.g., donation, membership fee).
   - Enter the **Amount** and **Received Date** (defaults to today).
   - Set the **Status** (default is Completed).
   - Fill any custom fields if your organisation uses them.
   - Optionally assign a **Soft Credit** if the donation is linked to a campaign or fundraiser.
   - Add any notes or details, including if the contribution is in honor of someone or if a premium (gift) is associated.
5. Click **Save** or **Save and New** if entering more contributions.

If you have many contributions to enter, consider using batch entry instead.

## Batch entry of contribution, membership, or pledge payments

Batch entry lets you enter many payments quickly using a grid interface, which can speed up data entry and help you verify totals against your deposit slips.

### Workflow for batch entry:

1. **Create a new batch**:
   - Go to *Contributions > Batch Data Entry* or *Membership > Batch Data Entry*.
   - Enter a **Batch Name** (you can edit the default).
   - Select the **Type** of payment (Contribution, Membership, or Pledge Payment).
   - Enter the **Number of items** and **Total amount**.
   - The batch will start with status “Open”.

2. **Enter payments**:
   - For each line, select or create the **Contact**.
   - Fill in **Financial Type**, **Amount**, **Status**, **Received Date**, and other fields like **Soft Credit**, **Source**, **Paid By** (payment method), **Check Number**, and **Invoice ID**.
   - For memberships, you can add new memberships or renew existing ones with start and end dates.
   - For pledge payments, assign payments to pending pledges and adjust amounts if needed.

3. **Validate and process the batch**:
   - You can save the batch and return later to add more payments.
   - When finished, click **Validate & Process the Batch** to close it.
   - If totals or counts don’t match, you will be alerted and can either correct entries or override and close the batch.

### Searching processed batches

You can find contributions or payments in closed batches by:

- Using *Searches > Find Contributions* and filtering by batch name.
- Using *Searches > Advanced Search* with contribution criteria and batch name.
- Browsing *Contributions > Batches*, *Memberships > Batches*, or *Pledge Payments > Batches* and filtering by status “Closed”.
- Creating reports filtered by batch name.

## Configuring profiles for batch entry

CiviCRM uses profiles (sets of fields) to control what information appears during batch entry and when creating new contacts inline.

- To change fields for creating new contacts during batch entry, edit the reserved profiles **New Individual**, **New Household**, or **New Organization** under *Administer > Customize Data and Screens > Profiles*.
- To customize fields shown when entering contributions or memberships in batches, edit the **Contribution Batch Entry** or **Membership Batch Entry** reserved profiles.
  
Be aware that changes to these reserved profiles affect other areas where new contacts are created inline.

## Importing contributions

If you have a large number of contributions to add, importing data from CSV files may be faster.

- Required fields for import include **Financial Type**, **Total Amount**, and a way to match the contribution to a contact (Contact ID, Email, or External Identifier).
- Contributors must already exist as contacts in your database before importing contributions.
- If needed, import contacts first, including external IDs, then import contributions linked to those contacts.

Remember to keep CSV files under 2MB; split large files into smaller ones if necessary.
