---
categories:
  - Tutorial
level: Basic
summary: Learn how to build a customized, clickable list of upcoming events in CiviCRM using SearchKit, step by step, with no technical background required.
section: Search Kit
---

# Create a custom upcoming events overview using SearchKit

## Introduction

This tutorial will guide you through creating a custom, interactive list of upcoming events in CiviCRM using SearchKit. You'll learn how to display event details, show speakers and hosts, count participants, and make the list easy to access and use for your organisation.

## What you will achieve

- A tailored list of upcoming events, showing key details

- Clickable links to event settings and participant lists

- Participant counts, including registered and no
-shows

- Optional filters and easy menu access for your team

## Step 1: Start a new search for events

- Go to **Administer > Search > SearchKit**.

- Click **New Search**.

- Name your search (e.g. "Upcoming Events").

- In the "Search for" dropdown, select **Events**.

- In the "Where" section, filter for events where **Event Start Date** is **greater than or equal to** **Now** (or choose a date range as needed).

- Click **Search** to see your initial results.

*Tip: Remember to save your search as you go.*

## Step 2: Add event details to your list

- By default, you’ll see event ID and title.

- Add more columns, like **Event Start Date**, by selecting them from the right
-hand list.

## Step 3: Show speakers and hosts

- Add the **Participant** entity to your search.

- In the "Where" section for participants, filter by **Role** to include only **Speaker** or **Host**.

- Add the **Participant Contact** entity so you can display the names of speakers and hosts.

## Step 4: Group results by event

- To avoid listing the same event multiple times (if it has several speakers or hosts), group your results by **Event ID**.

- Use a field transformation to combine speaker and host names into a single, comma
-separated list.

## Step 5: Add participant counts

- Add another **Event Participants** entity to your search.

- Use the **Count** field transformation on **Participant ID** to show the number of registered/attended participants.

- For no
-shows and cancellations, add another **Event Participants** entity and count those as well.

- Make sure to check the **Distinct** box so each participant is only counted once.

## Step 6: Organize and name your columns

- Click **Add...** under "Compose Search" and select **Table** to create a table display.

- Give your table a name and set a **Sort By** option (e.g. by event date).

- In the table settings, rename columns to something meaningful (e.g. "Event Name", "Speakers", "Registered Participants").

## Step 7: Make numbers and titles clickable

- For the number of registered/attended participants, add a link:
  `civicrm/event/search?reset=1&force=1&event=[id]&status=true`

- For cancellations/no
-shows, use:
  `civicrm/event/search?reset=1&force=1&event=[id]&status=false`

- For the event title, link to the event settings page:
  `civicrm/event/manage/settings?reset=1&action=update&id=[id]`

## Step 8: Add optional filters

- In the upper right of your search, find the button to add a filter form.

- This opens FormBuilder. Name your form and set a page link (e.g. `civicrm/upcoming
-events`).

- On the "Upcoming Events Table" tab, drag and drop form elements (like date pickers or dropdowns) to help users filter the list.

- Use a container for neat layout.

## Step 9: Add your overview to the navigation menu

- Go to **Administer > Customize Data and Screens > Navigation Menu**.

- Create a new menu item using your page link (e.g. `civicrm/upcoming
-events`).

- Now your team can easily access the custom upcoming events overview from the main menu.

## What you’ve accomplished

You now have a custom, interactive list of upcoming events, tailored for your organisation’s needs. Team members can quickly see event details, participant counts, and click through for more information or to manage events.

<!--
Source: https://docs.civicrm.org/user/en/latest/search/example
-upcoming-events-form/ -->

<!--
Suggestion: This page is a clear, step
-by-step walk-through for a practical task, matching the Diátaxis "Tutorial" category. It assumes no prior expertise and is suitable for new users. The content is best placed in the "Search Kit" section, as it demonstrates a hands-on SearchKit use case. -->
