# Authoring Guide

This guide explains how to write new skills that match the v0.6 library standard.

## Required anatomy

Every skill should include:

- `Purpose`
- `Use when`
- `Avoid when`
- `Inputs to gather`
- `Operating rules`
- `OpenClaw tool pattern`
- `Expanded workflow`
- `Output contract`
- `Failure modes to avoid`
- `Handoff cues`
- `Example invocation`
- `Quality bar`

## Writing principles

- make the skill operational, not just aspirational
- define when the skill should not be used
- tell the operator what inputs actually matter
- shape tool use without assuming one exact runtime path
- define what “done” looks like
- include handoff behavior so the work survives beyond one turn

## Style

- use short bullets
- prefer specific operating language over abstract advice
- avoid hype
- avoid redundant prose
- keep frontmatter compact
- keep descriptions short because metadata is what OpenClaw carries by default

## Naming

- use short, stable snake_case names
- keep the prefix aligned with the library taxonomy
- prefer names that describe the owned output or mode of work

## Validation

Run `python scripts/validate_skills.py` after changes.
