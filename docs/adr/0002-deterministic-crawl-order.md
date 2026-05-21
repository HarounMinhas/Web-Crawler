# ADR 0002: Deterministic Crawl Order and Scope

## Status
Accepted

## Context
Backlog requirements call for deterministic architecture constraints.

## Decision
- Use BFS traversal.
- Normalize URLs (remove query + fragment).
- Keep crawl scope on seed host.
- Sort discovered links before enqueueing.

## Consequences
- Repeatable output for tests and reproducibility.
- Some dynamic pages become intentionally de-prioritized.
