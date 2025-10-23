# Source: https://docs.civicrm.org/user/en/latest/contributions/manual-receipts-and-thank-yous/

---
categories: Guide
level: Basic
summary: Learn how to manually send receipts and thank-you letters for donations in CiviCRM, including options for email, PDF, and grouped contributions.
section: Contributions
---

# Sending receipts and thank-you letters in CiviCRM

## Overview

This guide helps non-profit staff who are new to CiviCRM send receipts and thank-you letters to donors, whether for individual gifts or grouped contributions (such as annual tax statements). You’ll learn how to send these communications manually, choose between email and PDF formats, and understand when to use grouped letters.

## Sending individual receipts

When a donor gives online, CiviCRM can send an automatic receipt if this option is enabled. If you need to send or resend a receipt manually:

- **Edit the contribution record**: Find the contact, open their contribution, tick the “Send Receipt?” box, and save. An email receipt will be sent immediately.
- **Send to multiple donors**: Use the “Find Contributions” search, select the relevant contributions, and choose “Receipts – print or email” from the actions menu. You can email receipts or generate PDFs to print and mail.
- **Customizing receipts**: By default, receipts show basic information. For more customization, you’ll need some technical knowledge (Smarty templates), but for most users, the standard options are sufficient.

## Sending thank-you letters

Thank-you letters are ideal for campaign updates, annual summaries, or any situation where you want to communicate more personally with donors.

- **Find contributions**: Use “Find Contributions” or “Advanced Search” (set to display results as contributions).
- **Select contributions**: Choose which donations should trigger a thank-you letter.
- **Choose action**: Select “Thank-you letters – print or email”. You’ll see options to update the thank-you or receipt date.
- **Print and email options**: You can generate PDFs for printing, send emails where possible (with PDFs for those without email), or do both.
- **Letter templates**: Use an existing template, create a new one for this occasion, or save a new template for future use. For help with templates, see the sections on tokens and mail merge.
- **Complete the process**: Click “Make Thank-you Letters” to generate your communications. A “Print/Merge Document” activity is created for each letter.

## Grouped contribution thank-you letters

For donors who give multiple times (such as monthly), you may want to send a single letter summarizing all their gifts—especially for annual tax statements.

- **Group contributions**: When generating letters, choose how to group contributions (e.g., by contact, campaign, or other criteria).
- **Separator options**: Use “Comma” to list amounts and dates in a sentence, or “Table Cell” to display them in a table. Note: The table format works best with a small number of gifts.
- **Including yearly totals**: By default, CiviCRM cannot show the total yearly amount in grouped letters. To include this, you (or a developer) must enable Smarty functionality in your templates and use the {$contribution_aggregate} token. This is an advanced feature and may require technical support.

## Tips for success

- **Check settings**: Always review your page format and template settings before sending a batch of letters.
- **Respect preferences**: By default, CiviCRM honors “Do not email” and “Do not mail” settings, but you can override these if needed.
- **Keep records**: Each letter generation creates an activity record, helping you track communications with donors.

## When to ask for help

If you need highly customized receipts or letters (especially with yearly totals in grouped letters), you may need assistance from someone familiar with CiviCRM templates and Smarty. For most day-to-day tasks, the built-in options will meet your needs.

---

This guide is designed for non-profit users who are learning CiviCRM and focuses on practical, step-by-step instructions for common tasks[1][3]. If your organization has complex needs (such as advanced template customization), consider creating a separate, more advanced guide or reaching out to your CiviCRM support team.