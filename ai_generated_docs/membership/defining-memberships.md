---
categories: Explanation  
level: Basic  
summary:  This page explains membership types in CiviCRM
section: Membership
---

# Understanding membership types


Memberships in CiviCRM let you track who belongs to your organisation, when their membership starts and ends, and what benefits they receive.

A **membership type** is the template that defines how each kind of membership works. You’ll create one for every type of membership you offer — for example:

* *Individual Member (Annual)*

* *Student Member (Discounted)*

* *Organisation Member (Corporate)*

Each membership type describes:

* **Duration** – how long the membership lasts (for example, one year or lifetime).

* **Start and renewal rules** – whether it starts on the date someone joins or on a fixed date, and how renewals are calculated.

* **Who it applies to** – individual people, organisations, or related contacts.

* **Payment details** – whether it’s paid or free, and how payments are recorded.

Having clear membership types helps your organisation:

* Keep consistent records for reporting and renewals.

* Automate reminders and renewals.

* Offer different levels of membership without confusion.

Once these types are defined, you’ll use them in online sign-up forms, renewal pages, or when manually adding memberships in the system.

---

## **Page 2: Creating a membership type**

**Type:** Guide  
 **Level:** Basic

# **Creating a membership type**

This guide walks you through the steps to create a membership type in CiviCRM.  
 You don’t need any technical skills — just a clear idea of the kinds of memberships your organisation offers.

## **Before you start**

You’ll need:

* The **CiviMember** component enabled.

* A contact record for your organisation (this is the “Membership organisation”).

* A list of the membership types or categories you want to create.

## **Step 1: Go to the membership types screen**

1. From the main menu, choose **Administer → Membership Types**.

2. Click **Add Membership Type**.

## **Step 2: Name and describe your membership type**

Enter a clear name that your members will recognise — for example, *Individual (Annual)*.

Use the description field to record any internal notes, such as eligibility or benefits.

## **Step 3: Set the membership organisation**

Select your organisation from the list.  
 This ensures that memberships are linked to the correct organisational record in CiviCRM.

If you manage memberships for another group, select their organisation instead.

## **Step 4: Choose duration and renewal settings**

Define how long the membership lasts and what happens at renewal:

* **Duration unit** – for example, *1 year* or *6 months*.

* **Period type** – choose between *rolling* (starts on join date) or *fixed* (starts on a set calendar date).

* **Renewal option** – decide whether members can renew early and how the system calculates new end dates.

Tip: Rolling memberships are simpler to manage if members join throughout the year.

## **Step 5: Link to a financial type**

If the membership is paid, link it to a **financial type** such as *Membership Dues*.  
 This ensures payments are recorded correctly for accounting and reporting.

For free memberships, leave this blank.

## **Step 6: Save and check your setup**

Click **Save**.

Then, test your new membership type by adding a sample membership to a contact record.  
 Make sure:

* Start and end dates look correct.

* It appears under the **Memberships** tab.

* Renewal behaves as expected.

You can edit any of the settings later if you need to adjust them.

## **What’s next**

Once your basic membership types are set up, you can move on to more advanced options, such as linking memberships to relationships or automating renewals.

## **Page 3: Advanced membership settings**

**Type:** Guide  
 **Level:** Intermediate

# **Advanced membership settings**

This guide covers the optional settings you can use to make your membership system more powerful and flexible.  
 These settings are useful once you’re comfortable creating and managing basic membership types.

## **Linking memberships to relationships**

You can automatically grant membership to related contacts — for example, when an organisation joins and their staff members also become members.

This is done using **related memberships**.

Example:

* When *Organisation A* joins as a *Corporate Member*, all their employees automatically get an *Individual Member* record.

To set this up:

1. Edit your membership type.

2. In the **Relationship** section, choose the type of relationship that triggers related membership (for example, *Employee of*).

3. Choose which membership type the related contact receives.

This feature helps you manage complex membership structures without manual data entry.

## **Fixed-period memberships**

If your membership year runs on fixed dates (for example, January to December), use the *fixed period* option when setting the membership type.

CiviCRM will automatically align start and end dates for all members, regardless of when they join.

You can also specify whether new joiners get a *pro-rated* membership (for example, a shorter period for those joining late in the year).

## **Custom fields for memberships**

You can add **custom fields** to membership records to capture extra information — for instance:

* How members heard about your organisation.

* Which branch or region they belong to.

* Their preferred communication method.

To do this, create a new **Custom Field Set** for Memberships and add the fields you need.

## **Automating renewals and reminders**

You can use **CiviRules** or **Scheduled Reminders** to automate tasks like:

* Sending renewal reminder emails before membership expiry.

* Notifying staff when a member joins or lapses.

* Automatically updating membership status when payment is received.

Automation saves time and reduces errors, especially for organisations with many members.

## **Keeping things simple**

Not every organisation needs advanced options. If your membership structure is straightforward, start with a single rolling membership type and expand later as your needs grow.

## **What’s next**

Now that you understand both basic and advanced settings, you can:

* Create online membership sign-up forms.

* Set up renewal reminders.

* Generate membership reports for your board or funders.

