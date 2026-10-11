# Tu Día de Blanco glossary (couple-facing)

This is a packaged vocabulary reference for the connector, maintained against `tudiadeblanco-docs/CONTEXT.md` in the product repository. It is not an independent product specification; implementation limits below were checked against source on 7 October 2026.

| Term | Meaning | Don't say |
| --- | --- | --- |
| Wedding | The celebration and everything about it: guests, seating, budget, website. | event, project |
| Couple | The two people getting married. | client, customer |
| Wedding Planner | A professional who may help run the wedding. Their private tasks and notes are never visible here. | vendor, coordinator |
| Workspace | Where the couple manages the wedding on tudiadeblanco.com. | control panel, dashboard |
| Guest | A person on the guest list. Has no account. | attendee, invitee |
| Guest list | Everyone invited. Curated by the couple in the Workspace. | contact list |
| RSVP status | `awaiting` (not invited yet) → `pending` (invited) → `confirmed` / `declined`. | |
| Plus-one | A companion a guest brings, up to the number the couple allows. | plus-one nomination |
| Invitation Website | The public page guests visit: story, schedule, RSVP, gifts, updates, letters. | wedding page |
| Update | A post on the Invitation Website. The assistant saves new ones as drafts; publishing or scheduling one needs publication consent and a confirmation from the user. | news, announcement |
| Letter | A private message from a guest to the couple; read and managed in the Workspace. | comment |
| Concierge | The website's chatbot that answers guests' questions. | bot |
| Workbook | The wedding's tasks and notes. Each Side sees its own and what the other Side Shares. Tasks can have due dates and email reminders 24 or 48 hours before. | to-do app |
| Module | A part of the Workspace (guests, seating, budget…). The plan decides which modules a wedding has. | feature |

## RSVP flow

1. The couple adds a guest (`awaiting`).
2. The couple sends invitations from the Workspace, and the status becomes `pending`.
3. The guest answers on the Invitation Website: `confirmed` or `declined`, plus dietary needs and notes.
4. The couple sets how many companions each guest may bring (`companions_allowed`, 0–10, via `add_guest`/`update_guest`). On the RSVP the guest chooses from 0 up to that number and names each one. Each companion is registered as its own Guest (`companion_of` is the host Guest's ID), seatable like any other, but with no email, code or invitation of their own. The allowance is not attendance. A legacy plus-one flag without named companions still stands for one unnamed extra attendee.

## Budget language

Use **Section**, **Expense**, **Planned**, **Cost**, **Paid**, **Still due**, and **Payment state** with the couple. Tool fields remain `category`, `budgeted`, `actual`, `deposit_paid`, `outstanding` and `paid_status`.

`deposit_paid` stores the cumulative amount paid, including subsequent payments. `paid_status: "deposit_paid"` means Partial; `fully_paid` means Paid. Currency is a display choice and never converts amounts.

The connector currently calculates `outstanding` from Cost when positive, otherwise Planned, minus Paid; a Paid state forces it to zero. The product owner confirmed this rule on 30 September 2026; the canonical glossary uses the same definition. Label figures based on Planned as estimates when the agreed Cost is unknown.
