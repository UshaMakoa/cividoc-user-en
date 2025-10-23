---
categories:
  - Guide
level: Basic
summary: This guide helps you understand and manage duplicate contacts in CiviCRM by explaining how to find, merge, and prevent duplicates.
section: Common Workflows
---

# deduping and merging contacts in civicrm

## what is deduping?
Deduping is the process of identifying and merging duplicate contacts in your database. Duplicate contacts can occur due to various reasons such as user errors, import issues, or self-service sign-ups with different email addresses or names.

## civicrm features for deduping
CiviCRM offers several features to help manage duplicate contacts:

- **Automatic Scanning**: CiviCRM can automatically scan your database for duplicates using predefined rules.
- **Manual Merging**: You can manually select and merge duplicate contacts.
- **Dedupe Rules**: These rules help define what constitutes a duplicate contact based on fields like email address or name.

## using dedupe rules
Dedupe rules are categorized into **Unsupervised**, **Supervised**, and **General** rules:

- **Unsupervised Rules**: Used automatically when contacts are created through online registrations or imports.
- **Supervised Rules**: Used when contacts are added or edited via the user interface, alerting users to potential duplicates.
- **General Rules**: Additional criteria for scanning duplicates.

## configuring rules
To configure rules, you can specify up to five fields for comparison and set a threshold for determining duplicates. Each field has a weight that contributes to the overall match score.

## merging duplicate contacts
To merge duplicates:

1. **Find Duplicates**: Go to Contacts > Find and Merge Duplicate Contacts.
2. **Select Rule**: Choose a dedupe rule to scan for duplicates.
3. **Merge Contacts**: Select duplicates to merge, and choose which data to keep or discard.

## merging multiple contacts
You can also batch merge multiple duplicates at once. However, be cautious as this process is irreversible without database logging.

## multi-stage deduping process
For thorough deduping, use a multi-stage process:

1. Apply the **Unsupervised Rule** for initial batch merging.
2. Use **Supervised or General Rules** to catch remaining duplicates.

## merging from search results
You can also merge duplicates directly from search results for efficient database cleanup.
