---
categories:
  - Guide  
level: Basic  
summary: This guide explains how to enable and set up the CiviEngage component in CiviCRM, including how to customize its contact subtypes, custom fields, and surveys to support your organization's community engagement work.  
section: Set-up  
---

# Set up CiviEngage in CiviCRM

## Enabling CiviEngage

CiviEngage is included as a Drupal module when you install CiviCRM, so you only need to activate it. To do this, you need Drupal Administrator permissions to:

- Enable the CiviEngage component within the CiviCRM module in Drupal.
- Update the Administrator role permissions by checking access to the `civicrm_engage` module and its settings.

Make sure the CiviCampaign component is also enabled, as CiviEngage depends on it.

## Understanding CiviEngage contact subtypes

CiviEngage uses contact subtypes to organize contacts with specific roles and to show related custom fields. When you install CiviEngage, it creates these subtypes:

### Individual contact subtypes:
- **Media Contact**: Tracks media-specific details like media type (newspaper, radio, TV), beat (coverage area), and media issue interests.
- **Elected Official**: Includes information such as elected level (city council, senate) and role (spokesperson, scheduler).
- **Funder Contact**: Captures funder details like program areas and issue interests.

### Organisation contact subtypes:
- **Media Outlet**: Stores media outlet details like type (TV, radio, newspaper).
- **Foundation**: Tracks grant-related information such as average grant amount and funding areas.

## Customizing custom field sets

CiviEngage comes with predefined custom fields designed to help with community organizing. These fields mostly use multiple-choice options pre-filled with sample values. Before using CiviEngage, review and update these options to fit your organization's needs.

**Important:** Do not delete any custom fields or field sets, as other features like reports and searches depend on them.

To review or modify these fields, go to **Administer > Customize > Custom Data** in CiviCRM.

### Overview of key custom field sets

- **Communications Details**: Best time to contact, communication status, and reasons for do-not-contact preferences.
- **Voter Info**: Voter ID, party registration, precinct, district info, and voting history.
- **Constituent Info - Individuals**: Contact classification (volunteer, donor, etc.), staff responsible, and how/when the contact joined.
- **Grassroots Info**: Member status, leadership level, issue interests, and volunteer interests.
- **Constituent Info - Organizations**: Organization type (member, affiliate, business, government).
- **Grant Info**: Average grant amount, funding areas, and requirements notes.
- **Proposal Info**: Grant proposal details like ask amount, status, and dates.
- **Participant Info**: Event participant needs and contact history.
- **Event Details**: Additional event information including contact persons.
- **Organizational Details**: Organization ratings and evaluations.
- **Demographics**: Ethnicity, secondary language, and other demographic data.
- **Media Outlet Info** and **Media Info**: Media type and interests for media contacts and outlets.
- **Funder Info**: Program areas and issue interests for funder contacts.
- **Elected Official Info**: Government level and staff roles.

## Modifying custom value options

Many custom fields use shared option lists for consistency across different contexts. For example, the **Issue Interests** list is used for individuals, media contacts, funders, and grants.

Review and customize these option lists to reflect your organization's focus areas and volunteer activities.

## Using custom profiles

CiviEngage provides custom profiles to help you update groups of fields easily for individuals or organizations, such as voter demographics or volunteer interests.

## Setting up surveys for walklists and phonebanking

CiviEngage works with CiviCampaign to help you create surveys for canvassing and phonebanking. When setting up surveys, consider:

- Creating custom data sets with your survey questions and response options.
- Building custom profiles to display these questions during data collection.
- Defining your target audience as a group or smart group.
- Associating surveys with campaigns if applicable.
- Using default survey result options (e.g., Completed, Not Home, Moved) to track responses.

### Tips for survey setup

- If running many surveys with few questions, create one large custom data set and multiple profiles for each survey.
- If running few surveys with many questions, create separate custom data sets for each survey.

## Creating custom data sets and profiles for surveys

To create surveys for walklists or phonebanking:

1. Create a custom data set for your survey questions.
2. Add custom fields as questions with response options.
3. Create a custom profile that includes these questions.
4. Use the profile during survey activities to collect responses.

This approach helps you organize survey data efficiently and supports better analysis of your outreach efforts.
