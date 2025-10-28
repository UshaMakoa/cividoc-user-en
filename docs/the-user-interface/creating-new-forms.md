---
categories:
  - Tutorial
level: Basic
summary: Learn how to create, configure, and customize forms in CiviCRM using FormBuilder, step by step, designed for non-profit users with no technical background.
section: Customising the user interface > FormBuilder
---

# Creating forms with FormBuilder

## Introduction

FormBuilder is a tool in CiviCRM that lets you create custom forms for your organisation’s needs, such as collecting information or scheduling activities. You don’t need to be a technical expert to use FormBuilder, and this guide will walk you through each step.

## Step 1: Enable FormBuilder

- Go to your CiviCRM dashboard.

- Navigate to **Administer > System Settings > Extensions**.

- Look for **FormBuilder** (sometimes called Afform). If it’s not enabled, click to install or enable it.

Once enabled, you’ll see a **FormBuilder** link under **Administer > Customize Data and Screens**.

## Step 2: Create a new form

- Click on **Administer > Customize Data and Screens > FormBuilder**.

- Click **Add Form** or **New Form**.

- Choose the type of form you want to create (for example, for activities or contacts).

*Note: Currently, you can make forms for activities, contacts, and some other types. More types may be added in future versions.*

## Step 3: Configure form settings

On the left side of the screen, you’ll see the configuration panel:

- **Title**: Give your form a clear name. This will show up on the form itself.
- **Description**: Add a short description to help users understand what the form is for.
- **Permission**: Choose who can access the form (e.g., only logged-in users, anyone with a special link, or all users).
- **URL**: Set the web address for your form. It must start with `civicrm/`.
- **Front-end access**: Tick the box if you want the form to be available on your website.
- **Navigation menu**: Tick the box to add the form to your site’s menu.
- **Expose to**: Decide if the form should be available in other areas, like the Contact Layout editor or dashlets.
- **Log submissions**: Choose whether to keep a record of form submissions.

## Step 4: Build your form layout

On the right side, you’ll see the layout panel:

- Drag and drop the fields you want from the left onto the layout area.

- You can rearrange fields and group them using containers.

- Use formatting options to add text blocks or HTML for instructions or section headings.

## Step 5: Customize fields

For each field, you can:

- Change how data is entered (for example, use a rich text editor for detailed answers).

- Mark fields as required or optional.

- Set default values.

- Show or hide the label.

- Add help text before or after the field.

- Rename labels or add placeholder text for guidance.

## Step 6: Save and use reusable blocks

- If you create a group of fields you’ll use often, save them as a block. You can reuse blocks in other forms, saving time and keeping things consistent.

- To update a block, edit it once and all forms using it will update automatically.

## Step 7: Set preset values

- At the top of the left panel, use the **Values** section to set preset data, such as default status or who added the activity.

- This is useful for forms that need to keep certain information the same every time.

## Step 8: Save and publish your form

- Review your form layout and settings.

- Click **Save**.

- Share the form’s URL with your team or add it to your website as needed.

## Tips

- You can always go back and edit your form later.

- Test your form by submitting sample data to check everything works as expected.

- Ask for feedback from colleagues to make sure the form is clear and easy to use.

<!--
Source: https://docs.civicrm.org/some/page/
 -->

<!--
This page is a Tutorial because it provides a step
-by-step walkthrough for first-time users to create and configure forms using FormBuilder. It does not focus on solving a specific problem (Guide), list exhaustive options (Reference), or explain underlying concepts (Explanation). The level is Basic, suitable for non-expert non-profit users. If more advanced features or troubleshooting steps are added, those could be split into separate Guides or Reference pages. -->
