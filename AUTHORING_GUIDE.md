# Authoring Guide

## Overview
New skills must follow the same anatomy as v0.6 skills.

## Structure
Each skill must include:
1. Frontmatter (yaml header)
2. Purpose
3. Use when
4. Avoid when
5. Inputs to gather
6. Operating rules
7. OpenClaw tool pattern
8. Expanded workflow
9. Output contract
10. Failure modes to avoid
11. Handoff cues
12. Example invocation
13. Quality bar

## Frontmatter
```yaml
---
name: <skill-key>
description: "<short description>
user-invocable: true
disable-model-invocation: false
metadata:
  openclaw:
    emoji: "🔥"
```

## Validation
Run `python scripts/validate_skills.py` to verify all skills meet the required anatomy.

## Profile updates
When adding a new skill, update the relevant profiles to include it.
