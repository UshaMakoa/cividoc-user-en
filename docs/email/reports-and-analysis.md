---
categories:
  - Guide
level: Basic
summary: Learn how to use CiviMail’s reporting tools to track, understand, and improve your email campaigns, including managing bounces and analyzing recipient actions.
section: Email > Reports and analysis
---

# Understanding reports and analysis in CiviMail

## Viewing individual mail reports

You can see a report for each email campaign you send by going to **Mailings > Scheduled and Sent Mailings** in CiviCRM. These reports update in real time, so you can refresh the page to see the latest results. Each report is split into sections, showing different statistics about your mailing. The information available depends on whether you enabled tracking options (like opens and clicks) when you set up your mailing.

## Delivery summary

The delivery summary provides an overview of your email campaign’s performance. Here’s what you’ll see:

- **Intended recipients**: The number of people you tried to send your email to.
- **Unique opens**: The number of people (or bots) CiviCRM believes have opened your email, if open tracking is enabled.
- **Total opens**: The total number of times your email was opened, counting repeat views by the same person or bot.
- **Click-throughs**: The number of times people clicked links in your email, if click tracking is enabled.
- **Forwards**: How many times people forwarded your email using the special forward link.
- **Replies**: The number of replies received, if reply tracking is enabled.
- **Bounces**: The number of emails that couldn’t be delivered, if bounce processing is enabled.
- **Unsubscribe requests**: How many people clicked an unsubscribe link in your email.

### How open tracking works

CiviCRM uses a small, unique image in each email to track opens. When someone views the email and their email client downloads the image, CiviCRM records it as an open. Many email programs ask users whether to download images, so not every open is tracked. The actual number of readers is usually higher than reported. Use these numbers to compare your mailings and try different approaches to see what works best for your audience.

## Managing bounces and contacts with invalid emails

If your server processes bounces, contacts whose emails bounce are marked as **On Hold** and won’t receive further messages. You can review bounces by clicking the **Bounces** link in the delivery summary. Investigate the reason for each bounce (like a typo in the email address), fix it, and remove the **On Hold** status if appropriate. You can then reuse your mailing and exclude those contacts from future sends.

You can also search for bounces using **Search > Advanced search** and filter by bounce type.

## Click-through summary

This section shows statistics for each link in your email:

- **Clicks**: The total number of times each link was clicked.
- **Unique clicks**: The number of individual people who clicked each link.

## Mailing reports with CiviReport

CiviReport provides four useful reports for email campaigns:

- **Mail Bounce Report**
- **Mail Summary Report**
- **Mail Clickthrough Report**
- **Mail Opened Report**

These reports let you analyze multiple mailings at once and offer extra features, such as adding reports to dashboards or having them emailed to you.

For more details, see the Reporting section in the user guide.

<!--
Source: https://docs.civicrm.org/user/en/latest/email/reports
-and-analysis/ -->

<!--
This page is a Guide: it helps users achieve specific goals (track and analyze mailings, manage bounces) with step
-by-step actions and practical advice, but does not provide deep background or systematic reference. The level is Basic because it assumes no prior expertise and explains concepts in accessible language. -->
