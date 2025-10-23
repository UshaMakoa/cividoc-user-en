---
categories:
  - Uncategorized
  - Guide  
level: Basic  
summary: This guide explains how to create and customize search displays in CiviCRM to show your search results in different formats, helping non-profit users present data clearly and usefully.  
section: Searching and reporting  
---

# Search displays

## What are search displays?

Search displays let you show the results of your saved searches in different ways on your CiviCRM site. They help you present your data clearly and make it easier for you and your team to use search results for your work.

## Adding a search display

Each saved search can have zero, one, or many displays. This means you can show the same search results in different formats depending on your needs.

To add a display:

- Open your saved search for editing.
- Click the **Add...** button on the left side.
- Choose the type of display you want.

## Default display

By default, every search can be shown as a simple table when you click the **Search** button. This default table can be viewed on its own page or embedded in a form without creating a separate display.

However, creating your own display allows you to customize how the results look and behave.

## Types of displays

When you add a display, you can choose from several types:

- **Table**: Shows results in rows and columns, with options to sort, page through, and take actions on rows. You can change how rows and columns look.
- **List**: Shows results in one or more lines, with flexible styling for each field.
- **Grid**: Displays items side-by-side, great for image galleries or similar layouts.
- **Tree**: Shows hierarchical data in a nested tree format.
- **Data Entry**: Lets you enter or edit data in a spreadsheet-like form.
- **Autocomplete**: Provides live search suggestions as you type, which can be customized and used in forms.
- **DB Entity**: Creates a database table or view accessible by SearchKit, API, or SQL tools.

## Additional display types from extensions

You can add more display types by installing extensions from the Extensions Directory, such as:

- **ChartKit**: For charts and graphs.
- **SearchKit Calendar**: For time-based event displays.
- **SearchKit Maps**: To show locations on maps.
- **SearchKit Tokens**: To create custom tokens for mailings.
- **SearchKit Column Display**: To stack fields in columns.

Check the Extensions Directory regularly for new options.

## Customizing your search display

Each display can be tailored with settings like:

- Which fields to show and in what order.
- Column headers and labels.
- Sorting options.
- Links in the results.
- Inline editing features.
- Who can see the display (permissions).
- Styling and formatting.
- Pagination (how many results per page).

## Changing how results appear (rewriting fields)

You can customize how data fields show up in your display using:

### Basic field combining

Join multiple fields together using square brackets:

```
[first_name] [last_name]
[street_address], [city] [postal_code]
```

This will show combined values like "Jane Smith" or "123 Main St, Springfield 12345".

### Smarty syntax for advanced formatting

For more control, use Smarty template code with curly braces `{}`:

- Conditional display example:

```
{if $nick_name}[nick_name]{else}[first_name]{/if} [last_name]
```

- Math example:

```
{$total_amount - $fee_amount}
```

- Value transformation example:

```
{if $age_years >= 18}Adult{else}Minor{/if}
```

### Tips for rewriting

- Use square brackets `[field_name]` to insert field values.
- Use `{$field_name}` in Smarty to get raw values (e.g., numbers without currency formatting).
- Smarty modifiers like `|date_format` or `|crmMoney` help format dates and money.
- You can mix square bracket and Smarty syntax as needed.
- Remember, rewritten fields only change what users see; they do not change the stored data.

## Summary

Search displays are a flexible way to show your search results in CiviCRM. By choosing the right display type and customizing it, you can make your data easier to understand and work with, even if you are new to the system.
