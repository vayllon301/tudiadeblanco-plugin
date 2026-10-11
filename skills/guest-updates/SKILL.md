---
name: guest-updates
description: Use when the couple or planner wants to review Letters from Guests, prepare an Update for the Tu Día de Blanco Invitation Website, design the invitation email or send invitations. Reads Letters, changes read state when requested, saves new Updates as drafts and changes the invitation email.
---

# Letters and Updates

Use the rules in `wedding-workspace`. Letters and Updates are different records with different module permissions.

## Letters

Read `list_letters`; anonymous authors remain hidden. `mark_letter_read` and `archive_letter` change read and archive state, including restoring it. Never infer identity or publish private Letter text implicitly. No tool replies to or submits Letters.

## Updates, invitation email and invitations

Read `list_news_posts`. Use `draft_news_post` for a new draft and `update_news_post` to edit, publish, unpublish or schedule an existing Update; `delete_news_post` removes it. Writes apply immediately; confirm with the user before publishing or deleting, and public effects require publication consent. A saved draft never contacts Guests.

The invitation email is the design Guests receive with their invitation link. Read it with `get_invitation_email`; null texts use the default copy in the Wedding's language. `update_invitation_email` changes texts, layout, image, alignment, spacing, font and colours; omitted fields stay unchanged and it sends nothing. It requires publication consent. For an image, use `prepare_upload` with purpose `email_image` (1 MB), wait for `get_upload_status` to complete and pass its `url` as `image_url`; other addresses are refused. `send_invitation_email_test` sends the saved design only to the connected Account's own address; it needs communication consent.

For explicitly requested invitations, read and reconcile exact Guest IDs, then use `send_guest_invitations`. It sends immediately and requires communication consent, so confirm the exact recipients with the user first. Check `get_communication_status` with the returned `proposal_id`; accepted, failed and unknown outcomes are distinct from delivery. Never expose invitation tokens or automatically retry unknown attempts.

## Language

Support English and Spanish. Reply in the language the user uses, and follow an explicit language preference. Explain statuses in that language. Preserve proper names, user-authored content, IDs, tool names and enum values; do not translate stored content unless requested.
