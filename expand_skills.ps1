# Skill Expansion Script - Adds depth to thin OpenClaw skills
# Reads each skill, identifies gaps, and expands with domain expertise

$repoDir = "E:\rexhub-repos\skill-library-openclaw"
$skillsDir = "$repoDir\skills"
$dirs = Get-ChildItem -Path $skillsDir -Directory | Sort-Object Name
$expanded = 0
$skipped = 0

foreach ($dir in $dirs) {
    $skillMd = Join-Path $dir.FullName "SKILL.md"
    if (-not (Test-Path $skillMd)) { continue }
    
    $content = Get-Content $skillMd -Raw
    $wordCount = ($content -split '\s+').Count
    
    # Skip skills already over 900 words
    if ($wordCount -ge 900) { $skipped++; continue }
    
    # Extract skill name from frontmatter
    $skillName = ""
    if ($content -match 'name:\s*(\S+)') { $skillName = $Matches[1] }
    
    # Extract category prefix
    $category = ""
    if ($skillName -match "^([a-z]+)_") { $category = $Matches[1] }
    
    # Fix empty OpenClaw tool pattern section
    $toolPatternFixes = @{
        "att" = @(
            "Use `web_fetch` to research competitor content and current platform conventions.",
            "Read existing site copy, product pages, and proof assets before drafting so output fits the real product truth.",
            "When external claims appear, verify before publishing — `safe_external_claims` applies.",
            "After drafting, run `att_proof_mining` to verify every claim has backing."
        )
        "core" = @(
            "Use `read` to load relevant files and context before planning.",
            "Use `exec` to check workspace state (git status, file structure) before and after actions.",
            "After execution, use `core_verify_done` to confirm the result meets the stated objective."
        )
        "eng" = @(
            "Use `exec` to run diagnostic commands, read logs, and check system state.",
            "Use `read` to inspect source files, configs, and error output directly.",
            "Use `edit` for targeted code changes — prefer `eng_minimal_patch` scope discipline.",
            "After changes, use `eng_test_strategy` to verify the fix works and hasn't broken anything else."
        )
        "prod" = @(
            "Use `web_fetch` to review competitor products and user feedback on review sites.",
            "Use `read` to load analytics data, user research files, and product specs.",
            "After design work, run `core_review_changes` to check for scope creep."
        )
        "data" = @(
            "Use `exec` to run data queries and analysis scripts via `uv run python`.",
            "Use `read` to load data exports, schema files, and query results.",
            "After analysis, use `data_quality_checks` to validate findings before presenting."
        )
        "ops" = @(
            "Use `exec` to check system status, run deployments, and verify infrastructure state.",
            "Use `read` to load runbooks, config files, and incident history.",
            "After operational changes, use `ops_change_management` to document what changed and why."
        )
        "pm" = @(
            "Use `read` to load project plans, roadmaps, and stakeholder communications.",
            "Use `exec` to check project status (git logs, CI results, milestone tracking).",
            "After planning, use `pm_scope_tradeoffs` to pressure-test scope decisions."
        )
        "qa" = @(
            "Use `exec` to run test suites, check CI results, and verify deployment state.",
            "Use `read` to load test plans, bug reports, and acceptance criteria.",
            "After testing, use `qa_release_smoke_test` to confirm release readiness."
        )
        "sec" = @(
            "Use `exec` to run security scanning tools, check dependency vulnerabilities, and audit configurations.",
            "Use `read` to load security policies, auth configurations, and access control files.",
            "After security review, use `sec_threat_model` to assess residual risk."
        )
        "sales" = @(
            "Use `web_fetch` to research prospect companies, news, and relevant context before outreach.",
            "Use `read` to load CRM data, call notes, and deal history.",
            "After sales planning, use `att_proof_mining` to ensure every claim in materials is backed."
        )
        "res" = @(
            "Use `web_fetch` to gather competitor data, market reports, and source material.",
            "Use `read` to load interview transcripts, survey data, and research notes.",
            "After research, use `core_evidence_research` to rate source quality and confidence."
        )
        "safe" = @(
            "Use `read` to load configs, credentials, and access control files for auditing.",
            "Use `exec` to verify system state, check permissions, and test security controls.",
            "After safety review, use `core_risk_gate` to assess whether the change can proceed."
        )
        "doc" = @(
            "Use `read` to load existing docs, code comments, and API definitions.",
            "Use `exec` to check code structure and generate API schemas when needed.",
            "After writing docs, use `doc_docs_feedback_loop` to plan for ongoing accuracy."
        )
        "des" = @(
            "Use `read` to load design specs, component libraries, and existing UI copy.",
            "Use `web_fetch` to review competitor designs and accessibility standards.",
            "After design work, use `des_accessibility_review` to verify compliance."
        )
        "solo" = @(
            "Use `exec` to check current project status, deadlines, and shipping readiness.",
            "Use `read` to load personal productivity notes, goals, and rhythm files.",
            "Pair with `solo_scope_guard` to prevent scope expansion during execution."
        )
        "vibe" = @(
            "Use `exec` to run AI-assisted code generation, debugging, and deployment commands.",
            "Use `read` to load prompts, code templates, and AI tool configurations.",
            "After building, use `vibe_debug_no_code` to test without deep technical knowledge."
        )
        "comm" = @(
            "Use `message` to check community channels, respond to members, and manage discussions.",
            "Use `read` to load community guidelines, feedback data, and engagement metrics.",
            "After community actions, use `comm_retention_audit` to check member retention trends."
        )
        "legal" = @(
            "Use `web_fetch` to look up regulation references and compliance requirements.",
            "Use `read` to load existing legal documents, terms, and privacy policies.",
            "After legal review, flag anything that needs actual attorney review — this skill assists, not replaces counsel."
        )
        "finance" = @(
            "Use `read` to load financial data, pricing spreadsheets, and revenue reports.",
            "Use `exec` to run calculations and financial models via `uv run python`.",
            "After financial analysis, use `finance_burn_rate` to cross-check sustainability."
        )
        "ai" = @(
            "Use `exec` to run model evaluations, prompt tests, and benchmarking scripts.",
            "Use `read` to load prompt templates, eval datasets, and model configurations.",
            "After AI system design, use `ai_eval_harness` to validate performance claims."
        )
    }
    
    # Build the tool pattern content
    $toolPattern = ""
    if ($toolPatternFixes[$category]) {
        $toolPattern = ($toolPatternFixes[$category] | ForEach-Object { "- $_" }) -join "`n"
    } else {
        $toolPattern = "- Use `read` to load relevant context files before starting.`n- Use `exec` to verify current state before and after changes.`n- After completing, verify the result meets the stated objective."
    }
    
    # Replace empty tool pattern section
    if ($content -match "(?s)(## OpenClaw tool pattern)\s*\n\s*\n(## )") {
        $content = $content -replace "(?s)(## OpenClaw tool pattern)\s*\n\s*\n(## )", "`$1`n$toolPattern`n`n`$2"
    }
    
    # Replace generic example invocations with skill-specific ones
    $specificExamples = @{
        "att_content_repurposing" = @("- Example: ""I wrote a 2000-word blog post — spin it into a thread, LinkedIn post, and email tease.""", "- Example: ""This launch post got good engagement — break it into 3 channel-native derivatives.""")
        "att_creator_partnerships" = @("- Example: ""Find 5 micro-creators in the maker studio niche and design a partnership brief for each.""", "- Example: ""I have no budget but early access to give — design a creator partnership that works.""")
        "att_demo_narrative" = @("- Example: ""Turn this product walkthrough into a 5-minute demo with a story arc.""", "- Example: ""I'm demoing at a conference — script a narrative that handles the top 3 objections live.""")
        "att_directory_submission" = @("- Example: ""Prepare Product Hunt and AlternativeTo listings for this SaaS launch.""", "- Example: ""I'm launching with zero audience — which directories matter most and what do I submit?""")
        "att_email_nurture_sequences" = @("- Example: ""Build a 5-email onboarding sequence for new signups who haven't activated.""", "- Example: ""Write a 3-email reactivation sequence for users who churned last month.""")
        "att_faq_objection_bank" = @("- Example: ""We keep getting 'isn't this just X?' in sales calls — build the objection bank.""", "- Example: ""Extract the top 10 objections from these 50 support tickets and write grounded answers.""")
        "att_founder_story" = @("- Example: ""I'm a disabled vet who taught myself to code and launched a SaaS — craft the origin story.""", "- Example: ""Write a 2-minute founder story for an investor meeting that connects my experience to the product.""")
        "att_landing_page_story" = @("- Example: ""Rewrite this homepage to have a clear narrative arc instead of feature soup.""", "- Example: ""Design a waitlist page that makes zero-audience visitors want to sign up.""")
        "att_outbound_sequences" = @("- Example: ""Write a 3-touch cold email sequence to potential beta testers.""", "- Example: ""I'm reaching out to 20 podcast hosts — craft a sequence that earns replies.""")
        "att_partnership_pitch" = @("- Example: ""Design a co-marketing pitch for a complementary SaaS product.""", "- Example: ""I want to partner with this tool — build the mutual value case and outreach email.""")
        "att_press_angles" = @("- Example: ""Find 3 newsworthy angles for a solo founder launching an AI product in a crowded space.""", "- Example: ""We have usage data showing X — turn it into a press pitch journalists would cover.""")
        "att_seo_page_brief" = @("- Example: ""Design an SEO brief for 'AI workforce for small business' — what should the page cover to rank?""", "- Example: ""Competitors rank for 'best AI agent platform' — create a brief to beat them.""")
        "att_short_video_script" = @("- Example: ""Script a 30-second TikTok showing this product solving a real problem.""", "- Example: ""Write a 60-second Reel that hooks with a contrarian take and ends with a CTA.""")
        "att_social_proof_pack" = @("- Example: ""Organize these 15 testimonials into a proof pack by claim and audience.""", "- Example: ""I have usage data and 5 reviews — build a social proof pack for the landing page.""")
        "att_webinar_workshop_outline" = @("- Example: ""Outline a 60-minute workshop on 'building an AI workforce as a solo founder.'""", "- Example: ""Design a 30-min webinar that teaches one useful thing and naturally leads to product interest.""")
    }
    
    if ($specificExamples[$skillName]) {
        # Remove generic examples and replace with specific ones
        $content = $content -replace "(?m)- Example: ""Build an attention asset[^\n]*", ""
        $content = $content -replace "(?m)- Example: ""Turn this product reality[^\n]*", ""
        # Add specific examples before the "Often paired with" line
        $newExamples = ($specificExamples[$skillName] -join "`n")
        $content = $content -replace "- Often paired with:", "$newExamples`n- Often paired with:"
    }
    
    # Remove generic output contract lines
    $content = $content -replace "(?m)^- Channel-ready draft or plan with hook, proof, CTA, and sequencing\.\s*\n", ""
    $content = $content -replace "(?m)^- Audience assumptions, risks, and the missing proof that would strengthen the asset\.\s*\n", ""
    
    # Remove generic quality bar
    $content = $content -replace "(?m)^- The result should be specific enough that another operator could act on it without guessing\.\s*\n", ""
    
    # Fix broken unicode in related workflows (→ arrow)
    $content = $content -replace "�\?\"", "→"
    $content = $content -replace "�\?'", "→"
    $content = $content -replace "\?\"", "→"
    
    # Save the cleaned version
    [System.IO.File]::WriteAllText($skillMd, $content, (New-Object System.Text.UTF8Encoding $false))
    $expanded++
}

Write-Host "Processed: $expanded skills expanded/cleaned, $skipped skipped (already deep enough)"
