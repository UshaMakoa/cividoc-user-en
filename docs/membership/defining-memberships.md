---
categories:
  - Reference
level: Basic
summary: Learn what membership types and status rules are in CiviCRM, how to define them, and what each option means for managing your organisation’s members.
section: Membership > Membership setup
---

# Defining memberships

## What are membership types?

**Membership types** let you define the different kinds of memberships your organisation offers, such as “regular”, “student”, or “honorary”. You can create as many types as you need, depending on how simple or complex your membership structure is.

- For simple needs, one membership type may be enough.

- For more complex needs, create separate types for each category (e.g., different levels, benefits, or publications).

If your membership structure is very complex, you may want to use *membership price sets* (an advanced feature) for extra flexibility.

## How to create a membership type

To add a new membership type:

1. Go to **Administer > CiviMember > Membership Types**.

2. Click **Add Membership Type**.

You will need to fill in several options:

- **Name**: The name shown to both staff and members. Choose a clear, appropriate name.
- **Description**: Optional. Add details about this membership type if helpful.
- **Membership organisation**: If you manage memberships for more than one organisation, select which one this type belongs to. For most, just choose your own organisation.
- **Minimum fee**: Enter the minimum payment for this membership. Use 0 for free memberships.
- **Financial type**: Choose how payments are tracked in your accounts (default is “Member Dues”).
- **Auto-renew**: Enable if you want memberships to renew automatically (only works with some payment processors and for memberships of one year or less).
- **Duration**: Set how long the membership lasts (days, months, or years).
- **Period type**: Choose “rolling” (starts on sign-up date) or “fixed” (starts on a set date each year or month).
- **Relationship type**: Allows memberships to be inherited (e.g., employees of a member company).
- **Visibility**: Set to “Public” for online sign-up, or “Admin” for admin-only types.
- **Order**: Controls where this type appears in lists.
- **Enabled**: Untick to hide this type without deleting it.

## Membership status rules

Memberships move through different **statuses** during their life cycle. Statuses help track whether someone is a current member, has lapsed, or is in another state.

Common statuses include:

- **Pending**: Member has applied but not paid.
- **New**: Recently joined or payment just received.
- **Current**: Active member.
- **Grace**: Membership expired but still within a grace period.
- **Expired**: Membership fully lapsed.
- **Cancelled**: Manually cancelled by an admin.
- **Deceased**: Member has passed away (automatically set).

You can view and edit these rules at **Administer > CiviMember > Membership Status Rules**. Most statuses can be customised (except Pending and Deceased).

Each status is defined by when it starts and ends, based on membership dates (join, start, or end date). You can also specify if a status means someone is counted as a member.

If you need to override the status for a particular membership, use the “membership override” option on that record.

## Keeping membership statuses updated

CiviCRM automatically updates membership statuses when memberships are added or renewed, according to your rules. If statuses are not updating, check that the **Update Membership Statuses** scheduled job is enabled and runs at least daily. Ask your system administrator if you need help.

## Collecting extra information about members

You can create **custom fields** to collect more information about your members. Custom fields can be linked to all memberships or just certain types. If you need different information for different membership types, set up separate custom field sets for each one.

<!--
Source: https://docs.civicrm.org/user/en/latest/membership/defining
-memberships/ -->

<!--
This page is best categorised as Reference, as it systematically explains all options for defining membership types and status rules, without focusing on step
-by-step tasks or conceptual background. It is suitable for users learning what each setting means, rather than how or why to use them. If desired, step-by-step creation of a membership type could be split off as a Tutorial, and the explanation of status logic as an Explanation. -->
