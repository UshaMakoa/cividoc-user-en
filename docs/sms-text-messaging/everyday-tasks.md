---
categories:
  - Guide
level: Basic
summary: Learn how to send text messages (SMS) to individuals or groups using CiviCRM, including step-by-step instructions for both one-off and bulk messaging.
section: SMS (text messaging) > Everyday tasks
---

# Sending text messages (SMS) in CiviCRM

## Before you start

Make sure your organisation has already set up an SMS provider in CiviCRM. If you haven’t done this yet, please see the “Set-up” section for SMS.

## Sending an SMS to a few individuals

To send a text message to one or more existing contacts:

1. Open the contact’s profile in CiviCRM.

2. Click the **Actions** button and select **Send SMS**.

- Alternatively, you can go to the **Activities** tab, choose **New Activity**, and select **Send SMS**.

3. On the SMS message page, fill in the details:

   - **From:** Choose your SMS provider.
   - **To:** This will automatically include the selected contact’s mobile number. You can add more recipients by typing their names (only contacts with a mobile number will appear).
   - **Name the SMS:** Give your message a clear name (e.g., “Event Reminder”) to help you identify it later.
   - **Use Template:** If you have an SMS template, you can insert it here.
   - **Plain-text format:** Enter your message (up to 160 characters). You can use tokens to personalise the message with contact details.
   - **Save as New Template:** If you want to reuse this message in the future, tick this box.

4. Send the SMS.

After sending, you’ll see a confirmation. The SMS will also appear as an activity in each recipient’s contact profile. To review, open the contact, go to the **Activity** tab, and look for “Text Message (SMS)”.

## Sending a bulk (mass) SMS

To send a personalised SMS to many people at once:

1. **Select your recipients:**

- For a one
-time message, use **Advanced Search** to find the right contacts. Select them, then choose **Send SMS to Contacts** from the Actions menu.

- For regular group messages, use a pre
-made mailing list (see the “Set-up” section in the Email chapter if you need help creating one).

2. **Start a new bulk SMS:**

- Go to **Mailings > New SMS**.

3. **Step 1: Name and select recipients**

- Give your SMS a clear name (this will appear in each recipient’s activity history).

- Select the groups you want to include by moving them to the right
-hand box. You can also exclude groups if needed (contacts in both included and excluded groups will not receive the message).

- Click **Next**.

4. **Step 2: Write your message**

- Choose your SMS provider.

- Decide whether to use an existing template or write a new message (up to 160 characters). You can also upload a text file with your message.

- Use tokens if you want to personalise the message.

- If you want to reuse this message later, tick **Save as New Template**.

- Click **Next**.

5. **Step 3: Schedule or send**

- Choose to send the message immediately or schedule it for later.

- If you want to finish later, click **Continue Later**. To find your draft, go to **Mailings > Draft and Unschedule Mailings**, tick **Is SMS**, and search. Click **Continue** on your draft to finish.

- You can preview your message before sending.

- Click **Submit Mass SMS** to send.

<!--
Source: https://docs.civicrm.org/user/en/latest/sms/everyday
-tasks/ -->

<!--
This content is a Guide because it provides step
-by-step, goal-oriented instructions for sending SMS messages in CiviCRM, addressing specific user tasks without background explanation or exhaustive reference details. The level is Basic since it is aimed at non-expert users performing common tasks. The page logically belongs in the "SMS (text messaging) > Everyday tasks" section. -->
