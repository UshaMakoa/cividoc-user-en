---
categories: Guide
level: Basic
summary: Learn how to set up and use A/B testing in CiviMail to compare two email versions and send the most effective one to your audience.
section: Email > CiviMail A/B Testing
---

# CiviMail A/B testing

## What you can do with A/B testing

A/B testing in CiviMail lets you compare two different emails by sending each to a small, random sample of your mailing list. After you see which version performs better, you can send the winning email to the rest of your recipients.

## Before you start

- Make sure your recipients are already in a mailing list (group). If you need help creating a mailing list, see the sections on Groups and Tags.

## Steps to create an A/B test

1. **Start a new A/B test**
   
   - Go to the CiviCRM menu and select **Mailings > New A/B Test**.

2. **Set up your test**
   
   - Choose the campaign for your mailing (optional).
   - Pick the type of test you want to run:
     - Compare different subject lines.
     - Compare different From (sender) lines.
     - Compare two entirely different emails.

3. **Select your recipients and test size**
   
   - On the Target screen, pick your mailing list.
   - Decide what percentage of your audience will receive each test email. Use the blue bar to adjust the split. The remaining recipients will get the final, winning email. The total (test group plus final group) will always add up to 100%.

4. **Compose your emails**
   
   - The compose screen changes based on your test type:
     - For subject line tests: Enter Subject (A) and Subject (B).
     - For From line tests: Enter From (A) and From (B).
     - For different emails: Choose a template for each version, and enter separate From and Subject fields.
   - Always send yourself a test email before scheduling or sending the real mailing.

5. **Send your test**
   
   - Schedule or send the test emails to your selected test group.

6. **Review results and send the final mailing**
   
   - Go to **Mailings > Manage A/B Tests** and select **Results** to see how each version performed.
   - Choose the best-performing email to send to the rest of your recipients.

## Tips

- Use clear and meaningful differences between your test emails (for example, a different subject or a different sender name).
- Check your results carefully before sending the final mailing.

# comment: Source: https://docs.civicrm.org/user/en/latest/email/ab-testing/
# comment: This page is a How-to Guide because it is focused on the steps to achieve a specific task (setting up and running an A/B test) and does not provide background theory or exhaustive reference details. The instructions are practical and goal-oriented, matching the Diátaxis definition of a Guide[1][4].