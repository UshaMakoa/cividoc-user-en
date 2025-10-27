---
categories:
  - Guide
level: Basic
summary: This guide provides step-by-step instructions for setting up a petition in CiviCRM.
section: Petitions
---

# setting up a petition in civicrm

## enabling the civicampaign component
To use the petition feature, you must first enable the CiviCampaign component. Refer to the **Campaign** section for more information on enabling components.

## setting cms permissions
To allow users to sign your petition, you need to set the appropriate CMS permissions. Follow these steps:

1. Go to your CMS's Access Control page (linked from Administer > Users and Permissions > Permissions).
2. Grant the following permissions for the roles you require:
   - Sign CiviCRM Petition
   - Profile Create
   - Access all Custom Data
3. If your petition is public, grant these permissions to anonymous users and authenticated users.

## creating custom profiles
To capture signer information and petition responses, create two custom profiles:

1. **Contact Information Profile**:
   - Go to Administer > Customize Data and Screens > Profiles.
   - Create a profile with fields for contact information such as First Name, Last Name, and Email.
   - Ensure you collect at least an email address for verification purposes.

2. **Petition Responses Profile**:
   - Go to Administer > Customize Data and Screens > Custom Fields.
   - Add custom fields to capture petition responses.
   - Select "Activities" from the Used For dropdown and "Petition Signature" for the Activity Type.
   - Create a profile for these responses under Administer > Customize Data and Screens > Profiles.

## creating a new petition
Once you have created the profiles, follow these steps to create a new petition:

1. Go to Campaigns > New Petition.
2. Enter the following information:
   - **Petition Title**: Enter the name of your petition.
   - **Introduction**: Describe your petition to encourage signers.
   - **Campaign**: Select the campaign if applicable.
   - **Contact Profile**: Choose the profile for signer contact information.
   - **Activity Profile**: Select the profile for petition responses.
3. Check the boxes for "Is Active?" and "Is Default?" if desired.
4. Click Save to save the petition information.
