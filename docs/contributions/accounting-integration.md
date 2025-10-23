---
categories:
  - Uncategorized
  - Guide  
level: Basic  
summary: This guide explains how non-profit users can create, manage, and export accounting batches in CiviCRM to integrate contribution transactions with their accounting software.  
section: Accounting Integration  
---

# Accounting integration

## What is accounting integration?

Accounting integration in CiviCRM helps you export groups of financial transactions (called batches) so you can import them into your accounting software. This makes it easier to keep your accounting records up to date with your contributions.

## Using batches created through batch data entry

If you use batch data entry to record contributions, once you finish and close a batch, it automatically appears in the accounting batches list with the status *Closed*. You can use these batches directly for accounting export.

## Creating a new accounting batch from existing transactions

1. Go to **Contributions > Accounting Batches** and click **New Batch**.  
2. Fill in the batch details:  
   - **Batch name**: Required. CiviCRM suggests a default name you can change.  
   - **Description**: Optional notes about the batch.  
   - **Payment method**: Choose if you want to include only transactions paid by a specific method (e.g., Credit Card, Check).  
   - **Number of transactions**: If you know how many transactions will be in the batch, enter this to help with verification later.  
   - **Total amount**: If you know the total money amount expected, enter it for verification.  
3. Save the batch. You can edit these details later as long as the batch is open.

## Assigning transactions to a batch

1. After creating or opening a batch, you will see the batch details at the top of the page, including status, payment method, and totals.  
2. Use the *Edit Search Criteria* section to find contributions to add. If you selected a payment method when creating the batch, it will filter transactions automatically.  
3. From the search results, assign transactions one by one by clicking **Assign**, or select multiple and use the action menu to assign them all at once.  
4. Assigned transactions appear in the list in the middle of the page.

## Viewing and removing assigned transactions

- To remove a transaction, click **Remove** next to it, or select multiple transactions and choose **Remove from Batch** from the action menu.  
- The batch totals update automatically as you add or remove transactions.  
- You can leave the batch open and return later to continue editing.

## Closing and exporting a batch

- When you finish assigning transactions, you can **Close** or **Close and Export** the batch.  
- If the number or total amount of assigned transactions does not match what you entered, CiviCRM will warn you. You can fix the mismatch or override the warning to close the batch.  
- Closing without exporting sets the batch status to *Closed*. You can reopen it later to export.  
- Closing and exporting lets you choose an export format:  
  - **CSV**: A spreadsheet format.  
  - **IIF**: A format for QuickBooks and other Intuit products.  
- Once exported, the batch status changes to *Exported* and cannot be reopened.

## Managing batches

- Go to **Contributions > Accounting Batches** and select **Open Batches** to see all batches.  
- You can filter batches by status (Open, Closed, Exported), name, creator, payment method, number of transactions, or total amount.  
- For *Open* batches, you can assign/remove transactions, edit details, close, export, or delete.  
- For *Closed* batches, you can view transactions, export, reopen, or delete.  
- For *Exported* batches, you can view transactions, download the export file again, or delete the batch. Exported batches cannot be reopened.  
- You can also select multiple batches and perform bulk actions like re-open, close, export, or delete.

## Finding transactions by batch

- Use the **Advanced Search** or **Find Contributions** and search by batch name to see all transactions included in a specific batch.
