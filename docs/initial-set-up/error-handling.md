---
categories:
  - Reference
level: Basic
summary: Learn how to set up error handling in CiviCRM to manage what happens when a system error occurs.
section: Initial set up
---

# Error handling

## Overview

CiviCRM lets you customize how the system responds when a serious (fatal) error occurs. This can help your organisation provide a better experience for users and make troubleshooting easier.

## Options for error handling

You can adjust error handling settings by going to:

**Administer → System Settings → Debugging and Error Handling**

Here are the main options you can configure:

- **Fatal error template**: Enter the path and filename for a custom Smarty template if you want to show a personalised error screen when a fatal error happens.
- **Fatal error handler**: Enter the path and class for a custom PHP error-handling function if you want to override CiviCRM’s default error handling.

## Saving your changes

- After making changes, click **Save** to apply them or **Cancel** to discard them.

- If successful, you will see the message: “Your changes have been saved.”

<!--
Source: https://docs.civicrm.org/user/en/latest/initial
-set-up/error-handling/ -->

<!--
This content is best categorized as Reference. It provides factual, systematic information about configuration options, not step
-by-step instructions or conceptual background. The intended audience is new or non-expert users, so the level is Basic. The logical section is "Initial set up," as it covers a core configuration option. The summary is tailored for non-experts. If users need step-by-step instructions for creating a custom template or handler, a separate Tutorial or Guide would be appropriate. -->
