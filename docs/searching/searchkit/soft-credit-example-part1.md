---
categories:
  - Uncategorized
  - Guide
level: Intermediate
summary: Step-by-step instructions for creating a soft credit search and table display in CiviCRM, helping you recognize and thank supporters who helped raise donations.
section: Searching and reporting
---

# Create a soft credit search and display

## What are soft credits?

Soft credits in CiviCRM let you acknowledge people who helped bring in a donation, even if they didn’t give it themselves. For example, if someone asks friends to donate for their birthday, those friends’ gifts can be “soft credited” to the organizer. This helps you thank everyone involved and understand who your most effective fundraisers are.

## Before you begin

You’ll need access to CiviCRM and permission to use Search Kit. No technical expertise is required—just follow the steps below. If you’re new to searching in CiviCRM, consider starting with a basic contact search to get comfortable with the interface.

## Step 1: Start a new search

- Go to **Search** > **Search Kit**.
- Click **New Search** to begin.
- Give your search a clear name, like “Soft Credit Fundraisers.”
- (Optional) Add a tag, such as “Fundraising,” to help organize your searches.

## Step 2: Choose your entities

- The default entity is **Contacts**. For soft credits, select **Contribution Soft Credits** from the dropdown.
- To see details about the actual donation and donor, click **+Entity** and add **Contribution** and **Contact**.
- Search Kit will automatically link these entities using contribution and contact IDs.

## Step 3: Set your filters

- In the **Where** section, you can limit results to a specific date range (e.g., January 1, 2021 to April 30, 2022).
- To focus on donations only, add a filter for **Financial Type = Donation**.
- You can add other filters as needed for your reporting.

## Step 4: Select your fields

- By default, you’ll see basic fields like ID and name.
- Click **Add** to include more fields, such as:
  - **Soft credit amount**
  - **Soft credit type**
  - **Contributor name** (the person who made the donation)
  - **Contribution amount**
  - **Contribution date**
  - **Contribution source**
  - **Contribution status**
  - **Payment method**
- Remove any fields you don’t need by clicking the trash icon.
- Click **Search** to see your results.

## Step 5: Transform your fields (optional)

- Under **Field Transformations**, you can customize how fields appear.
- For example, make the contributor’s name uppercase or show only the date (not the time) for the contribution.
- Click **Search** again to see your changes.

## Step 6: Save your search

- Click **Save** in the top right to keep your search for future use.
- You can always come back and edit it later.

## Step 7: Add a table display

- Click **Add...** and choose **Table**.
- Give your table a name, like “Soft Credit Fundraisers Table.”
- Reorder columns by dragging them, or remove columns you don’t need.
- You can add a menu column with links to view the soft credit contact, contributor, or contribution.
- Click **Save** to keep your table.

## Step 8: View and share your results

- Click **View Results** to see your table.
- You can copy the table’s URL and add it to your CiviCRM menu for easy access by your team (**Administer > Customize Data and Screens > Navigation Menu**).

## Tips for success

- **Save often** to avoid losing your work.
- **Name your searches and tables clearly** so others can understand their purpose.
- **Experiment with filters and fields** to get the exact report you need.
- **Share your results** with colleagues who manage thank-yous and donor recognition.
