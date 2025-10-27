---
categories: Reference
level: Basic
summary: Learn how to set an expiration date for saved searches in CiviCRM so your list stays tidy without deleting searches.
section: Search Kit
---

# Expiration date for searches

## What is the expiration date?

An **expiration date** for a saved search in CiviCRM is a date you can set so that the search is automatically hidden from your list after that date. This helps keep your list of saved searches manageable, especially if some searches are only useful for a limited time.

## How does it work?

- You set an expiration date when creating or editing a saved search.
- After the expiration date passes, the search will no longer appear in your list of saved searches.
- The search is **not deleted**—it is just hidden from view.
- If you need to see or restore a search after it has expired, you must remove the expiration date using the API explorer or a direct SQL statement.

## Important notes

- Expired searches are hidden, not removed from the database.
- There is no built-in button in the user interface to restore expired searches; this requires technical access.

# comment: Source: https://docs.civicrm.org/some/page/
# comment: This page is systematic and factual, describing what the expiration date is, how it behaves, and its limitations, without procedural or motivational text. This fits the “Reference” category in Diátaxis. The content is basic, as it introduces a simple feature for non-expert users. If more step-by-step instructions for setting or restoring expiration dates were needed, those would belong in a Guide or Tutorial.