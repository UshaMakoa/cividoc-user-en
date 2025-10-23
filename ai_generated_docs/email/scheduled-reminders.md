---
categories: Tutorial
level: Intermediate
summary: Learn how to create and test a scheduled reminder in CiviCRM, step by step.
section: Email and communications
---

# Creating and testing a scheduled reminder

Once you understand how reminders work, you can create your first one.

This tutorial walks you through building and testing a reminder in CiviCRM to automate communications.

## Step 1: Create a new reminder
1. Go to **Mailings → Scheduled Reminders**  
2. Click **Add Reminder**  
3. Give your reminder a title, e.g. “Membership Renewal — 30 Days Before Expiry”  
4. Choose the **entity type** (Membership, Event, or Activity)

## Step 2: Set the timing
- Choose to send **before**, **on**, or **after** a date.  
- Enter how many days before or after.  
- Optionally, repeat the reminder for follow-ups.  

## Step 3: Select recipients
- Membership: members of a type  
- Event: registered participants  
- Activity: assignees or target contacts  
- Filter further by group, tag, or status.  

## Step 4: Write your message
Use tokens for personalisation:

> Hi {contact.first_name},  
> Your membership will expire on {membership.end_date}.  
> Please renew today to keep your benefits active.

## Step 5: Choose delivery method
- **Email** → for contacting supporters  
- **Activity** → for internal tasks or teams  

## Step 6: Test your reminder
1. Create a test record.  
2. Trigger the scheduled job manually.  
3. Verify that the reminder sends correctly.  

## Step 7: Activate
Once satisfied, **Save** and **Enable** the reminder.  

## Best practice
- Test new reminders with internal contacts.  
- Use clear subject lines.  
- Review timing carefully.
