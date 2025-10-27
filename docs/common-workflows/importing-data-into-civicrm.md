---
categories:
  - Guide  
level: Basic  
summary: This guide explains how non-expert users at non-profits can import data into CiviCRM using CSV files, covering preparation, required fields, the import steps, and handling related data.  
section: Importing data  
---

# Importing data into CiviCRM

## Introduction  
Many non-profits have data stored outside CiviCRM, such as spreadsheets or other databases. Manually entering this data can be time-consuming, so CiviCRM provides tools to import data in bulk, usually from CSV files. This guide will help you understand how to prepare your data and complete an import successfully.

## Before you start: planning your import  
- Understand your existing data and how it will map to fields in CiviCRM.  
- Read about organizing your data and mapping it into CiviCRM to avoid issues.  
- Always do a test import with a small set of records first to check everything works as expected.  
- Consider creating a test contact with all possible data fields filled to verify import results.  
- If you will import similar files regularly, save your field mappings during import to reuse later.  
- If imports take too long or time out, split your data into smaller batches or adjust server settings if possible.  
- Assign groups or tags carefully since all contacts in one import share the same groups/tags. Use batches or custom fields if you need different tags per contact.

## Preparing your CSV file  
- Use separate columns for each piece of information (e.g., first and last names, city and postal code).  
- Make sure country names match CiviCRM’s naming conventions (e.g., “United States”, not “USA”).  
- If importing multiple addresses, the first location becomes the primary address. Arrange columns accordingly.  
- For multi-choice fields (checkboxes, radio buttons), use either the label or the value consistently. Separate multiple values with commas.  
- Use accepted date formats and select the matching format during import.  
- Ensure any prefixes or suffixes used are set up in CiviCRM’s administration options.  
- If importing related data later (like contributions or event participation), include unique IDs in your contact records mapped to CiviCRM’s External ID field to link data correctly.

## Required fields for contact imports  
At minimum, your CSV must include one of these to identify contacts:  
- Email (used for matching contacts)  
- External Identifier (for updating existing contacts)  
- First Name and Last Name (at least one of these is required if no email or external ID)

## The import process  
Importing data has four main steps:

### Step 1: Setup  
- Choose your data source (CSV file or SQL query).  
- Indicate if your file’s first row contains column headers.  
- Select a deduplication rule to handle duplicates: skip, update, fill missing fields, or no duplicate checking.  
- Save your field mapping if you want to reuse it later.

### Step 2: Match the fields  
- Match each column from your CSV to a CiviCRM field.  
- Use the dropdown menus to select appropriate fields or choose “- do not import -” to skip columns.  
- If you have a saved mapping, it will auto-fill here but can be adjusted.  
- Add new columns after previously mapped ones to reuse saved mappings efficiently.

### Step 3: Preview  
- Review a preview of your import data and check for errors.  
- Download and fix any errors before proceeding.  
- Choose to add imported contacts to an existing or new group or tag for easy management.

### Step 4: Summary  
- Review the import results, including successful records, duplicates, and errors.  
- Verify imported data by searching for new contacts and checking their details.

## Importing related data  
- Import related data (like relationships, activities, contributions, memberships) in separate CSV files.  
- Use unique external IDs to link related records correctly.  
- Import contacts first, then import related data referencing those contacts.  
- For example, import a child contact with an external ID, then import parents linked to that child using the child’s external ID.

## Address standardisation  
- Standardising addresses (e.g., following USPS standards in the US) improves search accuracy.  
- When entering or importing addresses, use consistent formats for street, apartment, city, and postal codes.

## Importing specific data types  
- **Activities:** Require fields like Activity Date, Activity Type ID, Target Contact ID, and Subject.  
- **Contributions:** Require fields to identify contacts and financial details; with the Civi-Import extension, you can create or update contacts and soft credits in one import.  
- **Memberships:** Require contact identifiers, membership type, and start date.  
- **Participants (event registrations):** Require contact identifiers, event ID, and participant status.  
- **Tags:** Cannot be imported directly; assign tags by importing contacts in batches or using custom fields and then tagging contacts afterward.
