# Tu Día de Blanco glossary (couple-facing)

This is a packaged vocabulary reference for the connector, maintained against `tudiadeblanco-docs/CONTEXT.md` in the product repository. It is not an independent product specification; implementation limits below were checked against source on 30 September 2026.

| Term | Meaning | Don't say |
| --- | --- | --- |
| Wedding | The celebration and everything about it: guests, seating, budget, website. | event, project |
| Couple | The two people getting married. | client, customer |
| Wedding Planner | A professional who may help run the wedding. Their private tasks and notes are never visible here. | vendor, coordinator |
| Workspace | Where the couple manages the wedding on tudiadeblanco.com. | control panel, dashboard |
| Guest | A person on the guest list. Has no account. | attendee, invitee |
| Guest list | Everyone invited. Curated by the couple in the Workspace. | contact list |
| RSVP status | `awaiting` (not invited yet) → `pending` (invited) → `confirmed` / `declined`. | |
| Plus-one | One extra person a guest may bring. | companion |
| Invitation Website | The public page guests visit: story, schedule, RSVP, gifts, updates, letters. | wedding page |
| Update | A post on the Invitation Website. The assistant can only create drafts. | news, announcement |
| Letter | A private message from a guest to the couple; read and managed in the Workspace. | comment |
| Concierge | The website's chatbot that answers guests' questions. | bot |
| Workbook | The couple's tasks and notes. Tasks can have due dates and email reminders 24 or 48 hours before. | to-do app |
| Module | A part of the Workspace (guests, seating, budget…). The plan decides which modules a wedding has. | feature |

## RSVP flow

1. The couple adds a guest (`awaiting`).
2. The couple sends invitations from the Workspace, and the status becomes `pending`.
3. The guest answers on the Invitation Website: `confirmed` or `declined`, plus dietary needs and notes.
4. The current RSVP stores a plus-one flag. It does not create an additional Guest, issue that person a code or reserve an extra seat; the future companion workflow remains pending at the product owner's latest request.

## Budget language

Use **Section**, **Expense**, **Planned**, **Cost**, **Paid**, **Still due**, and **Payment state** with the couple. Tool fields remain `category`, `budgeted`, `actual`, `deposit_paid`, `outstanding` and `paid_status`.

`deposit_paid` stores the cumulative amount paid, including subsequent payments. `paid_status: "deposit_paid"` means Partial; `fully_paid` means Paid. Currency is a display choice and never converts amounts.

The connector currently calculates `outstanding` from Cost when positive, otherwise Planned, minus Paid; a Paid state forces it to zero. The product owner confirmed this rule on 30 September 2026; the canonical glossary uses the same definition. Label figures based on Planned as estimates when the agreed Cost is unknown.
