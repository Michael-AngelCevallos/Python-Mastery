# Engineering Decision #008

## Title

Reserve 001 for Index Files

---

## Status

Accepted

---

## Context

As the repository grew, every major section required a consistent navigation starting point.

Without a standard, users would need to learn a different layout for each section.

---

## Decision

The file number `001` is permanently reserved for the index file of every major section.

Examples include:

- 001_Engineering_Principles_Index.md
- 001_Engineering_Decisions_Index.md
- 001_Knowledge_Base_Index.md
- 001_Progress_Index.md

Content begins at `002`.

---

## Why

- Creates consistent navigation.
- Makes every section predictable.
- Simplifies website generation in the future.
- Reduces confusion when adding new content.

---

## Alternatives Considered

- No index files.
- README.md as the index.
- Number content starting at 001.

---

## Consequences

### Positive

✔ Consistent structure across the academy.

✔ Easier navigation.

✔ Scales to future language repositories.

### Negative

• Content numbering begins at 002 instead of 001.