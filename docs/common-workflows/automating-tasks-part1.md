---
categories:
  - Guide  
level: Basic  
summary: This guide helps non-profit users of CiviCRM understand how to automate routine tasks in the system to save time and reduce repetitive work.  
section: Automating tasks  
---

# Automating tasks

## Introduction

If you often find yourself repeating the same decisions or actions in CiviCRM, you can use automation to let the system handle these routine tasks for you. Automating tasks, also called workflows, takes some initial setup but can save a lot of time and reduce errors in the long run.

## What does automating tasks mean?

Automating tasks means teaching CiviCRM to make decisions and take actions based on specific criteria you define. For example, you might want the system to automatically send thank-you letters to donors, remind you about upcoming events, or notify you when a membership is about to expire.

## How to get started with automation

1. **Identify the task you want to automate.**  
   Think about a routine task you do regularly that could be handled by the system, such as sending reminders or generating reports.

2. **Define the criteria for making decisions.**  
   Consider what information helps you decide how to handle each case. For example, you might want to send a special letter if a donor’s gift is above a certain amount or if they live nearby.

3. **Find or create the information fields in CiviCRM.**  
   Use existing fields or create custom fields to store the information you need for your criteria. For example, you might add a custom field for “Fund Name” or “Tax Receipt Eligibility.”

4. **Set up the automation actions.**  
   Use CiviCRM features such as custom tokens, print/merge documents, scheduled jobs, or email templates to tell the system what to do when the criteria are met.

## Example: Personalizing acknowledgment letters automatically

- **Goal:** Automatically customize thank-you letters for donors.  
- **Criteria:** Include or exclude certain text based on donation fund, tax receipt eligibility, or donor location.  
- **Setup:**  
  - Create custom fields like “Fund Name” and “Tax Receipt Type.”  
  - Use custom tokens to insert donor-specific information like first gift date or address.  
  - Design letter templates that include conditional language based on these fields.

## Tips for successful automation

- **Plan carefully before creating custom fields.**  
  Use dropdowns or predefined options instead of free text to avoid inconsistent data entry.

- **Understand your data and relationships.**  
  Knowing how contacts, organizations, and relationships work in CiviCRM helps you set up accurate automations.

- **Use existing reports and scheduled jobs.**  
  Many common automation needs can be met with built-in features like scheduled reminders or reports.

- **Consider professional help for complex tasks.**  
  If you need custom reports or advanced workflows, investing in expert support can save time and improve accuracy.

## Where to learn more

Explore chapters and guides on specific CiviCRM components like Events, Membership, Contributions, and Scheduled Jobs to find detailed instructions on automating tasks related to those areas.

## Encouragement

Automating your routine work in CiviCRM frees you to focus on what matters most—building relationships and advancing your mission. Take small steps to set up automation, and you’ll see how much easier managing your data and communications can become.
