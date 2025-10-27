---
categories: Guide
level: Basic
summary: Learn how to manually add, update, and manage memberships for your contacts in CiviCRM, including entering payments and handling gift memberships.
section: Membership > Managing memberships
---

# Manually entering memberships

## When to enter memberships manually

While CiviCRM allows people to sign up for memberships themselves through your website, there are many times when your staff or volunteers will need to add or update memberships directly. For example, you might need to:

- Add a new member who joined by mail or in person
- Record a gift membership paid for by someone else
- Enter a batch of memberships collected at an event
- Import a list of members from another system

This guide shows you the main ways you can manually enter and manage memberships in CiviCRM.

## Permissions needed

To add or edit memberships, your user account must have the right permissions:

- **Find and view memberships:** Needs “access CiviMember”, “view contributions” (if payments involved), and “view contact” permissions.
- **Create or edit memberships:** Needs “edit memberships”, “edit contributions” (if payments involved), and “edit contact” permissions.

Ask your CiviCRM administrator if you are not sure you have these permissions.

## Adding a new membership

You can add a membership in two main ways:

### 1. From a contact’s record

1. Find the contact in CiviCRM.
2. Click the **Memberships** tab.
3. Click **Add Membership**.
4. Fill in the membership details:
   - **Membership organization and type:** Choose the correct organization and membership type.
   - **Number of terms:** Enter the number of membership periods (not shown if using price sets).
   - **Source:** Leave blank to let CiviCRM fill in details automatically.
   - **Campaign:** Select if this membership is part of a campaign.
   - **Member since, start date, end date:** These are auto-filled but can be changed if needed.
   - **Auto-renew:** Only shown if the membership type supports auto-renewal and you are using credit card payments.
   - **Status override:** Use only if you need to set a custom status (this stops automatic status updates).

5. To record a payment, check **Record Membership Payment?** and fill in payment details:
   - **Record payment from a different contact?** (for gift memberships)
   - **Financial type, amount, received date, paid by, check number, transaction ID, payment status**

6. To send a confirmation, check **Send Confirmation and Receipt?** and choose the sender and add a message if you wish.

7. Save the membership.

### 2. From the Memberships menu

1. Go to **Memberships > New Membership**.
2. Select an existing contact or create a new one.
3. Fill out the membership form as above.

**Note:** Credit card payments can only be processed when adding a membership from an existing contact’s record.

## Creating auto-renewing memberships

If you want a membership to renew automatically:

1. Go to the contact’s summary.
2. Click the **Memberships** tab and then **Submit Credit Card Membership**.
3. Select a membership type that supports auto-renew.
4. Check **Membership renewed automatically**.
5. Complete the payment details.

If successful, CiviCRM will automatically renew the membership each period until cancelled. The member will receive a receipt with a link to cancel auto-renewal.

## Recording gift memberships

To record a membership paid for by someone else:

- When adding the membership, check **Record Payment from a Different Contact?**
- Select the person who is paying (the gifter) or create a new contact.
- The payment will be recorded for the gifter, and the membership for the recipient.
- The receipt will go to the gifter. You will need to notify the recipient separately.

## Entering batches of memberships

If you have a stack of membership forms or payments to enter at once:

1. Use the **Batch Data Entry** feature in the Memberships menu.
2. Enter information for multiple members in a grid-style form.
3. Use the copy feature to speed up data entry for similar memberships.
4. You can create new contacts directly in the batch entry screen.
5. The fields available depend on your CiviCRM profiles; these can be customized if you need to collect other information.

## Importing memberships

To import a large list of memberships from another system:

1. Make sure all contacts already exist in CiviCRM. If not, import contacts first, including an External ID.
2. Prepare a CSV file with at least **Membership Type** and **Start Date** for each membership.
3. Go to **Memberships > Import Memberships**.
4. Upload your CSV file and match your columns to CiviCRM fields.
5. Preview the import. Fix any errors as needed.
6. Complete the import.

You must import different contact types and new memberships/renewals separately.

# comment: Source: https://docs.civicrm.org/user/en/latest/membership/manual-entry-of-memberships/
# comment: This page is a Guide because it provides step-by-step instructions for specific tasks (manual entry, batch entry, import), not general learning or background. The level is Basic because it is aimed at non-experts performing common admin tasks. If needed, the batch entry and import sections could be split into their own short guides for clarity.