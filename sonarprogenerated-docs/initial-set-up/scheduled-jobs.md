---
categories: Reference
level: Intermediate
summary: This page lists and describes all scheduled jobs in CiviCRM, including how they work, how to configure them, and details for each job, to help your organisation keep data and communications up to date automatically.
section: Initial set up
---

# Scheduled jobs in CiviCRM

## What are scheduled jobs?

Scheduled jobs are automated tasks that CiviCRM runs at regular intervals to keep your organisation’s data accurate and your communications timely. These jobs handle things like sending reminders, updating membership statuses, processing mailings, and more.

## How are scheduled jobs started?

CiviCRM cannot start scheduled jobs by itself. Instead, it relies on a tool called **cron**, which is software installed on your server. Cron is set up by your system administrator to tell CiviCRM when to run these jobs (for example, every 5, 10, or 60 minutes). You cannot set up cron from within CiviCRM; this must be done outside the CiviCRM interface.

- If cron runs every hour, jobs can only run hourly or less often.
- Some jobs can be set to run more or less frequently, but they cannot run more often than cron itself.

## Configuring scheduled jobs

To manage scheduled jobs, go to:

**Administer > System Settings > Scheduled Jobs**

From here, you can:

- See all available jobs
- Add, edit, or delete jobs
- Set how often each job should run (hourly, daily, weekly, etc.)
- Manually run a job by clicking **More > Execute Now**
- View logs to check if jobs ran successfully or troubleshoot errors

## Scheduled jobs and the API

Each scheduled job is based on a CiviCRM API call (an instruction for CiviCRM to do something). You don’t need to know API details to use scheduled jobs, but it helps to understand that each job performs a specific action, sometimes with extra parameters you can set.

## Default scheduled jobs

When you install CiviCRM, it comes with several scheduled jobs already set up. You can rename, delete, or re-create these jobs as needed. Some jobs need extra parameters to work correctly.

## Job frequency and timing

- Choose how often a job runs: yearly, quarterly, monthly, weekly, daily, hourly, or every time cron runs.
- The actual frequency depends on how often cron is set to run.
- You cannot specify exact days (like "the 15th of each month") from within CiviCRM.

## Command parameters

Some jobs accept extra settings called “command parameters.” Enter one parameter per line, using `parameter=value` (no spaces or quotes). Each job’s parameters are listed below.

**Example for Job.mail_report:**
```
instanceId=7
format=csv
```

## Viewing job logs

On the Scheduled Jobs page, you can view logs for all jobs or a specific job. Logs show when jobs started and finished, and display any error messages.

## List of scheduled jobs

Below is a summary of the most common scheduled jobs, their purpose, recommended frequency, and parameters.

| Job name                        | Purpose                                              | Recommended frequency | Parameters (if any)                          |
|----------------------------------|------------------------------------------------------|----------------------|----------------------------------------------|
| Clean-up Temporary Data and Files| Removes old temp data and cache                      | Hourly               | session, tempTables, jobLog, prevNext, dbCache, memCache, tplCache, wordRplc (all optional, 1=clean, 0=skip) |
| Disable expired relationships    | Disables relationships past their end date           | Daily                | None                                         |
| Process Inbound Emails           | Adds activities from incoming emails                 | Hourly               | None                                         |
| Fetch Bounces                    | Records bounced emails from mailings                 | Hourly               | is_create_activities (optional, 1=create)    |
| Geocode and Parse Addresses      | Adds geocodes and parses street addresses            | Daily                | geocoding (required), parse (required), start, end, throttle (optional) |
| Rebuild Smart Group Cache        | Rebuilds smart group cache                           | Never                | limit (optional)                             |
| Mail Reports                     | Sends report instance by email                       | Daily                | instanceId (required), format, sendmail      |
| Send Scheduled Mailings          | Sends scheduled email campaigns                      | Every cron run       | None                                         |
| Update Membership Statuses       | Updates membership statuses                          | Daily                | None                                         |
| Update Participant Statuses      | Updates event participant statuses                   | Every cron run       | None                                         |
| Process Pledges                  | Updates pledge statuses and sends reminders          | Daily                | send_reminders (optional, 1=send)            |
| Send Scheduled SMS               | Sends scheduled SMS messages                         | Every cron run       | None                                         |
| Send Scheduled Reminders         | Sends scheduled email reminders                      | Daily                | None                                         |
| Update Greetings and Addressees  | Updates greetings/addressees for contacts            | Daily                | ct, gt (required), id, force, limit (optional) |
| CiviCRM Update Check             | Checks for software updates                          | Daily                | None                                         |
| Validate Email Address from Mailing| Updates email reset date after successful delivery  | Daily                | minDays, maxDays (optional)                  |

## Multisite / multi-domain considerations

- Most jobs only need to be set up for your primary domain (usually domain ID 1).
- For CiviMail in multisite setups, **Send Scheduled Mailings** and **Process Inbound Emails** must be configured for each site, with unique job names.

# comment: Source: https://docs.civicrm.org/user/en/latest/initial-set-up/scheduled-jobs/
# comment: This page is primarily a Reference, as it lists and describes scheduled jobs, their parameters, and configuration details. Some sections (like configuring jobs and viewing logs) could become How-to Guides if split off. For non-experts, the Reference format is most useful for quick lookup and understanding what each job does.