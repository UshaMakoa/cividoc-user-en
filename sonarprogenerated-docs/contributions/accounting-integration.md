---
categories: Guide
level: Intermediate
summary: Learn how to group, review, and export CiviCRM financial transactions in batches for easy import into your accounting software.
section: Contributions > Accounting Integration
---

# Accounting integration: managing and exporting batches

## What is accounting integration?

Accounting integration helps your organisation organise and export groups of financial transactions (like donations or payments) from CiviCRM, so you can import them into your accounting software. You can create a new batch for existing transactions, or use a batch created during manual data entry.

## Using a batch created through batch data entry

If you already use batch data entry for contributions, those batches can also be used for accounting integration. Once you validate and close a batch, it will appear in the accounting batch list with the status "Closed".

## Creating a new batch from existing transactions

### Create the batch

1. Go to **Contributions > Accounting Batches** and select **New Batch**.
2. Enter a **Batch Name** (required). CiviCRM suggests a default name, but you can change it.
3. Optionally, add a **Description** to help you identify the batch.
4. If you want to include only certain payment types (like credit card, check, cash, or EFT), select the **Payment Instrument**.
5. If you know the number of transactions or the total amount in advance, enter these. CiviCRM will check these when you close the batch, but you can override any warnings if they don’t match.
6. Click **Save**.

You can edit these details later as long as the batch is still open.

## Assigning transactions to a batch

After creating or opening a batch, you’ll see the batch details at the top of the screen (such as who created it, its status, payment method, and totals).

To add transactions:

1. Use the **Edit Search Criteria** section to filter which contributions you want to add.
2. In the search results, assign transactions one at a time (using **Assign**) or select several and use the action menu to assign them all at once.
3. Assigned transactions move to the batch list and disappear from search results.

## Viewing and removing assigned transactions

- All assigned transactions appear in the batch list.
- To remove a transaction, click **Remove** next to it, or select several and use the action menu to remove them.
- The batch totals update as you add or remove transactions.
- You can return and edit an open batch at any time.

## Closing and exporting a completed batch

When you’re done assigning transactions:

1. Choose **Close Batch** or **Close and Export**.
2. If the number or total amount of assigned transactions doesn’t match what you entered, you’ll see a "Mismatch" warning. You can fix the numbers or override the warning to update them.
3. Closing the batch changes its status to "Closed". You can reopen it before exporting if needed.
4. Exporting the batch lets you choose a format:
   - **CSV**: For spreadsheets.
   - **IIF**: For importing into QuickBooks and similar software.
5. Once exported, the batch status is "Exported" and it cannot be reopened.

## Searching for and managing batches

- Go to **Contributions > Accounting Batches** to see all batches.
- Filter batches by status, name, creator, payment method, number of transactions, or total amount.
- For **Open** batches: assign/remove transactions, edit details, close, export, or delete.
- For **Closed** batches: view transactions, export, reopen, or delete.
- For **Exported** batches: view transactions, download export files, or delete (cannot reopen).

You can also select multiple batches from the list and use the action menu to reopen, close, export, or delete several at once.

## Finding transactions by batch

- In **Advanced Search** or **Find Contributions**, you can search by batch name to see all transactions in a specific batch.

---

# comment: Source: https://docs.civicrm.org/user/en/latest/contributions/accounting-integration/
# comment: This page is a Guide, as it provides step-by-step instructions for achieving a specific task (managing and exporting accounting batches) without focusing on background theory or exhaustive reference details. The level is Intermediate, as it assumes users are familiar with contributions and basic CiviCRM navigation but may not know about accounting integration. The page logically belongs under Contributions > Accounting Integration. If further split is needed, a Tutorial could be created for first-time users, and Reference material could list all batch fields and export formats.