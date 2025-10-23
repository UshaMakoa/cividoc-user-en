# Source: https://docs.civicrm.org/user/en/latest/contributions/offline-fundraising/

---
categories: Guide  
level: Basic  
summary: This guide explains how non-profit users can manage offline fundraising in CiviCRM by creating contact lists, preparing postal mailings, and manually entering contribution data to keep records accurate.  
section: Offline fundraising  
---

# Offline fundraising

## Introduction

Offline fundraising includes collecting donations at events or through postal mailings. Since these donations happen outside of online forms, you need to manually enter the contribution details into CiviCRM to keep your records and reports accurate.

This guide will walk you through the three main steps for offline fundraising in CiviCRM:

- Creating your contact lists  
- Preparing postal mailings  
- Manually entering contribution information  

## Creating your lists

To reach supporters with offline appeals, first create a list of contacts:

1. Go to **Search > Find Contacts** in CiviCRM.  
2. Use search filters to select the contacts you want to include (this could be your entire database or a specific group).  
3. To track who receives your mailing, save the search results as a group:  
   - Select all contacts using the checkbox.  
   - From the **Actions** dropdown, choose **Group - add contacts** or **Group - create smart group**.  
4. Later, you can mark contacts in this group as recipients of a mailing by adding an activity via the **Actions** menu.

If you want to create letters for postal mailings, you can either:

- Use CiviCRM's built-in PDF letter printing feature, or  
- Export the contact list as a CSV file for use in mail merge with a word processor like LibreOffice or Microsoft Word.

### Exporting a contact list

To export contacts for mail merge or other uses:

1. Select the contacts you want to export using the checkboxes.  
2. From the **Actions** dropdown, choose **Export Contacts**.  
3. Choose whether to export **Primary fields** or **Select fields for Export**.  
   - If you select primary fields, the CSV file is generated immediately.  
   - If you choose to select fields, you will be prompted to pick which data columns to include.  
4. Optionally, save your field selections as an export mapping for future use.  
5. Click **Export** to download the CSV file.  
6. Click **Done** to return to your contact list.

## Creating postal mailings

Once you have your contact list or CSV file:

- Use your word processor’s mail merge feature to create personalized letters.  
- Alternatively, create mailing labels directly in CiviCRM:

  1. Perform the same contact search to get your mailing list.  
  2. From the **Actions** dropdown, select **Mailing labels - print**.  
  3. Choose the label type that matches your label sheets.  
  4. Decide whether to exclude contacts who have "do not mail" checked (recommended).  
  5. Choose whether to merge multiple contacts at the same address into one label (useful for households or organizations).  
  6. Click **Make Mailing Labels** to generate a printable PDF of your labels.

Note: Labels are printed in a column-by-column order matching the contact search results.

## Manually entering contributions

After your offline fundraising events or mailings, enter the donations into CiviCRM manually to keep your financial records complete. (This step is covered in detail in the next guide: Manual entry of contributions.)

---

This guide is designed to help non-profit users new to CiviCRM manage offline fundraising tasks confidently and accurately. For more complex scenarios or automations, consider exploring additional documentation or tutorials.