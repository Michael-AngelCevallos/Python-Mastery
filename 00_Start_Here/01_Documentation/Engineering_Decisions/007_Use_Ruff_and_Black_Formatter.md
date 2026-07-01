# Engineering Decision #007

## Title

Use Ruff and Black Together

---

## Status

Accepted

---

## Context

Professional code should remain clean and consistent throughout development.

---

## Decision

Black will automatically format code.

Ruff will lint the code and identify potential issues.

---

## Why

Using both tools keeps the repository clean while reducing manual formatting work.

---

## Alternatives Considered

- Manual formatting
- Black only
- Ruff only

---

## Consequences

### Positive

✔ Consistent formatting

✔ Fewer mistakes

✔ Professional code quality

### Negative

• Requires two development tools.