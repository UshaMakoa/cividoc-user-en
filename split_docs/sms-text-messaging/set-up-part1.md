# Source: https://docs.civicrm.org/user/en/latest/sms-text-messaging/set-up/

Based on the Diátaxis framework, the page you're describing appears to be a **Guide**. It provides step-by-step instructions on how to set up an SMS gateway in CiviCRM, which is a task-oriented process. Here's how you might structure the top of the page:

---
categories: Guide
level: Basic
summary: Learn how to set up an SMS gateway in CiviCRM to send text messages to your contacts.
section: SMS Setup
---

# Setting Up SMS in CiviCRM

## Introduction to SMS Setup
This guide will walk you through the steps to configure an SMS gateway in CiviCRM. This allows you to send text messages to contacts with mobile phone numbers.

## Configuring a Clickatell SMS Gateway
### Registering for a Clickatell Account
1. Go to [Clickatell's registration page](http://www.clickatell.com/register/) and sign up for a Developer's Central account.
2. Once registered, sign in and select Central API as the product, entering your Client ID.

### Completing the SMS Provider Settings in CiviCRM
1. Install the Clickatell extension in CiviCRM.
2. Go to **Administer > System Settings > SMS Providers** and click **Add New Provider**.
3. Fill in the required settings:
   - **Name**: Select Clickatell.
   - **Title**: Give the SMS provider a title (e.g., "Clickatell SMS").
   - **Username**: Enter your Clickatell username.
   - **Password**: Enter your Clickatell password.
   - **API Type**: Select HTTP.
   - **API URL**: Use `https://api.clickatell.com`.
   - **API Parameters**: Enter your API ID in the format `api_id=8473658`.
4. Enable the SMS gateway by ticking the box.

## Testing the SMS Gateway
Follow the instructions in the "Everyday Tasks" section to test the gateway.

## Configuring a Twilio SMS Gateway
### Registering for a Twilio Account
1. Sign up for a Twilio account at [Twilio's trial page](https://www.twilio.com/try-twilio).
2. Verify your account phone number via SMS or call.

### Setting Up Your Twilio Mobile Phone Number
1. In the Twilio Console, click **Programmable SMS** and then **Get Started**.
2. Click **Get a number** and choose a mobile phone number.

### Setting Up Your Twilio Provider in CiviCRM
1. Install the Twilio extension in CiviCRM.
2. Go to **Administer > System Settings > SMS Providers** and click **Add New Provider**.
3. Fill in the required settings:
   - **Name**: Select Twilio.
   - **Title**: Give the SMS provider a title (e.g., "Twilio SMS").
   - **Username**: Enter your Twilio Account SID.
   - **Password**: Enter your Twilio Auth Token.
   - **API Type**: Leave as HTTP.
   - **API URL**: Leave as `https://api.twilio.com/`.
   - **API Parameters**: Enter your Twilio mobile phone number in international format, followed by `mo=1`.

## Testing CiviSMS with Twilio
Follow the instructions in the "Everyday Tasks" section to test sending SMS messages.

---

If the content becomes too extensive or complex, consider splitting it into multiple pages focused on different aspects of SMS setup, such as separate pages for Clickatell and Twilio configurations.