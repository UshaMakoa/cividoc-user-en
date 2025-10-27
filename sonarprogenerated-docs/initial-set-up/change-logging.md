---
categories: Explanation
level: Basic
summary: Learn how CiviCRM tracks changes to your data and when you might need detailed logging for your organisation.
section: Initial set up
---

# Understanding logging in CiviCRM

CiviCRM automatically keeps track of changes made to your data. This helps you see who updated information and when it happened. You have two options for logging: basic change tracking (which is always on) and detailed logging (which you can turn on if needed).

## Basic change tracking

Every contact record in CiviCRM includes a change log tab. This shows you a simple history of when someone added or edited that contact's information. You'll see who made the change and the date and time it happened.

This basic tracking works well for many organisations. However, it doesn't show you exactly what information was changed—only that a change occurred.

## Detailed logging

When you enable detailed logging, CiviCRM records much more information about every change made to your data. For each update, the system captures:

- The original value before the change
- The new value after the change
- When the change happened
- Who made the change

Detailed logging covers nearly everything in your CiviCRM system, including contacts, memberships, events, contributions, and even your configuration settings like activity types and contribution types.

### What detailed logging looks like

When you view a contact's change log with detailed logging enabled, you'll see an "update" link next to each change. Clicking this link reveals the specific fields that were modified and shows both the old and new values side by side.

### Undoing changes

One major advantage of detailed logging is the ability to reverse changes. If someone accidentally updates information or if unwanted changes occur through your website, you can revert the data back to its previous state. CiviCRM provides a revert button for many types of changes, making this process straightforward.

For some changes, the revert button isn't available through the interface, but the information is still recorded. In these cases, you'll need help from your system administrator or someone familiar with CiviCRM's database to restore the data.

### Things to consider

Detailed logging records a substantial amount of information over time, which means your database will grow larger than it would without logging. There's also a small impact on your database performance. This is why CiviCRM doesn't turn on detailed logging automatically—you can decide whether the benefits outweigh these considerations for your organisation.

## Alternative ways to track changes

Before enabling detailed logging, consider whether other CiviCRM features already meet your tracking needs.

### Using activities as a log

Activities in CiviCRM naturally create a timeline of interactions with your contacts. Since each activity includes a date, the activity tab on a contact record becomes a chronological history of that relationship. You don't need to create an activity for every small data change, but for significant events (phone calls, meetings, important updates), activities provide a meaningful record of what happened and when.

For many organisations, this activity-based approach to tracking changes provides enough detail without needing to turn on detailed logging.

### Membership history

Membership records in CiviCRM automatically build their own history over time. Each membership shows all associated contributions, renewals, and upgrades. This built-in tracking often gives you the historical information you need about member relationships without requiring detailed logging across your entire system.

## Deciding what's right for your organisation

**You might not need detailed logging if:**
- Your activity records provide enough historical context
- Membership histories cover your tracking needs
- You have a small team with clear responsibilities
- You trust your website forms and processes

**You should consider detailed logging if:**
- You need to track exactly what changed in contact records
- Multiple people update the same data
- You want the ability to undo accidental changes
- You need detailed audit trails for compliance or reporting
- Public forms on your website allow data changes

Remember that you can always enable detailed logging later if your needs change. Many organisations start with basic tracking and add detailed logging as they grow.

# comment: Source: https://docs.civicrm.org/user/en/latest/initial-set-up/logging/
# comment: This page is primarily Explanation because it helps users understand the concept of logging, why it exists, when they might need it, and how it relates to other features. It provides context about trade-offs (database size, performance) and discusses alternatives (activities, membership logs) to help users make an informed decision. While it mentions that detailed logging can be enabled and describes what users will see, it doesn't provide step-by-step instructions for turning it on or configuring it.
```