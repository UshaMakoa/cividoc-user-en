---
categories:
  - Uncategorized
  - Guide  
level: Basic  
summary: This page explains how to set up CiviGrant in CiviCRM, including enabling the extension, configuring grant types and statuses, and adding custom data fields to grants.  
section: Set-up  
---

# Set up CiviGrant

## Enable the CiviGrant extension

To start using grants in CiviCRM, first enable the CiviGrant extension:

- Go to **Administer > System Settings > Extensions**.
- Find **CiviGrant** in the list and enable it.

This step activates the grant functionality in your system.

## Configure grant types

Grant types define the categories of grants your organization offers. To set them up:

- Navigate to **Administer > CiviGrant > Grant types**.
- Click **Add Grant Type**.
- Enter a clear **title** and optional **description** for each grant type.

At this time, you cannot add custom fields directly to grant types, but you can add custom data to individual grants.

## Set up grant statuses

Grant statuses help you track the progress of each grant application. To manage statuses:

- Go to **Administer > System Settings > Option Groups**.
- Locate the **Grant status** option group and click **Options**.
- Edit existing statuses or add new ones that fit your grant workflow (e.g., Pending, Approved, Rejected).

Customizing statuses helps you reflect your organization's process clearly.

## Add custom data to grants

You may want to collect additional information for each grant, such as application forms or specific details. To add custom fields:

- Go to **Administer > Customize Data and Screens > Custom Fields**.
- Click **Add Set of Custom Fields**.
- Set **Used For** to **Grant**.
- Create fields to capture the extra information you need.

For example, you can add a field to upload the original application form. Consider converting documents to PDF to keep them read-only and compatible in the future.

For more details on creating custom fields, see the relevant section in the documentation.
