# Source: https://docs.civicrm.org/user/en/latest/initial-set-up/addresses/

---
categories: Guide  
level: Basic  
summary: Learn how to set up and use address settings in CiviCRM, including formatting addresses and integrating with the USPS address standardization service to ensure accurate mailing information.  
section: Initial set up  
---

# Addresses

## Introduction

This guide helps you understand how to manage addresses in CiviCRM. You will learn how to format addresses for display and mailing labels, set limits on addresses per contact, and connect CiviCRM to the United States Postal Service (USPS) for address standardization. This makes sure addresses are accurate and consistent, which is important for sending mail and keeping your contact information clean.

## Address settings

### Mailing labels

You can customize how names and addresses appear on mailing labels. For example, you can choose the order of name parts like prefix, first name, middle name, and last name.

The default name format looks like this:

```
{individual_prefix} {first_name} {middle_name} {last_name}
```

For mailing labels, use tokens to define the layout. Make sure to include `{contact_name}` if you want the contact’s name on the label.

A typical mailing label format is:

```
{contact_name}
{street_address}
{supplemental_address_1}
{supplemental_address_2}
{city}, {state_province} {postal_code}
{country}
```

You can choose to display the state or province as an abbreviation (`state_province`) or the full name (`state_province_name`).

### Address formatting

Addresses can also be formatted for display on screen or in reports. Use tokens to set the order and fields shown.

A common format for display is:

```
{street_address}
{supplemental_address_1}
{supplemental_address_2}
{city}, {state_province} {postal_code}
{country}
```

### Other address options

- **Maximum locations:** Set the maximum number of different addresses a contact can have.
- **Include county:** Choose whether to include a county field in address forms.

## Address standardization with USPS

Address standardization helps ensure addresses are correct and follow USPS rules. CiviCRM can connect to the USPS Address Standardization web service, but you need to register with USPS and get a User ID.

### How to get started with USPS address standardization

1. **Register for a USPS Web Tools User ID**  
   Go to the USPS registration page and sign up for a Web Tools ID to use their address services.

2. **Request access to the Address Information API**  
   After registration, request permission to use the Address Information API by providing details about your website and how you will use the API. USPS requires that the service is used only for shipping addresses entered by users on your website, not for bulk processing.

3. **Send test requests**  
   In CiviCRM, enter your USPS User ID and set the test server URL:  
   `http://testing.shippingapis.com/shippingapitest.dll`  
   Then try entering some sample addresses to see if the system can standardize them.

4. **Request production access**  
   Once testing is successful, contact USPS to get access to the production server. You may need to provide a URL to your live website and explain how you use the API.

5. **Configure CiviCRM for production**  
   Update the server URL in CiviCRM to the production server:  
   `http://production.shippingapis.com/shippingapi.dll`

### Important notes and tips

- The USPS User ID is unique to your organization and must not be shared or sold.
- Address standardization runs even during contact imports. To avoid issues, turn off standardization during imports or import only addresses.
- If you develop websites for clients, each client needs their own USPS User ID.
- Not all addresses will validate with USPS, especially during testing.
- The USPS Internet Customer Care Center (ICCC) can help if you have questions:  
  Email: icustomercare@usps.com  
  Phone: 1-800-344-7779 (7:00 AM to 11:00 PM Eastern Time)

## Summary

Setting up addresses properly in CiviCRM helps keep your contact data clean and mailing accurate. Using USPS address standardization improves address quality and reduces mailing errors. Follow the steps here to register with USPS, test the service, and configure your system for live use.