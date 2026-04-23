# Start Here

This is the **RexBot / Rex Hub community OpenClaw skill library**.

It is written specifically for **OpenClaw**, but it is **not** an official OpenClaw bundle.

## What this pack is for

Use this pack when you want OpenClaw agents to have a broad but structured operating library across:

- engineering
- product
- docs
- data
- design
- program management
- AI/agent work
- sales and revenue work
- quality
- security
- project attention and distribution

## What changed in v0.6

v0.6 is the first version where the entire library behaves like a **playbook system** rather than a loose collection of short role prompts.

Every skill now contains the same deeper anatomy:

- purpose
- use/avoid guidance
- inputs to gather
- operating rules
- OpenClaw tool pattern
- expanded workflow
- output contract
- failure modes
- handoff cues
- invocation examples
- quality bar

Average depth in this release: **619.4 words per skill**.

## The safest way to deploy it

Do **not** enable the whole library everywhere by default.

Use the included profiles:

1. start with `minimal_core`
2. add one domain profile per agent
3. only use broad profiles after the routing behavior is stable
4. keep safety, quality, and security layers enabled for risky work

## Read these next

- `SYSTEM_OVERVIEW.md`
- `TRAINING_MANUAL.md`
- `PROFILE_SELECTION_GUIDE.md`
- `SKILL_ROUTING_GUIDE.md`
- `examples/AGENTS.skill-library.md`

## Attribution note

- Publisher: RexBot / Rex Hub
- Platform target: OpenClaw
- Status: community-maintained, not an official OpenClaw bundle
