# Source: https://docs.civicrm.org/user/en/latest/pledges/everyday-tasks/

---
categories: Guide  
level: Basic  
summary: This page explains how to manage pledge payments in CiviCRM, including recording individual payments, entering multiple payments in batches, and canceling pledges.  
section: Everyday tasks  
---

# Managing pledge payments in CiviCRM

## Recording individual pledge payments

If a donor pays offline (for example, by cash or cheque), you need to record their payment manually in CiviCRM:

- Search for the contact in CiviCRM using **Search > Find Contacts**.
- Open the contact’s record and go to the **Pledges** tab.
- Click the small arrow next to the pledge to view scheduled payments.
- Find the next scheduled payment and mark it as **Completed**.
- You can also edit the scheduled payment to change the due date or amount if needed.

## Entering multiple pledge payments using batch data entry

When you have many pledge payments to record at once, use the Batch Data Entry feature to save time:

1. **Create a new batch:**
   - Go to **Contributions > Batch Data Entry > New Data Entry Batch**.
   - Enter a batch name (you can keep the default), select **Payment Type** as *Pledge Payment*, and fill in the total number of items and total amount.
   - Optionally, add a description.

2. **Enter pledge payments:**
   - In the batch entry grid, start typing a contact’s name to select an existing contact or create a new one.
   - Use the drop-down to select an open pledge for that contact.
   - The payment amount and financial type will fill automatically but can be adjusted if you have permission.
   - Fill in payment details such as payment status (defaults to Completed), date received, payment method (cash, check, EFT, etc.), check number if applicable, and source.
   - You can also choose to send a receipt by email.

3. **Save and process the batch:**
   - You can save the batch and continue later by clicking **Save & Continue Later**.
   - To add or edit payments later, go to **Contributions > Batch Data Entry** and select **Enter Records** for your batch.
   - When finished, click **Validate & Process the Batch** to close it.
   - If the total amount or count of payments does not match the batch totals you entered, you will be warned and can either fix the entries or override the totals.

## Canceling pledges

If a pledge will not be fulfilled, you can cancel it:

- Find the pledge via the contact record or the **Find Pledges** search tool.
- Click the **more** link next to the pledge and select **Cancel**.

---

This guide helps non-profit users easily manage pledge payments in CiviCRM by explaining straightforward steps for recording payments, using batch entry for efficiency, and handling cancellations. The instructions use plain language and focus on everyday tasks to support users new to CiviCRM.