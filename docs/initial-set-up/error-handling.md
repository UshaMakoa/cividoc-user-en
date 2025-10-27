---
categories:
  - Tutorial
level: Basic
summary: This guide helps non-profit users understand how to manage error handling in CiviCRM to ensure smooth operation of their systems.
section: Initial set up
---

# Error handling in CiviCRM

When using CiviCRM, it's important to know how to handle errors effectively to keep your system running smoothly. This guide will walk you through the basic steps to set up error handling in CiviCRM, making it easier for you to troubleshoot issues as they arise.

## Understanding error handling

Error handling in CiviCRM allows you to manage how errors are displayed and logged. This is particularly useful for non-technical users who want to ensure that they can address issues without needing extensive programming knowledge.

## Setting up error handling

1. **Access the error handling settings:**
   To begin, navigate to the "Administer" section in your CiviCRM dashboard. From there, go to "System Settings" and then select "Debugging and Error Handling."

2. **Customize error display:**
   - **Fatal Error Template:** If you'd like to create a custom screen for displaying fatal errors, enter the path and filename for your Smarty template here. This allows you to provide a user-friendly message when something goes wrong.
   - **Fatal Error Handler:** If you want to override the built-in error handling, you can specify a custom PHP error-handling function by entering its path and class here.

3. **Save your changes:**
   Once you've made your adjustments, click "Save" to apply your changes. If successful, you will see a message confirming that "Your changes have been saved."

## Conclusion

By setting up error handling in CiviCRM, you can create a more user-friendly experience for yourself and your team. This ensures that when issues arise, they can be addressed quickly and effectively, allowing you to focus on your important work in the non-profit sector.

If you have further questions or need assistance, don't hesitate to reach out for help. You're not alone in this journey!
