---
categories:
  - Explanation
level: Basic
summary: Learn how your organisation can adapt CiviCRM to your local language, currency, and regional formats, and how you can contribute to translations.
section: The CiviCRM Community > Localising CiviCRM
---

# Localising CiviCRM

## What is localisation in CiviCRM?

Localisation means adapting CiviCRM so it works well for organisations in different countries and regions. This includes translating the interface, setting the correct currency, and using local date and number formats. For example, the way dates and currencies are shown in CiviCRM can be changed to match what’s standard in your country. You can do this by going to:
**Administer > Configure > Global Settings > Localization** in CiviCRM.

## Why is localisation important?

- **Language**: CiviCRM is built in English, but it can be translated into many other languages so your team and supporters can use it comfortably.
- **Currency**: You can set the currency to match your country (like USD for United States or GBP for Great Britain).
- **Date and number formats**: Dates and numbers are displayed differently in different countries. CiviCRM lets you choose formats that make sense for your region.

## How does translation work in CiviCRM?

- CiviCRM relies on its community to translate the software into different languages.

- Some languages are almost fully translated, while others might only have a few words done.

- You can check the progress and help with translations using the online tool called **Transifex**.

- If you want to use terms that fit your organisation better, you are encouraged to join the translation effort.

## Mapping languages to regional versions

Sometimes, you need a more specific version of a language (for example, Canadian French instead of French from France).
To do this, you can adjust a setting in CiviCRM’s configuration file (`civicrm.settings.php`). For example:
```php
define('CIVICRM_LANGUAGE_MAPPING_FR', 'fr_CA');
```
This tells CiviCRM to use Canadian French.

## Facilities for translation

CiviCRM offers tools and resources to help with translation:

- **Transifex**: An online platform where translators work together and track progress.
- **Glossary**: A list of common terms to keep translations consistent.
- **Wiki pages**: Tips, tricks, and frequently asked questions about localisation.

## Getting started with translation

If you want to help translate CiviCRM:

- Create an account on Transifex.

- Find your language and join the translation team, or request a new team if needed.

- Start translating!

## Working as a team

Translation works best when done together. Most languages have teams you can join. Teams use glossaries, review each other’s work, and give feedback. If there’s no team yet, you can start one!

## Components and files

CiviCRM is divided into components (like CiviMail or CiviContribute). Each component has files with text to translate. You can focus on the part most relevant to your organisation.

## Online and offline translation

- **Online**: Use Transifex for quick and easy translations—no extra software needed.
- **Offline**: Download files and use tools like PoEdit for more features. When you’re done, upload your translations back to Transifex.

## Building a translation memory

Translation software can build a memory of translated phrases to help keep things consistent. You can use glossaries and memories from other projects, but it’s best to focus on CiviCRM terms for accuracy.

## Version control (for advanced users)

Transifex uses version control to keep track of translation files. Some users prefer working with these files directly, especially if they are comfortable with tools like GitHub.

## Ensuring consistency

Teams should use glossaries and peer review to keep translations consistent. Building and sharing a translation memory also helps everyone use the same terms.

## Team building and translation sprints

A translation sprint is when your team gets together to translate as much as possible in a short time. Tips for a successful sprint:

- Choose a location with good internet and enough computers.

- Prepare instructions and glossaries ahead of time.

- Set clear goals for what you want to achieve.

- Make sub
-teams for different components.

- Demo CiviCRM features if needed.

- Assign someone to answer questions.

- Keep snacks and drinks handy!

- At the end, review your progress and celebrate your achievements.

<!--
Source: https://docs.civicrm.org/some/page/
 -->

<!--
Suggestion: Most content is background and context, explaining localisation and translation in CiviCRM, so it fits the Explanation category. Some sections (like "Getting Started" and "Team building and sprints") could be split into Guides or Tutorials for step
-by-step instructions. For non-experts, this page should be Basic level and placed in "The CiviCRM Community > Localising CiviCRM". -->
