# Training Manual

This manual teaches operators how to use the **RexBot / Rex Hub community skill library for OpenClaw**.

## What the library teaches

The pack teaches an OpenClaw setup how to:

- route work before jumping into specialist behavior
- choose a safe operating path before touching risky surfaces
- gather only the context that changes the answer
- produce artifacts another operator can continue from
- prefer minimal, verifiable moves over broad speculative action

## Core habits

### 1. Start with routing
For mixed or ambiguous tasks, route first.

Good pattern:
- `core_route_request`
- `core_plan_task`
- relevant specialist skill
- `core_review_changes`
- `core_verify_done`

### 2. Turn on risk thinking early
Use safety layers whenever the task touches:
- credentials
- public claims
- production or live systems
- installs or unknown scripts
- security-sensitive surfaces
- regulated or privacy-heavy data

### 3. Use specialists for the bottleneck
Do not invoke a domain because it sounds related. Invoke it because it owns the actual bottleneck.

Examples:
- bug root cause -> engineering
- market truth -> research
- artifact clarity -> docs
- handoff reliability -> operations
- buyer movement -> sales
- risk ranking -> security

### 4. End every pass with a usable result
A pass is not done because text exists. It is done when the next operator can act.

## How to read a v0.6 skill

Every skill has the same anatomy:

1. **Purpose** — what the skill exists to do
2. **Use when** — right-fit triggers
3. **Avoid when** — bad-fit cases
4. **Inputs to gather** — what context matters
5. **Operating rules** — hard constraints for the skill
6. **OpenClaw tool pattern** — how the skill should interact with workspace or web context
7. **Expanded workflow** — default ordered steps
8. **Output contract** — what the result should contain
9. **Failure modes to avoid** — common weak patterns
10. **Handoff cues** — what to leave behind for continuity
11. **Example invocation** — slash and natural-language activation ideas
12. **Quality bar** — what “good” looks like

## Common routing chains

### Repo change
- `core_scout_workspace`
- `eng_repo_onboarding`
- `eng_debug_systematically` or `eng_code_review_pass`
- `qa_risk_based_testing`
- `core_verify_done`

### Public launch asset
- `res_source_check`
- `att_message_house`
- `att_landing_page_story` or `att_launch_plan`
- `safe_external_claims`

### Docs/support problem
- `doc_docs_feedback_loop`
- `doc_quickstart_guide` or `doc_troubleshooting_guide`
- `ops_support_triage`

### AI/agent system work
- `ai_agent_spec`
- `ai_prompt_system` or `ai_rag_design`
- `ai_eval_harness`
- `ai_guardrail_review`

## What not to do

- do not enable every profile on every agent
- do not skip safety because the user is in a hurry
- do not trust stale web claims or stale local assumptions
- do not let a skill expand scope just because it can
- do not mark a task complete without a verification or handoff note

## Release mindset

The library is broad. The right deployment pattern is still **selective composition**.

Use this order:
1. minimal core
2. one or two work-domain profiles
3. add deeper specialists only when a workflow actually needs them
4. raise prompt budget only if the narrower profile approach is insufficient

## Attribution note

- Publisher: RexBot / Rex Hub
- Platform target: OpenClaw
- Status: community-maintained, not an official OpenClaw bundle
