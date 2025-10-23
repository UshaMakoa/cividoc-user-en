# Source: https://docs.civicrm.org/user/en/latest/initial-set-up/installation-and-basic-set-up/

---
categories: Tutorial
level: Basic
summary: This guide provides step-by-step instructions for installing and setting up CiviCRM for non-profit organizations, ensuring a smooth start to using the system effectively.
section: Installation and basic set-up
---

# Installation and basic set-up

Setting up CiviCRM can seem daunting, but with this guide, you'll be able to navigate the installation and configuration process with confidence. Whether you are setting it up on your own or working with a technical team, this guide will help you get started.

## Prerequisites

Before you begin, make sure you have the following:

- A web server (like Apache or nginx)
- PHP and MySQL installed on your system

If you're new to this, you might want to try CiviCRM on your local computer first. You can use packages like WAMP or XAMPP for Windows, or MAMP and LAMP for Mac and Linux, respectively. It's also important to discuss with your System Administrator about where to host your CiviCRM instance.

## Choosing your CMS

Decide which Content Management System (CMS) you want to integrate with CiviCRM. Your options include:

- Drupal
- WordPress
- Joomla!
- Standalone CiviCRM

Refer to the System Administrator Guide for detailed installation instructions based on your choice.

## Internet vs. local installs

Most organizations use CiviCRM over the internet. However, if your organization prefers to keep data internal for security reasons, you can install CiviCRM on an internal network. Just keep in mind that this limits your contacts from being able to update their information themselves.

## Securing your system

Once CiviCRM is installed, securing your system is crucial. The System Administrator Guide provides important techniques for securing your server and website.

## Upgrades

CiviCRM releases new versions every month. Keeping your CiviCRM core software up to date is essential for security and accessing new features. Be sure to plan resources for applying upgrades and always back up your site and database before running an upgrade.

## Configuration

After installation, it's time to configure CiviCRM to suit your organization's needs. Log in and navigate to Administer > Administration Console > Configuration Checklist. This checklist will guide you through the necessary tasks to customize CiviCRM for your organization.

## Localization

If your organization operates in a different country or language, you will need to localize CiviCRM. This involves translating text and setting region-specific formats for dates and currency. You can find translations contributed by community members and also consider creating your own if needed.

## Organization address and contact info

Enter the identifying information for your organization, such as the name and address, which will be used in automated emails and communications.

## Enable components

CiviCRM comes with several components, such as CiviContribute and CiviEvent, which are enabled by default. You can enable or disable components based on your organization's needs.

## Display preferences

Customize how CiviCRM displays information by modifying the screen and form elements. You can control what tabs and sections appear when viewing or editing contact records, as well as simplify forms by hiding unnecessary fields.

## Address settings

Adjust the default fields for adding and editing contact and event address data. You can also modify the layout for mailing labels and how addresses are displayed on the screen.

## Mapping and geocoding

Enable mapping services like Google or OpenStreetMap to display contact addresses on a map. You will need to obtain a key from your chosen provider to use this feature.

## Search settings

Adjust search behaviors to improve performance, especially if you have a large dataset. You can customize how searches are conducted and what data is included in quick search results.

## Miscellaneous settings

Explore additional settings that control various behaviors within CiviCRM, such as logging, email notifications, and contact management.

## Contact types

Modify the names of built-in contact types and create subtypes to better fit your organization's needs.

## Outbound email

Configure settings to allow CiviCRM to connect to your mail server for sending automated emails. Always test your email settings to ensure they are functioning correctly.

## Payment processors

If you plan to accept online contributions, you will need to set up a payment processor. Research the options available to find the best fit for your organization.

## System workflow templates

Review and customize the system-generated emails that will be sent out under your organization's name. Test any changes to ensure they work as intended.

## System status

Check the system status screen to identify any potential issues with your installation or configuration. This will help you maintain a smooth operation of CiviCRM.

With this guide, you are now equipped to install and set up CiviCRM for your organization. Remember to refer back to this document as you navigate through the installation process, and don’t hesitate to seek help if you encounter challenges along the way. Happy CRM-ing!