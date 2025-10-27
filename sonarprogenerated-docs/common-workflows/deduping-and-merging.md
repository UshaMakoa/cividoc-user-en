---
categories: Guide
level: Basic
summary: Learn how to find, review, and merge duplicate contacts in CiviCRM so your organisation’s contact list stays clean and accurate, using easy-to-follow steps and built-in tools.
section: Common workflows
---

# Deduping and merging contacts

## Why duplicate contacts happen

Duplicate contacts can appear in your CiviCRM database for several reasons:
- Someone creates a new contact without realising that person already exists.
- A supporter signs up online using a different email address or name.
- Contacts are imported from external lists that may already include duplicates.

Duplicates can cause confusion and make it harder to manage your relationships and communications.

## How CiviCRM helps you manage duplicates

CiviCRM provides tools to help you:
- **Find duplicate contacts** using flexible rules.
- **Review and merge duplicates** so all information is kept together.
- **Prevent duplicates** during imports and online sign-ups.

These tools work in two main ways:
- **Automatic checks (unsupervised):** CiviCRM tries to spot duplicates automatically when you import contacts or when people sign up online.
- **Manual checks (supervised):** You can search for duplicates and decide which records to merge.

## What are dedupe rules?

**Dedupe rules** tell CiviCRM how to decide if two contacts are duplicates. For example, a rule might say, “If the email address and first name match, treat these as duplicates.”

There are three types of dedupe rules:
- **Unsupervised rules:** Used for automatic checks during imports and online registrations. These are strict to avoid accidental merges.
- **Supervised rules:** Used when you add or edit contacts manually. These are broader, and you get to decide if the contacts should be merged.
- **General rules:** Extra rules you can set up for special cases.

You can adjust which fields are checked (like name, email, address) and how closely they must match.

## How to find and merge duplicate contacts

1. Go to **Contacts > Find and Merge Duplicate Contacts** in CiviCRM.
2. Choose which rule you want to use for finding duplicates (default rules are available for individuals, organisations, and households).
3. Decide if you want to search all contacts or just a specific group.
4. Review the list of possible duplicates. You can see details for each pair and choose which data to keep.
   - **Green rows:** Same data in both contacts.
   - **Red rows:** Different data—choose which value to keep.
   - **Yellow rows:** Data like tags or group memberships—by default, these are added together.
5. Click **Merge** to combine the contacts, or **Mark as not a duplicate** if they are not the same person.

## Merging multiple contacts at once

If you have a lot of duplicates:
- Select multiple pairs from the list.
- Use **Batch Merge All Duplicates** or **Batch Merge Selected Duplicates**.
- Batch merging will only merge contacts if there are no conflicting data (for example, if both have different phone numbers, they won’t be merged automatically).
- Always back up your database before running a batch merge, as merged contacts cannot be recovered unless you have database logging enabled.

## Using dedupe rules in stages

To clean up your database thoroughly:
1. Start with a strict unsupervised rule to find obvious duplicates and batch merge them.
2. Then use a broader supervised or general rule to find and review less obvious duplicates.

## Merging duplicates from search results

You can also merge contacts directly from search results:
- Select the duplicate contacts using the checkboxes.
- Choose **Merge Contacts** from the Actions menu.
- Follow the steps to combine the records.

# comment: Source: https://docs.civicrm.org/user/en/latest/common-workflows/deduping-and-merging/
# comment: Suggestion: This content is a problem-oriented Guide, as it helps users achieve the specific goal of managing duplicate contacts. It does not cover background theory (Explanation), exhaustive options (Reference), or provide a step-by-step onboarding lesson (Tutorial). The level is Basic, as it is intended for non-expert users learning to perform a practical task. The logical section is "Common workflows". If needed, detailed configuration options for dedupe rules could be split into a Reference page for advanced users.