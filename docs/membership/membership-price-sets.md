---
categories:
  - Guide
level: Basic
summary: Learn how to set up and use membership price sets in CiviCRM to let people join, renew, or select extra options for their memberships.
section: Membership > Membership price sets
---

# Membership price sets

## What are membership price sets?

Membership price sets let your organisation offer flexible membership options—such as signing up for multiple terms, joining more than one group in a single transaction, or adding non-membership items (like donations or club gear) during sign-up. You must define your membership types and financial types before creating a price set.

## When to use membership price sets

Use membership price sets when you want to:

- Allow people to sign up for several years at once.

- Let people join more than one organisation or chapter at the same time.

- Offer extras (like merchandise or donations) alongside membership sign
-up.

Membership price sets work for online join and renewal pages, and for new member sign-ups processed manually in CiviCRM’s back office. They cannot be used for manual renewals—each membership must be renewed individually.

## Creating a new price set

To create a price set:

- Go to **Memberships > New Price Set** or **Administer > CiviMember > New Price Set**.

- Enter a clear, descriptive name for your price set (this helps both public users and admin staff).

- Tick the **Membership** box.

- Set the **Default Financial Type** (this affects accounting—see the Contributions section for details).

- Add help text for users if needed.

- Make sure the price set is marked **Active**.

- Click **Save**.

After saving, you’ll be prompted to add your first price field.

## Adding price fields

For each price field:

- Enter a **Field Label** (shown to users).

- Choose an **Input Field Type**:

  - **Text/Numeric Quantity**: Users enter a quantity, and the total is calculated by multiplying by the unit price.
  - **Select**: Users pick one option from a dropdown.
  - **Radio**: Users pick one option from a list.
  - **Checkbox**: Users can pick multiple options.

- The **Financial Type** defaults to the one you set for the price set, but you can change it.

- Decide if you want to **Display Amount** next to the label.

- Set other options as needed (order, help text, required, active).

- Use **Active On** and **Expire On** dates to control when a price field is visible (for example, to manage price changes).

- Set **Visibility** to Public (for your website) or Admin (for back office use only).

## Examples

### Multiple membership terms

To let users sign up for more than one term:

- Use the **Radio** input type.

- Pick the relevant membership type.

- Adjust the number of terms and price as needed.

- Note: Multi
-term memberships set up this way cannot be auto-renewed.

### Membership in more than one organisation

To let users join more than one organisation:

- Use the **Select** input type.

- Pick the membership types for each organisation.

- Users can choose one option per field.

- Remember: Each person can only have one active membership per organisation.

### Non
-membership price fields

To offer extras (like gear or donations):

- Use **Checkbox** for multiple items (e.g., club gear).

- Leave membership type and number of terms blank for non
-membership items.

- Set label, amount, and financial type for each option.

- Use **Text/Numeric Quantity** for items like raffle tickets (users enter how many they want).

- For donations, set the unit price to 1 and allow users to enter any amount.

Always test your price set thoroughly before using it on your live site to make sure everything works as expected.

<!--
Source: https://docs.civicrm.org/some/page/
 -->

<!--
Suggestion: This page is a Guide because it focuses on how to set up and use membership price sets to solve specific practical problems (not a step
-by-step tutorial, not reference, and not conceptual explanation). It is Basic level, suitable for non-experts. If more detailed step-by-step instructions or background were needed, these could be split into separate Tutorial or Explanation pages. -->
