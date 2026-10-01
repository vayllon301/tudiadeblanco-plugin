---
name: guest-updates
description: Use when the couple wants to review Letters from Guests or prepare an Update for their Tu Día de Blanco Invitation Website. Reads Letters, changes read state when requested, and saves new Updates as drafts.
---

# Letters and Updates

Use the rules in `wedding-workspace`. Letters and Updates are different records with different module permissions.

## Letters

Read `list_letters`; anonymous authors remain hidden. `mark_letter_read` and `archive_letter` prepare reviewed changes, including restoring archive state. Never infer identity or publish private Letter text implicitly. No tool replies to or submits Letters.

## Updates and invitations

Read `list_news_posts`. Use `draft_news_post` for a new draft and `update_news_post` to edit, publish, unpublish or schedule an existing Update; `delete_news_post` removes it. Every write needs web approval, and public effects require publication consent. A saved draft never contacts Guests.

For explicitly requested invitations, read and reconcile exact Guest IDs, then use `send_guest_invitations`. It requires communication consent and an Account-authenticated recipient review. Check `get_proposal_status` and `get_communication_status`; accepted, failed and unknown outcomes are distinct from delivery. Never expose invitation tokens or automatically retry unknown attempts.
