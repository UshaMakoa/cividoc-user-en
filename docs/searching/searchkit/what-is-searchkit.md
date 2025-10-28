---
categories:
  - Explanation
level: Basic
summary: SearchKit lets you create custom searches and displays in CiviCRM, helping your organisation find and organise information in flexible ways.
section: Searching and reporting
---

# Introduction to SearchKit

## What is SearchKit?

**SearchKit** is a tool in CiviCRM that helps you build powerful, custom searches to find the information your organisation needs. You can use it to search for contacts, contributions, memberships, and more, and then display those results in different ways that suit your work.

SearchKit is designed for users who want more control over searching and reporting, but it may take some learning if you are new to CiviCRM. More experienced users or administrators can also create search displays and share them with others in your organisation.

## Who can use SearchKit?

- **Permissions** control who can use SearchKit and who can see or use specific searches and forms.

- Permissions are set in several places: within SearchKit, in FormBuilder, through your website’s user roles (like WordPress roles), and with CiviCRM’s detailed access controls.

- Each search or form can be set to respect these permissions, or you can choose to let anyone who can view the display see all results. Be careful with this setting to avoid sharing sensitive information by accident.

## Key concepts and terminology

- **Entity**: This means the type of information you want to search for, such as Contacts, Contributions, or Events.
- **Fields**: These are the pieces of information you want to see in your search results (like name, email, or amount).
- **Filters/Criteria/Where**: These help you narrow down your search. For example, you might filter for contacts in a certain city or contributions above a certain amount.
- **Joins (With/Without)**: Sometimes you want to include related information, like showing contacts with or without addresses. This is called a "join." You can choose:

- With (required): Only show results that have the related information.

- With (optional): Show all results, and include related information where it exists.

- Without: Only show results that do not have the related information.

- **Group By**: If your search results have multiple rows for the same contact (for example, one row for each address), you can use Group By to only show one row per contact.
- **Primary fields**: Contacts usually have one main address, email, and phone number. These can be shown easily, but if you add more detailed joins, you may see both the primary and additional information.

## How does SearchKit fit with other CiviCRM search tools?

- SearchKit replaces the older Search Builder and is more flexible than Advanced Search.

- Some users may still prefer Advanced Search or other quick searches for simple tasks.

- The Quick Search box is still the fastest way to find a record by name or email.

## Getting started

- You can find SearchKit in the CiviCRM menu under **Search > SearchKit**.

- If you don’t see it, your site administrator may need to enable the SearchKit extension.

<!--
Source: https://docs.civicrm.org/user/en/latest/searching/search
-kit/introduction-to-search-kit/ -->

<!--
Suggestion: This page is an Explanation, as it introduces concepts, background, and relationships in SearchKit, not step
-by-step instructions or exhaustive reference. The content is aimed at helping new or non-expert users understand what SearchKit is, why it matters, and how it fits with other CiviCRM tools. For best clarity, step-by-step usage (Tutorial) and specific problem-solving (Guide) should be split into separate pages. -->
