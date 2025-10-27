---
categories: Guide
level: Basic
summary: Learn how to record, batch-enter, and cancel pledge payments in CiviCRM, step by step, for non-profit staff handling offline donations.
section: Pledges > Everyday tasks
---

# Everyday pledge tasks

## Record a payment for a pledge

If someone makes a pledge and pays by cash, cheque, or another offline method, you need to manually record that payment in CiviCRM.

1. Search for the contact:
   - Go to **Search** and select **Find Contacts**.
2. Open the pledges tab:
   - In the contact’s record, click the **Pledges** tab.
3. View scheduled payments:
   - Click the small arrow next to the pledge to show scheduled payments.
4. Mark a payment as completed:
   - Find the next scheduled payment and set its status to **Completed**.
5. Edit payment details (optional):
   - You can also edit the scheduled payment to change the due date or amount if needed.

## Enter multiple pledge payments in a batch

If you have many payments to enter at once (for example, after a fundraising event), use the Batch Data Entry feature.

1. Create a new data entry batch:
   - Go to **Contributions > Batch Data Entry** and select **New Data Entry Batch**.
   - Fill in the required fields:
     - **Batch Name** (edit if you wish)
     - **Type:** Choose **Pledge Payment**
     - **Description** (optional)
     - **Number of Items** (required)
     - **Total Amount** (required)
2. Enter pledge payments:
   - For each line, start typing an existing contact’s name or create a new contact.
   - Click the arrow to see all open pledges for that contact and assign the payment.
   - The financial type and amount will fill in automatically but can be changed if you have permission.
   - Enter payment details:
     - **Status** (defaults to Completed)
     - **Date and Time** (defaults to now, can be changed)
     - **Source** (describe where the payment came from)
     - **Paid by** (required: cash, cheque, EFT, etc.)
     - **Check Number** (if paid by cheque)
     - **Send Receipt** (tick if you want to send a receipt by email)
     - **Invoice ID**, **Soft Credit**, **Soft Credit Type** (if needed)
3. Save or process the batch:
   - You can save and return later, or enter all transactions in one go.
   - To continue later, click **Save & Continue Later**.
   - When finished, click **Validate & Process the Batch** to close it.
   - If totals or counts don’t match what you entered at the start, you’ll be alerted. You can:
     - Click **Ignore Mismatch & Process the Batch** to update the batch totals, or
     - Continue editing until the totals match, then process again.

## Cancel a pledge

If a pledge will not be fulfilled, you can cancel it.

1. Find the pledge:
   - Search for the contact or use the **Find Pledges** tool.
2. Cancel:
   - Click the **more** link next to the pledge and select **Cancel**.

---

# comment: Source: https://docs.civicrm.org/user/en/latest/pledges/everyday-tasks/
# comment: Suggestion: This page is a How-to Guide (problem-oriented, step-by-step instructions for common tasks, no background or reference material). The content is basic, suitable for new or non-expert users. If needed, batch data entry could be split into a separate guide for clarity, but for this audience, grouping all everyday pledge tasks together is likely most approachable.