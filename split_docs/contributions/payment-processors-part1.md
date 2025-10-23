# Source: https://docs.civicrm.org/user/en/latest/contributions/payment-processors/

To re-write the documentation on payment processors for non-profit users of CiviCRM using the Diátaxis framework, you can structure it as follows:

### Categories and Level
Given the content, the page can be categorized as a **Guide** because it provides specific instructions and considerations for selecting and setting up payment processors. The level can be considered **Intermediate** since it assumes some familiarity with CiviCRM and payment processing concepts.

### Summary
Here is a one-sentence summary for the top of the page:
"Learn how to select and configure payment processors in CiviCRM, including considerations for onsite vs. offsite processors, regional availability, and managing recurring contributions."

### Markdown Structure
Here is how you can structure the page in Markdown:

```markdown
---
categories: Guide
level: Intermediate
summary: Learn how to select and configure payment processors in CiviCRM, including considerations for onsite vs. offsite processors, regional availability, and managing recurring contributions.
section: Contributions
---

# setting up payment processors
## introduction to payment processors
CiviCRM supports a variety of payment processors, both out-of-the-box and through community contributions. This guide will help you understand how to choose and set up a payment processor for your organization.

## selecting a payment processor
When choosing a payment processor, consider factors such as cost, suitability for your use case, and availability. It's beneficial to consult with similar organizations about their experiences.

### onsite vs. offsite processors
- **Onsite Processors**: Allow users to enter credit card details directly on your site, providing a seamless experience. However, they require an SSL certificate for security.
- **Offsite Processors**: Transfer users to another site for payment, which can lead to a less seamless experience but doesn't require an SSL certificate.

## regional availability
Ensure the payment processor supports your local currency. If not, consider developing a custom processor or seeking third-party assistance.

## merchant account vs. built-in
Most organizations use a merchant account, but some processors like PayPal do not require one.

## support for recurring contributions
Not all processors support recurring contributions within CiviCRM. Some require management through the processor's portal.

## managing recurring contributions
For processors that support recurring contributions within CiviCRM, you can manage them directly from the Contributions tab on a contact record.

## cost considerations
The cost-effectiveness of a payment processor depends on transaction volume and fees. Consider monthly fees vs. commission rates.

## usability and support
Ensure the payment workflow is intuitive and supported by either CiviCRM or the community.

## setting up a payment processor
1. Go to Administer > System Settings > Payment Process.
2. Click on New Payment Processor and select the processor type.
3. Assign a name and description, and select a financial account.
4. Make the processor active and fill in live and test payment details.

## testing payments
Use dummy payment processors for testing purposes.

### writing a new payment processor
If needed, you can develop a custom payment processor integration.

```

### Suggestion for Splitting Content
If the content becomes too extensive, you might consider splitting it into separate pages for:
- **Introduction to Payment Processors**: Overview of available processors and their types.
- **Selecting a Payment Processor**: Detailed considerations for choosing a processor.
- **Setting Up a Payment Processor**: Step-by-step guide for configuration.
- **Managing Recurring Contributions**: Specific instructions for handling recurring payments.
- **Customizing Payment Processors**: Information on developing custom processors.

Each page can be tailored to focus on a specific aspect of payment processors, making the documentation more manageable and user-friendly. 

```plaintext