# Source: https://docs.civicrm.org/user/en/latest/organising-your-data/mapping-your-data/

---
categories: Tutorial
level: Basic
summary: Follow these steps to map a simple contact list from your old system into CiviCRM, using default fields and avoiding common pitfalls.
section: Organising your data
---

# Tutorial: Mapping a contact list to CiviCRM

## Before you begin

Gather your current contact list (Excel, CSV, or another format). Identify which columns hold names, emails, phone numbers, and addresses.

## Step 1: Review CiviCRM’s default fields

Open CiviCRM and look at the “Add Contact” form. Note the fields for name, email, phone, and address. These are where most of your data will go.

## Step 2: Match your columns to CiviCRM fields

Create a table to match each column in your old list to a CiviCRM field. For example:

| Your column name | CiviCRM field      |
|------------------|--------------------|
| First Name       | First Name         |
| Email            | Email              |
| Phone            | Phone              |
| Address          | Street Address     |

## Step 3: Handle special cases

- **Organizations and households**: If your list includes companies or families, decide which contacts are Individuals, Organizations, or Households.
- **Custom data**: If you have unique information (like “Volunteer interest”), note whether it needs a custom field or fits an existing CiviCRM feature.

## Step 4: Prepare your data file

Clean your data: remove duplicates, fix formatting, and fill in missing values where possible. Save your file as a CSV for easy import.

## Step 5: Import a test batch

Import a small sample of contacts to check that everything maps correctly. Review the imported records and adjust your mapping if needed.

## Step 6: Import the full list

Once your test looks good, import the rest of your contacts. Celebrate—you’ve taken a big step toward better data management!

---