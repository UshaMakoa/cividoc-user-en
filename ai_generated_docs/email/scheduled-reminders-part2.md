---
categories: Explanation
level: Basic
summary: Understand what scheduled reminders are, how they work, and why they're useful for automating communications in CiviCRM.
section: Email and communications
---

# Understanding scheduled reminders

Scheduled reminders are automated messages that CiviCRM sends based on dates or events in your database.

They save time, reduce manual work, and make sure important messages always go out on schedule.

## What scheduled reminders do

Scheduled reminders automatically find contacts who meet certain conditions — for example, members whose renewal date is approaching — and send them an email or log an activity.

Common uses include:

- Membership renewal notices  
- Event confirmations or follow-ups  
- Payment or invoice reminders  
- Case or task deadlines  
- Thank-you messages after donations or registrations  

By automating these communications, you ensure consistency and avoid missed tasks.

## How scheduled reminders work

CiviCRM runs a background process (a **scheduled job**) that checks for reminders to send.

It looks for records matching your chosen criteria and triggers emails or activities at the right time.

Examples:

- A reminder set for “7 days before membership end date” will message members whose memberships expire next week.  
- A reminder set for “1 day after event start” could thank attendees automatically.  

## Why use scheduled reminders

Reminders help non-profit organisations maintain consistent communication while reducing workload.

They let you:

- Stay on top of renewals and deadlines  
- Improve supporter engagement and retention  
- Reduce missed opportunities  
- Keep messages timely and professional  

Once set up, reminders run automatically so your staff can focus on other priorities.

## Checking if reminders are enabled

To use reminders, the **Send Scheduled Reminders** job must be active.

Admins can verify this under:

> **Administer → System Settings → Scheduled Jobs**

If reminders are not being sent, check that this job is enabled and scheduled to run frequently enough.

## Best practice

- Start with one or two core reminders (e.g. membership renewals).  
- Test each before expanding to new workflows.  
- Keep reminder text clear and helpful, especially for billing or renewal messages.
