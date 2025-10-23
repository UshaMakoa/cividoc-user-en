---
categories:
  - Uncategorized
  - Guide  
level: Intermediate  
summary: This guide explains how to manage membership renewals in CiviCRM and how to set up automatic reminders so members are encouraged to renew on time.
section: Membership
---


# Managing membership renewals and reminders

This guide explains how to manage membership renewals in CiviCRM and how to set up automatic reminders so members are encouraged to renew on time.

You’ll learn the difference between manual and automatic renewals, how to configure renewal settings, and how to use scheduled reminders to save your team time and reduce lapsed memberships.

It’s written for membership managers and administrators who already have membership types set up and are ready to improve their renewal process.

## **Understanding membership renewal**

A membership renewal is when an existing member extends their current membership for another period.

Renewals can be:

* **Manual** – when a staff member or administrator updates a record directly, or when a member renews through a paper form or phone call.

* **Online** – when members renew through your website using a contribution page.

* **Automatic** – when the system renews memberships linked to recurring payments.

CiviCRM can handle all of these methods and keep each renewal recorded as a separate entry, preserving membership history for every contact.

## **Step 1: Setting up renewal options**

Each membership type includes its own renewal settings.

To check or edit them:

1. Go to **Administer → CiviMember → Membership Types**.

2. Click **Edit** next to the membership type.

3. Review the **Duration** and **Period Type** settings to ensure they reflect your renewal model.

4. If you want to allow early renewals, tick the option **Renewal extend current end date**.

Tip: Allowing early renewal helps members who want to renew before their current term expires.

## **Step 2: Renewing a membership manually**

To renew a membership from a contact record:

1. Search for the contact and open their record.

2. Go to the **Memberships** tab.

3. Click **Renew** next to the membership you want to extend.

4. Confirm or update the renewal date and contribution details.

5. Click **Save**.

CiviCRM automatically creates a new membership record for the new period and keeps the old one for reference, maintaining a complete membership history.

## **Step 3: Enabling online renewals**

If you use online membership sign-up pages, you can also allow members to renew directly through the same form.

To enable this:

1. Go to **Contributions → Manage Contribution Pages**.

2. Edit your membership sign-up page.

3. Open the **Memberships** tab.

4. Ensure that **Membership section enabled** is ticked.

5. Add text in the **Renewal message** area so returning members know they can renew.

6. Save the page.

When existing members visit the page and log in, CiviCRM will recognise them and offer renewal instead of new sign-up.

If your payment processor supports it, you can also offer **auto-renewal** — where a recurring payment automatically renews the membership at the end of each term.

## **Step 4: Setting up renewal reminders**

Automated reminders help you communicate with members before and after their membership expires.

To create one:

1. Go to **Administer → Communications → Scheduled Reminders**.

2. Click **Add Reminder**.

3. In **Entity**, choose **Membership**.

4. Select the membership type or status this reminder applies to.

5. Set the timing (for example, *2 weeks before membership end date*).

6. Choose the email template or write your own message.

7. Select who should receive the reminder — member, staff contact, or both.

8. Set it to **Active** and **Save**.

You can create multiple reminders — for example:

* One before expiry (“Your membership is due for renewal”)

* One after expiry (“Your membership has lapsed — we’d love to have you back”)

Once reminders are active, CiviCRM automatically sends them when the scheduled job runs.

## **Step 5: Testing your renewal process**

Before going live, test the full renewal process from start to finish:

* Renew a membership manually and check that dates update correctly.

* Complete a renewal through your online page and confirm payment links to the new membership record.

* Run the **Scheduled Jobs** manually to trigger reminders and check that the correct messages are sent.

Testing ensures your process works smoothly before members begin using it.

## **Step 6: Monitoring renewals**

To keep track of renewals and expirations:

* Use the **Find Memberships** search to filter by membership status (Current, Grace, or Expired).

* Create a **Smart Group** for members due to renew soon — for example, those with memberships ending in the next 30 days.

* Review the **Membership Summary Report** to track overall renewal rates and trends.

Monitoring regularly helps you identify members who may need a reminder or personal follow-up.

## **Best practices**

* Always test renewal forms with real-world examples before launching.

* Make your reminder messages friendly and appreciative, not just transactional.

* Avoid overwhelming members with too many reminders — one before and one after expiry is usually enough.

* Keep your message consistent with your organisation’s tone and brand.

* If you manage multiple membership types, ensure each one has the correct renewal and reminder settings.

## **What’s next**

Once your renewal and reminder processes are in place, you can:

* Add automation with CiviRules (for example, send a thank-you when someone renews).

* Build dashboards or reports to track renewals and lapsed members.

* Test auto-renew options for regular supporters who prefer set-and-forget memberships.
