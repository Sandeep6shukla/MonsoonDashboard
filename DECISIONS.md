# Engineering Decisions

## Decision 1

Date:
06 Jun 2026

Decision:

CAP XML is the canonical government source.

Reason:

Contains structured severity, urgency, area and instructions.

Status:

ACTIVE

------------------------------------

## Decision 2

Date:
06 Jun 2026

Decision:

RSS feed is an index only.

Reason:

CAP XML provides richer information.

Status:

ACTIVE

------------------------------------

## Decision 3

Decision:

Use ETag caching.

Reason:

Official NDMA recommendation.

Status:

ACTIVE

------

Decision: Cache before optimizing.

Reason: Reduces rate limits.

Simplifies debugging.

Allows parser improvements without redownloading.

-----

Decision:

Cache raw source data.

Reason:

Parser improvements should not require re-downloading.

Status:

ACTIVE