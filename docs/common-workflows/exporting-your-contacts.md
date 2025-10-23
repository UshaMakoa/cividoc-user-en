---
categories:
  - Uncategorized
  - Guide
level: Basic
summary: Step-by-step instructions for exporting your contacts from CiviCRM, including how to select fields, save mappings, and handle common scenarios for non-profit users.
section: Common workflows
---

# Exporting your contacts from CiviCRM

## Overview

Exporting your contacts lets you share CiviCRM data with other applications by creating a file in a standard CSV format. This is useful for tasks like sending thank-you letters, creating mailing lists, or analyzing data in a spreadsheet. You can export a predefined set of fields or create your own custom export mapping to use again later.

## Step 1: Search for contacts

Begin by searching for the contacts you want to export. You can use any of CiviCRM’s search tools, such as Quick Search, Find Contacts, Advanced Search, or Search Builder. If you’re working with a specific group, you can also start from the group view.

## Step 2: Select contacts to export

After your search, you’ll see a list of contacts. You can export all contacts in your results or select specific ones using the checkboxes next to each record.

## Step 3: Start the export

From the **Actions** dropdown menu, choose **Export Contacts**. This opens the export wizard, where you can customize your export.

## Step 4: Choose what to export

You have two main options:

- **Primary fields:** Export a standard set of 80 core contact fields (including primary email, phone, and address).
- **Custom fields:** Select exactly which fields to include, such as non-primary contact details, custom fields, or data from related contacts. You can also use a previously saved export mapping.

If you’re creating mailing labels, you can choose to export one record per household or one per address. You can also exclude contacts marked “do not mail,” those without a street address, or those who are deceased.

## Step 5: Add contacts from another group (optional)

If needed, you can add contacts from an additional group to your export.

## Step 6: Select fields and save mappings

If you chose to select your own fields or use a saved mapping, you’ll see a list of fields. You can use the mapping as is, modify it, or save your changes as a new mapping for future use.

## Step 7: Export your file

When you’re ready, click **Export**. Your file will download in CSV format, ready to use in a spreadsheet or other application.

## Tips

- **Field separator:** By default, CiviCRM uses a comma to separate fields in the CSV. If you need a different separator, you can change this in **Administer > Localization > Languages, Currency, Locations**.
- **Reusing mappings:** Saving your export mappings saves time on future exports with similar requirements.

## Next steps

Now that you’ve exported your contacts, you can use the file for mail merges, data analysis, or sharing with colleagues. If you need to import data back into CiviCRM, see the guide on importing data.
