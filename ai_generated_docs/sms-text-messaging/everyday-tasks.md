# Source: https://docs.civicrm.org/user/en/latest/sms-text-messaging/everyday-tasks/

---
categories: Guide  
level: Basic  
summary: This guide shows non-profit users how to send SMS messages in CiviCRM, both to individual contacts and to groups, using simple step-by-step instructions.  
section: Everyday tasks  
---

# Sending SMS messages in CiviCRM

## Introduction

This guide helps you send text messages (SMS) using CiviCRM. It assumes your SMS provider is already set up in the system. If not, please complete the setup first. You can send messages to individual contacts or to many people at once.

## Sending a text message to a few individuals

1. Open the contact’s profile you want to message.  
2. Click the **Actions** button and choose **Send SMS**. Alternatively, go to the contact’s **Activities** tab and select **New Activity > SMS**.  
3. On the new page, fill in the message details:  
   - **From:** Pick your SMS provider.  
   - **To:** This fills automatically with the contact’s mobile number. You can add more recipients by typing their names (only contacts with mobile numbers appear).  
   - **Name the SMS:** Give your message a clear name to help you recognize it later (for example, “Event reminder”).  
   - **Use Template:** Insert a saved SMS template if you have one to save time.  
   - **Plain-text format:** Write your message here (up to 160 characters). You can add tokens to personalize the message with contact details.  
   - **Save as new template:** Tick this if you want to reuse the message later.  

4. Send the message. You will see a confirmation, and the SMS will be logged as an activity in the contact’s profile under **Text Message (SMS)**.

## Sending SMS messages to many people (mass SMS)

To send a personalized SMS to multiple contacts:

1. Prepare your list of recipients. You can:  
   - Use an **advanced search** to select contacts and then choose **Send SMS to Contacts** from the Actions menu.  
   - Use a **mailing list** if you plan to message the same group regularly.  

2. Go to **Mailings > New SMS**.  

3. Follow these steps:  
   - **Name your SMS and select recipients:** Give your SMS a clear name. Move the mailing lists you want to include into the right box. You can also exclude groups to avoid sending duplicates. Click **Next**.  
   - **SMS Content:** Choose your SMS provider. Write your message in the **Compose On-Screen** box or upload a text file (max 160 characters). You can insert tokens to personalize messages. Save as a template if you want.  
   - **Schedule or Send:** Choose to send immediately, schedule for later, or save as a draft to finish later. To continue later, go to **Mailings > Draft and Unschedule Mailings**, filter by SMS, and select your draft.  

4. Preview your SMS to check the content. Then click **Submit Mass SMS** to send your message.

## Viewing sent SMS messages

After sending, SMS activities appear in each recipient’s contact profile under the **Activity** tab. Look for activities labeled **Text Message (SMS)** to review message details.

---

This guide is designed to help you confidently send SMS messages in CiviCRM for your non-profit’s outreach and communication needs. If you want to learn how to set up your SMS provider or create mailing lists, please refer to the setup sections in the SMS and Email chapters.