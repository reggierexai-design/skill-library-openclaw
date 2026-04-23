# System Overview

This library is a **community OpenClaw skill system published by RexBot / Rex Hub**.

## Design goal

The library is designed to solve two problems at once:

1. give OpenClaw a broad set of specialist behaviors
2. keep the default prompt budget under control by using profiles, allowlists, and slash-first specialists

## The operating model

The pack is intentionally layered.

### Layer 1: core control plane
These skills shape how work starts, routes, executes, reviews, and closes.

Examples:
- `core_route_request`
- `core_plan_task`
- `core_execute_safely`
- `core_review_changes`
- `core_verify_done`

### Layer 2: safety gates
These slow the system down when secrets, public claims, live systems, or high-impact changes are involved.

Examples:
- `core_risk_gate`
- `safe_secret_hygiene`
- `safe_external_claims`
- `safe_high_impact_changes`

### Layer 3: domain specialists
These produce the actual work products in engineering, research, product, docs, data, design, AI, sales, quality, security, and attention work.

### Layer 4: profile composition
Profiles keep each agent lean by exposing only the subset of skills it should normally see.

## How skill depth works in v0.6

Each skill is now written as a mini-playbook. The goal is not maximum verbosity. The goal is to make each skill:

- easier to invoke correctly
- harder to misuse
- more consistent across categories
- better at producing handoff-ready outputs
- better aligned with real OpenClaw operator flows

## How to think about skill visibility

- **model-visible** skills are eligible to appear in OpenClaw's compact available-skills list
- **slash-first** skills are intentionally specialized and kept out of the default model prompt
- **internal** skills are primarily routing, safety, or orchestration layers

## Recommended mental model

Use this pack like a **toolbox with a dispatcher**, not like one giant prompt.

- narrow profile + good routing beats universal enablement
- deeper skill instructions beat vague role labels
- safety skills should remain active when the task gets riskier
- handoff discipline matters as much as initial generation quality

## Attribution note

- Publisher: RexBot / Rex Hub
- Platform target: OpenClaw
- Status: community-maintained, not an official OpenClaw bundle
