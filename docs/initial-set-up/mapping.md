---
categories:
  - Guide
level: Basic
summary: Learn how to set up mapping and geocoding in CiviCRM so your organisation can display maps and automatically fill in location details for contacts.
section: Initial set up
---

# Set up mapping and geocoding

## What you can do with mapping

With mapping enabled, your organisation can display maps for contact addresses and automatically fill in latitude and longitude information (geocoding) when you add or edit records.

## Steps to set up mapping and geocoding

1. Go to **Administer > System Settings > Mapping and Geocoding** in your CiviCRM menu.

2. **Choose your mapping provider**:

- Select either **OpenStreetMap** or **Google**.

- Pick the provider that works best for the locations your contacts are in.

3. **Choose your geocoding provider**:

- Select **Google** or another available provider.

- This service translates addresses into latitude and longitude.

4. **Enter your API key**:

- If your chosen provider requires an API key, enter it in the **Geo Provider Key** field.

5. Click **Save** to apply your changes.

6. If successful, you’ll see a message confirming that your changes have been saved.

## Important notes

- If your server cannot access the public internet (for example, due to a firewall), mapping and geocoding may not work. You may see errors when adding or editing contacts. In this case, either resolve the connectivity issue or disable mapping and geocoding.

- After setting up mapping, make sure to configure the **job.geocode** scheduled job. This job automatically geocodes any addresses that do not already have latitude and longitude.

- Some providers have usage limits. If you exceed these limits, you may see an error when saving an address.

## Alternative providers

If you need more options, consider using the **Geocoder extension** for additional geocoding providers and features.

<!--
Source: https://docs.civicrm.org/user/en/latest/initial
-set-up/mapping/ -->

<!--
This page is a Guide because it provides step
-by-step instructions for a specific configuration task, without background or systematic reference details. The content is basic, as it is for first-time setup by non-expert users. The logical section is "Initial set up". -->
