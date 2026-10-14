---
name: guest-list-import
description: Use when the couple or planner pastes or uploads a list of people and wants it added to or reconciled with the Tu Día de Blanco Guest list, using an atomic import.
---

# Guest import and reconciliation

Check `get_capabilities` once per conversation or after a permission error and follow `wedding-workspace`. Parse first/last names, contact details, explicit companion allowances and only the other details needed for this import. `companions_allowed` is 0–10, not actual attendance; a named companion is its own Guest record. Do not set the legacy `plus_one` flag; clear it (`false`) only when the user asks to stop counting an unnamed extra. Normalise emails, deduplicate (check `possible_duplicates` from `list_guests` and `possible_duplicate_of` from `add_guest`) and ask about ambiguous people or companion links; never infer permission to bring someone.

Read all relevant `list_guests` pages using next_offset, or use targeted searches. An incomplete result is not evidence that a person is new. Match email first, then names; separate new, unchanged and uncertain rows. Existing edits use returned IDs. Do not infer RSVP answers; new Guests default to awaiting.

Show the planned additions/edits, then call `import_guests` for up to 200 explicit add_guest/update_guest operations in one transaction. Duplicate email or invalid/foreign IDs roll back the whole batch. After the returned status is `applied`, check the affected list and report actual results. For larger inputs, apply sequential batches, rereading the list between them, or use the web spreadsheet import.

Importing never sends an invitation. `send_guest_invitations` is a separate explicitly requested communication workflow with separate consent, recipient confirmation and persisted status. Check uncertain outcomes before retrying.

## Language

Support English and Spanish. Reply in the language the user uses, and follow an explicit language preference. Explain statuses in that language. Preserve proper names, user-authored content, IDs, tool names and enum values; do not translate stored content unless requested.
