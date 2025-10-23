---
categories: Explanation  
level: Basic  
summary:  This page explains  membership price set - a flexible tool in CiviCRM that allows you to create forms with multiple membership and pricing options.
section: Membership
---

# Understanding membership price sets


A **membership price set** is a flexible tool in CiviCRM that allows you to create forms with multiple membership and pricing options. It helps when your membership structure is more complex than a single type and fee.

Instead of one fixed membership level, a price set can include different membership types, durations, and optional extras, all on one form.

You might use a price set when you want to:

* Offer different membership levels (for example, Standard, Concession, or Corporate)

* Allow multi-year memberships

* Combine membership sign-up with optional extras such as merchandise or donations

* Let members join more than one branch or chapter at once

Price sets are most useful when you want to give members choice and flexibility. If you only have one membership type and fee, you can simply use the standard membership setup without a price set.

Before you start using price sets, make sure your membership types and financial types are already defined.

# **Page 2: Creating a membership price set**

**Type:** Guide  
 **Level:** Intermediate

## **Creating a membership price set**

This guide walks you through how to create a price set in CiviCRM and prepare it for use in your membership forms.

### **Step 1: Create a new price set**

1. Go to **Administer → CiviMember → New Price Set**.

2. Give your price set a clear name, such as “Membership levels and extras”.

3. In the **Used For** field, select **Memberships**.

4. Choose a **Default Financial Type** — usually “Membership Dues”.

5. Add help text to explain the form to users if needed.

6. Tick **Active** to make the price set available.

7. Click **Save**.

You’ll now add your membership and other options as price fields.

### **Step 2: Add price fields**

Each **price field** represents one choice or item on your form, such as a membership option or an add-on.

1. Click **Add Price Field**.

2. Enter a **Field Label** that clearly describes the option (for example, “Annual membership – £50”).

3. Choose an **Input Field Type**:

   * **Radio buttons** – one choice from several options.

   * **Checkboxes** – multiple selections allowed.

   * **Select** – a drop-down menu.

4. Choose the **Financial Type**.

5. Tick **Display Amount** if you want the price to appear beside the label.

6. For membership items, choose the relevant **Membership Type**.

7. If you want to offer multi-year membership, set the **Number of Terms** (for example, “2” for a two-year membership).

8. Add help text and ensure the field is active.

9. Click **Save**.

Repeat these steps for each option you want to offer.

Tip: Keep your options simple and clear. Too many choices can make your form harder to use.

---

# **Page 3: Advanced price set options**

**Type:** Guide  
 **Level:** Intermediate

## **Advanced price set options**

Once you understand the basics of creating price sets, you can use these additional options to make your forms more flexible.

### **Adding non-membership options**

You can include optional extras in the same price set, such as:

* Donations

* Merchandise (for example, T-shirts or badges)

* Event tickets

* Services like training or certification

To do this, create a price field but leave the **Membership Type** blank. The item will appear on the form but won’t create a membership record.

This allows members to join and purchase extras in one transaction.

### **Using multi-year memberships**

To let people pay for more than one membership period at once:

1. In the price field, select the **Membership Type**.

2. Set the **Number of Terms** to reflect how many years the membership should cover.

CiviCRM will calculate the start and end dates automatically based on your membership type settings.

Note that auto-renew is not always available when multi-year options are used, so test carefully.

### **Setting visibility and availability**

Each price field can be:

* **Public**, shown on online forms

* **Admin only**, used by staff for back-office entry

You can also set start and end dates for when an option appears, which is useful for time-limited offers or seasonal pricing.

### **Combining with other components**

A single price set can be reused for contribution, event, or membership forms. However, be cautious when editing shared price sets — changing them may affect other forms that use the same configuration.

---

# **Page 4: Testing and maintaining price sets**

**Type:** Guide  
 **Level:** Intermediate

## **Testing and maintaining price sets**

After creating your price set, it’s important to test and maintain it so that it works reliably and records data correctly.

### **Assigning a price set to a form**

To use a price set for an online membership page:

1. Go to **Contributions → Manage Contribution Pages**.

2. Open your membership page and go to the **Memberships** tab.

3. Select **Use a Price Set** and choose the one you created.

4. Save the page.

Now visitors will see your membership and add-on options when they sign up.

### **Testing your setup**

Before publishing, test the form carefully:

* Try every combination of options and check the total amounts.

* Verify that membership records are created correctly.

* Check that payments link to the right financial types.

* Test optional extras to confirm they appear in the contact’s contribution history.

* If you use recurring payments, test how renewals behave.

It’s safest to test using a sandbox or staging site so no real payments are taken.

### **Editing existing price sets**

You can manage and edit your price sets under **Administer → CiviMember → Price Sets**.

Be careful when editing price sets already used on live forms — changing or removing fields may affect existing records and reports. If you need major changes, create a new price set instead.

### **Best practices**

* Use clear, concise labels for all options.

* Group related items together to make the form easy to follow.

* Avoid overloading one form with too many options.

* Keep a record of how each field maps to financial or membership data.

* Review your reports regularly to make sure payments and memberships align.

### **When not to use price sets**

A price set may not be necessary if:

* You only have one membership type and fee.

* You rely on auto-renewal for most members.

* You prefer to keep your forms as short as possible.

### **Keeping your system tidy**

Review your price sets periodically. Remove or disable old or unused ones to keep your system clean and easy to manage.

