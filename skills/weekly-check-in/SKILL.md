---
name: weekly-check-in
description: Use when the couple asks for a status update, a weekly check-in, "what should we do next?", or a countdown summary for their wedding on Tu Día de Blanco. Produces a short prioritised briefing from the tudiadeblanco connector without changing anything.
---

# Weekly wedding check-in

This is read-only: don't change anything unless the couple asks afterwards. Follow the rules in the `wedding-workspace` skill.

## Steps

1. Call `get_wedding_overview`.
2. Drill down only where something needs attention:
   - RSVPs: `invited_no_answer` > 0 and the wedding is within 8 weeks → `list_guests` with `rsvp_status: "pending"`.
   - Seating: `confirmed_unseated` > 0 → `get_seating_plan`.
   - Budget: `get_budget` for `overdue_payments` and `due_next_30_days`.
   - Tasks: `list_tasks`, open tasks, sorted by due date.
   - Letters: `unread_letters` > 0 → `list_letters` with `unread_only: true`. Summarise them warmly; don't quote them in full unless asked.
3. Write the briefing:

```
**Faltan N días** (or "N days to go")

Esta semana (this week)
1. … the most urgent item, with the concrete next step
2. …
3. …

Números (the numbers): RSVPs x/y confirmed · mesas x/y sentados · presupuesto x/y pagado
```

## Prioritising

1. Overdue payments.
2. Overdue tasks.
3. RSVP chasing: within 8 weeks of the date.
4. Unseated confirmed guests: within 4 weeks.
5. Payments due in the next 30 days.
6. Unread letters.

Keep it to at most five items. End by offering one concrete action, e.g. "¿Quieres que cree una tarea para llamar a los que no han contestado?".
