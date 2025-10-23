---
categories: Guide  
level: Basic  
summary:  This guide explains how to set up an online membership sign-up form on your website.
section: Membership
---

# Online membership sign up


This guide explains how to set up an online membership sign-up form on your website. You’ll learn how to build a page where visitors can join or renew their membership, pay (if required), and have everything recorded automatically in CiviCRM.

It’s aimed at non-technical users working in charities, community groups or other non-profits, so you don’t need to be a tech expert to follow these steps.

## **About membership sign up pages**

In CiviCRM, a membership sign-up page is built using a contribution page. Because joining a membership is much like making a contribution (people pay, supply details, and you record data), using the contribution page gives you access to lots of useful features.

Even if your membership is free, you still use a contribution page (just with no payment element).

## **The Title tab**

* This is the first step when creating your membership sign-up page.

* You’ll give your page a clear title (for example, “Join us as a member”).

* You’ll choose which financial type will record the payment or membership fee.

* You can add an introductory message that appears on the web form; you can include images or simple formatting to make it inviting.

## **Organisational memberships**

If your organisation offers memberships for other organisations (instead of just individuals), you can enable “Organisations sign up” in the Title tab.

* Tick the option for “Become a member on behalf of an organisation”.

* Choose a profile that collects organisation details (legal name, contact person, etc).

* Decide if this is required or optional for the person filling in the form.

## **The Amounts tab**

On the Amounts tab you:

* Choose your payment processor(s) so people can pay online.

* Set whether the form only collects membership fees, or also extra donations.

* Note: Membership fees themselves are not configured here — the fee is set in the Memberships tab (below).

If your membership is free, you leave the “Execute real-time monetary transactions” option unchecked and pick a membership type with a zero fee.

## **The Memberships tab**

Here you enable the membership functionality on the page. Key tasks include:

* Tick **Membership section enabled** so this page handles membership sign-up/renewal.

* Enter the text that will show to new members, and separately text for renewals (people who already have or had membership).

* Select which membership types are available on this form, set a default, and decide whether auto-renew is allowed (which requires a payment processor and recurring payment support).

* Optionally: If your setup is more complex (e.g., multiple membership levels or terms in one form), you may use a membership price set instead.

## **The Receipt tab**

After someone completes the form, you’ll want to thank them and send confirmation. On this tab:

* Customize the thank-you page message (the message that appears on screen).

* Choose the “From” email address and subject for the receipt email.

* Add staff emails in CC or BCC if you want organisation staff to receive notification when someone signs up — but be careful: if those addresses bounce, it could affect email deliverability for the member.

## **The Tell-A-Friend tab**

If you like, you can add a “tell a friend” feature on the thank-you page:

* This allows new members to share a link with friends via email.

* If their friends click the link and sign up, the friend is added in CiviCRM and the “source” field shows they came through this refer-a-friend route.

## **Collecting additional information (Profiles tab)**

To gather more than just basic info (email, name), you can use a profile on your membership form:

* The Profiles tab lets you pick or build a profile form that collects contact info (address, phone) or custom fields (interests, membership branch).

* If someone is logged in when they sign up, CiviCRM pre-fills fields where possible.

* Warning: If you edit an existing profile here, it affects *all* uses of that profile elsewhere—so be cautious.

## **Premiums tab**

If you offer a thank-you gift or incentive with membership (for example a T-shirt or badge), you use the Premiums tab:

* First configure the premium items in Contributions → Premiums.

* Then on this tab you set up how the premium works with this membership page — introductory text, what qualifies for the gift, etc.

## **Testing membership sign-up pages**

Before you publish your page for the public, run through tests:

* In Contributions → Manage Contribution Pages, click “Links” next to your page and choose “Test-drive”.

* Use the form as though you’re a member. Check that data appears in CiviCRM as expected (under Memberships).

* For payment testing use a sandbox or dummy processor (so you are not actually charged).

* Ask colleagues or a friendly volunteer to test too — different browsers, devices, scenarios.

* Regularly revisit and test your page: if members are getting confused, you may need to refine the form or wording.

## **Adding the sign-up page to your website**

Once your form works:

* Copy the public URL (from Contributions → Manage Contribution Pages → “Links” → “Live Page”).

* On your website (depending on your CMS: Drupal, WordPress, Joomla) insert the link or embed the form into your page/menu.

* For example: in WordPress you might use a shortcode; in Joomla you might create a menu item for the contribution page.

* The sign-up page should match your website’s theme by default. You can enhance it with images or styling if desired.

## **Permissions needed for online membership sign-up / renewal**

To allow both anonymous visitors and logged-in users to join or renew memberships online, your CMS roles must have the following:

* Permission to view profiles and forms so basic contact details can be collected.

* Permission to access all custom data (if you’ve added custom fields).

* Permission to make online contributions (unless all your memberships are free and you’re not collecting any payments).

