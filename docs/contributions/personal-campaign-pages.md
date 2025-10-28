---
categories:
  - Guide
level: Basic
summary: Learn how your organisation can set up, manage, and use Personal Campaign Pages in CiviCRM so supporters can fundraise on your behalf.
section: Contributions > Personal Campaign Pages
---

# Personal campaign pages

## What are personal campaign pages?

Personal campaign pages (PCPs) let your supporters create their own fundraising pages to raise money for your organisation or a specific event. These pages allow individuals to share their personal stories and reasons for supporting your cause, and invite their friends and contacts to contribute.

## Administrator tasks

As an administrator, you can:

- **Require approval** before a new fundraising page goes live.
- **Enable or disable “tell a friend”**, which lets fundraisers email others about their page.
- **Set notification emails** so you’re alerted when a new PCP is created.
- **Choose how PCP owners are notified** when someone donates through their page.
- **Select which supporter information to collect** using profiles.
- **Customise the “create” button text** for fundraisers.

Once PCPs are active, you can:

- **Approve, reject, or disable PCPs** as needed.
- **Edit PCP content** if updates are required.
- **View fundraising progress** for each PCP.
- **Run summary reports** using CiviReport to see overall results.
- **Credit offline donations (like checks)** to the appropriate PCP.

## Fundraiser options

Supporters who create PCPs can:

- **Choose their own page title and description**.
- **Set a fundraising goal**.
- **Upload a single image** for their page.
- **Decide whether to display a list of donor names (“honor roll”)**.
- **Show a progress thermometer** to track donations.
- **Create a username** (or use an existing one) to edit their page later.

## Limitations

- **Team fundraising is not supported**—each PCP is for an individual, not a group.
- **Only one image can be uploaded** per PCP, and it is not resized automatically.
- **Customising the thermometer and honor roll** requires coding skills and affects all PCPs.
- **Automated emails** sent to PCP owners and administrators can be changed, but you need some technical knowledge (Smarty 2).

## How to set up personal campaign pages

You must first create an online contribution page or event in CiviCRM:

1. Go to **Contributions > New Contribution Page** or **Events > New Event**.

2. Edit the page or event, find the **Personal Campaigns** tab, and click **Enable personal campaign pages**.

3. Configure options such as:
   - **Approval required**: Moderate all PCP requests; admins must approve before pages go live.
   - **Notification email**: Enter addresses to alert admins when PCPs are created.
   - **Supporter profile**: Choose which fields to collect from PCP creators.
   - **Owner email notification**: Decide if PCP owners get emails when donations are made.
   - **Tell a friend**: Allow PCP owners to invite others to their page.
   - **Campaign type** (for events): Let registrants create a fundraising event or a contribution page.

## How supporters create a personal campaign page

Supporters can create a PCP in two ways:

- **After donating or registering**, they see an option to build their own PCP on the “thank you” page.
- **Via a direct link** you provide (by email, on your website, or as a menu item), which lets anyone create a PCP without donating first.

To create a direct link, use:

```
http://YOUR-SITE.ORG/civicrm/contribute/campaign?action=add&reset=1&pageId=CONTRIBUTION_OR_EVENT_ID&component=EVENT_OR_CONTRIBUTE
```

Replace:
- **YOUR-SITE.ORG** with your organisation’s website address.
- **CONTRIBUTION_OR_EVENT_ID** with the ID of the contribution page or event.
- **EVENT_OR_CONTRIBUTE** with “contribute” (for contribution pages) or “event” (for events).

## Managing personal campaign pages

When a supporter clicks the “create your own fundraising page” button or direct link, they fill out a form with their page details. If moderation is enabled, you must approve the page in **Contributions > Personal Campaign Pages**. Find the PCP, then click **Approve**, **Reject**, or **Delete**. You can also enable/disable PCPs later.

After approval, the supporter gets an email with instructions to promote and edit their page. Both administrators and PCP owners can edit page settings at any time.

<!--
Source: https://docs.civicrm.org/some/page/
 -->

<!--
This content is best classified as a Guide: it provides step
-by-step instructions and options for setting up and managing Personal Campaign Pages, focusing on “how” rather than “why” or technical reference details. Some reference-like details (limitations, options) are included, but the primary user need is practical guidance for non-experts. For improved clarity, the limitations and administrator/fundraiser features could be split into separate Reference pages, but for basic users, keeping them together is appropriate. -->
