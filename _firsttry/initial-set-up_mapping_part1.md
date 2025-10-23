# Source: https://docs.civicrm.org/user/en/latest/initial-set-up/mapping/

---
categories: Guide  
level: Basic  
summary: Learn how to set up and use mapping and geocoding in CiviCRM to display maps for contact addresses and automatically get geographic coordinates.  
section: Initial set up  
---

# Mapping and geocoding in CiviCRM

## What is mapping and geocoding?

Mapping lets you show maps for your contacts’ addresses inside CiviCRM. Geocoding means converting these addresses into latitude and longitude coordinates so they can be placed accurately on a map.

## Choosing a mapping provider

CiviCRM supports two main mapping services:

- **Google Maps**  
- **OpenStreetMap**

You can pick the one that works best for your area or preference. Some places may have better map coverage with one service over the other.

## Setting up mapping and geocoding

1. Go to **Administer > System Settings > Mapping and Geocoding** in your CiviCRM menu.
2. Choose your **Mapping Provider** (Google Maps or OpenStreetMap).
3. Choose your **Geocoding Provider** (usually Google).
4. Enter the **API key** required by your chosen geocoding provider. This key lets CiviCRM connect to the mapping service.
5. Click **Save** to apply your settings.

If everything is set up correctly, you will see a confirmation message: “Your changes have been saved.”

## How geocoding works in CiviCRM

When you add or update a contact or event address, CiviCRM will automatically fill in the latitude and longitude if your geocoding provider covers that location. This helps place the address on the map accurately.

## Important tips and troubleshooting

- If your CiviCRM server cannot access the internet or if a firewall blocks it, mapping and geocoding will not work. You might see errors when saving addresses. To fix this, either disable mapping and geocoding or work with your IT team to open the necessary connections.
- Some mapping services have limits on how many times you can use their API for free. If you hit these limits, you may get errors when saving addresses.
- After enabling geocoding, set up the **job.geocode** scheduled job in CiviCRM. This job will automatically find coordinates for addresses that don’t have them yet.

## Using alternative geocoding providers

If you want more options or features, you can explore the **Geocoder** extension available from the CiviCRM extensions directory. This extension supports additional geocoding services and improvements.

---

If you want to learn more about working with addresses or managing contacts, check out the related guides on those topics.