# Agent Integration Guide

Use this guide when wiring the **RexBot / Rex Hub community pack** into OpenClaw agents.

## Integration principle

Attach skills to agents based on the work they actually perform, not on the fact that the skills exist.

## Good patterns

### Engineering agent
- core
- safety
- engineering
- quality
- selected docs/release skills

### Research/strategy agent
- core
- safety
- research
- product
- selected attention skills

### Launch/content agent
- core
- safety
- attention
- research
- docs
- selected product skills

### AI builder agent
- core
- safety
- AI
- engineering
- quality
- security

## Bad patterns

- every agent gets every profile
- no safety layer on public or risky work
- no quality/security layer on shipping workflows
- one profile doing both broad orchestration and narrow domain work without routing support

## AGENTS usage

Use the included examples as starting points, then trim aggressively. Broad skill availability should be earned by proven need.
