---
name: website-management
description: Use when the user wants to manage their Tu Día de Blanco Invitation Website, give it a design of their own (a Custom design instead of a catalog template), or manage the public schedule, guest Updates, Concierge configuration or custom Domain.
---

# Website Management

Check `get_capabilities` once per conversation or after a permission error and follow `wedding-workspace`. Read `get_invitation_website`, `get_schedule` and relevant Concierge/Domain state before editing. Preserve omitted settings. All public changes, including edits to already public content, require publication consent and apply immediately, so confirm with the user before publishing. Read `get_website_service` for expiry and usage; never change commercial limits.

Use the Website tools for design, visibility, access, Story, FAQ, Gifts and Gallery; `set_website_published` controls publication. Design is the `template`: `classic`, `romantic`, `modern`, `stationery`, `magazine`, `gazette`, `watercolor`, `letter`, `deco`, `mediterranean`, `boarding`, `zen`, `premiere`, `gallery`, `vinyl`, `blueprint`, `herbarium`, `bistro`, `manuscript`, `riviera`, `neon`, `papercut` or `toile`. Each carries its own colours; there are no palettes. `replace_schedule` takes the complete ordered timeline with durations and pins. Upload images via `prepare_upload`; obtain the result before using it in a public section. An uploaded image has not automatically been published in a Gallery.

## Custom design

When the couple wants a look of their own rather than a catalog template, build a Custom design. Read `get_custom_design_spec` first: it is the contract (Sections and their pages, the `<tdb-*>` components, Liquid variables, allowed HTML and CSS, tokens and hosted fonts), the Wedding's current variable values and a complete example. Ask what the day should feel like (colours, mood, references) before writing. Use only real content through the Liquid variables; never invent names, dates, venues or images. Images must be the Wedding's own: the URLs in the variables, or ones the user uploads through `prepare_upload` with purpose `website_image`.

Write `invitation_html`, `ourday_html` and `css`, then call `validate_custom_design` and fix every error until `valid` is true; tell the user about any warning that leaves something out. `save_custom_design` stores a revision without changing what guests see and returns a `preview_url` the user opens while signed in. Only after they approve, and after confirming whether the Website is published (guests then see it at once), call `apply_custom_design`. To change an existing design, read it with `get_custom_design`, edit it and save a new revision. `update_invitation_website` with a `template` switches back to the catalog; saved designs stay available, and the Templates tab in the Workspace can switch back to the latest one.

Read `get_concierge_config`; `update_concierge_config` preserves omitted fields and affects guest answers immediately. Keep private Documents/Notes out of the guest-shared brief unless the user explicitly asks to share the selected content. `preview_concierge` tests the published Concierge, consumes normal usage and follows its existing quota and availability gates.

Custom Domain writes are Owner-only. Pending attachment, DNS instructions and active verified status are different states. Never claim ownership is verified before the tool returns the active state.

## Language

Support English and Spanish. Reply in the language the user uses, and follow an explicit language preference. Explain statuses in that language. Preserve proper names, user-authored content, IDs, tool names and enum values; do not translate stored content unless requested.
