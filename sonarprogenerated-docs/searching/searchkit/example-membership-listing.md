---
categories: Tutorial
level: Basic
summary: Learn how to create a filterable public membership list with logos for your website using CiviCRM’s SearchKit and FormBuilder, step by step.
section: Searching and reporting > Search Kit > Examples
---

# Create a filterable public membership list with logo grid

## Introduction

This tutorial will guide you through creating a public web page that displays your organisation’s members in a filterable grid, showing each member’s logo and website link. You’ll use CiviCRM’s SearchKit and FormBuilder tools. No technical expertise is required—just follow each step.

## Step 1: Create a new search and define the data

1. Go to **Administer > Search > SearchKit** in CiviCRM.
2. Click **New Search**.
3. Enter a title for your search, such as “Our Members”.
4. In the “Search for” list, select **Memberships**.
5. Add a “With” for **Membership Contact** to use member contact details (like display name).
6. Add another “With” for **Contact Websites** to include each member’s homepage link.
7. Click **Search** to preview the results.

*Tip: When you add Membership Contact and Contact Websites, SearchKit automatically includes columns from these sources in your results.*

## Step 2: Add columns to show extra data

1. Click the **+Add** button at the top right of the results table.
2. Choose the column you want to display, such as **Membership Contact: Image URL** (this shows the member’s logo).
3. Click **Search** again to refresh the results.

*Note: If you want to use a custom image field, first add the relevant data source.*

*Tip: Don’t forget to click **Save** after making changes.*

## Step 3: Add and configure a grid display

1. Under the search’s title field, click the **+Add** button to add a display.
2. Choose **Grid** for the display type—this arranges results in tiles.
3. Give the display a title, such as “Our Members”.
4. By default, all columns appear; you can drag and drop to reorder them.
5. Click **Preview** to see the grid layout.
6. Remove unnecessary items by clicking the remove symbol (leave only the logo column for this example).
7. Check the **Image** box to show logos as images.
8. (Optional) Set the image height (e.g., 200px) for consistent logo sizes.
9. Check the **Link** box. In the dropdown, choose “Other…”, then select **Membership Contact - Contact Websites: Website**.
10. Remove any “/civicrm” prefix from the token so it links directly to the member’s website.
11. Check the **Tooltip** box and use the Display Name token for the tooltip.

*Note: Only members with logos will appear. To include those without logos, check the “Alternative image” box.*

## Step 4: Add and configure a form for the website

1. Return to the SearchKit dashboard.
2. Click **Forms > + Create Form** for your grid.
3. Enter a name and description for the form.
4. Enter the URL where you want the results to appear (e.g., ‘civicrm/members’).
5. Click **Save**.
6. Click **View Page** to see the results grid.
7. To filter by membership type, switch to the grid tab and drag **Membership Type** into the form layout.
8. Adjust filter presets and layout details as needed.

*Tip: The form will be visible at your chosen URL while you’re logged in.*

## Step 5: Set permissions for public access

1. In the display configuration, click the **Enforce Permissions** button to unlock it (it will change to “Bypass Permissions”).
2. Save your changes.
3. In the form configuration, set permissions:
   - Select **Generic: Allow all users (including anonymous)**.
   - Check the **Accessible on front-end of website** box.

Now, anyone—logged in or not—can view and filter your membership grid on your website.

# comment: Source: https://docs.civicrm.org/user/en/latest/searching/search-kit/example-membership-list-logo-grid/
# comment: This page is a Tutorial because it provides a step-by-step lesson for first-time users to achieve a specific goal (creating a public membership list with logos). It is basic in level, suitable for non-experts. The logical section is "Searching and reporting > Search Kit > Examples". If any steps contain extensive troubleshooting or options, those could be split into separate Guides or Reference pages for advanced users.