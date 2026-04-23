# Skill Routing Guide

This routing guide explains how to steer the **RexBot / Rex Hub OpenClaw skill library**.

## First question

What is the real bottleneck?

- uncertainty about what to do -> core routing/planning
- safety uncertainty -> safety
- truth uncertainty -> research
- code/system change -> engineering
- decision framing -> product/program
- shipping confidence -> quality/security
- audience attention -> attention/sales/docs

## Routing ladder

1. route
2. plan
3. risk-gate if needed
4. invoke the domain specialist
5. review
6. verify
7. hand off

## Fast routing hints

- ambiguous request -> `core_route_request`
- risky step -> `core_risk_gate`
- stale claim risk -> `res_source_check` + `safe_external_claims`
- bug/fix -> engineering
- user flow confusion -> design or product
- release blocker -> QA + engineering + safety as needed
- buyer movement problem -> sales
- public narrative problem -> attention + proof + research

## When to re-route

Re-route when:
- the actual bottleneck changed
- the task crossed into a new risk class
- the current skill is producing generic output
- the missing input belongs to another domain
