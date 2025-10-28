---
categories:
  - Guide
level: Basic
summary: Learn how to choose, set up, and manage payment processors in CiviCRM so your organisation can securely accept online payments and donations.
section: Contributions > Payment processors
---

# Payment processors

## Choosing a payment processor

When your organisation wants to accept payments (such as donations, membership fees, or event registrations) online using CiviCRM, you need to select a **payment processor**. CiviCRM supports many processors out-of-the-box, and more are available as extensions. Some processors are maintained by the CiviCRM community, while others are developed by third parties. Before choosing, check that you have access to technical support for your chosen processor, especially if it is community-contributed.

To find the best fit for your needs:

- Talk to other similar organisations using CiviCRM about their experiences.

- Consider configuring more than one payment processor to give your supporters a choice.

## Onsite vs offsite processors

Payment processors work in two main ways:

- **Onsite processors** let users enter their card details directly on your website, providing a seamless experience. Admins can also process payments from within CiviCRM.
- **Offsite processors** redirect users to a separate payment site, which can be branded to some extent. However, this workflow is less smooth and may result in users abandoning the payment process.

If you use onsite processors, you must have an SSL certificate for your website to keep card details secure. Your hosting provider or system administrator can help set this up. Note: CiviCRM never stores credit card details on your server—it only transmits them to the payment processor.

## Regional availability

Not all payment processors support every country or currency. If your preferred processor is not available, you may need to develop a custom integration or seek help from a third party.

## Merchant account vs built-in

Some payment processors require your organisation to have a **merchant account** with a bank, which usually involves monthly fees but lower transaction commissions. Others, like PayPal or WorldPay, do not require a separate merchant account.

## Support for recurring contributions

Recurring payments (such as monthly donations or auto-renewing memberships) are important for many organisations. Not all processors support this feature:

- Some processors (e.g., PayPal, Authorize.net) require you to manage recurring payments from their own portal.

- Others (e.g., IATS, eWay, Payment Express, SagePay, PayPal Commerce/Checkout) let you manage recurring payments directly in CiviCRM.

Once set up, you can enable recurring contributions in your contribution page settings.

## Managing recurring contributions

To manage recurring payments:

- Go to the **Contributions** tab on a contact record in CiviCRM.

- Use the **Recurring Contributions** section to view, edit, or cancel recurring payments.

You can update the amount, number of installments, next payment date, financial type, status, start date, and email notifications. The payment frequency (weekly, monthly, etc.) cannot be changed from within CiviCRM.

For some processors, you can view and edit the card on file. For iATS, there is a dedicated administrative page under Contributions > iATS Payments Administration.

## Cost

The cost of a payment processor depends on your transaction volume and average payment size. Processors may charge:

- Commission percentages

- Per
-transaction fees

- Fixed monthly charges

- Set
-up costs

High transaction volumes may make a monthly fee with lower commissions worthwhile. For infrequent payments, avoid monthly fees and accept higher commissions.

## Usability

Consider the user experience of the payment process. Some workflows, such as PayPal Standard, may confuse users (e.g., whether a PayPal account is required), which can reduce completed payments.

## Support

CiviCRM provides support for processors included in its core codebase. Community-contributed processors rely on their authors or the community for support.

## Setting up a payment processor

To add a payment processor in CiviCRM:

1. Go to **Administer > System Settings > Payment Processor** and click **New Payment Processor**.

2. Select the processor type from the dropdown.

3. Enter a descriptive name and optional description (helpful for multiple accounts).

4. Select a **Financial Account** where payments will be deposited. Consult your bookkeeper or accountant for advice.

5. Make the processor active so it can be used for events and contribution pages.

6. If you have multiple processors, set a default (can be changed per transaction).

7. Fill in the required payment and test details (fields vary by processor).

You may need to complete additional setup on your payment gateway’s website. Once finished, the processor will be available for paid events and contribution pages.

## Test payments and dummy processors

For testing purposes, you can set up dummy payment processors. Use the following card details for test transactions:

- Card type: Visa

- Card number: 4111 1111 1111 1111

- CVV: any three digits

- Expiry: any future date

## Writing a new payment processor

If you cannot find a suitable payment processor, you can develop a custom integration or hire someone to do it.

<!--
Source: https://docs.civicrm.org/user/en/latest/contributions/payment
-processors/ -->

<!--
This page is a Guide: it is problem
-oriented, showing users how to select, configure, and manage payment processors for specific organisational needs. It is not a Tutorial (no step-by-step lesson for first-time use), Reference (not systematic/factual listing), or Explanation (no background/why). Some sections (e.g., test card details) could be split into Reference for clarity, but overall the page is best presented as a Guide for non-expert users. -->
