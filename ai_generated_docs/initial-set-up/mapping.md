# Source: https://docs.civicrm.org/user/en/latest/initial-set-up/mapping/

---
categories: Tutorial
level: Basic
summary: This guide helps non-profit users set up and configure mapping and geocoding in CiviCRM to enhance contact management with geographic data.
section: Mapping
---

# Mapping in CiviCRM

## Introduction to mapping and geocoding

Mapping and geocoding in CiviCRM allow you to visualize contact addresses on a map. This feature can help your organization better understand where your contacts are located, which can be useful for planning events, outreach, and more.

## Setting up your mapping provider

To get started, you need to choose a mapping provider. CiviCRM supports two main options: OpenStreetMap and Google Maps. Here’s how to set it up:

1. Navigate to **Administer > System Settings > Mapping and Geocoding**.
2. In the **Mapping Provider** section, select either **OpenStreetMap** or **Google** based on your preference.
3. If you choose Google, you will also need to enter your **Geo Provider Key**, which is an API key required by Google.

Make sure to save your changes. You should see a confirmation message stating, "Your changes have been saved."

## Understanding geocoding

Geocoding is the process of converting addresses into latitude and longitude coordinates. This is particularly useful for mapping your contacts accurately. If you have configured a geocoding provider, CiviCRM will automatically fill in the latitude and longitude fields when you add or edit a contact.

## Troubleshooting connectivity issues

If your CiviCRM installation is on a server without internet access, or if there’s a firewall blocking communication with your mapping provider, you may encounter errors when trying to save contact records. In this case, you will need to either disable mapping and geocoding or resolve the connectivity issue.

## Setting up scheduled jobs

After enabling your mapping provider, it’s important to configure the **job.geocode** scheduled job. This job will geocode addresses that do not have latitude and longitude information based on your configured settings.

## Be mindful of usage limits

Keep in mind that some mapping and geocoding providers have usage limits. If you exceed these limits, you may receive an error message when trying to save an address. 

## Alternative geocoding options

If you need to explore other geocoding options, consider checking out the [Geocoder extension](https://civicrm.org/extensions/geocoder), which offers additional features and improvements.

With these steps, you’re now ready to utilize mapping and geocoding in CiviCRM to enhance your organization’s contact management capabilities!