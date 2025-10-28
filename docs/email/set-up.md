---
categories:
  - Guide
level: Basic
summary: Learn how to set up your organisation's contact details, mailing groups, and email templates in CiviCRM so you can send mass emails and manage your mailing lists.
section: Email > Set-up
---

# Set up email and mailing lists

## Configure your organisation's contact information

To send mass emails using CiviCRM, you must enter your organisation’s basic details: name, description, email address, and postal address. This information is required by privacy laws in many countries and will be included in your emails using special tokens.

- Go to **Administer > Communications > Organization Address and Contact Info**.

- Fill in your organisation’s name, description, email, and postal address.

- Save your changes.

## Create mailing groups

Mailing groups help you organise who receives your emails.

- Go to **Contacts > New Group**.

- Enter a name and description for your group.

- Under **Group Type**, check **Mailing List** so it can be used for mailings.

- Add contacts to the group as needed.

You can also create **Smart Groups** that automatically update based on search criteria (for example, all active members or contacts in a specific city):

- Use **Advanced Search** or **Find Contact** to search for the contacts you want.

- Select all results.

- From the **Actions** menu, choose **Group
 - create smart group**.

- Name your Smart Group and make it a Mailing List if needed.

- Save the Smart Group.

**Note:** If you create a Smart Group from a participant search, you may need to edit its settings in **Contacts > Manage Groups** to mark it as a Mailing List.

## Allow people to sign up for your mailing lists online

To let people join your mailing lists themselves:

- Make sure the group is marked as a **Mailing List**.

- Set the group’s **Visibility** to **Public Pages** in **Contacts > Manage Groups**.

- For sites using Drupal, ensure anonymous users have the “Access CiviMail subscribe/unsubscribe pages” permission.

People can sign up using a special subscribe link, a profile form, or (for Drupal) a webform.

## Let users subscribe using a link

Share the appropriate subscribe link for your website:

- **Drupal, Backdrop, WordPress, Joomla:** The link format depends on your site. See your CiviCRM documentation for the exact URL.

Anyone with the link can subscribe to your public mailing list groups.

## Use a profile for sign-ups

You can collect more information from subscribers by using a profile form:

- Create a profile (for example, “Newsletter Sign
-up”) with the fields you want users to fill out.

- Make sure the email field is required and visible to Public Pages.

- Share the profile’s public link or embed the form on your website.

- For WordPress, use the CiviCRM button in the page editor to insert the profile form.

## Use a webform (Drupal only)

Drupal sites can use webforms for newsletter sign
-ups, which offer advanced features like spam control and custom design. Ask your site administrator for help if you want to use this option.

## Automatically add people to mailing groups with a profile

To add users to mailing groups when they fill out your sign-up form:

- Option A: Add a “Group(s)” field to your profile so users can choose which lists to join.

- Option B: In the profile’s advanced settings, set a default group for all new sign
-ups.

## Mailing list confirmation workflow

CiviCRM can require users to confirm their subscription (double opt-in):

- Enable **Double Opt
-in** in **Administer > Administration Console > CiviMail Component Settings**.

- When someone subscribes, they get a confirmation email. Their status is “Pending” until they confirm.

- Once confirmed, their status changes to “Added” and they receive a welcome message.

**Note:** If someone subscribes to multiple groups at once, they’ll receive a separate confirmation email for each group.

## Set up scheduled jobs and cron jobs

To send mass mailings and handle bounces automatically, you need to enable scheduled jobs:

- Go to **Administer > System Settings > Scheduled Jobs**.

- Enable the **Send Scheduled Mailings** and **Fetch Bounces** jobs.

Your server must trigger these jobs, usually with a cron job. Ask your system administrator for help if you’re unsure how to set this up.

## Automated messages and mailing list management

CiviCRM can send automated emails for actions like:

- Confirming a new subscription

- Sending a welcome message

- Confirming an unsubscribe or opt
-out

- Sending an auto
-response to replies

Edit these messages at **Mailings > Headers, Footers, and Automated Messages**.

For more on managing your email lists, see the “Maintaining Healthy Email Lists” section.

## Create headers and footers for your mailings

Headers and footers help standardise your emails:

- Go to **Mailings > Headers, Footers, and Automated Messages**.

- Create and edit headers (top of the email) and footers (bottom of the email).

- Include your organisation’s logo and required unsubscribe links.

- Staff can select these when creating new mailings.

Headers and footers can be plain text or HTML. You may need to write or paste in HTML code.

## Test your email templates

Test your templates in different email clients (like Outlook, Gmail, etc.) to make sure they display correctly. Use a test group with contacts representing each email service. Keep your HTML simple and use inline CSS or tables for best results.

## Auto
-filing email conversations in CiviCRM

You can automatically file emails sent or received in your regular email client as activities in CiviCRM:

- Include a special email address (set up by your administrator) in the Bcc field.

- CiviCRM matches email addresses to contacts, or creates new ones if needed.

Your administrator must configure this feature.

## Allow users to edit inbound emails

By default, activities created from inbound emails are not editable. To allow editing:

- An administrator can grant the **CiviCRM: edit inbound email basic information** or **CiviCRM: edit inbound email basic information and content** permissions to the appropriate user roles.

The first permission allows editing activity fields except the original message. The second allows editing all fields, including the message content.

<!--
Source: https://docs.civicrm.org/user/en/latest/email/set
-up/ -->

<!--
Suggestion: This page is a "Guide" because it provides step
-by-step instructions for setting up email and mailing lists, addressing practical tasks non-expert users need to accomplish. It is not a Tutorial (no single hands-on scenario), not Reference (not exhaustive or systematic), and not Explanation (no conceptual background). Level is Basic because it covers first-time setup for non-experts. If desired, parts about Smart Groups or cron jobs could be split into separate, more advanced guides. -->
