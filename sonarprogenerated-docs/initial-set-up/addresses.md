---
categories: Reference
level: Basic
summary: This page explains how to set up and manage address formats and address standardization in CiviCRM, including options for mailing labels and integration with USPS for US addresses.
section: Initial set up > Addresses
---

# Address settings

## Mailing labels

- **Individual name format**: Choose the order and fields for individual contact names on mailing labels. The default format is: `{individual_prefix} {first_name} {middle_name} {last_name}`.
- **Mailing label format**: Use tokens to customize how addresses appear on mailing labels. To include the contact name, use the `{contact_name}` token. For US addresses, use `{state_province}` for abbreviations or `{state_province_name}` for the full name.
- **Standard mailing label format**:
  ```
  {contact_name}
  {street_address}
  {supplemental_address_1}
  {supplemental_address_2}
  {city}, {state_province} {postal_code}
  {country}
  ```

## Address formatting

- **Address formatting**: Use tokens to set how addresses display in CiviCRM. The standard format is:
  ```
  {street_address}
  {supplemental_address_1}
  {supplemental_address_2}
  {city}, {state_province} {postal_code}
  {country}
  ```
- **Maximum locations**: Decide how many addresses you want to allow per contact.
- **Include county?**: Choose whether to add a County field to contact address forms.

## Address standardization

- CiviCRM can connect to the United States Postal Service (USPS) Address Standardization service, which helps ensure US addresses are formatted correctly.
- To use this, you must register with USPS for a Web Tools ID and get approval. Once approved, USPS will provide a User ID and service URL.
- **Provider**: Currently only 'USPS' is supported.
- **User ID**: Enter the USPS-provided User ID.
- **Web service URL**: Enter the USPS-provided URL.
- Click **Save** to apply changes or **Cancel** to discard.

---

# comment: Source: https://docs.civicrm.org/some/page/
# comment: This page is a Reference because it lists configuration options and factual details about address settings and standardization, without step-by-step instructions or conceptual background. For non-experts, this content is best kept concise and factual. If users need step-by-step help integrating USPS, that should be split into a Guide or Tutorial page.