# Profile Selection Guide

Use this guide to choose the right profile in the **RexBot / Rex Hub OpenClaw pack**.

## Best starting profiles

### `minimal_core`
Use when you want a safe default. This is the first profile to enable on almost any deployment.

### `generalist_builder`
Use when one operator handles mixed work across planning, docs, research, engineering, and execution.

### Specialist profiles
Use these when the agent has a stable role:
- `builder_engineering`
- `docs_support`
- `data_analytics`
- `design_product`
- `program_operator`
- `ai_builder`
- `commercial_operator`
- `security_quality`
- `attention_builder`

## Selection rule

Choose the smallest profile set that still lets the agent:
- route correctly
- solve its common bottlenecks
- stay safe in the risk domains it touches

## Expansion rule

Only add another profile when you can point to a workflow gap that the current composition cannot handle cleanly.

## Full-library rule

Treat `full_library` as a diagnostic or expert mode, not the default deployment.
