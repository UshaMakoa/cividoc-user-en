# Source: https://docs.civicrm.org/user/en/latest/campaign/set-up/

Here's how you can reformat the provided CiviCRM documentation page using the Diataxis framework:

```markdown
---
categories: Guide
level: Basic
summary: This guide walks you through setting up CiviCampaign to track activities like contributions, surveys, and mailings for campaigns or projects.
section: Campaign
---

# setting up civicampaign
## enabling civicampaign
To start using CiviCampaign, you need to enable it in your CiviCRM system. Here's how:

1. Go to **Administer > System Settings > Components**.
2. Select **CiviCampaign** and click **Enable**, then **Save**.
3. Once enabled, CiviCampaign will appear as a new menu item called **Campaigns** at the top of your CiviCRM screen.

## adding a new campaign type
CiviCampaign comes with three default campaign types: Direct Mail, Referral Program, and Constituent Engagement. You can add custom types suitable for your organization:

1. Navigate to **Administer > CiviCampaign > Campaign Types**.
2. Click **Add Campaign Type** and give it a label and optional description.
3. Optionally, adjust the default weight to change its order in drop-down menus.
4. Click **Save**.

## assigning campaign status
You can track the stage of your campaigns by assigning statuses:

1. Go to **Administer > CiviCampaign > Campaign Status**.
2. The default statuses are Planned, In Progress, Completed, and Cancelled.
3. Click **Add Campaign Status** to create a new one, giving it a name and optional description.
4. Adjust the weight if needed to change its order in menus.
5. Click **Save**.

## configuring the engagement index
The Engagement Index helps track an individual's level of interest or engagement in activities:

1. Navigate to **Administer > CiviCampaign > Engagement Index**.
2. Configure the index as a numerical value, where 1 represents high engagement and 5 represents low engagement.
3. This information can help assess member engagement.