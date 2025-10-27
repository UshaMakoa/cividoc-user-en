---
categories: Guide
level: Intermediate
summary: Learn how to set up and manage complex event fees in CiviCRM using price sets and discounts, so your organisation can offer flexible event registration options.
section: Events > Event Fees
---

# Complex event fees

## Using price sets for flexible event fees

Sometimes your event needs more than a simple, single fee—maybe you want to offer optional meals, workshops, or merchandise during registration. **Price sets** in CiviCRM let you break down event fees into smaller, customizable pieces, so participants can choose the options that suit them.

### Example

Imagine you’re running a conference. With a price set, you can let people select:
- Pre-conference training sessions (optional, extra cost)
- Meals (choose which ones to attend)
- Lodging (pick a room type)

## How to create a new price set

1. Go to **CiviEvent > New Price Sets** in your CiviCRM dashboard.
2. Enter a clear name for your price set.
3. Tick the **Used For > Event** box.
4. Choose the **financial type** (usually “Event Fee”).
5. (Optional) Add help text for users, before or after the form.
6. Tick **Is this price set active**.
7. Click **Save**.

Now you’re ready to add fields to your price set.

## How to add price fields

Each price field is an item or option you want to offer (like “Gala Dinner” or “Workshop A”).

- Enter a **Field Label** (the name people will see).
- Choose an **Input Field Type**:
  - **Text/Numeric Quantity**: Participants enter a number (e.g., number of tickets). The system multiplies this by your set price.
  - **Select**: A dropdown menu for one choice.
  - **Radio**: A list where only one option can be picked.
  - **Checkbox**: Multiple options can be chosen.

You can mix these types to build the fee structure you need.

- For **Text/Numeric Quantity**: Set the unit price.
- For **Select/Radio/Checkbox**: Enter a price for each option.
- If you want the price to show next to the item, tick **Display Amount?**.
- Use **Participant Count** if one selection counts for several people (e.g., a table for 8).
- Add help text, set if the field is required, and adjust visibility (public or admin-only).
- Set **Active dates** if you want this option available only for certain periods (e.g., early bird rates).

Click **Save** to finish, or **Save and New** to add another price field.

## Assigning your price set to an event

When creating or editing your event, go to the **Fees** tab and select your price set in the **Price Set** field.

**Tip:** It’s best to plan and create your price set before building your event, but you can always return and add it later.

## Reusing and managing price sets

Price sets can be reused for multiple events—perfect for recurring workshops or seminars.

To manage existing price sets:
- Go to **Manage Price Sets** and choose **Events**, or
- Navigate to **CiviEvent > Manage Price Sets > Administer**.

## Setting up discounts

You can offer **early bird discounts** or other date-based price reductions:
- In your event’s fee section, tick **Discounts by sign up date**.
- Create your discount set and add it to the fee table.
- Edit labels and fees for each discount period.

You can have several date-based discount sets (e.g., early bird, regular, last-minute).

For more advanced discounts (like codes or member-only rates), consider installing the **CiviDiscount extension**.

# comment: Source: https://docs.civicrm.org/user/en/latest/events/complex-event-fees/
# comment: This page is a Guide, as it gives step-by-step actions to achieve a specific goal (setting up complex event fees), not a linear learning experience (Tutorial), exhaustive options (Reference), or background/conceptual context (Explanation). The level is Intermediate because it assumes users are comfortable with basic event setup and want to add more advanced fee structures.