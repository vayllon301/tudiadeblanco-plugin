---
name: website-management
description: Use when the user wants to manage their Tu Día de Blanco Invitation Website, public schedule, guest Updates, Concierge configuration or custom Domain.
---

# Website Management

Check `get_capabilities` once per conversation or after a permission error and follow `wedding-workspace`. Read `get_invitation_website`, `get_schedule` and relevant Concierge/Domain state before editing. Preserve omitted settings. All public changes, including edits to already public content, require publication consent and apply immediately, so confirm with the user before publishing. Read `get_website_service` for expiry and usage; never change commercial limits.

Use the Website tools for design, visibility, access, Story, FAQ, Gifts and Gallery; `set_website_published` controls publication. Design is the `template`: `classic`, `romantic`, `modern`, `stationery`, `magazine`, `gazette`, `watercolor`, `letter`, `deco`, `mediterranean`, `boarding`, `zen`, `premiere`, `gallery`, `vinyl`, `blueprint`, `herbarium`, `bistro`, `manuscript`, `riviera`, `neon`, `papercut` or `toile`. Each carries its own colours; there are no palettes. `replace_schedule` takes the complete ordered timeline with durations and pins. Upload images via `prepare_upload`; obtain the result before using it in a public section. An uploaded image has not automatically been published in a Gallery.

Read `get_concierge_config`; `update_concierge_config` preserves omitted fields and affects guest answers immediately. Keep private Documents/Notes out of the guest-shared brief unless the user explicitly asks to share the selected content. `preview_concierge` tests the published Concierge, consumes normal usage and follows its existing quota and availability gates.

Custom Domain writes are Owner-only. Pending attachment, DNS instructions and active verified status are different states. Never claim ownership is verified before the tool returns the active state.

## Language

Support English and Spanish. Reply in the language the user uses, and follow an explicit language preference. Explain statuses in that language. Preserve proper names, user-authored content, IDs, tool names and enum values; do not translate stored content unless requested.
