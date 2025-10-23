# Source: https://docs.civicrm.org/user/en/latest/common-workflows/automating-tasks/

# Planning your automation

## Reflect on your current workflows

Write down the tasks you do repeatedly and the decisions you make for each. Ask yourself:

- What information do I use to decide what to do?  
- Where do I find or store that information in CiviCRM?  
- What actions do I want the system to take automatically?

## Writing your decision rules

Try to express your decisions as simple if-then statements. For example:

- If the spouse name is entered, include it in the letter address.  
- If the last donation is over $10,000 and the donor lives in a certain zip code, add a personal invitation to visit.

This will help you translate your workflow into CiviCRM’s automation features.

## Avoid workarounds—fix root causes

If something doesn’t work as you expect, investigate why. For example, relationship types might be limited to certain contact types. Fixing these settings is better than using complicated workarounds.