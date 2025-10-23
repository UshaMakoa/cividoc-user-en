---
categories:
  - Guide
level: Basic
summary: Step-by-step instructions for importing donation records into CiviCRM using the Civi Import extension, designed for non-profit users new to the process.
section: Contributions
---

# Importing donations into CiviCRM

## Before you begin

Make sure you have installed the Civi Import extension in your CiviCRM system. If you need help with this, see the Extensions section of the documentation.

## Prepare your donation data

Gather your donation records in a file—this could be a spreadsheet (.xlsx or .ods) or a CSV file. If you use a CSV, ensure it is saved with UTF-8 encoding if you have special characters (like accents or non-English letters). Check that numbers with decimals use the correct separator for your region to avoid errors during import.

## Start the import process

1. **Go to Contributions > Import Contributions** in your CiviCRM menu.
2. **Choose your data source**—select the type of file you are importing (CSV, spreadsheet, etc.).
3. **Select your file**—upload the file from your computer or network.
4. **Set import options**:
   - Choose the contact type (usually Individuals for donations).
   - Decide if you are adding new donations or updating existing ones.
   - Pick the date format used in your file.
   - If you have a saved field mapping, you can select it here.
5. **Map your fields**—match the columns in your file to the correct fields in CiviCRM. You can set default values for any empty fields. If you plan to do similar imports in the future, save your field mapping for reuse.
6. **Preview your import**—review the data before finalizing. Make sure everything looks correct.
7. **Complete the import**—click to import your donations. You’ll see a summary of successful imports and any errors.

## After importing

Check the results to confirm your donations were imported correctly. You can view details for each imported donation by clicking its ID. If there were errors, review them and correct your file if needed, then try the import again.

## Tips for success

- **Double-check your data file** for missing or incorrect information before importing.
- **Save your field mapping** if you’ll import similar files in the future—this saves time and reduces errors.
- **Reach out for help** if you run into problems—your CiviCRM community is here to support you.
