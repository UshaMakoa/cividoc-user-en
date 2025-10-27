---
categories: Guide
level: Basic
summary: Learn how to export your contacts from CiviCRM into a spreadsheet or other application, step by step, with tips for choosing the right fields for your needs.
section: Common workflows
---

# Exporting your contacts

Exporting contacts from CiviCRM allows you to save your contact information in a file format (CSV) that you can open in a spreadsheet program, import into other databases, or use for mail merges and labels.

## Steps to export your contacts

1. **Search for the contacts you want to export**

   Use any search tool in CiviCRM—such as Quick Search, Find Contacts, Advanced Search, Search Builder, or a custom search—to find the contacts you need.

2. **Select the contacts**

   After your search, select the contacts you want to export. You can select all results or choose specific contacts using the checkboxes next to each name.

3. **Choose the export action**

   Find the “- actions -” dropdown menu above your search results. Select **Export Contacts** from the list.

4. **Choose what to export**

   You can:
   - Export a set of standard “primary fields” (basic contact details, primary email, phone, and address).
   - Select specific fields to export, including custom fields or additional contact details.
   - Use a saved export mapping if you have one, to reuse a set of fields you’ve chosen before.

   If you’re preparing data for mailing labels, you can choose to export one record per household or per address, and set how names and greetings appear.

   You can also:
   - Exclude contacts with “do not mail” privacy settings, no street address, or who are marked as deceased.
   - Add contacts from another group to your export.

5. **Continue and confirm fields**

   Click **Continue**. If you chose the primary fields, your download will start right away. If you chose to pick your own fields or use a mapping, you’ll see a screen to review and adjust your field selections. You can save your choices as a new mapping for future use.

6. **Download your file**

   When you’re ready, click **Export**. Your contacts will be downloaded as a CSV file, which you can open in Excel or another spreadsheet program.

   By default, fields are separated by commas. If you need a different separator (for example, for use in another country), you can change this in **Administer > Localization > Languages, Currency, Locations** under “Import/Export Field Separator”.

# comment: Source: https://docs.civicrm.org/user/en/latest/common-workflows/exporting-your-contacts/
# comment: Suggestion: The page is a classic "How-to Guide" in Diátaxis terms: it is task-oriented, provides clear steps, and is focused on helping users achieve a specific outcome (exporting contacts). No background or technical reference is included. The appropriate level is Basic, as it is intended for non-experts and covers a common, essential task. The section is "Common workflows". The summary is tailored for non-expert users. If needed, a separate Reference page could list all export options and field definitions, but this page is best as a Guide.