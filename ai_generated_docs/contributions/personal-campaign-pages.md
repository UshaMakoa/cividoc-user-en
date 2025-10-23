# Source: https://docs.civicrm.org/user/en/latest/contributions/personal-campaign-pages/

---
categories: Guide  
level: Basic  
summary: This guide explains how non-profit users can set up and manage Personal Campaign Pages (PCPs) in CiviCRM to enable supporters to create and share their own fundraising pages.  
section: Contributions  
---

# Personal campaign pages

## What are personal campaign pages?

Personal Campaign Pages (PCPs) let your supporters create their own fundraising pages linked to your organization’s events or contribution pages. These pages allow individuals to share their personal reasons for fundraising and invite friends to contribute. Examples include campaigns like "Sponsor my 5k walk" or "Help fund our trip."

## Setting up personal campaign pages

To use PCPs, you first need an existing online contribution page or event in CiviCRM:

- Go to **Contributions > New Contribution Page** or **Events > New Event** to create one.  
- While editing the page or event, find the **Personal Campaigns** tab and enable personal campaign pages.  
- Configure options such as:  
  - **Approval required**: Choose if an admin must approve new PCPs before they go live.  
  - **Notification email**: Enter admin email(s) to get notified when a new PCP is created.  
  - **Supporter profile**: Select which supporter information fields to collect.  
  - **Owner email notification**: Decide if PCP owners get emails when donations come in, always, never, or optionally.  
  - **Allow 'tell a friend'**: Enable fundraisers to email their contacts to promote their PCP.  
  - **Campaign type** (for events): Let registrants create either a fundraising event or a contribution page.

## Creating personal campaign pages

There are two ways supporters can create PCPs:

- After making a donation or registering for an event, they see a button on the thank-you page to create their own PCP.  
- You can also share a direct link that lets anyone create a PCP without donating or registering first. This link needs your site domain and the contribution or event ID.

## Managing personal campaign pages

Supporters can personalize their PCP by: 

- Choosing a title and writing a message  
- Setting a fundraising goal  
- Uploading one image (note: image resizing is not automatic)  
- Deciding whether to show a donor honor roll  
- Displaying a progress thermometer  
- Activating or deactivating their campaign  

If approval is required, an admin must review and approve the PCP in **Contributions > Personal Campaign Pages** before the page becomes active. Admins can also edit, disable, or delete PCPs at any time.

## Features for administrators

Admins can:  

- Require approval for new PCPs  
- Enable or disable the "tell a friend" feature  
- Receive notifications when new PCPs are created  
- Choose supporter profile fields to collect  
- Customize the create button text  
- View fundraising totals per PCP  
- Run reports summarizing PCP fundraising  
- Enter offline contributions credited to PCPs  

## Limitations to be aware of

- PCPs do not support team fundraising or tracking individual team member contributions.  
- Only one image can be uploaded per PCP, and it is not resized automatically.  
- Customizing the thermometer or honor roll appearance requires coding skills.  
- Modifying automated emails sent to PCP owners or admins requires knowledge of the Smarty template system.

---

This guide introduces the basics of setting up and managing Personal Campaign Pages in CiviCRM, helping your supporters fundraise effectively while giving you control and oversight. For more advanced customization or team fundraising features, additional technical expertise or extensions may be needed.