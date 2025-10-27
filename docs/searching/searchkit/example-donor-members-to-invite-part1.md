---
categories:
  - Guide  
level: Basic  
summary: This guide helps non-profit users learn how to create a list of donor members to invite to an event using CiviCRM’s Search Kit, with clear step-by-step instructions.  
section: Searching and reporting  
---

# Create a list of donor members to invite

## Introduction  
This guide shows you how to create a list of donor members to invite to an upcoming event using CiviCRM’s Search Kit. You will learn how to find current members who have never attended an event, filter for donors, and export the list for invitations. The steps are simple and designed for users new to CiviCRM.

## Step 1: Select current members  
Start by creating a new search in Search Kit. Choose **Contacts** as the base entity because you want a list of people. Then link **Memberships** as a required entity to include only contacts who are current members. Add a filter to select membership status as **New** or **Current** to focus on active members. Give your search a name and save it. You can click **Search** to see the results.

## Step 2: Find members who never attended an event  
To exclude members who have attended events, add a **Without** condition for **Contact Participants**. This tells Search Kit to find contacts with no event participation records.

## Step 3: Filter for donors  
Add a required entity for **Contact Contributions** to narrow the list to donors. Under filters, set the **Financial Type** to **Donation** to include only donation contributions.

## Step 4: Identify major donors  
To focus on major donors, group your results by **Contact ID** to avoid duplicates. Then add a field for **Total Amount** and apply a **Sum** transformation to calculate each contact’s total donations. Use a **Having** filter to include only contacts whose total donations are above a set amount.

## Step 5: Add contact details  
Since you want to invite these donors, add their primary **Email** and **Phone Number** as optional entities. Note that not every contact may have these details, and some may have opted out of communications, so this step helps ensure you have contact info where available.

## Step 6: Export the list  
Once your search results look right, click the **Actions** button above the results and choose to export the data as a **CSV file**. This file can be used to send invitations via email or phone.

## Tips  
- Remember to respect contacts’ communication preferences shown on their contact summary.  
- You can save your search to reuse or adjust it later.  
- If you want to explore more complex searches, consider learning about additional Search Kit features.
