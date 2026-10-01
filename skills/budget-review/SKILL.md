---
name: budget-review
description: Use when the couple asks about their wedding budget on Tu Día de Blanco — how much is spent or owed, upcoming or overdue payments, where they're over budget, or recording a quote, deposit or payment. Reads and updates budget lines through the tudiadeblanco connector.
---

# Budget review

Requires the `budget` module. Follow the rules in the `wedding-workspace` skill.

## Reviewing

1. Call `get_budget`. It returns `currency`, `totals`, `overdue_payments`, `due_next_30_days` and `items`. Amounts are plain numbers in `currency`; never convert them.
2. Report:
   - **Totals:** Planned vs Cost, Paid and Still due. Map tool fields to those labels; `deposits_paid` is cumulative Paid, not only deposits.
   - **Over budget:** items where `actual > budgeted`, largest overrun first.
   - **Cash flow:** overdue payments first, then what's due in the next 30 days, with dates.
   - **Gaps:** common Sections that are missing, compared with typical weddings (venue, catering, photography, flowers, music, attire, rings, stationery, transport, hair & make-up). Mention them only; don't add them unasked.

## Recording changes

| The couple says | Call | With |
| --- | --- | --- |
| "Got a quote" | `add_budget_item` or `update_budget_item` | `budgeted` for a planning estimate; `actual` for an agreed Cost. Ask when the distinction is unclear. |
| "Made a payment" | `record_budget_payment` | `amount` is the new payment already made; fully_paid only when confirmed |
| "Paid in full" | `update_budget_item` | Confirm final Cost and set cumulative `deposit_paid` to total Paid, with `paid_status: "fully_paid"` |
| "Due on …" | `update_budget_item` | `payment_due_date` (ISO date) |

- For an existing vendor, find the line in `items` first. Don't create a duplicate.
- `delete_budget_item` is destructive. Confirm first; prefer updating.
- For a payment, establish whether the supplied amount is a new payment or the cumulative total. `update_budget_item` replaces the cumulative `deposit_paid`; `record_budget_payment` adds a new payment atomically. Ask if the final Cost or payment amount needed for a full-payment update is missing.
- The connector uses Planned as a fallback when Cost is zero, and treats a Paid state as zero outstanding. This is the confirmed Still due rule; label figures based on Planned as estimates when the agreed Cost is unknown.
- After changes, call `get_budget` again and show the returned updated totals.

## Review and batches

Start with `get_capabilities` and follow `wedding-workspace`. Writes prepare pending web proposals; give the approval URL and inspect get_proposal_status. Read totals after applied status, never before claiming a save. Check uncertain outcomes before retrying.

Use record_budget_payment for a vendor payment already made. It never charges money. apply_budget_batch reviews up to 100 additions/edits atomically, and export_budget reads paginated rows. Omitted fields stay unchanged. Currency changes labels without converting amounts.

## Language

Support English and Spanish. Reply in the language the user uses, and follow an explicit language preference. Explain statuses and approval steps in that language. Preserve proper names, user-authored content, IDs, tool names and enum values; do not translate stored content unless requested.
