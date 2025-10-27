---
categories: Guide
level: Basic
summary: Learn how to use CiviCRM to prepare and send postal mailings, including generating letters and mailing labels for your contacts.
section: Common workflows > Postal mail communications
---

# Postal mail communications

## Plan your postal mailing

Before you start, think about your goals and the steps you need to take. Ask yourself:

- What types of mailings does your organisation send (for example, newsletters, event invites, or donation requests)?
- Do you send mailings to everyone in your database, or only to certain groups?
- How do you want to address your recipients (for example, "Dear Jane" or "Dear Jane Doe")?

You can use CiviCRM in three main ways for postal mailings:

- **Generate address labels** when you don’t need to personalise the content, such as for sending brochures.
- **Export contacts** and use a mail merge in a word processor (like Microsoft Word or LibreOffice Writer) for more control over layout and sorting.
- **Create and print personalised letters directly in CiviCRM** using the Print/merge document feature.

If your organisation needs to sort mailings by zip code (for example, for bulk mail discounts in the USA), it’s best to export contacts and do the mail merge in your word processor, where you can sort the data as needed.

## Set up greetings and salutations

You can personalise how you greet each contact. CiviCRM lets you choose from options like "Dear John," "Dear Mr. John Doe," or a custom greeting. To change a contact’s greeting:

- Edit the contact and go to the Communications Preferences section.
- Choose or enter the postal greeting you want.

If you need to update greetings for many contacts at once, you can use CiviCRM’s Scheduled Jobs feature.

## Create and print merged letters

CiviCRM’s Print/merge document feature lets you create personalised letters for your contacts. Here’s how to do it:

1. **Find your recipients**: Use Search > Find Contacts > Advanced Search, or go to Contacts > Manage Groups and click "Contacts" next to the group you want.
2. **Select contacts**: Tick the boxes next to the people you want to include.
3. **Choose action**: From the Actions dropdown, select Print/merge document.
4. **Pick a template (optional)**: You can use an existing template or start from scratch. You can also link the letter to a specific campaign.
5. **Adjust page settings**: Set your paper size, margins, and orientation.
6. **Write your letter**: Enter your text in the editor. You can add your organisation’s logo or a signature by clicking the Image icon.
7. **Personalise with tokens**: Insert tokens (placeholders) like Postal Greeting, which will be replaced with each contact’s details. Click where you want the token, then use the Insert Tokens dropdown.
8. **Save as template (optional)**: If you’ll reuse this letter, save it as a new template.
9. **Choose output format**: Pick PDF, HTML, MS Word (.docx), or Open Document (.odt).
10. **Download your letters**: Click Download Document. Check the file to make sure everything looks right. You can make changes and download again if needed.

**Tips:**

- You can use this feature for other documents, like certificates or thank-you letters.
- Generating many letters, especially as PDFs, can use a lot of computer resources. For large batches, consider setting up the wkhtmltopdf tool (ask your system administrator).
- You can also print merged documents from a single contact’s record or for contributions (like thank-you letters for donations).

## Generate mailing labels

To create address labels for your mailing:

1. **Find your recipients**: Search for the contacts you want.
2. **Choose action**: Select Mailing Labels from the Actions dropdown and click Go.
3. **Pick a label style**: Choose the format that matches your label sheets.
4. **Set options**:
   - Exclude people who have "do not mail" set (recommended).
   - Merge records with the same mailing address into one label if you don’t want to send duplicates.

When merging, each name at the same address appears on its own line of the label. Your system administrator can adjust which fields appear on labels in the address settings.

# comment: Source: https://docs.civicrm.org/user/en/latest/common-workflows/postal-mail-communications/
# comment: Suggestion: This page is best classified as a Guide, as it provides step-by-step instructions for achieving specific tasks (sending postal mail, generating labels, and merged letters) rather than teaching the system from scratch (Tutorial), listing exhaustive options (Reference), or explaining underlying concepts (Explanation). The content is appropriate for a Basic level, as it addresses common tasks for non-expert users. If needed, the sections on greetings and salutations could be split off as a Reference page for greeting options, but for most non-expert users, keeping them together in a single guide is clearer.