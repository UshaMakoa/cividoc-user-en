# Source: https://docs.civicrm.org/user/en/latest/contributions/online-contributions/

---
categories: Guide  
level: Basic  
summary: This guide helps non-profit users create and manage online contribution pages in CiviCRM, enabling supporters to donate easily through their website.  
section: Contributions  
---

# Online contributions

## Introduction

This guide explains how to create and manage online contribution pages in CiviCRM. These pages let visitors to your website make donations to your organization. While CiviContribute offers many advanced options, this guide focuses on simple, practical steps to get you started.

## Creating a simple contribution page

Before you begin, make sure you have a payment processor set up in CiviCRM.

1. Go to **Contributions > New Contribution Page**.  
2. Enter a clear **Title** for your page (e.g., "Donate to Our Cause").  
3. Select the appropriate **Financial Type** (like Donation).  
4. Click **Continue**.  
5. On the next page, check **Allow Other Amounts** if you want donors to enter any amount. You can also set minimum or maximum amounts.  
6. Click **Save and Done**.  
7. Follow your website’s instructions to display the contribution page (for example, adding a menu link or button).

This creates a basic page where donors can contribute, and receipts will be sent automatically by your payment processor.

## Adding a thank-you receipt from your organization

To send a thank-you email from your organization instead of just the payment processor:

1. Create your contribution page as above but click **Save** (not Save and Done) after step 5.  
2. Go to the **Receipt** tab.  
3. Enter a **Title** for the thank-you page.  
4. Check **Email Receipt to Contributor**.  
5. Enter the **From Email** address you want to appear on the receipt.  
6. Click **Save and Done**.

Donors will now receive a thank-you email from your organization after donating.

## Setting up contribution page details

When creating or editing a contribution page, you will see several tabs to customize:

### Amounts tab

- **Execute real-time monetary transactions** is checked by default for online payments. Uncheck if you want free signups or offline payments only.  
- Select the **Currency** and one or more **Payment Processors**.  
- Enable **Pay Later** if you want donors to pay offline (e.g., by check). Provide instructions for this option.  
- You can enter fixed contribution amounts or use a **Price Set** for more complex options.  
- Enable **Recurring Contributions** if your payment processor supports it and you want donors to give regularly.  
- Enable **Pledges** to allow donors to promise future payments.  
- Set the label for the contribution amount area (e.g., "Donation amount").  
- Allow donors to enter other amounts if you want flexibility.

### Memberships tab

If you want to link contributions to memberships, set this up here (see the Memberships guide for details).

### Profile tab

Profiles let you collect extra information from donors, like their interests or skills.

- You can add existing profiles or create new ones to appear on the contribution page.  
- Profiles can only include fields related to contacts or contributions.  
- If you include address fields in a profile at the top of the page, CiviCRM can show a checkbox to copy that address as the billing address.  
- Be careful when editing profiles used elsewhere, as changes affect all uses.

## Automatic contribution recording

CiviCRM automatically records donations from your contribution pages. If a donor’s contact exists, the contribution is added to their record; otherwise, a new contact is created. To reduce errors, you can adjust duplicate matching rules (see the Deduping and Merging guide).

## Customizing thank-you emails and alerts

- After creating your contribution page, customize the thank-you email under **Thank-you and Receipting**.  
- Enable **Email Receipt** so donors get immediate confirmation.  
- Add staff emails in **CC Receipt To** or **BCC Receipt To** fields to get notifications of new contributions.  
- Ensure these emails are valid to avoid bounce issues that could affect your contact records.

## Publicizing your contribution page

Make it easy for supporters to find your donation page:

- Add a **menu item** in Joomla!, Drupal, or WordPress linking to the contribution page.  
- In WordPress, embed the contribution page directly into a post or page using the CiviCRM plugin.  
- Use **"pretty" URLs** to create simple, memorable web addresses for your donation page by setting up URL redirects or aliases in your CMS.  
- Send personalized emails with links to the contribution page using CiviMail to encourage donations.

---

This guide covers the basics of setting up online contribution pages in CiviCRM. For more detailed options like pledges, personal campaign pages, or advanced profile settings, consider exploring related guides or tutorials.