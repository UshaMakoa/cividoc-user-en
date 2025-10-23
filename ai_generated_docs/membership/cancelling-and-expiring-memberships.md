---
categories: Guide  
level: Advanced  
summary: This guide explains how to automate common membership tasks in CiviCRM using CiviRules.
section: Membership
---


# Automating membership processes using CiviRules


This guide explains how to automate common membership tasks in CiviCRM using **CiviRules**.  
 You’ll learn how to set up rules that respond automatically when a membership is created, renewed, or expired — helping you save time and ensure members always receive timely communication.

This page is for staff and administrators who are comfortable with membership setup and want to make routine actions automatic rather than manual.

## **What is CiviRules**

CiviRules is a tool that lets you set up “if this happens, then do that” actions inside CiviCRM.  
 You define a **trigger** (something that happens), a **condition** (what must be true), and an **action** (what the system should do).

For example, you can create rules like:

* When a new membership is created, send a welcome email.

* When a membership is renewed, extend related benefits or tags.

* When a membership expires, notify staff or move the contact to a “Lapsed Members” group.

Automation ensures that your members get consistent and timely follow-ups without you needing to remember every task.

## **Step 1: Planning your automation**

Before creating a rule, decide what you want to happen and when.  
 Ask yourself:

* What event should trigger the rule (for example, membership created, updated, or expired)?

* Who should the action affect (the member, a staff person, or another related contact)?

* What outcome do you want (an email, a tag, a group update, or a task)?

Start simple — one action per rule — and expand as you get comfortable.

## **Step 2: Creating a new rule**

1. Go to **Administer → Automation → CiviRules**.

2. Click **Add Rule**.

3. Enter a clear name (for example, “Welcome email for new members”).

4. Choose **Membership** as the trigger type.

5. Select the specific event, such as **Membership is added** or **Membership is renewed**.

6. Click **Save** to move to the next step.

## **Step 3: Adding conditions**

Conditions make your rule more precise.  
 For example, you may want the rule to apply only if:

* The membership type is “Individual Member”.

* The status is “New”.

* The membership fee is above a certain amount.

To add conditions:

1. Click **Add Condition**.

2. Choose a condition type such as *Membership Type*, *Status*, or *Source*.

3. Set the required values.

4. Click **Save Condition**.

If you don’t add any conditions, the rule will apply to all memberships triggered by your chosen event.

## **Step 4: Adding actions**

Actions are what the system will do when the rule is triggered.

Common actions include:

* **Send email to contact** – a welcome or renewal confirmation.

* **Add contact to group** – for example, “Active Members” or “Renewal Needed”.

* **Add tag to contact** – to help with reporting or segmentation.

* **Create activity** – to log a note or task for staff follow-up.

To add an action:

1. Click **Add Action**.

2. Choose the type of action from the list.

3. Configure the details, such as which email template to use or which group to add members to.

4. Save the action.

You can add more than one action if needed, but try to keep each rule simple and easy to maintain.

## **Step 5: Testing your rule**

It’s important to test your automation before using it with real members.

To test:

1. Create a test contact.

2. Add or renew a membership for that contact to trigger your rule.

3. Check that the correct action happens — for example, that an email is sent or a group is updated.

4. Review your CiviRules log to confirm that the rule ran successfully.

If it doesn’t behave as expected, check the conditions and make sure the trigger event matches your scenario.

## **Step 6: Managing your rules**

Once you have several rules in place, you can:

* Enable or disable rules temporarily using the toggle switch.

* Edit or delete rules you no longer need.

* Review the list of active rules regularly to make sure they’re still relevant.

If your organisation has multiple administrators, keep a shared record of what each rule does so everyone understands the automation in place.

## **Examples of useful membership automations**

Here are a few examples of practical automations you can set up:

* **Welcome emails** – send an automatic welcome message when a membership is created.

* **Renewal thank-you** – send a thank-you message after renewal.

* **Expiry follow-up** – email a lapsed member one month after expiry with a rejoin offer.

* **Internal notifications** – alert a staff member when a high-value membership renews.

* **Group management** – move contacts into or out of groups based on their membership status.

Automation can greatly reduce manual work, but always test carefully so that members don’t receive duplicate or confusing messages.

## **Best practices**

* Start with simple automations and build gradually.

* Use clear names for each rule so anyone can understand its purpose.

* Keep communication friendly and consistent with your organisation’s tone.

* Review rules every few months to ensure they still align with your membership policies.

* Avoid overlapping triggers that might cause multiple emails or updates for the same event.

## **What’s next**

Once you’re comfortable with CiviRules, you can:

* Combine multiple actions in one rule (for example, send an email and tag the contact).

* Trigger automations from other entities such as contributions or events.

* Use custom conditions to create advanced membership journeys.

