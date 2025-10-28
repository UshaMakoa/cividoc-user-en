---
categories:
  - Guide
level: Intermediate
summary: Learn how to enable and customise CiviEngage in CiviCRM, including setting up contact subtypes, custom fields, and survey tools for civic engagement work.
section: Civic Engagement > Set-up
---

# Set up CiviEngage

## Enable CiviEngage

To begin using CiviEngage, you need to enable it in your CiviCRM installation. CiviEngage is included as a module when you install CiviCRM on Drupal, but you must turn it on:

- Make sure you have **Drupal Administrator** permissions.

- Enable the **CiviEngage component** within the CiviCRM module in Drupal.

- Update permissions for the Administrator role to allow access to CiviEngage settings (look for a permission like "access civiengage settings").

- Ensure the **CiviCampaign** component is also enabled, as CiviEngage depends on it.

## Understand CiviEngage contact subtypes

CiviEngage uses special contact subtypes to organise your data and expose relevant custom fields for different types of contacts.

**Individual subtypes:**

- **Media Contact:** Tracks media-specific details (e.g., media type, beat, issue interests).
- **Elected Official:** Stores information about elected officials (e.g., office, staff role).
- **Funder Contact:** Captures funder-specific data (e.g., funding areas, programme interests).

**Organisation subtypes:**
- **Media Outlet:** Holds details about media organisations (e.g., type of media).
- **Foundation:** Manages grant and funding information for foundations.

## Review and customise custom field sets

When you install CiviEngage, it creates a variety of custom fields designed to help with community organising. Most are multiple-choice fields with example options.

- **Before using CiviEngage, review and adjust the options to fit your organisation’s needs.**

- If your organisation is outside North America, you may want to update the language, but the concepts are broadly applicable.

- **Do not delete** custom fields or field sets, as other features (like reports or searches) may depend on them.

To view and edit these fields:

- Go to **Administer > Customize > Custom Data** in CiviCRM.

You can add, edit, or disable options for each custom field, but avoid deleting fields or sets.

## Overview of CiviEngage custom field sets

Here’s a summary of the main custom field sets included with CiviEngage and what they track:

- **Communications Details:** Best time to contact, communication status, reasons for not contacting.
- **Voter Info:** State voter ID, party registration, precinct, voting history, and more.
- **Constituent Info – Individuals:** Type (e.g., volunteer, donor), staff responsible, how/when joined.
- **Grassroots Info:** Member status, leadership level, issue and volunteer interests.
- **Constituent Info – Organizations:** Organisation type (e.g., member, affiliate, business).
- **Grant Info:** Average grant amount, funding areas, requirements.
- **Proposal Info:** Grant proposal details (amounts, status, dates).
- **Participant Info:** Event participation needs and responses (childcare, rides, invitations).
- **Event Details:** Event contact person.
- **Organizational Details:** Organisation-specific ratings or categories.
- **Demographics:** Ethnicity, secondary language.
- **Media Outlet Info:** Media type for organisations.
- **Media Info:** Media type and beat for individuals.
- **Funder Info:** Programme areas and issue interests for funders.
- **Elected Official Info:** Level and staff role for elected officials.

## Modify CiviEngage’s custom value options

CiviEngage includes shared lists of value options for things like issue interests and volunteer activities. Review and update these lists to match your organisation’s work.

- **Issue Interests:** Used across individuals, media, funders, and grants. Create a list of issues important to your organisation.
- **Volunteer Interests:** List all volunteer activities your organisation offers or plans to offer.
- **Survey Default Result Set Options:** Standard labels for survey results (e.g., Completed, Not Home, Moved). Use short codes for easier reporting.

## Use custom profiles

CiviEngage provides custom profiles to help you update multiple contacts at once, such as for voter demographics, issue interests, or event participation.

## Set up surveys for walklists and phonebanking

CiviEngage, together with CiviCampaign, makes it easy to set up surveys for canvassing and phonebanking.

- Think about the questions and responses you need to collect for analysis.

- If you have multiple questions for an activity (Walklist or Phonebank), create a custom data set for those questions.

- Create a custom profile with the questions you want to ask.

- For phonebanking, you can include the phone number in the profile (set as view
-only) for easy reference during calls.

- Create a group or smart group of the contacts you plan to survey.

- Decide if the survey is part of a larger campaign (create the campaign if needed).

- When creating a survey, you can:

- Indicate if it’s for a walklist or phonebank.

- Link it to a campaign.

- Attach the custom profile of questions.

- Use default survey result options for tracking responses.

**Tip:**

- If you run many surveys with only a few questions each year, create one custom data set with all questions and separate profiles for each survey.

- If you run only a few surveys with more questions, create separate data sets for each survey.

## Create custom data sets and profiles for surveys

- Create a custom data set to hold your survey questions (see the "Organising your data" section for details).

- For Walklist surveys: link the data set to Walklist activities.

- For Phonebank surveys: link the data set to Phonebank activities.

- Add your questions as custom field labels and possible responses as option values.

- Create a custom profile to pull in the relevant questions for your survey.

<!--
Source: https://docs.civicrm.org/user/en/latest/civic
-engagement/set-up/ -->

<!--
Suggestion: This page is a Guide, as it provides step
-by-step, problem-oriented instructions for enabling and customising CiviEngage, but does not serve as a tutorial for first-time users nor as a systematic reference. The level is Intermediate, as it assumes some familiarity with CiviCRM administration and custom data management. If needed, the sections on custom field set definitions could be split into a Reference page, and the survey setup could be a standalone How-to Guide for clarity. -->
