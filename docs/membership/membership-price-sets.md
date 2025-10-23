---
categories:
  - Uncategorized
  - Explanation  
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
