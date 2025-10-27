---
categories:
  - Tutorial  
level: Basic  
summary: This tutorial guides non-profit users through managing surveys in CiviCRM, including reserving respondents, interviewing them, reviewing survey results, and conducting door-knock canvasses.  
section: Everyday tasks  
---

# managing surveys with CiviCRM

## overview  
This tutorial helps you learn how to manage surveys in CiviCRM step-by-step. You will find out how to reserve respondents, conduct interviews, review survey results, and prepare walk lists for door-to-door canvassing.

## viewing and managing surveys  
To start, go to **Campaign > Dashboard > Surveys**. Here you can see all your surveys. Use the links on the right side to manage existing surveys or click **Add Survey** to create a new one.

## reserving respondents  
Before interviewing, you need to select the group of people you want to survey. This is called *reserving respondents*. You can divide large groups into smaller sets to make the process easier.

To reserve respondents:  
1. Go to **Campaigns > Reserve Respondents**.  
2. Select your survey from the **Survey** dropdown.  
3. Choose the group of contacts you want to interview from the **Group(s)** dropdown.  
4. Optionally, add filters like street address or city to narrow down your list.  
5. Click **Search**.  
6. On the results page, select individuals or choose **All n records** to reserve everyone found.  
7. Click **Go**, then on the next screen click **Reserve** to confirm.

**Note:** For large door-to-door surveys, enable address parsing under **Administer > Administration Console > Configuration Checklist > Address Settings** by checking *Street Address Parsing*. This breaks down addresses into street name, unit, and number for easier filtering.

## interviewing respondents  
To record survey answers:  
1. Go to **Campaign > Interview Respondents**.  
2. Select your survey and group, then click **Search**.  
3. Choose individuals or select all contacts.  
4. Click **Go to record survey responses**.  
5. For each person, enter their answers and select the response status (e.g., Completed, No Answer).  
6. Click **Record Response**.  
7. When finished, click **Done** to return, or use **Release Respondents** if you want to free contacts for others to interview.

## reviewing survey results  
After collecting responses, program leads can review survey results in **Reports and Analysis** to understand outcomes and plan next steps.

## creating walk lists for door-knocking  
If your survey involves door-to-door canvassing, you can print walk lists for volunteers:  
1. Go to **Reports > Create Templates from Reports > Survey Report (Detail)**.  
2. In **Display Columns**, check *Street Number*, *Street Name*, *Street Unit*, and *Survey Responses*.  
3. In **Group By Columns**, check *Street Name* and *Odd/Even Street Number*.  
4. In **Set Filters**, select your survey name and set *Respondent Status* to *Reserved*.  
5. Click **Preview Report** and then **Print Preview**.  
6. Print the report, which includes a cover sheet with survey questions and is sorted by street name and number.

## conducting your door-knock canvass  
Volunteers use the printed walk lists to visit respondents and collect answers in person.

## recording responses from canvassing  
After canvassing sessions:  
1. Go to **Campaigns > Interview Respondents**.  
2. Enter your survey and group names, and optionally a street name to narrow the list.  
3. Select contacts and click **Go**.  
4. Enter responses matching the walk list and click **Record Response**.

This completes the process of managing surveys in CiviCRM, helping your non-profit gather valuable data efficiently.
