---
categories: Guide
level: Basic
summary: Learn how to report problems or bugs with CiviCRM so your organisation can get effective help and contribute to improving the software.
section: The CiviCRM Community
---

# Reporting problems and bugs in CiviCRM

## Before you report a problem

If CiviCRM is not working as expected, start by searching for similar issues on the CiviCRM question & answer site or Stack Exchange. You may find advice or solutions that resolve your problem without needing to report it.

If you do not find your issue, you can post a question. Be as detailed and specific as possible about:

- The version of CiviCRM you are using
- Which CMS platform (like WordPress, Drupal, Joomla) and its version
- Which web browser and version
- What you were trying to do, and how you tried to do it
- The URL you used (remove any confidential details)

Clear, detailed questions are more likely to get helpful replies.

## Using older versions of CiviCRM

If you are using an older version of CiviCRM and encounter a problem, be aware that you may be advised to upgrade to the latest version. Supporting multiple versions is difficult, and many issues are fixed in newer releases.

## Common causes of problems

Before reporting a bug, check these possible causes:

- **Misunderstanding the software:** Review the documentation carefully. Frustration can make it easy to miss details.
- **Server setup:** Server configuration can affect how CiviCRM works. Check if your server settings might be causing the issue.
- **Outdated software:** Using old versions of CiviCRM, PHP, or MySQL can cause unpredictable errors. Try to use the latest stable versions.
- **Customisations:** Changes to CiviCRM’s source code can create unexpected problems. If your site is customised, share this information and any relevant code when asking for help.
- **New modules or components:** Recently added modules or components might not be compatible with your version of CiviCRM. Make sure you are using supported and up-to-date modules.
- **Actual bugs:** If you have checked all of the above and still encounter the issue, it may be a bug in CiviCRM.

## Reproducing the problem on a demo site

Try to recreate your problem on a CiviCRM demo site that matches your version. If the bug appears there, it is likely a problem with CiviCRM itself. If not, it may be related to your server or customisations.

Some issues, such as those involving email or payment processing, cannot be tested on demo sites. If you cannot reproduce the bug on a demo site, provide as much information as possible about your server setup (but do not include sensitive information like database passwords).

If you confirm a bug on the demo site, explain exactly what you did and include the demo site URLs in your forum post.

## Writing a good bug report

A helpful bug report includes:

- What you did (step-by-step)
- What you expected to happen
- What actually happened
- CiviCRM version
- CMS platform and version
- Browser and version
- PHP and MySQL versions
- Screenshots of the issue, if possible
- Any history of the bug (has it happened before? is it consistent?)
- How often the bug occurs (always, sometimes, only with a certain browser, etc.)

The more background you provide, the easier it is for others to help.

## Getting bugs fixed

The time it takes to fix a bug depends on its severity and complexity. Some bugs are fixed quickly; others may take longer.

The easiest way to get bug fixes is to upgrade to the latest version of CiviCRM. If you have technical skills, you can apply a patch from the CiviCRM Developer’s Guide. Otherwise, you may need help from someone with technical experience.

# comment: Source: https://docs.civicrm.org/user/en/latest/the-civicrm-community/bug-reporting/
# comment: This is a Guide because it gives step-by-step actions to take when reporting problems and bugs, focusing on practical steps rather than background or exhaustive reference. The content is appropriate for basic users who are learning how to interact with the community and get support.