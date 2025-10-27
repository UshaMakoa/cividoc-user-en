---
categories: Guide
level: Basic
summary: Learn how to record individual and batch contributions, including offline payments, in CiviCRM so your organisation’s records and reports stay accurate.
section: Contributions > Recording contributions
---

# Manual entry of contributions

When your organisation receives a donation or payment that is not made through your website (for example, cash, cheque, or bank transfer), you need to add this contribution manually in CiviCRM to keep your records and reports up to date.

## Adding a single contribution manually

To record a new contribution for a supporter:

1. **Find the contact**: Use the search tools (for example, go to Search > Find Contacts) to locate the person or organisation who made the contribution.
2. **Open the Contributions tab**: On their contact record, click the Contributions tab.
3. **Click Record Contribution**: Choose "Record Contribution (Check, Cash, EFT...)" for offline payments. If you want to process a credit card payment directly, select "Submit Credit Card Contribution" (if your site is set up for this).
4. **Fill out the contribution form**:
   - **Financial Type**: Choose the type of contribution (for example, Donation, Membership Fee).
   - **Amount**: Enter the amount received.
   - **Received Date**: The date you received the payment (defaults to today).
   - **Receipt Date**: The date shown on the receipt.
   - **Status**: Set the status (usually "Completed").
   - **Custom fields**: Fill in any custom fields your organisation uses for contributions.
   - **Soft Credit To**: If the donation was made because of someone else's fundraising (for example, through a Personal Campaign Page), assign a soft credit to that person.
   - **Additional details**: Add notes, record when a thank-you letter was sent, or indicate if the contribution was made in honour of someone.
   - **Premium information**: If the donor received a gift in return, record it here.
5. **Save**: Click Save, or Save and New if you have more contributions to enter.

**Tip:** If you need to add a new donor who is not in your database, create their contact record first.

If you have several contributions to enter at once, consider using the batch entry feature.

## Batch entry of contributions, memberships, or pledge payments

Batch entry makes it easier to record many payments at once, such as after a fundraising event or when processing a bank deposit.

### 1. Create a new batch

- Go to Contributions > Batch Data Entry (or Membership > Batch Data Entry for membership payments).
- Enter:
  - **Batch Name** (required): Give your batch a clear name.
  - **Type**: Select Contribution, Membership, or Pledge Payment.
  - **Status**: Leave as "Open" while entering data.
  - **Number of items**: How many payments you plan to enter (required).
  - **Total amount**: The total value of all payments in this batch (required).

**Note:** Once you close a batch, it can’t be edited.

### 2. Enter payments in the batch

For each row in the batch grid, enter:

- **Contact**: Start typing to find an existing contact, or create a new one if needed.
- **Financial Type**
- **Amount**
- **Status**
- **Received Date and Time**
- **Send Receipt**: Tick if you want to email a receipt.
- **Soft Credit** and **Soft Credit Type** (if applicable)

Depending on the batch type, you may also need:

- **Source**: Where the payment came from.
- **Paid by**: How it was paid (cash, cheque, EFT, etc.).
- **Check Number**: If paid by cheque.
- **Invoice ID**

For membership payments, you can also set membership type, start and end dates, and renewal details.

### 3. Validate and process the batch

- When finished, click **Validate & Process the Batch** to close it.
- If you need more time, click **Save & Continue Later** and return to the batch when ready.
- If totals or counts don’t match what you entered, CiviCRM will alert you. You can either:
  - Ignore the mismatch and process the batch (the system will update the totals), or
  - Continue editing until the numbers match.

## Searching for contributions in batches

You can find contributions or payments from closed batches using:

- **Searches > Find Contributions**: Filter by batch name.
- **Searches > Advanced Search**: In the Contributions area, filter by batch name.
- **Contributions > Batches**: Filter by status "Closed".
- **Memberships > Batches** or **Pledge Payments > Batches**: Filter by status "Closed".
- **Reports > Create Reports from Templates**: Use the Contribution Report Detail and filter by batch name.

## Customising batch entry profiles

To change which fields appear when creating new contacts or entering batch data:

- Go to Administer > Customize Data and Screens > Profiles, then click the Reserved Profiles tab.
- Edit the "New Individual", "New Household", or "New Organization" profiles to change the fields for new contacts.
- Edit the "Contribution Batch Entry" or "Membership Batch Entry" profiles to change the fields shown in the batch entry grid.

**Note:** Changes to these reserved profiles affect all areas of CiviCRM where new contacts or batch entries are created.

# comment: Source: https://docs.civicrm.org/user/en/latest/contributions/manual-entry/
# comment: Suggestion: This page is a How-to Guide (problem-oriented, step-by-step instructions for specific tasks: entering contributions manually or in batches, and customising batch entry). The level is Basic, as it is aimed at new or non-expert users. The content belongs in the "Contributions > Recording contributions" section. No major splits are needed; the page is focused and practical.