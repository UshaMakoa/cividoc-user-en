---
categories:
  - Guide
level: Basic
summary: Learn how to import your organisation’s contact and related data into CiviCRM using CSV files, with practical steps and tips for avoiding common problems.
section: Common workflows
---

# Importing data into CiviCRM

## Before you start importing

Most organisations have data in spreadsheets, older databases, or email address books. Manually entering lots of data into CiviCRM is slow and error-prone, so CiviCRM lets you import data in bulk, usually from a CSV (Comma Separated Values) file. You can also use imports to update existing records.

Before you begin, review your data and decide how it will map to CiviCRM fields. If you’re unsure, see the “Organising your data” and “Mapping your data” sections for background.

## Preparing your data for import

- You can import data from:

- CSV files (recommended for most users; easy to clean and review in spreadsheet software).

- Another database on your server (advanced; only for users with technical experience).

- Each column in your CSV file should match a field in CiviCRM. Make sure each piece of information has its own column.

- If your CSV uses semicolons (;) instead of commas, change the field separator in CiviCRM’s localisation settings (Administer > Configure > Global Settings > Localization).

- Always test your import with a small sample first. Check the results in CiviCRM to confirm everything looks right.

- Create a test contact with every attribute you use, import it, and verify that all data appears as expected.

- You can save your field mapping during import for future use. This is helpful if you regularly import similar files.

- If imports are slow or time out, split your data into smaller batches. If possible, increase memory and execution time settings on your server.

- You can add all imported contacts to a group or tag. If you need to assign different groups or tags to different contacts, import in batches where all contacts share the same group/tag, or use custom fields and batch actions after import.

- Make sure first and last names, city, and postal code are in separate columns. Use spreadsheet tools to split data if needed.

- Use standard country names as CiviCRM expects (e.g., 'United States', not 'USA').

- For multiple addresses, the first location in your CSV becomes the primary address. Arrange columns to ensure the right address is primary.

- For multi
-choice fields (checkboxes, radio buttons), you can use either the label or value for custom fields, but only the value for core fields. To import multiple values, separate them with commas.

- Use accepted date formats and select the same format during import.

- Set up name prefixes and suffixes in CiviCRM before importing (Administer > Option Lists).

- If you plan to import related data later (e.g., contributions, event participation), make sure each contact has a unique identifier (External ID). Map this during import to simplify linking related data.

## Required fields for contact imports

Include at least one of these fields in your CSV file:

- **Email** (used to match contacts)
- **External Identifier** (for updating existing contacts)
- **First Name**
- **Last Name**

For deduplication, you need at least one identifier field.

## Setting up your CSV file

Plan your columns based on the data you collect. You may need multiple CSV files and imports if your data is complex or includes related records.

If importing related data (e.g., event participation), ensure each contact has a unique identifier or a combination of First Name, Last Name, and Email.

## Running an import: step-by-step

### Step 1: Setup

- Choose your data source (CSV or database).

- Indicate if your file has column headers.

- Select a deduplication rule:

  - **Skip**: Ignore duplicates.
  - **Update**: Update existing records.
  - **Fill**: Fill in missing data only.
  - **No duplicate checking**: Import all records without checking for duplicates.

- Save your field mapping for future imports if needed.

### Step 2: Match the fields

- Match each column in your CSV to a CiviCRM field.

- You can skip columns you don’t want to import.

- If your spreadsheet layout changes, update and save your field mapping.

### Step 3: Preview

- Review the preview screen to check for errors and confirm field matches.

- Download and fix any errors before continuing.

- Decide if you want to add imported contacts to a group or tag (recommended for tracking imports).

### Step 4: Summary

- The summary screen shows successful imports, duplicates, and errors.

- Check your imported contacts in CiviCRM to ensure all data appears correctly.

## Importing related data

To import related data (e.g., relationships, activities, contributions), import each type as a separate CSV file. Use unique identifiers to link records.

For relationships, import each contact (e.g., child, father, mother) separately, using external identifiers to link them.

After importing, verify relationships in CiviCRM.

## Address standardisation

Standardising addresses (especially in the US) improves search accuracy. Enter addresses according to postal standards. See the Configuration section for details on address parsing.

## Importing activities

To insert new activities, your CSV must include:

- Activity Date

- Activity Type ID

- Target Contact ID (who the activity is for)

- Subject

To update existing activities, include:

- Activity ID

- Activity Date

- Activity Type ID

- Target Contact ID

- Subject

Import contacts first, then import activities.

## Importing contributions

To insert new contributions, your CSV must include:

- Fields to match or create the contact

- Financial Type

- Total Amount

To update existing contributions, include:

- Transaction ID, Invoice ID, or Payment ID

- Financial Type

- Total Amount

See the Contributions chapter for more details.

## Importing memberships

To insert new memberships, your CSV must include:

- Contact ID, External Identifier, or deduplication fields

- Membership Type

- Membership Start Date

To update existing memberships, include:

- Membership ID

- Membership Type

- Membership Start Date

See the Memberships chapter for more details.

## Importing participants

To insert new registrations, include:

- Contact ID, External Identifier, or deduplication fields

- Event ID

- Participant Status

To update registrations, include:

- Participant ID

- Event ID or Event Title

- Participant Status

## Importing tags

CiviCRM does not have a built
-in way to import tags or tag sets directly. You can:

- Split your CSV file by tag and import each subset separately.

- Use temporary custom fields, import tags into them, then batch tag contacts after import.

<!--
Source: https://docs.civicrm.org/some/page/
 -->

<!--
This page is a Guide because it provides actionable steps for a specific goal (importing data), with practical instructions and problem
-solving tips, but minimal background or theory. Level is Basic, as it is aimed at non-expert users. Section is Common workflows. The page could be split further into Reference pages for required fields and accepted formats, and Tutorials for a step-by-step example import. -->
