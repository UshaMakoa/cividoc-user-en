---
categories: Guide
level: Basic
summary: Learn how to manually send receipts and thank-you letters to donors in CiviCRM, including grouped end-of-year statements.
section: Contributions > Common workflows
---

# Manual receipts and thank-you letters

## Sending manual receipts

You can send a receipt to a donor after they make a contribution, even if it was not sent automatically.

- If a donor contributed online and you set up the contribution page to send receipts, they will receive one automatically.
- To manually send or re-send a receipt for any contribution:
  - Find the donor’s contribution record.
  - Edit the record and tick the **Send Receipt?** option.
  - Click **Save** to send the receipt by email.
- To send receipts to multiple donors at once:
  - Use the **Find Contributions** search.
  - Select the contributions you want.
  - In the actions drop-down menu, choose **Receipts – print or email**.
  - Choose whether to send receipts by email or generate PDF receipts for printing.
  - By default, sending or printing receipts updates the receipt date, but you can keep the original date if needed.
  - You can also choose to ignore “Do not email/Do not mail” settings to ensure all selected donors receive a receipt.
- The standard receipt includes basic information. If you need to customize it, you will need technical knowledge (Smarty templates). For most users, using the thank-you letters workflow is easier for customized or delayed receipts.

## Sending thank-you letters

Thank-you letters are useful for acknowledging donors, especially for campaigns or end-of-year tax statements.

- You can send thank-you letters for individual or grouped contributions.
- To start:
  - Use **Find Contributions** or **Advanced Search** and set **Display Results As** to Contributions.
  - Select the contributions you want to include.
  - Choose **Thank-you letters – print or email** from the actions menu.
- You can choose to update the thank-you date or receipt date for these contributions.
- Print and email options:
  - Generate printable PDFs only.
  - Send emails where possible and create PDFs for those who cannot receive emails.
  - Send emails and create PDFs for all selected contacts.
- If a donor made multiple contributions:
  - To send a separate letter for each contribution, set **Group contributions by** to “no grouping.”
  - To combine multiple contributions in one letter, choose a grouping option.
- Check the **Page Format** settings to ensure your letters look right.
- You can use an existing template, create a new one-off letter, or save a new template for future use.
- For more on creating letter templates, see the sections on **Tokens and mail merge** and **Postal mail communications**.
- When you generate the letters, CiviCRM creates a “Print/Merge Document” activity for each letter, with the subject you specify.

## Grouped contribution thank-you letters

You can send donors a single statement covering all their contributions for a period, such as for tax purposes.

- To do this, select a grouping option other than “no grouping” for **Group contributions by**.
- Grouped letters can list each contribution’s amount and date, separated by commas or shown in a table.
- If you want to include the total amount donated in the letter, you or your technical support person must enable Smarty functionality for your emails.
- With Smarty enabled, you can use the token `{$contribution_aggregate}` to show the total amount in your letter.
- Example letter structure:
  - Greet the donor.
  - Thank them for their total donation.
  - List each contribution’s date, amount, and receipt number in a table.
  - Close with appreciation.

# comment: Source: https://docs.civicrm.org/user/en/latest/contributions/manual-receipts-and-thank-you-letters/
# comment: This page is a Guide because it provides step-by-step instructions for performing specific tasks (sending receipts and thank-you letters), but does not focus on first-time learning or background concepts. The grouped contribution section could be split into a Reference page for template tokens and formatting options if users need exhaustive details.