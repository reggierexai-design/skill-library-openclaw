#!/usr/bin/env python3
"""
Deep expansion script - adds domain-specific depth to thin skill sections.
Targets: Operating rules, Expanded workflow, Output contract, Failure modes, Quality bar.
"""

import os, re

REPO_DIR = r"E:\rexhub-repos\skill-library-openclaw"
SKILLS_DIR = os.path.join(REPO_DIR, "skills")

# Category-specific depth additions for operating rules
# These get prepended to the existing operating rules section
CATEGORY_DEPTH = {
    "sec": {
        "operating_rules_extra": [
            "Use STRIDE (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege) as the threat enumeration framework unless the context demands a different model.",
            "Rate each threat by likelihood (1-5) x impact (1-5). Threats scoring 15+ need mitigations before ship. Threats scoring 8-14 need accepted-risk documentation. Below 8 is monitored.",
            "Every threat model must name the trust boundaries explicitly: where does untrusted input cross into a trusted zone? That boundary is the highest-value attack surface.",
            "Distinguish between threats to confidentiality, integrity, and availability. A threat to one is not necessarily a threat to the others.",
            "Threat models are attackergoal-first, not feature-first. Start from what an attacker wants to achieve, then trace backwards to how they could do it.",
        ],
        "quality_bar_extra": [
            "Every high-likelihood threat has a named mitigation or an explicitly accepted risk with rationale.",
            "Trust boundaries are diagrammed or clearly described.",
            "At least one insider threat scenario is included.",
            "The model is specific enough that an engineer could implement mitigations without guessing.",
        ],
    },
    "ops": {
        "operating_rules_extra": [
            "Operational decisions need runbook-level specificity. If a new operator could not follow the instruction without guessing, it is not specific enough.",
            "Distinguish between planned operations (deployments, rotations, scaling) and unplanned operations (incidents, outages, security events). They need different protocols.",
            "Every operational change needs a rollback plan stated before execution. If you cannot describe how to undo it, do not do it.",
            "Prefer small reversible changes over large irreversible ones. Batch changes create batch failures.",
            "Document the blast radius: if this operation fails, what breaks and how far does the impact spread?",
        ],
        "quality_bar_extra": [
            "A new team member could execute the plan from the document alone.",
            "Rollback steps are explicit and tested, not theoretical.",
            "Blast radius is named for every change.",
            "Communication plan covers who to notify, when, and what to say.",
        ],
    },
    "core": {
        "operating_rules_extra": [
            "Before planning, audit the current state. Plans built on stale assumptions are worse than no plan.",
            "Prefer the smallest sufficient action. Overplanning is procrastination with a Gantt chart.",
            "Name the decision, the decider, and the deadline. Decisions without owners and deadlines are wishes.",
            "Every plan must state what would cause it to change. Rigid plans break; plans with exit criteria adapt.",
            "Distinguish between reversible and irreversible decisions. Spend 10x more time on irreversible ones and 10x less on reversible ones.",
        ],
        "quality_bar_extra": [
            "The next action is specific enough to start immediately without further clarification.",
            "Assumptions are explicitly named, not hidden in the plan.",
            "The plan states what would trigger a re-evaluation.",
            "Someone else could execute the plan from the document alone.",
        ],
    },
    "eng": {
        "operating_rules_extra": [
            "Read the code and the error before proposing a fix. Diagnose first, treat second.",
            "Prefer the minimal change that solves the problem. Every line added is a line that can break.",
            "Test the fix, test the surrounding area, test the edge cases. A fix that works for the happy path only is not a fix.",
            "Document why, not just what. Future engineers need to understand the reasoning, not just see the change.",
            "If the fix takes longer than 30 minutes, stop and reconsider the approach. Complex fixes usually indicate the wrong diagnosis.",
        ],
        "quality_bar_extra": [
            "The fix is the smallest change that resolves the issue without introducing new problems.",
            "Root cause is identified and documented, not just the symptom.",
            "Tests cover the fix, the regression, and at least one edge case.",
            "The change is reviewable in under 10 minutes.",
        ],
    },
    "prod": {
        "operating_rules_extra": [
            "Start from user problems, not feature ideas. A feature without a user problem is a solution looking for a problem.",
            "Quantify the impact before prioritizing. How many users does this affect? How severely? How often?",
            "Distinguish between must-have, nice-to-have, and distraction. Ship must-haves, queue nice-to-haves, kill distractions.",
            "Every product decision should be falsifiable. State what evidence would prove the decision wrong.",
            "Prototype before building. A prototype that takes 2 hours saves 2 weeks of building the wrong thing.",
        ],
        "quality_bar_extra": [
            "Every feature traces back to a specific user problem with evidence.",
            "Priority is based on user impact x effort, not internal politics or founder preference.",
            "The scope is small enough to ship and learn from within one cycle.",
            "Success metrics are defined before building begins.",
        ],
    },
    "qa": {
        "operating_rules_extra": [
            "Test the risk, not the coverage. 80% of bugs come from 20% of the code. Focus testing where failures hurt most.",
            "Distinguish between testing that the feature works and testing that nothing else broke. Both matter.",
            "Every test case should have an explicit pass/fail criterion. Vague assertions produce vague confidence.",
            "Automate regression tests. Manual regression testing is slow, error-prone, and demoralizing.",
            "Test the edges and error paths, not just the happy path. Users will find the error paths even if testers do not.",
        ],
        "quality_bar_extra": [
            "Test cases cover the highest-risk areas first, not just the easiest to test.",
            "Pass/fail criteria are explicit and unambiguous.",
            "Regression tests are automated.",
            "Edge cases and error paths have explicit test coverage.",
        ],
    },
    "sales": {
        "operating_rules_extra": [
            "Discovery before pitch. Understand the prospect's actual problem before presenting your solution. Pitching without discovery is guessing.",
            "Lead with the problem you solve, not the features you have. Buyers buy outcomes, not capabilities.",
            "Handle objections with proof, not pressure. A prospect who feels pressured will agree and then ghost.",
            "Track conversion at each stage of the funnel. A leak at any stage kills the pipeline regardless of top-of-funnel volume.",
            "Follow-up is where deals are won or lost. 80% of sales require 5+ touches but most sellers stop after 2.",
        ],
        "quality_bar_extra": [
            "Every outreach starts with the prospect's context, not your product pitch.",
            "Objection handling uses proof and reframing, not pressure.",
            "The funnel has measurable conversion rates at each stage.",
            "Follow-up cadence is defined and adhered to.",
        ],
    },
    "data": {
        "operating_rules_extra": [
            "Check data quality before analyzing. Dirty data produces dirty insights. Null counts, outlier ranges, and schema drift are the first things to verify.",
            "Distinguish between correlation and causation in every finding. A spike that coincides with a launch is not caused by the launch without a controlled comparison.",
            "Present confidence intervals, not just point estimates. An average without variance is a single number pretending to be information.",
            "Every metric needs a clear definition, a data source, and a known limitation. Undefined metrics produce untrustworthy decisions.",
            "Prefer simple analyses that answer the question over complex analyses that impress but confuse.",
        ],
        "quality_bar_extra": [
            "Data quality checks are run before any analysis is presented.",
            "Findings distinguish correlation from causation.",
            "Confidence intervals or variance measures accompany all point estimates.",
            "Every metric has a definition, source, and known limitation documented.",
        ],
    },
    "pm": {
        "operating_rules_extra": [
            "Scope is defined by what is excluded, not just what is included. A project that includes everything includes nothing on time.",
            "Dependencies are risks until they are resolved. Track them actively, not just list them.",
            "Stakeholder communication is a deliverable, not an afterthought. A project that succeeds technically but fails politically has failed.",
            "Milestones need objective completion criteria. A milestone that requires a meeting to confirm it is done is not a milestone.",
            "Risk management is ongoing, not a one-time exercise. Review the risk register weekly, not just at kickoff.",
        ],
        "quality_bar_extra": [
            "Scope explicitly names what is out of scope, not just what is included.",
            "Every dependency has an owner and a resolution date.",
            "Stakeholder communication plan exists and is being followed.",
            "Milestones have objective, verifiable completion criteria.",
        ],
    },
    "res": {
        "operating_rules_extra": [
            "Source quality matters more than source quantity. One verified primary source beats ten secondary blog posts.",
            "Separate findings from interpretations. Data first, conclusions second. Mixing them undermines credibility.",
            "Triangulate important claims across at least two independent sources. Single-source claims are hypotheses.",
            "Rate confidence on every finding: high (verified, replicable), medium (directionally sound, limited data), low (anecdotal, unverified).",
            "Name what you do not know. Unresearched questions are more valuable than poorly researched answers.",
        ],
        "quality_bar_extra": [
            "Every finding has a source citation and a confidence rating.",
            "Important claims are triangulated across independent sources.",
            "Findings and interpretations are clearly separated.",
            "Unanswered questions are explicitly named.",
        ],
    },
    "safe": {
        "operating_rules_extra": [
            "Safety reviews are about what could go wrong, not confirming that things went right. Actively seek failure modes.",
            "Distinguish between known risks (document and mitigate), unknown risks (create detection mechanisms), and unknowable risks (set resilience buffers).",
            "The blast radius of any change must be named before the change is made. If you cannot describe the worst case, you are not ready to proceed.",
            "Automated safeguards beat manual ones. A checklist that requires human memory is a checklist that will be skipped under pressure.",
            "When in doubt, do not proceed. Safety gates exist to stop things, not to rubber-stamp them.",
        ],
        "quality_bar_extra": [
            "Every identified risk has a mitigation, an owner, or an explicit acceptance with rationale.",
            "The blast radius of the proposed change is documented.",
            "Automated safeguards exist for the highest-consequence risks.",
            "The review actively sought failure modes, not just confirmed existing controls.",
        ],
    },
    "doc": {
        "operating_rules_extra": [
            "Write for the reader who is frustrated and in a hurry, not the reader who has time and patience. Docs are searched, not read cover-to-cover.",
            "Every doc needs a clear purpose statement: who is this for, what will they learn, what will they do after reading?",
            "Code examples should be copy-pasteable and runnable. Broken code examples destroy trust in the entire document.",
            "Structure for scanning: headers, bullets, short paragraphs. Wall-of-text documentation is unread documentation.",
            "Docs need maintenance like code needs maintenance. Stale docs are worse than no docs because they actively mislead.",
        ],
        "quality_bar_extra": [
            "A frustrated user can find the answer they need within 60 seconds.",
            "Every code example is copy-pasteable and tested.",
            "The document states its audience, purpose, and prerequisites upfront.",
            "Content is structured for scanning, not sequential reading.",
        ],
    },
    "des": {
        "operating_rules_extra": [
            "Design for the most common path first, then handle edge cases. Optimizing for edge cases creates mediocre mainstream experiences.",
            "Every design decision should be traceable to a user need or a brand principle. Decorative decisions without rationale accumulate as design debt.",
            "Consistency reduces cognitive load. A consistent mediocre pattern beats an inconsistent brilliant one.",
            "Accessibility is not optional. If a design excludes users with disabilities, it fails regardless of its aesthetic quality.",
            "Test with real users, not stakeholders. Stakeholder preferences are not user needs.",
        ],
        "quality_bar_extra": [
            "Every design decision traces to a user need or brand principle.",
            "The most common user path is optimized first.",
            "Accessibility requirements are met (WCAG 2.1 AA minimum).",
            "The design has been tested or is ready to test with real users.",
        ],
    },
    "data": {
        "operating_rules_extra": [
            "Check data quality before analyzing. Dirty data produces dirty insights. Verify null counts, outlier ranges, and schema drift first.",
            "Distinguish between correlation and causation in every finding. A spike that coincides with a launch is not caused by the launch without a controlled comparison.",
            "Present confidence intervals, not just point estimates. An average without variance is a single number pretending to be information.",
            "Every metric needs a clear definition, a data source, and a known limitation.",
            "Prefer simple analyses that answer the question over complex analyses that impress but confuse.",
        ],
        "quality_bar_extra": [
            "Data quality checks are run before any analysis is presented.",
            "Findings distinguish correlation from causation.",
            "Confidence intervals or variance measures accompany all point estimates.",
            "Every metric has a definition, source, and known limitation.",
        ],
    },
}

