---
categories:
  - Uncategorized
  - Guide  
level: Basic  
summary: This page explains the key concepts and settings you need to understand before using CiviContribute to manage donations and payments in CiviCRM.  
section: Contributions  
---

# Key concepts and configurations

## Introduction  
This guide introduces the main ideas behind managing contributions in CiviCRM and walks you through the important setup steps you need before recording donations, membership fees, or other payments.

## Financial types, accounts, and accounting codes  
Different organizations have different needs for tracking their income. Some just want to see totals, while others need detailed accounting records. CiviCRM helps by using **financial types** to group income, and linking these to **financial accounts** that record the money flow.

- Each contribution must have a financial type (like donation, membership dues, event fee).  
- Financial types connect to accounts that track income, assets, and fees automatically.  
- You can create new financial types if you want to separate income streams (for example, different donation campaigns).  
- Always check with your accountant before changing financial types or accounts.

To manage financial types, go to **Administer > CiviContribute > Financial Types**.

## Financial accounts  
Financial accounts represent the categories in your accounting system (like bank accounts or income categories). You can customize them if needed at **Administer > CiviContribute > Financial Accounts**.

- For accounting exports, you may need to add accounting codes exactly as your accounting software requires.  
- Changing a financial account name will also change the linked financial type name.

## Payment processors  
To accept online payments (credit cards, bank transfers), you must set up a **payment processor**. This connects your website to the payment networks.

## Payment methods  
CiviCRM comes with common payment methods like credit card, cash, check, and debit card. You can add or edit these at **Administer > CiviContribute > Payment Methods**. Make sure each method is linked to the correct financial account.

## Accepted credit cards  
You can specify which credit cards you accept at **Administer > CiviContribute > Accepted Credit Cards**. If billing happens on the payment processor’s site, you must configure accepted cards there too.

## Contribution status  
Each contribution has a status that shows its payment progress:

- **Pending (Pay Later):** entered but not yet paid (e.g., by check).  
- **Pending (Incomplete):** payment started but not completed or response not received.  
- **Failed:** payment declined or errored.  
- **Completed:** payment processed successfully.  

Other statuses like In Progress or Partially Paid relate to special cases like recurring payments. You can rename statuses but adding new ones is not recommended.

## Custom data fields  
CiviCRM includes many fields for contribution details. If you need to track extra information, you can create **custom fields** to capture what’s unique to your organization. Before adding custom fields, list what you want to track and compare it to existing fields to avoid duplication.
