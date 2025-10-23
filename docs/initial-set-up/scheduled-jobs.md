---
categories:
  - Uncategorized
  - Tutorial
level: Basic
summary: This guide introduces scheduled jobs in CiviCRM, explaining how they work and how to configure them for your non-profit's needs.
section: Scheduled Jobs
---

# Understanding scheduled jobs in CiviCRM

Scheduled jobs are essential for keeping your CiviCRM data up-to-date and ensuring important tasks run automatically. For example, these jobs can send reminders, check for software updates, and perform many other functions that help your organization stay organized. This guide will help you understand how scheduled jobs work and how to set them up effectively.

## How scheduled jobs are initiated

Scheduled jobs run automatically, but they need a tool called "cron" to start. Cron is a separate piece of software that tells CiviCRM when to execute these jobs. Your system administrator will need to set up cron to run at regular intervals, typically every 5 to 60 minutes. This setup is crucial because if cron runs infrequently, your scheduled jobs won't run as often as needed.

## Configuring scheduled jobs

To configure scheduled jobs in CiviCRM, navigate to **Administer > System Settings > Scheduled Jobs**. Here, you can see the jobs that are already set up and make adjustments as needed.

## Scheduled jobs vs API calls

CiviCRM has a feature called the "API," which allows for various tasks to be automated. Scheduled jobs combine an API call with a schedule. For example, a scheduled job might automatically send reminders to contacts every day. Understanding this connection can help you make the most of CiviCRM's capabilities.

## Default scheduled jobs

When you first install CiviCRM, several default scheduled jobs are already configured. These jobs provide a great starting point, and you can rename or delete them as needed. You can also refer to the specific jobs section for detailed information on how to recreate any of these default jobs.

## Job frequency

Different jobs need to run at different frequencies. For instance, tasks like sending emails should run every 5 or 10 minutes, while others, like updating memberships, can run daily. When setting up or editing a job, you can choose from several frequency options, including:

- Yearly
- Quarterly
- Monthly
- Weekly
- Daily
- Hourly
- Every time cron runs

Keep in mind that your cron setup will limit how often these jobs can run.

## Manually executing a scheduled job

If you need to run a scheduled job immediately, you can do so by clicking **More > Execute Now** for that job on the Scheduled Jobs page. This is helpful for jobs that don't need to run frequently, such as geo-coding or updating greetings.

## Viewing the job log

You can check the job log to see if your scheduled jobs are running correctly. From the Scheduled Jobs screen, click on **View Log** to see all jobs or **View Job Log** for a specific job. This log is useful for troubleshooting any issues that may arise.

## Conclusion

Understanding and configuring scheduled jobs in CiviCRM can significantly enhance your organization's efficiency. By automating routine tasks, you can focus more on your mission and less on administrative work. If you have any questions or need assistance, don't hesitate to reach out to your system administrator or consult further resources.
