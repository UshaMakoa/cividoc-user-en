---
categories: Guide
level: Basic
summary: Learn how to use and customize the CiviCRM menu, dashboard, and dashlets to access features and display key information for your organisation.
section: Customising the user interface
---

# Menu, dashboard, and dashlets

## Using the navigation menu

The **navigation menu** is always at the top of every CiviCRM page and helps you quickly access different features. The menu includes areas for:

- **Quick search**: Find a contact by name, email, or custom field.
- **Menu search and logout**: Search all menu items or log out.
- **Search**: Search your CRM data.
- **Contacts**: Find, add, and manage contacts.
- **Contributions**: Search and manage donations and contribution pages.
- **Events**: Create and manage event registrations.
- **Mailings**: Send bulk emails and view mailing history.
- **Reports**: Access and generate reports.
- **Administer**: Configure system settings and custom data.

## Quickly finding menu items

If you’re not sure where something is in the menu, you can use the **menu search**:

- Hover your mouse over the CiviCRM logo in the top bar (next to the quick search).
- A panel appears with a search field and a list of menu items.
- Click the search field and start typing part of a menu item name, such as “display preferences” or “groups”.
- The list will filter to show only matching items.
- Click the item you want to go straight to that page.

This helps you find features quickly without remembering the whole menu structure.

## Modifying the menu

You can change the navigation menu to fit your organisation’s needs:

- Go to **Administer > Customize > Navigation Menu**.
- Add, disable, or rearrange menu items as needed.

**Note:** Any changes you make will affect everyone with permission to see the menu. Be careful when editing, as this impacts all users.

## The home dashboard and dashlets

When you log in, you’ll see the **dashboard** (CiviCRM Home). The dashboard shows important information using **dashlets**—small reports or summaries.

Some common dashlets include:

- **Donor report**: A bar graph showing total contributions.
- **Activities**: A list of recent activities (emails, donations, meetings, etc.).
- **Membership report**: A table summarizing member information by month (number of members, payments, contributions, etc.).

You can add dashlets to your dashboard:

1. Click **Configure Your Dashboard**.
2. Drag dashlets into the left or right column.
3. Click **Done** to save.

Your dashboard will update each time you log in. To see the latest data, click **Refresh Dashboard Data**. Dashlets are cached for performance, but you can adjust how often they refresh by editing their report settings.

## Creating and adding custom dashlets

You can create new dashlets from any CiviReport:

1. Go to **Reports > My Reports** and click **New Report**.
2. Choose a report template.
3. Set up the report using the **Columns**, **Sorting**, and **Filters** tabs (for example, filter by “This Year”).
4. Click **View results**.
5. Choose the display style (Tabular, Bar Chart, Pie Chart).
6. On the **Access** tab, select **Available for Dashboard?** so users with permission can add it.
7. Click **Actions > Create Report**.

To add your new dashlet to the dashboard:

1. Go to the CiviCRM menu and click **CiviCRM Home**.
2. Click **Configure Dashboard**.
3. Drag your new dashlet from the “Available Dashlets” box to the column you want.
4. Click **Done**.

You can use Search Kit with FormBuilder to add dashlets as well. See the FormBuilder section for more details.

# comment: Source: https://docs.civicrm.org/user/en/latest/customising-the-user-interface/menu-dashboard-and-dashlets/
# comment: Suggestion: This page is a Guide because it provides step-by-step instructions for specific tasks (using and customizing the menu, dashboard, and dashlets), without focusing on background or exhaustive technical details. The level is Basic, as it is aimed at new or non-expert users. If needed, reference material about dashlet/report settings or a separate tutorial for first-time dashboard setup could be split off for clarity.