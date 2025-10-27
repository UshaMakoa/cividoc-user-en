---
categories: Guide
level: Basic
summary: Learn how to set up a petition in CiviCRM, including permissions and custom profiles, so your organisation can collect signatures online.
section: Petition > Set-up
---

# Set up a petition

This guide will help you set up a petition in CiviCRM, step by step, so your organisation can collect and manage petition signatures online.

## Before you start

- Make sure the **CiviCampaign** component is enabled. You cannot use petitions without it.
- If you need help enabling CiviCampaign, see the Campaign section of the user guide.

## Step 1: Set CMS permissions

To allow people to sign your petition, you must give the right permissions to user roles in your website’s content management system (CMS).

- Go to your CMS permissions page:
  - In Drupal, Joomla!, or WordPress, find this under Administer > Users and Permissions > Permissions (Access Control).
- For each role that should be able to sign (such as “anonymous” for public petitions), give these permissions:
  - **Sign CiviCRM Petition**
  - **Profile Create**
  - **Access all Custom Data**

If your petition is public, give these permissions to anonymous and authenticated users (called "Guest" in Joomla! or "Subscriber" in WordPress).

## Step 2: Create two custom profiles

You need two profiles:
- One profile to collect **contact information** from signers.
- One profile to collect **responses to petition questions**.

### Create the contact information profile

- Go to Administer > Customize Data and Screens > Profiles.
- Add a new profile.
- Add fields for information you want to collect (for example: First Name, Last Name, Email).
- Make sure to include an **Email** field (required for verification).
- You can make fields required if you want to ensure you can contact signers later.

### Create the petition responses profile

- Go to Administer > Customize Data and Screens > Custom Fields.
- Add a set of custom fields for your petition questions.
  - Set “Used For” to **Activities**.
  - Set “Activity Type” to **Petition Signature**.
- Go back to Administer > Customize Data and Screens > Profiles.
- Add a new profile for petition responses.
  - When adding fields, select **Activity** from the Field Name dropdown, then choose your custom fields.

### Advanced settings (optional)

- If you do not want to create a CMS user account for every signer, set “Drupal user account registration option?” to **No account create option**.
- If you want to allow duplicate contacts (for example, if anonymous users sign multiple times), set “What to do upon duplicate match” to **Allow Duplicate Contact to be Created**. You may need to deduplicate contacts later.

For more on creating custom fields or profiles, see the relevant chapters in the “Organising your data” section.

## Step 3: Create a new petition

Once your profiles are ready:

- Go to Campaigns > New Petition.
- Fill out the petition details:
  - **Petition Title** (required): Give your petition a name.
  - **Introduction**: Write a short message about your petition to encourage signers.
  - **Campaign**: If this petition is part of a campaign, select the campaign name.
  - **Contact Profile** (required): Choose the profile you created for contact information.
  - **Activity Profile**: Choose the profile for petition responses.
  - **Is Active?**: Tick this box to make your petition active.
  - **Is Default?**: Tick this box if you want this to be the default petition.

- Click **Save** to finish.

Your petition is now set up and ready to collect signatures.

# comment: Source: https://docs.civicrm.org/user/en/latest/petition/set-up/
# comment: Suggestion: The original page is a step-by-step guide focused on achieving a specific outcome (setting up a petition), which fits the Diátaxis "Guide" category. The instructions are basic and suitable for non-experts. The content logically belongs in the "Petition > Set-up" section. No significant overlap with other Diátaxis types, but background on why two profiles are needed could be split into an Explanation page if desired.