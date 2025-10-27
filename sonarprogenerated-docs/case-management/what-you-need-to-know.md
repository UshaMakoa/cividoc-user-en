---
categories: Explanation
level: Basic
summary: Learn the key concepts and structure of CiviCase to help your organisation manage complex client interactions and casework using CiviCRM.
section: Case management
---

# Key concepts of CiviCase

## What is CiviCase?

CiviCase is a part of CiviCRM designed to help your organisation manage complex interactions and ongoing processes with your clients, members, or constituents. It allows you to track a series of related activities, assign roles, and organise workflows so that everyone involved knows what needs to happen and when.

## Activities

- **Activities** are the main way CiviCRM records interactions, such as phone calls, meetings, or emails.
- Each activity includes details like date, duration, status, priority, who created it, and who it’s about.
- Activities can be one-off or grouped together as part of a larger process (a *case*).

## Cases

- A **case** is a collection of related activities that together make up a more complex process or service.
- Cases are useful when your organisation needs to track ongoing work with a client that involves multiple steps or people.

## Case types

- **Case types** define the kinds of processes or services your organisation provides (for example, “Housing Assistance” or “Job Training”).
- Each case type describes a typical workflow or set of tasks.
- Think about the regular, multi-step processes your team handles and use these as your case types.

## Case activities and activity types

- **Case activities** are the specific tasks or steps within a case.
- CiviCRM comes with common activity types like Phone Call, Meeting, or Email.
- You can add your own activity types to match your organisation’s needs (for example, “Client Intake” or “Skills Evaluation”).
- Some activities are created automatically, such as “Open Case” when a new case starts.

## Activity data

- Each activity records who did it, when and where it happened, a subject, and description.
- You can add custom fields to collect extra information if needed.

## Timelines and sequences

- **Timelines** let you plan out a schedule of activities for each case type, with expected dates or deadlines.
- A **standard timeline** is automatically created when a new case starts, but you can add more activities as needed.
- **Sequences** are a way to create activities one after another, without specific dates—useful if the timing depends on when previous steps are finished.

*Tip: Don’t use the same activity type in both a timeline and a sequence for the same case, as this can cause problems.*

## Case roles and relationships

- **Case roles** are the different people involved in a case (like Case Coordinator, Intake Specialist, or Counsellor).
- **Other relationships** are connections outside the case, like family members or doctors.
- **Case resources** are people or organisations that help with many cases (like a service provider or agency contact).
- You can define your own roles and relationships to fit your organisation’s structure.

## System status warnings (relationship types)

- Sometimes, you may see warnings about relationship types (the way people and roles are linked in CiviCRM).
- Common issues include duplicate names, labels, or confusion about direction (who is related to whom).
- If you spot a problem, you may need to rename, delete, or recreate relationship types to fix it.

## Key questions to consider

As you plan how to use CiviCase, ask yourself:
- What types of cases does your organisation manage?
- What activity types do you need for these cases?
- Who should activities be assigned to?
- Do you have a typical timeline for your cases?
- What roles are involved, and do you need new relationship types?

## Built-in assumptions

CiviCase is flexible, but it’s based on some key ideas:
- Activities are single tasks or interactions.
- A case is a series of activities that tell the “story” of the work done.
- Defining case types helps you organise and measure your work.
- Cases often follow a predictable timeline and involve specific roles.
- Some people or organisations are involved in many cases as resources.

# comment: Source: https://docs.civicrm.org/user/en/latest/case-management/what-you-need-to-know/
# comment: This page is best categorised as an Explanation: it introduces concepts, background, and the structure of CiviCase, helping users understand the “why” and “how it fits together” rather than providing step-by-step instructions or exhaustive technical details. It is suitable for users at a Basic level who are new to CiviCase. For best clarity, step-by-step setup and usage instructions should be provided in separate Tutorial or Guide pages.