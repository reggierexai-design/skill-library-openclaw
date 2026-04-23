# Agent Integration Guide

## Overview
This guide explains how to integrate the skill library into a running OpenClaw agent.

## Steps
1. Choose a profile from `profiles/`.
2. Install it using `python scripts/install_profile.py <profile>`.
3. Restart your agent and verify the skills are discoverable.
4. Keep standing guidance in `AGENTS.md` or equivalent workspace notes.

## Profile routing
Start with `minimal_core` and add domain profiles one at a time.
Do not enable the full library globally intead of using profiles.

## Model-ysing overhead
Each profile includes an `estimated_prompt_tokens` field.
Keep the total model-visible overhead under 4 K tokens for best results.

## Handoff between skills
Skills emit handoff cues when their work crosses into another skill‧ domain.
Follow the handoff cues in the skill's output contract to decide whether to re-route.
