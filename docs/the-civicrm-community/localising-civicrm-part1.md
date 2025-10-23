---
categories:
  - Uncategorized
  - Guide  
level: Basic  
summary: This guide helps non-profit users understand how to localize CiviCRM by adapting language, date formats, currency, and other settings to suit their organization's region and language needs.  
section: Localising CiviCRM  
---

# Localising CiviCRM

## Introduction

CiviCRM is designed for organizations worldwide and supports adapting the system to local languages and regional settings without changing the software itself. Localising CiviCRM means more than just translating the text on the screen. It includes adjusting currency symbols, date and time formats, and number styles to match local customs. For example, the date format in the United States is usually month/day/year (11/16/2009), but in Russia, it’s day.month.year (16.11.2009). Similarly, currencies and number separators differ by country.

You can set these options in CiviCRM by going to:  
**Administer > Configure > Global Settings > Localization**

## Translations

CiviCRM supports many languages, but translations depend on community volunteers. Some languages have nearly complete translations, while others are partial or missing. You can check the translation progress for your language on the online translation platform, Transifex. You are encouraged to help improve translations or adjust terms to better fit your organization's needs.

## Mapping Languages to Regional Variants

Sometimes, you may want to use a regional variant of a language. For example, Canadian French (fr_CA) is different from French spoken in France (fr_FR). To use a regional variant, you can update the `civicrm.settings.php` file with a language mapping, such as:  
```php
define('CIVICRM_LANGUAGE_MAPPING_FR', 'fr_CA');
```

## Translation Tools and Workflow

### Online Translation with Transifex

- Create an account on Transifex.  
- Join your language team or start a new one if it doesn’t exist.  
- Select the CiviCRM component you want to translate (e.g., core, CiviMail).  
- Translate strings directly on the website and submit for review.

### Offline Translation with PoEdit

- Download translation files from Transifex.  
- Use PoEdit (free software) to translate offline.  
- Upload completed translations back to Transifex.

### Building a Translation Memory

Translation tools like PoEdit help create a translation memory—a database of previously translated phrases—to keep translations consistent and speed up future work.

## Working as a Team

Translation is a team effort. Teams usually create a glossary of terms to ensure consistency and review each other's work. If no team exists for your language, you can start one.

### Organizing Translation Sprints

Translation sprints bring people together to work on translations collaboratively. Key tips for a successful sprint:

- Choose a location with good internet and enough computers.  
- Provide instructions and support for translation tools.  
- Prepare and share a glossary in advance.  
- Set clear goals and divide work into manageable parts.  
- Offer demonstrations of CiviCRM features to translators.  
- Keep the team motivated with refreshments and breaks.  
- Review and celebrate progress at the end.

## Summary

Localising CiviCRM helps your organization use the system in a way that feels natural and familiar to your users. By translating text and adjusting regional settings, you make CiviCRM more accessible and effective for your community.
