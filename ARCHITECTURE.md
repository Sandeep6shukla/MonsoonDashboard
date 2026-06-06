# Architecture

## Pipeline

RSS Feed

↓

Cache Layer

↓

Parser

↓

Raw JSON

↓

Business Processor

↓

Aggregation

↓

Dashboard

↓

Notifications

---

## Module Responsibilities

Collectors

Purpose:
Fetch data.

Never:
Interpret data.

---

Cache

Purpose:
Avoid unnecessary downloads.

Never:
Parse data.

---

Parser

Purpose:
Convert to structured JSON.

Never:
Apply business logic.

---

Processor

Purpose:
Generate business intelligence.

---

Dashboard

Purpose:
Display information.

Never:
Calculate business logic.