def expand_section(content, section_header, extra_lines, after_existing=True):
    """Add extra lines to a section. If after_existing=True, add after existing content.
    If the section doesn't exist, create it."""
    
    pattern = rf'(## {re.escape(section_header)}\s*\n(?:[^\n].*\n)*)'
    match = re.search(pattern, content)
    
    if not match:
        return content
    
    section = match.group(1)
    
    # Build the extra content
    extra = "\n".join(f"- {line.lstrip('- ')}" for line in extra_lines)
    
    if after_existing:
        # Find the last bullet point in the section before the next header
        section_end = match.end()
        # Find next ## header
        next_header = re.search(r'\n## ', content[section_end:])
        if next_header:
            insert_pos = section_end + next_header.start()
            # Insert before the next header
            content = content[:insert_pos] + "\n" + extra + "\n" + content[insert_pos:]
        else:
            content += "\n" + extra + "\n"
    
    return content


expanded = 0
skipped = 0

for skill_dir in sorted(os.listdir(SKILLS_DIR)):
    skill_path = os.path.join(SKILLS_DIR, skill_dir, "SKILL.md")
    if not os.path.exists(skill_path):
        continue
    
    with open(skill_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    word_count = len(content.split())
    if word_count >= 800:
        skipped += 1
        continue
    
    # Extract skill name and category
    name_match = re.search(r'^name:\s*(\S+)', content, re.MULTILINE)
    skill_name = name_match.group(1) if name_match else skill_dir
    category = skill_name.split("_")[0] if "_" in skill_name else "other"
    
    if category not in CATEGORY_DEPTH:
        continue
    
    depth = CATEGORY_DEPTH[category]
    
    # Expand operating rules
    op_rules = depth.get("operating_rules_extra", [])
    if op_rules:
        # Find the Operating rules section and add content after existing bullets
        # We need to insert before the next ## header after "## Operating rules"
        pattern = r'(## Operating rules\s*\n(?:- .*\n)+)'
        match = re.search(pattern, content)
        if match:
            extra = "\n".join(f"- {line.lstrip('- ')}" for line in op_rules)
            insert_point = match.end()
            # Find next ## header
            next_header = re.search(r'\n## ', content[insert_point:])
            if next_header:
                pos = insert_point + next_header.start()
                content = content[:pos] + "\n" + extra + content[pos:]
            else:
                content += "\n" + extra
    
    # Expand quality bar
    qbar = depth.get("quality_bar_extra", [])
    if qbar:
        pattern = r'(## Quality bar\s*\n(?:- .*\n)*)'
        match = re.search(pattern, content)
        if match:
            extra = "\n".join(f"- {line.lstrip('- ')}" for line in qbar)
            insert_point = match.end()
            next_header = re.search(r'\n## ', content[insert_point:])
            if next_header:
                pos = insert_point + next_header.start()
                content = content[:pos] + extra + content[pos:]
            else:
                content += extra
    
    with open(skill_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    expanded += 1

print(f"Deep expansion: {expanded} skills expanded, {skipped} skipped (already 800+ words)")
