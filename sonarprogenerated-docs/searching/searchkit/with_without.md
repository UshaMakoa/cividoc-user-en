---
categories: Explanation
level: Intermediate
summary: Understand how joining entities with "With (optional)", "With (required)", or "Without" affects which contacts and related information appear in your Search Kit results.
section: Search Kit
---

# Understanding join options in Search Kit

When you build a search in CiviCRM's Search Kit, you often need information from multiple sources. For example, you might want to see contacts along with their addresses, or contacts with their event registrations. Search Kit gives you three ways to combine this information: **With (optional)**, **With (required)**, and **Without**. Understanding these options helps you get exactly the results you need.

## How joining works in Search Kit

Every search starts with a primary entity—typically **Contacts**. You can then add related entities like addresses, memberships, contributions, or activities. Each time you add a related entity, you're creating a "join" between your primary data and this additional information.

The join option you choose determines **which rows appear** in your final results. This is crucial because selecting the wrong option can either show you too much information (including contacts you don't care about) or hide contacts you need to see.

## With (optional): Include everything, even if data is missing

**With (optional)** means the related information is nice to have, but not required. Your search will return rows from your primary entity **even when** the related entity doesn't exist.

For example, if you search for **Contacts With (optional) Contact Addresses**, you'll see:
- Every contact who has one or more addresses (with their address details filled in)
- Every contact who has **no addresses** (with empty/blank fields where address information would appear)

This option is useful when you want a complete list of contacts but would like to see address information when it's available. You're not filtering anyone out—you're just adding optional columns.

## With (required): Only show records where both exist

**With (required)** acts as a filter. Your search will **only return rows** where the related entity exists for your primary entity.

For example, if you search for **Contacts With (required) Contact Addresses**, you'll see:
- Every contact who has at least one address
- **No contacts** who lack addresses

If a contact has multiple addresses, you'll get a separate row for each combination of contact and address. This option is powerful when you specifically need contacts that have the related information—perhaps you're preparing a mailing list and only want contacts with physical addresses.

## Without: Show only records where the relationship doesn't exist

**Without** works as an exclusion filter. Your search returns rows from your primary entity **only when** the related entity does **not** exist.

For example, if you search for **Contacts Without Contact Addresses**, you'll see:
- Every contact who has **no addresses** recorded
- No contacts who have addresses

This is particularly useful for finding gaps in your data or identifying contacts who need follow-up. You might use **Without** to find all contacts who haven't registered for an upcoming event, or members who haven't made a contribution this year.

## Practical examples for non-profit scenarios

**Finding contacts ready for a mailing**: Use **Contacts With (required) Contact Addresses** to ensure you only export contacts who have addresses on file. Anyone without an address won't appear, saving you time and reducing errors.

**Identifying members without recent donations**: Start with **Contacts With (required) Current Membership**, then add **Contributions Without** and filter for contributions in the past 12 months. This shows members who haven't donated recently, perfect for targeted outreach.

**Creating a comprehensive event participant list**: Use **Contacts With (optional) Event Participants** and filter for your specific event. You'll see everyone, including those who registered and those who didn't, helping you understand who's missing.

## Choosing the right join option

Ask yourself these questions:

- **Do I want to see all primary records, or only those with related data?** If all records, use **With (optional)**. If only those with data, use **With (required)**.
- **Am I looking for what's missing?** Use **Without** to find contacts lacking certain information or activities.
- **Am I filtering or just adding columns?** **With (optional)** adds columns without filtering. **With (required)** and **Without** both filter your results.

Each additional entity you add uses one of these three options, and your choices stack. You might use **With (required)** for one entity and **Without** for another in the same search, creating precisely targeted results like "contacts with memberships but without recent event attendance."

# comment: Source: https://docs.civicrm.org/user/en/latest/searching/searchkit/with-optional-required-without/
# comment: This page is classified as Explanation because it clarifies the conceptual difference between three join types and helps users understand *why* choosing one option over another affects their search results. It provides context and relationships between concepts rather than step-by-step instructions (Tutorial) or task-oriented solutions (Guide). The original content mixed some reference-style description with conceptual explanation; this rewrite emphasizes understanding and conceptual clarity appropriate for non-expert users who need to grasp *how these options work* before applying them confidently.
```