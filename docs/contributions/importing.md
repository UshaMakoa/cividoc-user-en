---
categories:
  - Guide
level: Basic
summary: Learn how to import contributions (donations and payments) into CiviCRM using a step-by-step process designed for non-profit users.
section: Contributions > Importing contributions
---

# Importing contributions

## Overview

Importing contributions allows you to add donation and payment records from an external file (like a spreadsheet) into CiviCRM. This is helpful if your organisation receives donations through other systems or needs to update multiple records at once.

## Before you start

- Make sure you have the **Civi Import extension** installed in your CiviCRM system.

- Prepare your data file (for example, a CSV or spreadsheet) with all the contributions you want to import.

- Check that your file is **UTF
-8 encoded** if it contains special characters.

- Decide which field separator your file uses (commonly a comma or semicolon).

## Step 1: Start the import

- Go to **Contributions > Import Contributions** in the CiviCRM menu.

## Step 2: Choose your data source

- Select the type of file you want to import (CSV is most common, but spreadsheets like .odt or .xlsx are also supported).

- Click the button next to **Import Data File** to select your file from your computer or network.

- Specify your file’s field separator (for example, comma or semicolon).

    - *Tip:* If your numbers use commas as decimal separators, use a semicolon as the field separator to avoid errors.

## Step 3: Set import options

- Choose the **contact type** for these contributions (for example, Individuals).

- Decide if you are **adding new contributions** or **updating existing ones**.

- Select the **date format** used in your file (for example, mm/dd/yy).

- If you have saved a field mapping from a previous import, you can select it to save time.

## Step 4: Match fields

- On the next screen, match each column in your file to the correct CiviCRM field.

- If you don’t want to import a particular column, select “do not import” for that field.

- You can set a **default value** for any CiviCRM field if your file does not have data for it.

- Choose how you want CiviCRM to handle contacts:

- Update or create contacts (recommended if you are not sure if all contacts already exist).

- Match to existing contacts.

- Select a **deduplication rule** to help CiviCRM avoid creating duplicate contacts.

- (Optional) If your data includes soft credits, you can map those as well.

## Step 5: Review and import

- Preview the import to see how your data will look in CiviCRM.

- If everything looks correct, click **Import now**.

## Step 6: Check your results

- After the import, CiviCRM will show how many rows were successfully imported and if there were any errors.

- Click **See rows** to view details about errors or review specific records.

- You can click on a contribution’s ID number to view it directly in CiviCRM.

<!--
Source: https://docs.civicrm.org/user/en/latest/contributions/importing
-contributions/ -->

<!--
This page is a How
-to Guide because it provides step-by-step, goal-oriented instructions for a specific task (importing contributions), with minimal background or conceptual explanation. The level is Basic, as it is aimed at users new to this feature. If needed, more advanced troubleshooting or explanation of deduplication and soft credits could be split into separate Explanation or Reference pages for clarity. -->
