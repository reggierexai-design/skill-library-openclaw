# Deployment Guide

This guide covers deployment of the **RexBot / Rex Hub OpenClaw skill library**.

## Recommended install pattern

Place the skill pack in a shared or workspace-specific skills directory, then expose only the profiles the target agent really needs.

## Deployment modes

### Mode A: minimal default
Use `minimal_core` plus one domain profile.

Best for:
- daily operator work
- experimentation
- agents that must stay prompt-lean

### Mode B: role-based agents
Give each agent one primary role:
- engineering
- docs/support
- research
- product/design
- launch/attention
- sales/revenue
- AI builder
- security/quality
- program/operator

### Mode C: power-user workstation
Expose a broader profile set to an experienced operator who understands context-budget tradeoffs.

## Rollout checklist

- validate the pack locally
- start with a narrow profile
- test routing on representative tasks
- verify slash commands appear as expected
- check risky workflows still route through safety layers
- only then widen the profile

## Full-library warning

The pack ships with broad coverage, but the broadest deployment mode is not the recommended default. Use profile composition first.

## Files to use during deployment

- `PROFILE_SELECTION_GUIDE.md`
- `SKILL_ROUTING_GUIDE.md`
- `examples/openclaw.skill-pack.json5`
- `examples/AGENTS.skill-library.md`
