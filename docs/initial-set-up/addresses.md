---
categories:
  - Uncategorized
  - Guide  
level: Basic  
summary: This guide explains how non-profit users can set up and use address settings and USPS address standardization in CiviCRM to ensure accurate mailing information.  
section: Initial set up  
---

# Addresses in CiviCRM

## Overview

This guide helps you configure and use address settings in CiviCRM, including how to format addresses and enable address standardization using the United States Postal Service (USPS) web service. It is designed for non-profit users who want to manage contact addresses accurately and efficiently.

## Address settings

CiviCRM allows you to customize how addresses appear on mailing labels and on-screen. You can use tokens (placeholders) to control the order and content of addresses.

- **Individual name format**: Choose how individual names appear on mailing labels, for example, prefix, first name, middle name, and last name.
- **Mailing label format**: Define the layout of addresses on mailing labels using tokens like `{contact_name}`, `{street_address}`, `{city}`, `{state_province}`, `{postal_code}`, and `{country}`.
- **Address formatting**: Set how addresses display in the system, similar to mailing labels but for screen display.
- **Maximum locations**: Specify how many different addresses a contact can have.
- **Include county?**: Decide if a county field should be included in address forms.

## Address standardization with USPS

Address standardization helps ensure addresses are valid and formatted correctly according to USPS standards. This feature requires setting up access to the USPS Address Standardization API.

### What you need

- A **USPS Web Tools User ID** obtained by registering at the USPS Web Tools site.
- Access to the USPS Address Information API, which requires approval from USPS.
- The correct web service URL provided by USPS.

### Steps to configure USPS address standardization

1. **Register for a USPS Web Tools ID**  
   Go to the USPS registration page and sign up for a Web Tools ID to use exclusively on your website.

2. **Request access to the Address Information API**  
   Provide USPS with your website URL and explain that you will use the API only for transactional address validation associated with USPS shipping services.

3. **Send test requests**  
   In CiviCRM, go to *Administer > Localization > Address Settings*, select USPS as the provider, enter your Web Tools ID, and use the USPS testing server URL. Enter sample addresses to verify the setup.

4. **Request production server access**  
   After successful testing, contact USPS to gain access to the production server. You may need to provide URLs to your live forms for review.

5. **Set up production server in CiviCRM**  
   Update the server URL in CiviCRM to the production server address provided by USPS.

### Important notes

- The USPS User ID must not be shared outside your organization or used on multiple websites.
- Address standardization runs automatically during contact imports, so consider disabling it or limiting imports to addresses only.
- Not all addresses will validate; some may return errors if they do not match USPS records.
- If you develop websites for clients, each client needs their own Web Tools ID.

## Support and contacts

- USPS Internet Customer Care Center (ICCC) is available from 7:00 AM to 11:00 PM Eastern Time.
- Email: icustomercare@usps.com
- Phone: 1-800-344-7779

Use this contact for questions about API access or terms of service.

## Summary

By following this guide, you can configure address formats and enable USPS address standardization in CiviCRM to improve the accuracy of your mailing data and streamline communication with your contacts. This setup helps non-profit organizations maintain clean and reliable address information for their outreach efforts.
