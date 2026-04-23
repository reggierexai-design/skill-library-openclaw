#!/usr/bin/env python3
from __future__ import annotations
import json, re, sys, statistics
from collections import Counter
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape
import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
PROFILES_DIR = ROOT / "profiles"
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
NAME_RE = re.compile(r"^[a-z0-9_]+$")
CATEGORY_BY_PREFIX = {
    "att":"attention","core":"core","eng":"engineering","ops":"operations","prod":"product","res":"research",
    "safe":"safety","ai":"ai","data":"data","doc":"documentation","des":"design","pm":"program","sales":"sales",
    "qa":"quality","sec":"security"
}
REQUIRED_SECTIONS = [
    "## Purpose",
    "## Use when",
    "## Avoid when",
    "## Inputs to gather",
    "## Operating rules",
    "## OpenClaw tool pattern",
    "## Expanded workflow",
    "## Output contract",
    "## Failure modes to avoid",
    "## Handoff cues",
    "## Example invocation",
    "## Quality bar",
]

def parse_skill(path: Path):
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError("missing frontmatter")
    fm = yaml.safe_load(match.group(1))
    if not isinstance(fm, dict):
        raise ValueError("frontmatter must be a mapping")
    return fm, text[match.end():]

def estimate_skill_chars(name: str, description: str, location: str) -> int:
    return 97 + len(xml_escape(name)) + len(xml_escape(description)) + len(xml_escape(location))

def estimate_prompt_chars(rows):
    visible = [r for r in rows if not r[3]]
    return 0 if not visible else 195 + sum(estimate_skill_chars(*r[:3]) for r in visible)

def parse_profile_names(path: Path):
    return re.findall(r'"([a-z0-9_]+)"', path.read_text(encoding="utf-8"))

def main() -> int:
    failures, warnings = [], []
    rows = []
    by_category = Counter()
    word_counts = []
    for path in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        try:
            fm, body = parse_skill(path)
        except Exception as exc:
            failures.append(f"{path}: {exc}")
            continue
        folder = path.parent.name
        name = fm.get("name")
        if not isinstance(name, str) or not name:
            failures.append(f"{path}: invalid name")
            continue
        if folder != name:
            failures.append(f"{path}: folder name must match skill name")
        if not NAME_RE.match(name):
            failures.append(f"{path}: invalid skill name format")
        desc = fm.get("description")
        if not isinstance(desc, str) or not desc.strip():
            failures.append(f"{path}: invalid description")
        if isinstance(desc, str) and len(desc) > 115:
            warnings.append(f"{path}: long description ({len(desc)} chars)")
        if not isinstance(fm.get("user-invocable"), bool):
            failures.append(f"{path}: user-invocable must be boolean")
        if not isinstance(fm.get("disable-model-invocation"), bool):
            failures.append(f"{path}: disable-model-invocation must be boolean")
        metadata = fm.get("metadata")
        if not isinstance(metadata, dict):
            failures.append(f"{path}: metadata must be a mapping")
        prefix = name.split("_", 1)[0]
        category = CATEGORY_BY_PREFIX.get(prefix)
        if not category:
            failures.append(f"{path}: unknown prefix {prefix}")
        else:
            by_category[category] += 1
        if not body.strip().startswith("# "):
            failures.append(f"{path}: body must start with a level-1 heading")
        for section in REQUIRED_SECTIONS:
            if section not in body:
                failures.append(f"{path}: missing required section {section}")
        wc = len(re.findall(r"\b\w+\b", body))
        word_counts.append(wc)
        if wc < 300:
            warnings.append(f"{path}: shallow body ({wc} words)")
        rows.append((name, str(desc), f"skills/{folder}/SKILL.md", bool(fm.get("disable-model-invocation"))))
    skill_map = {r[0]: r for r in rows}
    for profile_path in sorted(PROFILES_DIR.glob("*.json5")):
        missing = [n for n in parse_profile_names(profile_path) if n not in skill_map]
        if missing:
            failures.append(f"{profile_path}: unknown skills referenced: {', '.join(missing)}")
    if failures:
        print("FAIL")
        for f in failures:
            print("-", f)
        return 1
    print("PASS")
    print(f"skills: {len(rows)}")
    print(f"model_visible_prompt_chars: {estimate_prompt_chars(rows)}")
    print(f"avg_skill_words: {statistics.mean(word_counts):.1f}")
    print(f"min_skill_words: {min(word_counts)}")
    print(f"max_skill_words: {max(word_counts)}")
    print("categories:")
    for cat, count in sorted(by_category.items()):
        print(f"  {cat}: {count}")
    if warnings:
        print("warnings:")
        for w in warnings[:40]:
            print("-", w)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
