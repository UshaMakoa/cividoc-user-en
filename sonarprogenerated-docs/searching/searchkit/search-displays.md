---
categories: Reference
level: Basic
summary: Learn about the different ways you can display and customize search results in CiviCRM using Search Displays, including available display types, configuration options, and useful extensions.
section: Searching and reporting > Search Kit
---

# Search displays

## What are search displays?

Search displays in CiviCRM let you show search results in different formats, making it easier for your organisation to share and use data from SearchKit. You can present the same search in multiple ways, depending on your needs.

## Adding a display

- You can add zero, one, or multiple displays to any saved search.
- To add a display, click the **Add...** button on the left side when editing your saved search.
- By default, every search can be shown as a simple table when you click the “Search” button.
- The default table can be viewed on its own or embedded in a form, but creating your own display lets you customise how results appear.

## Display types

When you add a new display, you can choose from several types:

- **Table**: Shows results in rows and columns, with options for paging and actions. You can adjust how each row and column looks.
- **List**: Presents results in lines, with each field styled separately or given a custom CSS class.
- **Grid**: Useful for showing images or content side-by-side, like a gallery.
- **Tree**: Displays hierarchical data in a nested structure.
- **Data entry**: Provides a spreadsheet-like form for entering or updating data in batches.
- **Autocomplete**: Shows results as you type in a field. You can customise how each result looks in the dropdown. These displays can be used in FormBuilder or set as the default autocomplete for forms.
- **DB entity**: Creates a database table or view for use with SearchKit, the API, or other SQL tools.

## Additional extensions

You can add more display options by installing extensions from the Extensions Directory:

- **ChartKit**: Visualise data with charts and graphs (included with CiviCRM core).
- **SearchKit Calendar**: Show events and activities on a calendar.
- **SearchKit Maps**: Display the location of contacts or events on a map.
- **SearchKit Tokens**: Create custom tokens for mailings using SearchKit.
- **SearchKit Column Display**: Stack fields into columns for a different look.
- And more—check the Extensions Directory for the latest options.

## Configuration options

Each display can be customised with settings, including:

- Which fields to show and in what order
- Column headers and labels
- Sorting options
- Links to other pages or actions
- Inline editing (edit data directly in the display)
- Permissions (who can see or use the display)
- Styling and formatting
- Pagination (how many results per page)
- How results are formatted or rewritten

## Rewriting results in search displays

You can change how data appears using field rewriting:

### Basic field combining

- Combine fields with square brackets to create custom text.
- Example: `[first_name] [last_name]` shows “Jane Smith”.
- Example: `[street_address], [city] [postal_code]` shows “123 Main St, Springfield 12345”.

### Smarty rewrites

For more advanced formatting, use Smarty template syntax with curly brackets:

- **Conditional display**: `{if $nick_name}[nick_name]{else}[first_name]{/if} [last_name]`
- **Math operations**: `{$total_amount - $fee_amount}`
- **Value transformation**: `{if $age_years >= 18}Adult{else}Minor{/if}`

### Tips for rewriting

- Field names in square brackets (like `[display_name]`) are automatically replaced with their values.
- Use `{$field_name}` in Smarty code to get raw values (e.g., 125 instead of $125.00).
- Smarty modifiers like `|date_format` and `|crmMoney` help with formatting.
- You can mix square bracket and Smarty syntax in the same rewrite.
- Rewritten fields only affect how data is displayed—they do not change the underlying data.

# comment: Source: https://docs.civicrm.org/some/page/
# comment: This page is best classified as Reference because it systematically lists and describes the options, features, and configuration settings for Search Displays. It does not provide step-by-step instructions (Tutorial), solve a specific problem (Guide), or explain underlying concepts (Explanation). For non-expert users, splitting out a simple Tutorial ("How to add a Search Display") and a Guide ("How to create a custom display for a specific use case") could be helpful.