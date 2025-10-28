---
categories:
  - Guide
level: Basic
summary: Learn how to manage membership renewals in CiviCRM, including sending reminders, handling automatic and manual renewals, and updating multiple memberships.
section: Membership
---

# Renewing memberships

## Understanding membership renewals

When a member’s end date is approaching and they want to continue, you should **renew** their existing membership instead of creating a new one. This keeps their membership history and financial records together.

Each membership has three main dates:
- **Member since**: The original join date. This does not change when renewing.
- **Start date** and **End date**: These may change depending on the member’s current status.

If you renew while the member’s status is still “active” (as set in your Membership Status Rules), the **start date stays the same** and the **end date is extended**. If you renew after the membership has lapsed, the **start date becomes the renewal date** and the **end date is set based on the new start date**.

Each renewal can also record a payment, linking the financial transaction to the membership record.

## Changing membership type during renewal (up-sell)

If a member wants to change to a different membership type within the same organisation while renewing, CiviCRM will update their existing membership to the new type. Their join date and payment history are kept. The new end date will be based on the new membership type’s duration.

If you want to prevent this (for example, to keep memberships separate), set up the new membership type under a different organisation in CiviCRM.

## Reminding members to renew

You can remind members about upcoming renewals by email or post.

### Sending email reminders

Use **Scheduled Reminders** (Administer > Communications > Schedule Reminders) to automatically email members before their membership expires. This is especially useful for memberships that end at different times.

Tips:

- Customise your reminder emails for different member types and timing.

- Include a **checksum token link** in your email so members can renew online easily—their information will be pre
-filled.

- Test your reminder templates to make sure they work for all your membership types.

- By default, reminders go to everyone, even those who opted out of bulk emails, unless you exclude them.

- Exclude members who have chosen automatic renewal from these reminders.

### Sending postal reminders

You can also send letters to members who are due to renew, especially those without email addresses or who opted out of email. Use CiviCRM’s postal mail features to generate these letters.

## Automatically renewed memberships

If a member has chosen automatic renewal, CiviCRM will process their payment automatically on the renewal date, update their membership end date, and send a thank
-you and receipt. See the relevant setup guides for enabling auto-renewal.

## Online renewals

CiviCRM uses the same web page for new memberships and renewals. Members who are **logged in** will see the renewal page. If they are not logged in, they will see the sign-up page. If CiviCRM matches their contact details, it will renew their membership; otherwise, it will create a new record (which can cause duplicates).

To reduce duplicates:

- Always include a checksum token in your renewal reminder emails.

- Remind members to log in before renewing.

## Setting up the default online renewal page

To allow all members to renew online (even those entered manually), set a **Default Online Membership Renewal Page**:

1. Create a membership page that includes all your membership types (use a price set if needed).

2. Go to Administer > CiviMember > CiviMember Component Settings.

3. Set the Default Online Membership Renewal Page to your membership page.

A “renew” link will then appear on the member’s Contact Dashboard.

## Manually renewing a membership for one member

1. Go to the member’s contact summary page.

2. Click the **Memberships** tab.

3. Click **MORE** next to the membership record.

4. Choose **Renew** (for cash, cheque, or EFT) or **Renew
-Credit Card** (for online payment).

## Updating multiple memberships at once

To update several memberships (for example, after a bulk payment):

1. Create a **Profile** with the membership fields you want to update.

2. Find the memberships: go to Memberships > Find Members, enter your criteria, and click Search.

3. Select the memberships in the results.

4. From the actions dropdown, choose **Update multiple memberships** and click Go.

5. Select your profile and click Continue.

6. Update the fields as needed. Use the “auto-copy” icon to fill down values.

7. Click **Update Memberships** when finished.

<!--
Source: https://docs.civicrm.org/user/en/latest/membership/renewals/
 -->

<!--
This page is a Guide because it provides step
-by-step instructions for common membership renewal tasks and addresses specific problems (how to remind, renew, and update memberships). It is not a Tutorial (no first-time onboarding flow), Reference (not exhaustive or systematic), or Explanation (no deep background or theory). Level is Basic, as it assumes minimal prior knowledge and is aimed at everyday users. -->
