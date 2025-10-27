---
categories:
  - Guide  
level: Intermediate  
summary:  This guide explains what membership statuses are in CiviCRM, how the system assigns them, and how you can configure them. 
section: Membership
---

# Membership statuses and how they work


This guide explains what **membership statuses** are in CiviCRM, how the system assigns them, and how you can configure them.  
 It’s aimed at staff who already have some basic membership setup and now want to understand the lifecycle of a membership.

## **What is a membership status?**

A membership status shows where a member is in their membership “journey” — for example, newly joined, current, in a grace period, or expired.  
 In CiviCRM, membership statuses:

* Help you report on who is actively a member and who is not.

* Trigger different workflows (renewals, communications, archival).

* Are usually updated automatically by the system (though you can override them).

## **Key dates that drive status rules**

Status rules use three important dates on each membership record:

* **Join date**: the date when the contact first became a member. [docs.civicrm.org](https://docs.civicrm.org/user/en/latest/membership/defining-memberships/?utm_source=chatgpt.com)

* **Start date**: when the current membership period begins. [docs.civicrm.org](https://docs.civicrm.org/user/en/latest/membership/defining-memberships/?utm_source=chatgpt.com)

* **End date**: when the current membership period ends. [docs.civicrm.org](https://docs.civicrm.org/user/en/latest/membership/defining-memberships/?utm_source=chatgpt.com)  
   By comparing today’s date with start and end, CiviCRM chooses the appropriate status.

## **Default membership statuses**

CiviCRM ships with these statuses by default. [docs.civicrm.org](https://docs.civicrm.org/user/en/latest/membership/defining-memberships/?utm_source=chatgpt.com)

* **Pending**: Someone has signed up but payment or approval is still pending.

* **New**: A just-joined member whose start date has begun.

* **Current**: A member within the valid period of membership.

* **Grace**: The membership has ended but you allow a transition period where they’re still counted as a member.

* **Expired**: They finished the membership period and the grace period (if any) — they are no longer counted as a member.

* **Cancelled**: A membership ended early (for example, at the contact’s request or due to withdrawal).

* **Deceased**: The contact is marked as deceased — prevents further communications, etc.

## **How CiviCRM assigns statuses**

Here’s how the system works in simple terms:

1. It checks if a membership **override flag** is set. If yes, that status is used. [docs.civicrm.org](https://docs.civicrm.org/user/en/latest/membership/defining-memberships/?utm_source=chatgpt.com)

2. If no override, it works down the list of status rules (from top to bottom) until one rule matches the membership’s dates. [docs.civicrm.org](https://docs.civicrm.org/user/en/latest/membership/defining-memberships/?utm_source=chatgpt.com)

3. When a rule matches, it applies that status and optionally whether that status counts the person as a “current member” (for reporting and renewal logic) or not. [docs.civicrm.org](https://docs.civicrm.org/user/en/latest/membership/defining-memberships/?utm_source=chatgpt.com)

## **Customising status rules**

You can change or add status rules to match your organisation’s needs (for example, you may want a longer grace period or a special “archived” status).  
 Here are the things you can set:

* Which event triggers the rule (join date, start date or end date). [docs.civicrm.org](https://docs.civicrm.org/user/en/latest/membership/defining-memberships/?utm_source=chatgpt.com)

* The offset: how many days/months before or after that event the rule begins. [docs.civicrm.org](https://docs.civicrm.org/user/en/latest/membership/defining-memberships/?utm_source=chatgpt.com)

* Whether someone with that status is counted as a “member”. [docs.civicrm.org](https://docs.civicrm.org/user/en/latest/membership/defining-memberships/?utm_source=chatgpt.com)

* Whether the status is publicly visible (for forms) or just admin use. [docs.civicrm.org](https://docs.civicrm.org/user/en/latest/membership/defining-memberships/?utm_source=chatgpt.com)

Tip: Keep the list of rules in the correct order — the system stops at the first match. A mis-ordered rule can lead to statuses not updating as expected. [CiviCRM Stack Exchange+1](https://civicrm.stackexchange.com/questions/38377/membership-status-rules-query?utm_source=chatgpt.com)

## **Why scheduled jobs matter**

Because statuses are updated automatically, you’ll need a scheduled job (cron) scan to apply changes over time (e.g., when someone’s end date passes).  
 Make sure the job **Update Membership Statuses** (or equivalent) is enabled and running at least daily. [docs.civicrm.org+2docs.civicrm.org+2](https://docs.civicrm.org/user/en/latest/membership/defining-memberships/?utm_source=chatgpt.com)  
 If it isn’t, statuses may remain outdated (for example, someone remains “Current” even though their end date has passed).

## **When you might override a status**

Sometimes you will want to force a membership into a specific status:

* If a member asked to pause or freeze their membership.

* If a member’s behaviour led to manual cancellation.

* If you need to flag an honorary membership differently.

You do this by editing the membership record and checking **Status override**, then picking the status. Note: While overridden, the automatic rules will not change it. [docs.civicrm.org](https://docs.civicrm.org/user/en/latest/membership/defining-memberships/?utm_source=chatgpt.com)

## **Tips & best practices**

* Ensure the rule list has a clear order: for instance, “Current” appears before “Grace”, “Grace” before “Expired”.

* Make the “Member – Yes/No” flag accurate: someone in grace may still count as a member, someone expired likely does not.

* Test your rules: create a sample membership with a short duration and manually change the start/end dates to see how the status flows.

* Document internal definitions of statuses (what “Grace” means for your organisation) so staff understand and act accordingly.

* Communicate clearly: if someone is in “Grace” they still get member benefits; once “Expired” they no longer do.

## **When things go wrong**

If statuses aren’t updating as expected:

* Check that the scheduled job for updating memberships is active and running.

* Open **Administer → CiviMember → Membership Status Rules** and review your rule list and dates.

* Check that the membership’s start and end dates are correct for their membership type.

* See if a status override is accidentally checked (which stops automatic updates).

* Review any custom status you added and confirm it’s marked correctly as “Member \= Yes/No”.
