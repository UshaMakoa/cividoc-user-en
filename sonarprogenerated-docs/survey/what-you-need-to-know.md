---
categories: Explanation
level: Basic
summary: Understand the essential concepts and decisions for using CiviCRM's Survey tool, including how to set up questions, manage respondents, and connect surveys to campaigns.
section: Survey
---

# What you need to know about CiviSurvey

## Key concepts

- **Custom fields and profiles:**  
  To collect survey responses, you use *profiles* in CiviCRM. Profiles display your survey questions to participants. Before you start, decide what questions you want to ask and what type of answers you need (for example, yes/no, multiple choice, or open-ended). For multiple choice questions, set up custom fields with option values. You can create a new profile either from the main profile screen or while creating your survey.

- **Reserving and releasing respondents:**  
  Before collecting responses, you need a *group* of contacts to survey. This can be an existing group or a new one created for the survey. In CiviCRM, this is called *reserving respondents*. After a contact completes the survey and their data is recorded, they are *released* from the group. Surveys are mainly for existing contacts; if you want to survey the general public, use the Petition tool instead.

- **CiviCampaign and CiviEngage:**  
  Surveys are part of the CiviCampaign component, so you need to have CiviCampaign enabled. However, you can create surveys that are not linked to a specific campaign—for example, to gather feedback from members without tying it to a campaign. If you use CiviEngage (on Drupal sites), you get extra options for tracking survey responses.

- **Drupal permissions:**  
  If your organisation uses Drupal, make sure to set permissions so the right roles can reserve and release campaign contacts for surveys.

## Key questions to consider

- Is your survey part of a campaign, or is it a standalone survey?
- What questions do you want to ask, and what type of answers do you need (standardised or open-ended)?
- How many questions will you include? If you have more than three, consider using the Petition tool instead.
- Who will conduct the survey, and how will responses be entered into CiviCRM?
- Which group of contacts do you want to survey?

# comment: Source: https://docs.civicrm.org/user/en/latest/survey/what-you-need-to-know/
# comment: This page is best categorised as an Explanation, as it provides essential background and context for the Survey tool in CiviCRM, helping users understand key concepts and decisions before they start. It does not provide step-by-step instructions or exhaustive technical details. The level is Basic, as it is aimed at new or non-expert users.