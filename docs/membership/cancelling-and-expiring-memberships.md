---
categories:
  - Guide
level: Basic
summary: Learn how to cancel or manually expire a member’s record in CiviCRM, and when to delete a membership instead.
section: Membership
---

# Cancelling and expiring memberships

## When to cancel or expire a membership

If someone wants to leave your organisation or stop their membership, you should **change their membership status to "Cancelled" or another non-current status** instead of deleting the membership. This keeps a record of their involvement and any related payments.

If a member’s period has ended (for example, they did not renew after a grace period), you can **set their status to "Expired"**. Use "Expired" if the member completed their full term, and "Cancelled" if they left early.

## How to cancel or manually expire a membership

To change a membership status:

- Search for the contact whose membership you want to change.

- Click on the **Membership** tab.

- Click **Edit** next to the membership record.

- On the edit screen, tick the **Status Override** box.

- Choose the new **Membership Status** (for example, "Cancelled" or "Expired").

- Save your changes.

**Tip:** CiviCRM can automatically expire memberships based on your organisation’s rules (set up in *Administer > CiviMember > Membership Status Rules*). Manual expiry is only needed if you want to override these automatic settings.

## Deleting memberships

Only delete a membership if it was entered by mistake (for example, if you added the wrong person). **Deleting a membership will also remove any linked contributions**, and this action cannot be undone. Only trusted staff should have permission to delete memberships.

To delete a membership:

- Find the contact, go to the **Membership** tab, click **More** next to the membership, then click **Delete**.

Or:

- Go to **Memberships > Find Members**, enter your search criteria, select the memberships to delete from the results, and click **Delete**.

<!--
Source: https://docs.civicrm.org/user/en/latest/membership/cancelling
-and-expiring-memberships/ -->

<!--
This page is a Guide because it provides step
-by-step instructions for a specific task (changing or deleting membership status), with no background or conceptual explanation. The content is basic because it covers essential, everyday tasks for non-expert users. If the page included more on the reasons for different statuses, that could be split as an Explanation. -->
