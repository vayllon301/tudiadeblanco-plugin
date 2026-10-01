---
name: guest-list-import
description: Use when the couple or planner pastes or uploads a list of people and wants it added to or reconciled with the Tu Día de Blanco Guest list, using a reviewed atomic import.
---

# Guest import and reconciliation

Start with `get_capabilities` and follow `wedding-workspace`. Parse first/last names, email, phone, dietary needs, plus-one flag and notes. Normalise emails, deduplicate the input and ask about ambiguous people; never invent companion policy.

Read all relevant `list_guests` pages using next_offset, or use targeted searches. An incomplete result is not evidence that a person is new. Match email first, then names; separate new, unchanged and uncertain rows. Existing edits use returned IDs. Do not infer RSVP answers; new Guests default to awaiting.

Show the planned additions/edits, then call `import_guests` for up to 200 explicit add_guest/update_guest operations in one transaction. Duplicate email or invalid/foreign IDs roll back the whole batch. Give the web approval URL. After get_proposal_status returns applied, check the affected list and report actual results. For larger inputs, split into sequentially reviewed batches or use the web spreadsheet import. A completed first batch makes later proposals need fresh revisions.

Importing never sends an invitation. `send_guest_invitations` is a separate explicitly requested communication workflow with separate consent, recipient review and persisted status. Check uncertain outcomes before retrying.

## Language

Support English and Spanish. Reply in the language the user uses, and follow an explicit language preference. Explain statuses and approval steps in that language. Preserve proper names, user-authored content, IDs, tool names and enum values; do not translate stored content unless requested.
