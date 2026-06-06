Project:
India Weather Intelligence Platform

Goal:
Business continuity weather intelligence.

Architecture:
Collector -> Cache -> Parser -> Processor -> Dashboard.

Canonical Sources:
Government structured data.

Current Stage:
CAP Integration.

Coding Rules:
1. Inspect data first.
2. Preserve structured fields.
3. Single responsibility.
4. Dashboard never calculates business logic.

Current Sprint:
ETag caching.

Live Dashboard:
https://sandeep6shukla.github.io/MonsoonDashboard/