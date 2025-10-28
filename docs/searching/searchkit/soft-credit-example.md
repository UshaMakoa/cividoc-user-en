---
categories:
  - Tutorial
level: Basic
summary: Learn how to create and display a soft credit search in CiviCRM using SearchKit, step by step, with clear instructions for non-expert users.
section: Searching and reporting > Search Kit
---

# Create a soft credit search and display

## Introduction

This tutorial will guide you through the process of building a soft credit search and displaying the results in a table using SearchKit in CiviCRM. Soft credits help your organisation recognise people who encouraged others to donate, even if they did not make the donation themselves.

## What are soft credits?

Soft credits are a way to track and thank someone who influenced or encouraged a donation, even if they were not the direct donor. For example, if a supporter asks friends to donate for their birthday, you can record the supporter as a soft credit on each friend’s donation.

## Step 1: Open SearchKit and start a new search

- Go to the **Search** menu and select **SearchKit**.

- You will see a list of saved searches. Click the **New Search** button to start.

## Step 2: Name your search

- At the top left, enter a name for your search, such as “Soft Credit Example Search”.

- Optionally, add a tag to help organise your searches (for example, “Fundraising”).

## Step 3: Select entities for your search

- At the top middle, choose the main entity for your search. Select **Contribution Soft Credits**.

- To include more information (like details about the actual contribution and the donor), click the **+Entity** button and add **Contribution** and **Contact**.

- SearchKit will automatically connect these entities for you.

## Step 4: Add search conditions

- In the **Where** box, you can set conditions to filter your results.

- For example, you might limit results to contributions with a financial type of “Donation” or to a specific date range (e.g., 1 Jan 2021 to 30 April 2022).

## Step 5: Choose the fields to display

- At the bottom, select which fields you want to see in your results.

- Useful fields for this search include:

- Name of the soft credit contact

- Soft credit amount

- Soft credit type

- Name of the contributing contact (the donor)

- Contribution total amount

- Contribution date

- Contribution source

- Contribution status

- Payment method

- Click **Search** to view your results.

## Step 6: Transform fields (optional)

- Expand the **Field Transformations** section if you want to change how fields appear.

- For example:

- Make the donor’s name uppercase for emphasis.

- Show only the date (not the time) for contribution dates.

- Click **Search** again to update the results.

## Step 7: Save your search

- Click the **Save** button at the top right to save your search.

- You can now view results at any time by clicking **View Results**.

## Step 8: Add a display for your results

- Click the **Add...** button on the left and choose **Table** to display your results in a table format.

- Name your table display and click **Save**.

- In the table settings, you can:

- Choose how to sort the results.

- Set the number of results per page.

- Customise the text shown if there are no results.

- Change the order of columns or remove columns you don’t need.

- Add extra features like a menu column for quick actions (e.g., viewing the soft credit contact or the donor).

- Click **View Results** to see your final table.

## Tips

- Save your work regularly to avoid losing progress.

- You can add the search or table to your CiviCRM navigation menu for quick access later.

<!--
This page is a Tutorial because it provides a step
-by-step, hands-on walkthrough for users new to SearchKit and soft credits, focusing on skill acquisition rather than background or exhaustive reference details[1][3][4]. -->

<!--
The original page contains some reference
-like details (such as the technical query JSON), but these are not needed for a basic non-expert tutorial and should be omitted or moved to a separate Reference page if necessary. -->
