---
categories: Guide
level: Basic
summary: Step-by-step instructions for non-profit staff to carry out everyday civic engagement tasks in CiviCRM, such as door-knock canvassing, phone banking, and mobilizing event participants.
section: Civic Engagement > Everyday Tasks
---

# Everyday civic engagement tasks

## Conducting a door-knock canvass

Door-knock canvassing helps your organisation connect with community members by visiting them at home and recording their responses to surveys. Here’s how you can organise and carry out a door-knock canvass using CiviCRM:

### 1. Create the campaign and survey for your walk list

- Make a new group of contacts you want to visit. You can search for people in a specific area or district.
- If you haven’t already, create a campaign: go to **Campaigns > New Campaign** and add your group of contacts.
- Create a new survey: go to **Campaigns > New Survey**, give it a title, and link it to your campaign.
- For **Activity Type**, choose **WalkList**.
- For **Profile**, select the custom profile you made for this survey.
- For **Survey Responses**, choose **Use existing result set** and select **Survey Default Results Set Options**.
- Click **Save**.

### 2. Reserve the target group you want to survey

- Go to **Campaigns > Reserve Respondents** and pick your survey.
- Select your target group in **Group(s)** and click **Search**.
- On the results screen, select the contacts you want to survey and click **Go to Reserve Respondents**.
- On the next screen, click **Reserve**.

### 3. Create your WalkList report

- Go to **Reports > Create Templates from Reports > Survey Report (Detail)**.
- In **Display Columns**, select: Street Number, Street Name, Street Unit, Survey Responses.
- In **Group By Columns**, select: Street Name, Odd/Even Street Number.
- In **Set Filters**, choose your survey name. For **Respondent Status**, select **Is Equal to** and **Reserved**.
- Click **Preview Report**, then **Print Preview**.
- Print your report. The printout will be sorted by street and include a cover sheet with response codes.

### 4. Conduct your door-knock canvass

- Volunteers or staff visit each address on the WalkList and record responses on the printed sheets.

### 5. Record responses from the canvass

- After canvassing, go to **Campaigns > Interview Respondents**.
- Enter the survey name and the target group (and street name if needed).
- On the results screen, select the contacts and click **Go**.
- Enter the responses from your WalkList sheets and click **Record Response**.

### 6. Review the results

- Program leads can review survey results using the reporting features in CiviCRM (see the Reports and Analysis chapter).