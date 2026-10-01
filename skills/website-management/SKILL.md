---
name: website-management
description: Use when the user wants to manage their Tu Día de Blanco Invitation Website, public schedule, guest Updates, Concierge configuration or custom Domain.
---

# Website Management

Start with `get_capabilities` and follow `wedding-workspace`. Read `get_invitation_website`, `get_schedule` and relevant Concierge/Domain state before proposing edits. Preserve omitted settings. All public changes, including edits to already public content, require publication consent and a web proposal. Read `get_website_service` for expiry and usage; never change commercial limits.

Use the Website tools for design, visibility, access, Story, FAQ, Gifts and Gallery; `set_website_published` controls publication. `replace_schedule` takes the complete ordered timeline with durations and pins. Upload images via `prepare_upload`; obtain the result before proposing its use in a public section. An uploaded image has not automatically been published in a Gallery.

Read `get_concierge_config`; `update_concierge_config` preserves omitted fields and affects guest answers after review. Keep private Documents/Notes out of the guest-shared brief unless the user explicitly asks to share the selected content. `preview_concierge` tests the published Concierge, consumes normal usage and follows its existing quota and availability gates.

Custom Domain writes are Owner-only and require review. Pending attachment, DNS instructions and active verified status are different states. Never claim ownership is verified before the tool returns the active state.
