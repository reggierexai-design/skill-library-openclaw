#!/usr/bin/env python3
"""Update manifest.json to reflect actual skill counts and stats."""
import os, json, re
from collections import defaultdict

REPO_DIR = r"E:\rexhub-repos\skill-library-openclaw"
SKILLS_DIR = os.path.join(REPO_DIR, "skills")

# Count actual skills and stats
categories = defaultdict(lambda: {"count": 0, "words": []})
total_skills = 0
total_words = 0
min_words = float('inf')
max_words = 0
slash_visible = 0
model_visible = 0
slash_first = 0
internal_only = 0

for skill_dir in sorted(os.listdir(SKILLS_DIR)):
    skill_path = os.path.join(SKILLS_DIR, skill_dir, "SKILL.md")
    if not os.path.exists(skill_path):
        continue
    
    with open(skill_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    word_count = len(content.split())
    total_words += word_count
    total_skills += 1
    min_words = min(min_words, word_count)
    max_words = max(max_words, word_count)
    
    # Extract category
    cat = skill_dir.split("_")[0]
    cat_map = {
        "ai": "ai", "att": "attention", "comm": "community", "core": "core",
        "data": "data", "des": "design", "doc": "documentation", "eng": "engineering",
        "finance": "finance", "legal": "legal", "ops": "operations", "pm": "program",
        "prod": "product", "qa": "quality", "res": "research", "safe": "safety",
        "sales": "sales", "sec": "security", "solo": "solo_founder", "vibe": "vibe_coding",
    }
    full_cat = cat_map.get(cat, cat)
    categories[full_cat]["count"] += 1
    categories[full_cat]["words"].append(word_count)
    
    # Check frontmatter flags
    if "user-invocable: true" in content:
        slash_visible += 1
    if "user-invocable: true" in content and "disable-model-invocation: true" in content:
        slash_first += 1
    if "disable-model-invocation: false" in content:
        model_visible += 1
    if "user-invocable: false" in content and "disable-model-invocation: false" in content:
        internal_only += 1

avg_words = round(total_words / total_skills) if total_skills > 0 else 0

# Build category counts
cat_counts = {}
for cat_name, data in sorted(categories.items()):
    cat_counts[cat_name] = data["count"]
    avg_cat = round(sum(data["words"]) / len(data["words"]))
    print(f"  {cat_name}: {data['count']} skills, avg {avg_cat} words")

# Build manifest
manifest = {
    "name": "openclaw-generalist-skill-library",
    "version": "1.0.0",
    "summary": f"The Ultimate OpenClaw Skill Library — {total_skills} domain-deep operating playbooks across {len(categories)} categories, including solo founder, legal, finance, vibe coding, and community skills. No filler, no boilerplate — every skill is genuine domain expertise.",
    "counts": {
        "skills": total_skills,
        "categories": cat_counts,
        "internal_only": internal_only,
        "slash_visible": slash_visible,
        "model_visible": model_visible,
        "slash_first": slash_first,
        "profiles": 24,
    },
    "prompt_overhead": {
        "full_library_model_visible_chars": round(avg_words * 5),
        "full_library_model_visible_tokens": round(avg_words * 5 / 4),
    },
    "content_depth": {
        "avg_skill_words": avg_words,
        "min_skill_words": min_words,
        "max_skill_words": max_words,
    },
    "publisher": "RexBot / Rex Hub",
    "homepage": "https://reggierexai-design.github.io/rexhub/",
    "project_attribution": f"Ultimate v1.0 OpenClaw skill library published by RexBot / Rex Hub. {total_skills} domain-deep skills, zero boilerplate.",
    "official_openclaw_pack": False,
    "platform_target": "OpenClaw",
}

manifest_path = os.path.join(REPO_DIR, "manifest.json")
with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)

print(f"\nManifest updated: {total_skills} skills, avg {avg_words} words, min {min_words}, max {max_words}")
