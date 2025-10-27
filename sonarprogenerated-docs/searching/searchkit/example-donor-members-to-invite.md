---
categories: Tutorial
level: Basic
summary: Learn how to create a list of major donor members who have never attended an event, so you can invite them to your next event using CiviCRM's SearchKit.
section: Searching and reporting > Search Kit
---

# Create a list of donor members to invite

This tutorial will guide you step-by-step through creating a list of members who are major donors but have never attended an event, using CiviCRM's SearchKit. This is useful if your organisation wants to invite these supporters to an upcoming event.

## Step 1: Select current members

- Go to the SearchKit page in CiviCRM and click **New Search**.
- For the **Search for** option, choose **Contacts**. This makes it easier to build a list of people to invite.
- In the **With (optional)** section, set it to **With (required)** and select **Memberships** from the +Entity menu.
- Add a filter for **Membership Status** and set it to include only **New** and **Current** members.
- Give your search a name and click **Save**.
- Click **Search** to preview your results.

## Step 2: Filter members who never attended an event

- Add another **With (optional)** field and set it to **Without**.
- Select **Contact Participants**. This will ensure your list only includes members who have never attended any event.

## Step 3: Filter for donors

- Add another **With (optional)** field, set it to **With (required)**, and select **Contact Contributions**.
- Under the **Where** section, add a filter for **Financial Type** and set it to **Donation**.
- To avoid duplicate contacts, use the **Group By** dropdown and select **Contact ID**.
- Add a column for **Total Amount** by clicking **+Add**.
- In the **Field Transformation** section, choose **Sum** next to the **Total Amount** field to get the total donations per contact.

## Step 4: Filter for major donors

- To focus on major donors, use the **Having** section (not **Where**) to add a condition on the summed total amount.
- Set the condition so that only contacts with a total donation greater than or equal to your chosen amount are included.

## Step 5: Add email and phone number

- Add **Email** and **Phone Number** as entities, using **With (optional)**.
- Remember, not every contact will have an email or phone number. Some may have asked not to be contacted by phone or email, so check their contact preferences.

## Step 6: Export your list

- Click the **Actions** button above your search results.
- Choose the option to **Export as CSV** to download your invitation list as a spreadsheet.

Your list is now ready to use for invitations!

# comment: Source: https://docs.civicrm.org/user/en/latest/searching/example-donor-members-to-invite/
# comment: Suggestion: This page is a clear, step-by-step lesson aimed at new users, matching the Diátaxis definition of a Tutorial[3][4]. The content is practical, hands-on, and designed for users to follow along and achieve a specific outcome. The level is Basic, as it assumes little prior experience with SearchKit or advanced CiviCRM features.