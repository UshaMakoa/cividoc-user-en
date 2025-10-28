---
categories:
  - Guide
level: Basic
summary: Step-by-step instructions for setting up SMS text messaging in CiviCRM using Clickatell or Twilio, written for non-profit users with no technical background.
section: SMS (text messaging) > Set-up
---

# Set up SMS messaging

## Before you start

You can use CiviCRM to send text messages (SMS) to your contacts if you set up an SMS gateway service. This guide will help you connect either Clickatell or Twilio to your CiviCRM system so your organisation can send single or mass text messages to contacts with a mobile phone number.

**What you need:**

- Access to your CiviCRM site as an administrator

- The ability to install CiviCRM extensions

- An account with either Clickatell or Twilio (these are SMS gateway providers)

- The “send SMS” permission in CiviCRM

**Important:** Only contacts with a mobile phone number will receive SMS messages.

## Setting up Clickatell

###
1. Register for a Clickatell account

- Go to the Clickatell website and sign up for a free Developer’s Central account.

- You’ll receive complimentary credits to try the service.

- After registering, log in and select “Central API” as the product. Enter your Client ID if asked.

###

2. Create a new API connection

- In your Clickatell dashboard, find the option to create a new connection (may be called “Get another API”).

- Choose **HTTP/S** (or “HTTP API”) as the connection type.

- Optional settings:

  - *Description*: Give your connection a name (e.g., “CiviCRM HTTP”).
  - *IP Address Restriction*: You can enter your CiviCRM server’s IP address for extra security.
  - *Delivery notifications*: Enter your site’s callback URL so CiviCRM can receive message delivery reports.

- For Drupal: `http://www.example.com/civicrm/sms/callback?provider=org.civicrm.sms.clickatell`

- For WordPress: `https://www.example.org/?page=CiviCRM&q=civicrm%2Fsms%2Fcallback&provider=org.civicrm.sms.clickatell`

- Click **Submit** to generate your API ID. Write this down.

###

3. Add Clickatell as an SMS provider in CiviCRM

- In CiviCRM, go to **Administer > System Settings > SMS Providers**.

- Click **Add New Provider**.

- Fill in the settings:

  - *Name*: Clickatell
  - *Title*: (e.g., “Clickatell SMS”)
  - *Username*: Your Clickatell username
  - *Password*: Your Clickatell password
  - *API type*: http
  - *API URL*: `https://api.clickatell.com`
  - *API Parameters*: `api_id=YOUR_API_ID`
  - *Is this provider active?*: Tick this box
  - *Is this a default provider?*: Tick if you want Clickatell as your main SMS provider

- Click **Save**.

###

4. Test your Clickatell SMS gateway

- Try sending a test SMS from CiviCRM (see “Everyday tasks” for how to send messages).

- If you are using free credits, your messages may include a thank
-you note from Clickatell until you purchase more credits.

###

5. After upgrading to a paid Clickatell account

- In CiviCRM, edit your Clickatell provider settings.

- In the API Parameters box, add two new lines below your `api_id`:
  ```
  from=YOUR_MOBILE_NUMBER
  mo=1
  ```

- In your Clickatell dashboard, set the “Primary Callback: Reply Path” to **HTTP Get** and use the same callback URL as before.

## Setting up Twilio

###

1. Register for a Twilio account

- Go to the Twilio website and sign up for a free trial account.

- Verify your phone number when prompted.

###

2. Get a Twilio mobile phone number

- In the Twilio Console, find the **Programmable SMS** section.

- Click **Get Started** and then **Get a number**.

- Choose a number (make sure it matches your country if needed) and write it down.

###

3. Set up your number in Twilio

- In the Twilio Console, go to **All Products & Services** > **Phone Numbers**.

- Click your new number.

- Under **Messaging**, set the “A message comes in webhook” to your CiviCRM callback URL:

- For Drupal: `https://example.com/civicrm/sms/callback?provider=org.civicrm.sms.twilio`

- For WordPress: `https://example.com/civicrm?civiwp=CiviCRM&q=civicrm%2Fsms%2Fcallback&provider=org.civicrm.sms.twilio`

- Click **Save**.

###

4. Get your Twilio provider settings

- In the Twilio Console homepage, copy your **Account SID** and **Auth Token**.

###

5. Add Twilio as an SMS provider in CiviCRM

- In CiviCRM, go to **Administer > System Settings > SMS Providers**.

- Click **Add New Provider**.

- Fill in the settings:

  - *Name*: Twilio
  - *Title*: (e.g., “Twilio SMS”)
  - *Username*: Your Account SID
  - *Password*: Your Auth Token
  - *API type*: http
  - *API URL*: `https://api.twilio.com/`
  - *API Parameters*: On the first line, enter `From=YOUR_TWILIO_NUMBER` (in international format, no spaces). On the second line, enter `mo=1`.

- If you have more than one Twilio number, list them separated by a pipe (`|`), e.g., `From=12345051212|19875052323`.

- Click **Save**.

###

6. Test your Twilio SMS gateway

- Send a test SMS from CiviCRM.

- Replies to SMS messages will be recorded as activities on your contact’s record.

###

7. Upgrading your Twilio account

- To remove trial limits and send messages to any number, upgrade to a paid Twilio account.

<!--
Source: https://docs.civicrm.org/user/en/latest/sms/set
-up/ -->

<!--
Suggestion: This content is a step
-by-step, task-focused guide for setting up SMS providers, matching the Diátaxis "Guide" category. It is written for users who want to accomplish a specific goal (enabling SMS in CiviCRM), not to teach concepts (Tutorial), provide technical details (Reference), or explain background/architecture (Explanation). The level is Basic, as it assumes no prior SMS setup experience. -->
