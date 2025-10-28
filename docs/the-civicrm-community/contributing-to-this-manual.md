---
categories:
  - Guide
level: Basic
summary: Learn how to contribute edits and improvements to the CiviCRM User Guide, whether you want to make a simple correction or propose multiple changes.
section: The CiviCRM Community
---

# Contributing to the CiviCRM User Guide

## Before you start

You can help improve the CiviCRM User Guide by suggesting changes, fixing mistakes, or adding new information. You do not need to be a technical expert—everyone is welcome to contribute.

If you want to make changes, you will need a civicrm.org account and access to lab.civicrm.org, where the documentation is managed.

## Making a single change

To correct a typo or update a small section:

1. **Sign up for a civicrm.org account** if you do not already have one, and log in at lab.civicrm.org.
2. **Find the page** you want to edit in the User Guide. For example, you might want to update the "Menu, dashboard and dashlets" page.
3. **Click the pencil icon** next to the page title to start editing.
4. **Edit the page** in the GitLab editing screen that appears.
5. **Describe your changes** in the commit message box so reviewers understand what you changed.
6. **Commit your changes**. This creates a merge request, which will be reviewed by the documentation team.
7. **Wait for review**. Your change will be published after it is reviewed and approved.

## Making multiple changes

If you want to make several related changes at once:

1. **Sign up for a civicrm.org account** and log in at lab.civicrm.org.
2. **Create a fork** of the User Guide repository by clicking the fork button at the top right of the page.
3. **Clone the repository** to your computer using your preferred git client.
4. **Find the Markdown file** (.md) you want to edit. For example, to update "What is CiviCRM?", look for `docs/getting-prepared/is-civicrm-for-you.md`.
5. **Make your changes** and commit them in your git client.
6. **Push your changes** to your forked repository.
7. **Create a merge request** in GitLab:

- Click "Merge request".

- Leave a descriptive message.

- Click "Create merge request".
8. **Wait for review**. The documentation team will review your changes and publish them if approved.

## Style guide

When you suggest changes, please follow the Documentation style guide to keep the guide consistent and easy to read.

## Additional resources

If you want to learn more about how CiviCRM documentation works, or about writing in Markdown, see the developer documentation.

## Versioning

All changes should be made to the master branch, which is based on the current version of CiviCRM. More details about versioning are available in the Developer Guide.

<!--
Source: https://docs.civicrm.org/user/en/latest/the
-civicrm-community/contributing-to-this-guide/ -->

<!--
Suggestion: This page is a "Guide" because it gives step
-by-step instructions for a specific task (contributing to documentation), focused on "how" rather than "why" or "what". The level is "Basic" because it is intended for new contributors, not requiring technical expertise. If the style guide or versioning sections become more detailed or technical, they could be split into Reference pages. -->
