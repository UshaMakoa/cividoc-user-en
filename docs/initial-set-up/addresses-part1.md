---
categories:
  - Tutorial
level: Basic
summary: This guide provides a step-by-step approach to setting up and managing address settings in CiviCRM, tailored for non-profit users.
section: Addresses
---

# Managing addresses in CiviCRM

In this tutorial, we will explore how to set up and manage address settings in CiviCRM. Understanding how to handle addresses effectively is crucial for maintaining accurate contact information and improving communication with your supporters.

## Address settings overview

CiviCRM allows you to customize how addresses are formatted and displayed. You can set up mailing labels, address formatting, and even integrate with the United States Postal Service (USPS) for address standardization.

### Mailing labels

Mailing labels are essential for sending out communications. Here’s how to format them:

1. **Individual Name Format**: This determines how individual names appear on your labels. The default format is:
   ```
   {individual_prefix} {first_name} {middle_name} {last_name}
   ```

2. **Mailing Label Format**: You can customize how addresses are displayed on mailing labels. The standard format is:
   ```
   {contact_name}
   {street_address}
   {supplemental_address_1}
   {supplemental_address_2}
   {city}, {state_province} {postal_code}
   {country}
   ```

### Address formatting

Address formatting is important for how addresses are displayed in your system. You can choose to show the state/province as either an abbreviation or the full name. The standard format is:
```
{street_address}
{supplemental_address_1}
{supplemental_address_2}
{city}, {state_province} {postal_code}
{country}
```

### Maximum locations

You can set the maximum number of addresses allowed for each contact. This helps in managing multiple addresses for individuals or organizations.

### Address standardization

CiviCRM offers an optional plugin to standardize addresses using USPS. This ensures that addresses are accurate and formatted correctly. Here’s how to set it up:

1. **Register for USPS Web Tools ID**: Go to the USPS registration page and apply for a User ID. This ID is necessary for using their services.

2. **Request access to the Address Information API**: After receiving your Web Tools ID, you need to request access to the Address Information API. This involves providing details about how you will use the API.

3. **Testing requests**: Before gaining access to the production server, you’ll need to send test requests using your Web Tools ID. This helps USPS verify that your setup is correct.

4. **Accessing the production server**: Once approved, you can set up CiviCRM to access the USPS production server for real-time address standardization.

5. **Important notes**: Ensure that you comply with USPS terms of service to avoid losing access. Each organization needs its own Web Tools ID, and sharing it can lead to termination of service.

By following these steps, you can effectively manage addresses in CiviCRM, ensuring that your data is accurate and up-to-date. This not only enhances your communication efforts but also supports your organization's mission.
