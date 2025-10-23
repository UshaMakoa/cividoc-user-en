---
categories:
  - Explanation  
level: Basic  
summary: This page introduces the key concepts and assumptions behind CiviCase, a flexible case management tool in CiviCRM, helping non-expert users understand how cases, activities, roles, and timelines work together to support complex workflows in their organisation.  
section: What you need to know  
---

# What you need to know about CiviCase

## Introduction to CiviCase

CiviCase is a part of CiviCRM designed to help organisations manage complex workflows that involve multiple steps and people. It groups individual interactions, called activities, into cases to provide structure and oversight over ongoing processes. Understanding how cases work and how to set them up will help you use CiviCase effectively.

## Key concepts

- **Activities** are single tasks or interactions, such as phone calls, meetings, or emails. Each activity records details like when it happened, who was involved, and what was done.
- **Cases** group related activities to track more complex processes that take place over time.
- Cases can use **timelines** or **sequences** to organise activities in a planned order.
- People involved in a case have **roles**, such as Case Coordinator or Intake Specialist, which help clarify responsibilities.
- CiviCase also manages **access control**, so only the right people can see or edit case information.

## Case types

A **case type** defines a category of cases your organisation handles, each with its own set of activities and workflows. For example, a community organisation might have case types like Housing Assistance or Job Training. Defining case types helps organise your work and tailor the case management process.

## Activities and activity types

Within each case, you track specific **activities**. CiviCRM comes with common activity types like Phone Call or Meeting, but you can add custom types to match your organisation’s needs. Recording detailed activities helps build a clear story of what happens in each case.

## Activity data

When you record an activity, you enter information such as who performed it, when and where it happened, and notes describing the interaction. You can also add custom fields to collect extra details if needed.

## Timelines and sequences

- A **timeline** is a schedule of activities expected to happen at specific times relative to the case start or end. It helps everyone stay on track by showing what should happen and when.
- A **sequence** creates activities one after another, only when the previous one is finished, without fixed dates. This suits cases where timing depends on progress rather than a set schedule.

You can use timelines and sequences to model your workflows, but avoid overlapping the same activity types in both within one case.

## Case roles and relationships

People connected to a case have **case roles** that describe their involvement, such as Case Coordinator or Counselor. You can also track other relationships related to the client, like family members or service providers, which may appear across multiple cases.

## Common system warnings

Sometimes, CiviCase may show warnings about relationship types if there are duplicates or inconsistencies. These usually happen when relationship types are renamed or deleted incorrectly. It’s important to keep relationship types clear and consistent to avoid confusion.

## Planning your use of CiviCase

Before setting up CiviCase, consider:

- What case types you need based on your organisation’s work.
- Which activities belong to each case type.
- Who should be assigned to activities.
- What timelines or sequences fit your workflows.
- What roles people will have in each case.

## Assumptions behind CiviCase

CiviCase assumes that:

- Cases are made of a series of activities that form a case story.
- Workflows can be defined by case types and timelines.
- Knowing who plays which role in a case helps coordination.
- Some people or organisations are involved across many cases as resources.

Understanding these ideas will help you plan and use CiviCase to support your organisation’s work effectively.
