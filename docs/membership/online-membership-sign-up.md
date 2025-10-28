---
categories:
  - Guide
level: Basic
summary: Learn how to set up and add an online membership sign up page to your website in CiviCRM, so people can easily join your organisation online.
section: Membership > Online membership sign up
---

# Online membership sign up

This page shows you how to create and add an online membership sign up page to your website using CiviCRM, so people can join your organisation as members.

## About membership sign up pages

- **Membership sign up pages** let people join your organisation online.

- You create them by making a *contribution page* and enabling membership options on it.

- Even if your membership is free, you should use a contribution page for online sign up.

- Contribution pages have several tabs for configuration—some are especially important for memberships.

## Steps to create an online membership sign up page

###
1. Create a contribution page

- Go to **Contributions > New Contribution Page** in CiviCRM.

- Give your page a name and fill in the required details.

- After saving, you will see several tabs to configure different options.

###

2. Configure the Title tab

- Set the title for your membership page.

- Choose the *Financial Type* that will be recorded for these memberships.

- Add an introductory message (you can include images and simple formatting).

#### Organisational memberships

- To let people join on behalf of an organisation, tick the relevant box.

- Choose a profile to collect organisation details.

- Decide if organisational sign up is optional or required.

###

3. Configure the Amounts tab

- Select which payment processor(s) people can use.

- If you do *not* want to collect extra donations, leave the "Contribution Amounts section enabled" box unticked.

- If you *do* want to collect donations as well as membership fees, tick the box and set up suggested options or a price set.

#### Free memberships

- For free memberships, leave "Execute real
-time monetary transactions" unticked.

- Choose a membership type with a zero minimum fee.

###

4. Configure the Memberships tab

- Tick "Membership Section Enabled" to use this page for memberships.

- Add text for the initial sign up and for renewals.

- Select which membership types are available, which is the default, and if any can be auto
-renewed.

- If you want to offer multiple memberships or terms at once, use a *membership price set*.

###

5. Configure the Receipt tab

- Set up the thank
-you page and email receipt options.

- Customise the message and the email address the receipt comes from.

- To further customise the email, use **Mailings > Message templates**.

#### Email alerts for staff

- Add staff emails to "CC Receipt To" or "BCC Receipt To" if you want notifications.

- Make sure these emails are correct—bounced emails can cause issues with member records.

###

6. Tell
-A-Friend tab (optional)

- Enable this to let new members invite friends by email.

- Friends who join this way are added to CiviCRM and marked as referred.

###

7. Profiles tab

- Add a profile to collect extra information (like address or interests) during sign up.

- Do *not* add a membership profile—membership data is collected automatically.

- Be careful: editing a profile here changes it everywhere it's used.

###

8. Premiums tab (optional)

- Offer thank
-you gifts for joining.

- Set up premiums first under **Contributions > Premiums (Thank
-you Gifts)**.

###

9. Test your membership sign up page

- Use the "Test
-drive" option (under **Contributions > Manage Contribution Pages**) to check everything works as expected.

- Test different scenarios (new member, renewal, different payment options).

- Ask colleagues or friends to try the form and give feedback.

- Test regularly to keep the process smooth.

###

10. Add the sign up page to your website

- **Drupal:** Copy the page URL from "Live Page" and add it to your site menu or content.
- **WordPress:** Copy the URL, use a plugin to create a custom link, or insert using a shortcode.
- **Joomla!:** Create a new CiviCRM menu item, select the contribution page, and save.

###

11. Set permissions

- Make sure users have the right permissions in your website CMS:

  - "Profile listings and forms" (to collect contact info)
  - "Access all custom data" (to collect extra fields)
  - "Make online contributions" (unless memberships are free and you don't want donations)

<!--
Source: https://docs.civicrm.org/user/en/latest/membership/online
-membership-sign-up/ -->

<!--
This page is a Guide: it is task
-focused, showing users how to achieve the specific goal of setting up online membership sign up. It is not a Tutorial (no hand-held learning, but assumes some familiarity), not Reference (not a systematic list of options), and not Explanation (no background or theory). The level is Basic, as it is intended for non-expert users learning to perform a common task. -->
