# OpenClaw Generalist Skill Library v0.6

**RexBot / Rex Hub community release for OpenClaw.**

A free, community-maintained, OpenClaw-native skill library for general-purpose execution across engineering, product, docs, data, design, program work, AI-agent building, revenue work, quality, security, and project attention.

## What changed in v0.6

v0.6 is the **depth release**.

Instead of inflating the raw skill count, this version deepens **every skill** into a fuller operator playbook. Each skill now follows the same expanded structure:

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

## Library stats

- **185 skills**
- **15 categories**
- **164 slash-visible skills**
- **21 internal-only orchestration or safety skills**
- **76 model-visible skills**
- **109 slash-first specialist skills**
- **619.4 average words per skill** (range: 581–669)

## Attribution

This is a **community OpenClaw skill library published by RexBot / Rex Hub**.

- **Platform target:** OpenClaw
- **Publisher / attribution:** RexBot / Rex Hub
- **Homepage:** `https://reggierexai-design.github.io/rexhub/`
- **Status:** community-maintained, not an official OpenClaw bundle

Use this wording when sharing the pack publicly:

> OpenClaw Generalist Skill Library for RexBot / Rex Hub — a community-maintained, OpenClaw-native skill pack.

## New and upgraded operator docs

- `START_HERE.md`
- `TRAINING_MANUAL.md`
- `SYSTEM_OVERVIEW.md`
- `DEPLOYMENT_GUIDE.md`
- `AGENT_INTEGRATION_GUIDE.md`
- `PROFILE_SELECTION_GUIDE.md`
- `SKILL_ROUTING_GUIDE.md`
- `AUTHORING_GUIDE.md`
- `SKILL_ANATOMY_REFERENCE.md`
- `WORKED_EXAMPLES.md`
- `ROUTING_RECIPES.md`
- `CATALOG_DETAILED.md`

## Recommended rollout

1. Start with `profiles/minimal_core.json5` or a narrow specialist profile.
2. Add one or two domain profiles per agent instead of enabling the entire library globally.
3. Keep high-risk domains routed through the safety, quality, and security layers.
4. Treat the full-library profile as a power-user mode, not the default.

## Included profiles

The pack still ships with the existing profile set so OpenClaw deployments can stay selective rather than enabling everything at once. See `PROFILE_SELECTION_GUIDE.md` for the recommended rollout order and `examples/` for config snippets.

## Quick positioning

This pack is best described as:

- **OpenClaw-specific**
- **community-maintained**
- **profile-first**
- **safety-forward**
- **deeper than a bare prompt pack**
- **built to support real operator workflows and handoffs**

## Validation

Run:

```bash
python scripts/validate_skills.py
```

The validator now checks the deeper skill anatomy, frontmatter integrity, profile references, and compact-prompt overhead estimates.

## License

See `LICENSE`.
