# Source: https://docs.civicrm.org/user/en/latest/common-workflows/automating-tasks/

# Creating custom fields and tokens

## Why create custom fields?

Custom fields let you store specific information your organization needs to automate tasks. For example, you might track whether a donor wants a tax receipt or which fund their donation supports.

## Best practices for custom fields

- Use dropdown menus or radio buttons instead of free text to keep data consistent.  
- Avoid creating many yes/no fields when a single dropdown with multiple options works better.  
- Plan fields carefully to make reporting and searching easier later.

## Using custom tokens

Tokens are placeholders you can insert into emails or documents that CiviCRM replaces with real data, like a donor’s name or donation amount. Creating custom tokens based on your custom fields lets you personalize communications automatically.

## How to create custom fields and tokens

Use the Administrator Console in CiviCRM to add custom fields. Then, create custom tokens linked to those fields to use in your templates.