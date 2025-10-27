---
categories: Guide
level: Intermediate
summary: Learn how to set up surveys in CiviCRM, including creating survey types, custom questions, and organizing your survey for your organisation’s needs.
section: Survey > Set-up
---

# Set up a survey

## Before you start

To create a survey in CiviCRM, you will:
- Define the type of survey you want to run.
- Create custom questions and responses.
- Organize your questions using profiles.
- Set up the survey so your team can collect and track responses.

If your survey is part of a campaign, review the Campaigns section for extra steps.

## Plan your survey questions

- Decide what questions you want to ask and how you want to record responses.
- If you plan to run many surveys with a few questions each (for example, 20–30 surveys a year with 3–4 questions each), create **one custom data set** that includes all possible questions, and use different profiles to select the questions for each survey.
- If you plan to run just a few surveys each year (for example, 3–4 surveys with up to 10 questions each), create **a separate custom data set for each survey**.

## Create or edit survey types

Survey types help describe the kind of activity you are conducting (such as canvassing, phone banking, or walk lists).

1. Go to **Administer > CiviCampaign > Survey Types**.
2. Click **Add Survey Type**.
3. Fill out the form with the details for your new survey type.

Default survey types include: Survey, Canvass, PhoneBank, WalkList, and Petition.

## Create your survey questions (custom fields)

1. Go to **Administer > Customize > Custom Data**.
2. Click **Add a Set of Custom Fields**.
3. Create the custom data set so it is used for **Activities**. Choose the appropriate activity type (Canvas, PhoneBank, Survey, or WalkList).
   - *Tip*: For phone surveys, add the phone number to your profile as view-only so interviewers can see it while calling.
   - *Tip*: For walk lists, use short values for answers (e.g., label: "Wrong address", value: "WA") to make printed lists easier to use.
4. Add your survey questions as fields in the set. Add help text if needed.
5. Click **Save**.

## Organize your survey questions (profiles)

- You can create a profile (a collection of fields) to hold your survey questions.
- Create a profile from the main profile screen, or while adding your new survey.
- When creating a profile within a survey, you can use the drag-and-drop builder to add and arrange fields.

## Create a new survey

1. Go to **Campaigns > New Survey**.
2. Enter a **Title** for your survey.
3. If your survey is part of a campaign, select the campaign from the dropdown menu.
4. Choose the **Activity Type** (e.g., Canvas, PhoneBank, Survey, WalkList).
5. Add **Instructions for Interviews** to help your volunteers.
6. Set **Maximum Reserved at one time** to control how many contacts each volunteer can reserve to interview at once.
7. Set **Total reserved per interview** to limit how many contacts each interviewer can reserve in total.
8. Set **Release frequency** (in days) to automatically release reserved contacts if they are not surveyed in time.
9. Click **Save** or **Save and Next** to add questions.

## Add questions to your survey

- You can add up to two profiles: one for contact information and one for survey questions.
- For each profile, you can select an existing profile, edit/copy one, or create a new one using the drag-and-drop builder.
- You can rename fields, change their order, and adjust settings as needed.

## Set up survey result statuses

- Survey results help you track the status of each completed survey (e.g., Completed, No Answer, Call Back).
- If you have used a result set before, select it. Otherwise, click **Create a new result set** and enter the statuses you want to track (e.g., Completed, Not Home, Moved, Wrong Address, Deceased).
- *Tip*: If you use the Drupal CiviEngage module, it provides default result set options for common statuses.

# comment: Source: https://docs.civicrm.org/user/en/latest/survey/set-up/
# comment: Suggestion: This page is a Guide, as it provides step-by-step instructions for a specific task (setting up surveys), not a full tutorial for first-timers, nor a reference or explanation. Level is Intermediate, as it assumes some familiarity with CiviCRM setup and custom data. If split, the section on planning custom data sets could be a brief Explanation, but it fits here for user context.