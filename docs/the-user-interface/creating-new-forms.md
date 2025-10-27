---
categories:
  - Guide  
level: Basic  
summary: This guide explains how to create and customize forms in CiviCRM using the FormBuilder extension, helping non-expert nonprofit users build simple forms for tasks like activity tracking and contact management.  
section: Customising the user interface  
---

# FormBuilder

## What is FormBuilder?

FormBuilder is a CiviCRM extension that lets you create your own custom forms easily. It is useful when you need a form with just a few fields, for example, to quickly create and assign activities like scheduling phone calls. Once enabled, you can find FormBuilder under **Administer > Customize Data and Screens**.

## Enabling FormBuilder

If FormBuilder is not already installed, you can enable it on the **Extensions** page in CiviCRM. After enabling, the FormBuilder link will appear in the menu.

## Creating a form

1. Go to **Administer > Customize Data and Screens > FormBuilder**.
2. Click to create a new form.
3. Choose the type of form you want to build (currently, activity and contact forms are available).

## Configuring form settings

The form settings screen has two main parts:

- **Left pane (configuration):**  
  - Set the form title (required) and description (recommended for clarity).  
  - Choose the permission needed to access the form.  
  - Define the URL path for the form (must start with `civicrm/`).  
  - Decide if the form should be accessible on your website front end.  
  - Optionally add the form to the navigation menu.  
  - Choose where the form is exposed (e.g., Contact Layout editor, dashlets, or tokens).  
  - Enable logging of form submissions if needed.

- **Right pane (layout):**  
  - See a live preview of the form.  
  - Drag and drop fields to build the form layout.  
  - Customize field settings such as making fields required, adding default values, and showing or hiding labels.  
  - Add text blocks or HTML containers to organize fields visually.

## Building the form layout

- Use the second tab in the left pane to select fields related to the chosen contact or activity type.
- Drag fields into the layout pane on the right and arrange them as needed.
- Click on fields to rename labels, add placeholder text, or change input styles (e.g., switch to a rich text editor).
- Group fields into containers and save these as reusable blocks to use on other forms.

## Using URL filters with forms

You can set default filter values in search forms by adding parameters to the URL. For example, adding `#?haircolor=brown` to the form URL will filter results by hair color brown automatically. Multiple filters can be combined with `&`.

This also works for setting default values in submission forms. For instance, a signup form URL can preset fields like hair color or event name, which users can change before submitting.

## Setting up secret links for forms

FormBuilder supports "secret links" (similar to checksums in other CiviCRM forms) that allow users to access pre-filled forms securely via unique URLs sent by email.

To enable this:

- On the form tab, set permissions to one of the generic options like "Anyone with secret link".
- Set the form’s page route (URL path) and enable front-end access.
- Expose the form to message tokens.
- On the individual tab, set security to "Form-Based", enable autofill for the current user, and allow update actions.

This setup allows users to access forms with pre-filled data securely without logging in.
