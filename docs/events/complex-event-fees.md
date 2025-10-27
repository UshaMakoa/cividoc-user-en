---
categories:
  - Guide  
level: Intermediate  
summary: This guide explains how to create and manage complex event fees in CiviCRM using price sets and discounts, helping non-profit users offer flexible pricing options for event registration.  
section: Events  
---

# Complex event fees

## Understanding complex event fees

When you create an event in CiviCRM, the basic fee setup lets registrants choose just one fee option. However, many events need more flexible pricing — for example, adding optional sessions, meals, or materials at extra cost. This guide shows you how to use **price sets** and **discounts** to create more detailed fee structures that fit your event’s needs.

## What are price sets?

Price sets break down event fees into smaller parts, each with its own price. This lets you offer optional extras, like a post-event dinner or training sessions, that attendees can add to their registration.

### Example

For a conference, you might have a price set that includes:

- Base registration fee  
- Optional pre-conference workshops  
- Meal options  
- Accommodation choices  

Each item can have its own price, and attendees select what they want.

## Creating a new price set

To create a price set:

1. Go to **CiviEvent > New Price Sets**.  
2. Enter a name for your price set.  
3. Under **Used For**, select **Event**.  
4. Choose the **financial type** (usually "Event Fee").  
5. Optionally, add help text to guide registrants.  
6. Check **Is this price set active**.  
7. Click **Save**.

After saving, you can add price fields to this set.

## Adding price fields to your price set

Each price field represents one part of the fee structure.

- Enter a **Field Label** (the name of the item).  
- Choose an **Input Field Type**:  
  - *Text/Numeric Quantity*: registrants enter how many units they want, multiplied by the unit price.  
  - *Select*: choose one option from a dropdown list.  
  - *Radio*: choose one option from multiple choices shown.  
  - *Checkbox*: select any number of options.  

- Set the **Price** for each option or unit.  
- If needed, enter a **Participant Count** to increase the event’s capacity based on this item (e.g., a table of 8 seats).  
- Decide whether to **display the price** next to the item.  
- Add **Field Help** text to explain the item.  
- Mark the item as **required** or optional.  
- Set **visibility** (public or admin only).  
- Activate the field and optionally set active dates to offer early bird or late registration pricing.

When done, click **Save** or **Save and New** to add more fields.

## Using price sets in your event

After creating your price set, assign it to your event on the **Fees** tab by selecting it in the **Price Set** field.

You can reuse price sets for multiple events, which is helpful for series or recurring events.

## Managing price sets

To edit or manage price sets:

- Go to **CiviEvent > Manage Price Sets** and select **Events** or **Administer**.

## Offering discounts

CiviCRM lets you create **early bird discounts** based on registration dates for simple fee structures.

To set up:

1. In your event’s fee section, check **Discounts by sign up date**.  
2. Create a discount set that duplicates your fee table.  
3. Edit the discount labels and prices to reflect the reduced rates.  
4. You can create multiple discount periods with different rates.

For more advanced discount options like discount codes or membership-based discounts, install the **CiviDiscount** extension.
