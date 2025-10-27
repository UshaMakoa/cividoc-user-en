---
categories:
  - Guide  
level: Basic  
summary: This guide explains how non-expert users of CiviCRM can use tokens to personalize emails and printed materials, and how to set up mail merges to save time and improve communication.  
section: Common workflows  
---

# Tokens and mail merge

## Overview

In CiviCRM, you can personalize your emails and printed letters by using **tokens**. Tokens are placeholders that automatically fill in information from your database, like a contact’s first name or your organization’s address. This helps you create mail merges that feel personal and save you time.

## Using basic contact data tokens

To greet someone by their first name in an email, type your greeting (for example, "Dear") and then click **Insert Tokens** above the message box. Search for "First name" and select the token `{firstname}`. When the email is sent, each person will see their own first name in the greeting.

You can explore the Insert Tokens popup to find many other tokens, including any custom fields your organization has added.

## Adding organizational tokens

You can also include your organization’s details, such as the postal address or phone number, using tokens like `{domain.address}`. These pull information from your organization’s settings, so your mailings always have the correct contact info.

## Special tokens for emails

Some tokens add special functions to your emails:

- **Action tokens** like `{action.optOutUrl}` and `{action.unsubscribeUrl}` add links that allow recipients to opt out or unsubscribe from mailings, which is required by law for mass emails.

- **Checksum tokens** create personalized links that let recipients update their information or register for events without filling in their details again. These links are secure and expire after seven days.

## Required tokens for mass emails

Every mass email sent through CiviMail must include:

- An **opt-out** or **unsubscribe** link token (`{action.optOutUrl}` or `{action.unsubscribeUrl}`)

- Your organization's address token (`{domain.address}`)

You can add these tokens directly in your email or include them in a standard footer so you don’t have to add them every time.

## Using checksum tokens for personalized links

Checksum tokens let you send links to forms or pages that are already filled with the recipient’s information. This makes it easier for people to donate, renew memberships, register for events, or sign petitions.

Here are examples of how to build these links for different platforms (replace `IDNUMBER` with your page or event ID):

| Platform | Contribution page link example |
|
