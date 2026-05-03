# OpenClaw Generalist Skill Library v1.0 Ultimate

**RexBot / Rex Hub community release for OpenClaw.**

A free, community-maintained, OpenClaw-native skill library for general-purpose execution across engineering, product, docs, data, design, program work, AI-agent building, revenue work, quality, security, project attention, solo founder operations, legal compliance, finance, vibe coding, and community building.

## What changed in v1.0 Ultimate

v1.0 is the **Ultimate release**. Every skill has been upgraded from boilerplate to genuine domain expertise, and five new categories have been added for solo founders, legal, finance, vibe coding, and community operators.

### Upgraded (185 → 215 skills)
- **All 185 existing skills** rewritten with domain-specific content replacing generic boilerplate
- Average skill depth increased from ~690 words to ~1,100 words
- All 9 boilerplate phrases eliminated
- Every skill has a "Related workflows" section
- Inputs, Failure modes, Quality bars, and Handoff cues are now skill-specific

### New categories (5 new, 30 skills)
- **Solo Founder** (6): rhythm, context switch, scope guard, energy audit, rapid ship, wearing hats
- **Legal & Compliance** (6): terms review, privacy policy, cookie consent, IP check, disclaimer audit, vendor DPA
- **Finance** (6): pricing model, revenue forecast, burn rate, unit economics, invoice tracker, tax checklist
- **Vibe Coding** (6): prompt-to-app, debug no-code, deploy novice, AI pair program, prototype sprint, learning path
- **Community** (6): onboarding flow, ritual design, conflict resolution, feedback system, growth loop, retention audit

### New profiles (4 new, 26 total)
- **solo_founder_full**: Complete solo founder with legal, finance, vibe coding, and community
- **vibe_coder**: AI-assisted development essentials
- **community_builder**: Community growth, retention, and operations
- **legal_finance_operator**: Legal compliance and financial management

## Library stats
- **215 skills** across **20 categories**
- **~1,100 average words per skill** (range: 800–1,500)
- **891 KB total library size**
- **26 profiles** including 4 new specialist profiles
- **12 required sections per skill**

## Attribution

This is a **community OpenClaw skill library published by RexBot / Rex Hub**.

- **Platform target:** OpenClaw
- **Publisher / attribution:** RexBot / Rex Hub
- **Homepage:** `https://reggierexai-design.github.io/rexhub/`
- **Status:** community-maintained, not an official OpenClaw bundle

Use this wording when sharing the pack publicly:

> OpenClaw Generalist Skill Library for RexBot / Rex Hub — a community-maintained, OpenClaw-native skill pack.

## Categories

| Category | Skills | Description |
|----------|--------|-------------|
| ai | 12 | Agent design, prompt architecture, evals, routing, memory |
| attention | 26 | Project attention, positioning, launch, proof, distribution |
| community | 6 | Onboarding, rituals, conflict, feedback, growth, retention |
| core | 13 | Essential planning, routing, handoff, and safety skills |
| data | 10 | Analytics, metrics, segmentation, experiments |
| design | 9 | Design briefs, critique, UX, accessibility, visual direction |
| documentation | 11 | Docs architecture, quickstarts, API refs, troubleshooting |
| engineering | 20 | Repo work, debugging, review, release, incident response |
| finance | 6 | Pricing, forecasting, burn rate, unit economics, taxes |
| legal | 6 | Terms, privacy, cookies, IP, disclaimers, vendor DPAs |
| operations | 16 | Sprint planning, hiring, KPIs, vendor eval, runbooks |
| product | 16 | Product strategy, journeys, metrics, onboarding, retention |
| program | 9 | Roadmaps, milestones, governance, stakeholder updates |
| quality | 8 | Test planning, smoke tests, regression, accessibility |
| research | 10 | Competitor scans, interviews, market maps, source checks |
| safety | 8 | Browser login, PII minimization, secret hygiene, install gates |
| sales | 9 | Discovery, demos, proposals, pipeline, expansion |
| security | 8 | AppSec, threat modeling, data flow, access review |
| solo_founder | 6 | Rhythm, scope guard, energy, rapid shipping, hat inventory |
| vibe_coding | 6 | AI code generation, debug, deploy, pair program, prototype |

## Recommended rollout
1. Start with `profiles/minimal_core.json5` or a narrow specialist profile.
2. Add one or two domain profiles per agent instead of enabling the entire library globally.
3. Keep high-risk domains routed through the safety, quality, and security layers.
4. Treat the full-library profile as a power-user mode, not the default.
5. Solo founders: start with `profiles/solo_founder_full.json5` for the complete toolkit.
6. Vibe coders: start with `profiles/vibe_coder.json5` for AI-assisted development.

## Included profiles

The pack ships with 26 profiles so OpenClaw deployments can stay selective rather than enabling everything at once. See `PROFILE_SELECTION_GUIDE.md` for the recommended rollout order and `examples/` for config snippets.

## Quick positioning

This pack is best described as:
- **OpenClaw-specific**
- **community-maintained**
- **profile-first**
- **safety-forward**
- **deeper than a bare prompt pack**
- **built to support real operator workflows and handoffs**
- **domain-deep, not boilerplate**

## Validation

Run:
```bash
python scripts/validate_skills.py
```

The validator checks skill anatomy, frontmatter integrity, profile references, and compact-prompt overhead estimates.

## License

See `LICENSE`.
