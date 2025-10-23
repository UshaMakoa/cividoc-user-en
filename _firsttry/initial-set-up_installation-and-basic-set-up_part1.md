# Source: https://docs.civicrm.org/user/en/latest/initial-set-up/installation-and-basic-set-up/

---
categories: Guide  
level: Basic  
summary: This guide helps non-profit users understand the initial installation and basic setup steps for CiviCRM, including key configuration options to get started confidently.  
section: Initial set up  
---

# Installation and basic set-up

## Introduction  
Welcome! This guide will walk you through the important first steps to get your CiviCRM system up and running. Whether you’re setting it up yourself or working with your technical team, this guide explains what you need to know in clear, simple language.  

## Prerequisites  
Before installing CiviCRM, make sure you have a web server (like Apache or nginx), PHP, and a MySQL database ready. If you want to try CiviCRM on your own computer first, you can use packages like WAMP (for Windows), MAMP (for Mac), or LAMP (for Linux).  
You’ll also need to decide which website system (called a CMS) you want to connect CiviCRM to — popular choices are Drupal, WordPress, or Joomla! If you don’t want to use a CMS, there is a standalone option.  

## Internet vs. local installs  
Most organizations use CiviCRM on the internet so people can access it anywhere. Some choose to install it only on their internal network to keep it private. If you do this, remember that your contacts won’t be able to update their own information online.  

## Securing your system  
After installation, it’s important to keep your system safe. Work with your technical team to follow security best practices for your server and website.  

## Upgrades  
CiviCRM is updated regularly with new features and important security fixes. Plan to apply these updates on a test copy of your site first, and always back up your data before upgrading the live system. Many organizations hire CiviCRM experts to help with upgrades.  

## Initial configuration checklist  
Once installed, log in to CiviCRM and go to **Administer > Administration Console > Configuration Checklist**. This checklist guides you through important settings to customize CiviCRM for your organization. Settings you haven’t reviewed yet will show in red, and those you’ve visited will turn green.  

## Localization  
Localization means adapting CiviCRM for your country and language. By default, CiviCRM is set up for the United States. You can change language, date formats, currency display, and more to fit your needs. If your organization works in multiple languages, you can enable multi-language support so users can choose their preferred language.  

## Organization address and contact info  
Enter your organization’s name, address, and a valid email address on the Domain Information screen. This information will appear on emails sent from CiviCRM, like donation receipts and event confirmations.  

## Enable components  
CiviCRM has different parts called components (for example, Contributions, Events, Memberships). When you first install, the most common components are already turned on. You can enable or disable components anytime based on what your organization uses.  

## Display preferences  
You can customize how information shows on the screen, such as which tabs appear on contact records or which fields show when adding contacts. For example, if you don’t track relationships, you can hide that tab to keep things simple. You can also choose whether to use a text editor with formatting options or simple text fields.  

## Address settings  
CiviCRM lets you customize how addresses are entered and displayed. You can hide fields you don’t use, change the order of address fields, and set up mailing label formats. If you want, you can enable address parsing to split addresses into parts like street number and apartment.  

## Mapping and geocoding  
You can show contact and event addresses on maps using Google Maps or OpenStreetMap. To do this, select a mapping provider and get an API key from them. You can also enable automatic geocoding so CiviCRM saves latitude and longitude for addresses.  

## Search settings  
Adjust how CiviCRM searches for contacts. For example, you can enable wildcards to find partial matches or include email addresses in name searches. These settings help make searching faster and more accurate, especially if you have a large contact list.  

## Miscellaneous settings  
This section includes useful options like:  
- How long dashboard data is cached  
- Whether deleted contacts go to a trash folder (so they can be restored)  
- Attaching PDFs to receipts  
- Alerts about new CiviCRM versions  
- Limits on file attachments and sizes  
- Permissions related to editing contacts connected by relationships  

## Contact types  
You can rename the main contact types (Individuals, Households, Organizations) and create subtypes like Student or Volunteer to better organize your contacts.  

## Outbound email  
To send emails from CiviCRM (like thank-you messages or event confirmations), you need to set up how CiviCRM connects to your mail server. You can use different methods like SMTP or Sendmail. After entering your settings, always send a test email to check everything works.  

## From email addresses  
Set the default email address that CiviCRM uses when sending automated emails. Users can also choose from other approved addresses when sending emails through CiviCRM.  

## Payment processors  
If you want to accept online payments for donations, memberships, or event fees, you need to set up a payment processor. CiviCRM supports several options, and you can add more with extensions. Choose the one that fits your organization best.  

## Permissions  
Permissions control who can see and do what in CiviCRM. Setting these up properly helps keep your data secure and your system easy to use.  

## System workflow templates  
CiviCRM sends automated emails for things like receipts and event registrations. You can review and customize these message templates but be careful not to change the behind-the-scenes logic. Always test emails after making changes.  

## System status  
CiviCRM includes a system status page that checks your installation and alerts you to any problems. Check this regularly to keep your system healthy.  

---

You’ve now covered the main steps to install and set up CiviCRM. For more detailed tasks, explore other guides focused on specific components and workflows.