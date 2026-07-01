# Python Mastery Repository Standards

Version: 1.0

---

# Purpose

This repository is designed to serve as both a Python learning environment and a long-term engineering knowledge base.

Every file has a specific purpose.

Every piece of information has exactly one authoritative home.

---

# Repository Philosophy

The goal is not simply to learn Python.

The goal is to build the habits, documentation, organization, and engineering mindset used by professional software engineers.

---

# Folder Responsibilities

## 01_Fundamentals → 13_Capstone

Contains:

- Python source code
- Exercises
- Challenges
- Projects
- Practice

Contains NO permanent documentation.

---

## 02_Knowledge_Base

Contains permanent reference documentation.

Every article answers:

"What is this?"

Examples:

- What is Python?
- What is a Variable?
- What is a Function?
- What is a Dictionary?

---

## 03_Progress

Contains learning progress.

Examples:

- Study Log
- Phase Completion
- Progress Tracking
- Milestones

Contains NO technical reference documentation.

---

## 04_Resources

Contains:

- PDFs
- Cheat Sheets
- Diagrams
- Books
- External Resources

---

## Templates

Contains reusable document templates.

---

## Sandbox

Contains temporary experiments.

Nothing inside Sandbox should be considered permanent.

---

## Portfolio Projects

Contains polished projects intended for GitHub portfolio presentation.

---

# Lesson Workflow

Every lesson follows the same workflow.

Study Concept

↓

Write Code

↓

Run & Test

↓

Code Review

↓

Knowledge Base Update

↓

Progress Update

↓

Git Commit

---

# Code Organization

Lesson folders contain code only.

Example

01_Fundamentals/

    01_Variables/

        lesson01_variables.py

        challenge01.py

        practice.py

Documentation does not belong here.

---

# Knowledge Base Standard

Every concept receives exactly one article.

Example

02_Knowledge_Base/

    02_Python/

        007_What_Is_A_Variable.md

Articles explain concepts.

They do not document lesson progress.

---

# Knowledge Base Template

Every article follows this structure.

- Definition
- Purpose
- Mental Model
- Syntax
- Examples
- Naming Conventions (if applicable)
- Common Mistakes
- Engineering Notes
- Related Topics

---

# Engineering Principles

Engineering Principles capture timeless software development practices.

Examples

- Write readable code.
- Prefer clarity over cleverness.
- Use descriptive variable names.

These are language independent whenever possible.

---

# Engineering Decisions

Engineering Decisions capture architectural decisions made throughout this project.

Examples

- One lesson per folder.
- One concept per Knowledge Base article.
- Run scripts from project root.

---

# Git Workflow

After every completed lesson:

1. Review Code
2. Update Knowledge Base
3. Update Progress
4. Commit Changes

Commit messages should describe completed work.

Example

Phase 1 - Complete Lesson 01 Variables

---

# Single Source of Truth

Every piece of information belongs in one location only.

Code belongs in lesson folders.

Concepts belong in the Knowledge Base.

Progress belongs in Progress.

Resources belong in Resources.

Engineering principles belong in Engineering Principles.

Engineering decisions belong in Engineering Decisions.

Avoid duplicating information.

Maintain one authoritative source for every topic.

---

# Long-Term Goal

This repository should evolve into a professional engineering reference that documents both Python knowledge and software engineering practices developed throughout the Python Mastery journey.