---
categories: Guide
level: Basic
summary: Learn how to enable and configure CiviCampaign so your organisation can track activities like contributions, surveys, and mailings for specific campaigns.
section: Campaign > Set-up
---

# Set up CiviCampaign

## Enable CiviCampaign

To start using campaigns in CiviCRM, you first need to enable the CiviCampaign component.

- Go to **Administer > System Settings > Components**.
- Find **CiviCampaign** in the list.
- Click **Enable** and then **Save**.

Once enabled, you will see a new menu item called **Campaigns** at the top of your CiviCRM screen.

## Add a new campaign type

CiviCRM comes with three campaign types by default: **Direct Mail**, **Referral Program**, and **Constituent Engagement**. You can add other types that fit your organisation’s needs or disable types you don’t use.

To add a new campaign type:

- Go to **Administer > CiviCampaign > Campaign Types**.
- Click **Add Campaign Type**.
- Enter a **Label** for the new type (and an optional description).
- (Optional) Set the **Weight** to control where this type appears in drop-down menus (lower numbers appear higher).
- Click **Save**.

Your new campaign type will now be available whenever you create a new campaign.

## Set campaign status

Campaign statuses help you track what stage each campaign is in. Default statuses include **Planned**, **In Progress**, **Completed**, and **Cancelled**.

To add a new campaign status:

- Go to **Administer > CiviCampaign > Campaign Status**.
- Click **Add Campaign Status**.
- Enter a **Name** (and an optional description).
- (Optional) Set the **Weight** to control the order in menus.
- Click **Save**.

You can now assign this status to campaigns as needed.

## Configure the engagement index

The engagement index lets you record how interested or involved someone is in a campaign activity (like sending an email, meeting, or phone call).

To set up the engagement index:

- Go to **Administer > CiviCampaign > Engagement Index**.
- Set up the index as a number (for example, 1 for high engagement, 5 for low engagement).

This helps your team track and understand supporter involvement.

# comment: Source: https://docs.civicrm.org/user/en/latest/campaign/set-up/
# comment: Suggestion: This page is a Guide, as it gives step-by-step instructions for setting up specific features, but does not cover background or exhaustive reference details. The level is Basic, as it is for new users learning to configure CiviCampaign. If the engagement index setup or campaign types list were very detailed, those could be split into a Reference page.