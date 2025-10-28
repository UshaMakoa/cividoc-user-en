---
categories:
  - Guide
level: Basic
summary: Learn how to send mass emails to your contacts using CiviMail, including how to choose recipients, set up your mailing, and track results.
section: Email > Mass mailings
---

# Send a mass email with CiviMail

## Choose your recipients

You can send a mass email in CiviMail to either:
- **Groups**: Predefined lists of contacts, such as your newsletter subscribers.
- **Search results**: Contacts found by searching (for example, new members added this month).

**Important:**
If you send to search results, you must select an **Unsubscribe Group**. This group keeps track of people who unsubscribe, so you don’t accidentally email them again. If you’re sending to a Group, this is handled automatically.

**Tip:**
If you don’t have a suitable group for unsubscribes, create one (for example, “General Unsubscribes”) and use it for future mailings.

## When are recipients set?

- The list of recipients is fixed when you schedule the mailing, even if it’s sent later.

- If you send to a **smart group**, the recipient list is based on who matches the smart group at the time you schedule the mailing.

- If you send to search results using “All NNN records,” CiviCRM creates a hidden smart group, which updates based on your search criteria at the time you submit the mailing.

- If you want to send only to specific people, use “NNN Selected records only” after ticking the checkboxes for those contacts.

## Set up your mailing

### Start a new mailing

- To send to a Group: Go to **Mailings > New Mailing**.

- To send to search results: Perform your search, then choose **Email

- Schedule/Send via CiviMail** from the Actions dropdown.

### Fill in the mailing details

**Mailing Name**
Give your mailing a clear name (e.g., “2025
-04-25 – Monthly Newsletter”). This is for your use only.

**Campaign**
Optionally link the mailing to a campaign.

**Template**
Select a message template to start from, or write your own content. You can edit the content for this mailing, but not the template itself.

**From**
Choose which email address the mailing will come from. Admins can add more addresses in **Administer > CiviMail > From Email addresses**.

**Recipients**
Choose which Groups to include or exclude. Only “Mailing List” type groups are shown. You can also exclude people who received previous mailings.

**Dedupe by email**
By default, CiviMail sends only one email per unique contact. If multiple contacts share an email address, you can choose whether to send one or multiple copies.

**Location type**
Choose which email address type to use for sending (for example, “Bulk Mailings” or “Primary”).

**Unsubscribe Group**
(For search-based mailings only) Choose the group that will track unsubscribes.

**Subject**
Enter the subject line for your email. You can use tokens to personalize it.

**Email content**
Write your message in the HTML or Plain Text section. Use tokens to personalize your message (like including the recipient’s name).

**Preview and test**

- Preview how your email will look.

- Send a test email to yourself or a test group to check formatting and links.

**Tip:**
Always test your email before sending to your full list.

### Optional tabs

**Attachments**
Add files to send with your email.

**Header and Footer**
Choose or create a header and footer for your email.

**Publication**
Set whether your email can be viewed publicly or only by recipients and admins.

**Responses**

- Track replies so they’re stored in CiviCRM.

- Set up automated replies.

- Edit opt
-out, resubscribe, and unsubscribe messages.

**Tracking**

- Track who clicks links and who opens your email.

- Note: Tracking may not work if recipients block images or use certain email settings.

## Review and schedule your mailing

- Review all details on the summary screen. You can check who will receive the email and view your message.

- Choose to send immediately or schedule for later.

- Click **Submit Mailing** to finish. CiviMail may take up to 15 minutes to start sending, and large mailings are sent in batches.

## Track and manage your mailings

- Go to **Mailings > Scheduled and Sent Mailings** to see your mailings.

- Click **Report** to view statistics like opens, clicks, and bounces.

- Click a statistic to see which contacts opened or clicked your email.

- Use **Draft and Unscheduled Mailings** to continue working on drafts.

- Use **Archive** to store old mailings.

<!--
Source: https://docs.civicrm.org/user/en/latest/email/mass
-mailings/ -->

<!--
This page is a Guide, as it walks users through the steps to accomplish a specific goal (sending a mass email), without focusing on background or exhaustive options. It is suitable for Basic level users. The content logically belongs under Email > Mass mailings. If desired, the “Tracking and managing your mailings” section could be split into a separate guide for clarity, but it is acceptable as a single page for non
-expert users. -->
