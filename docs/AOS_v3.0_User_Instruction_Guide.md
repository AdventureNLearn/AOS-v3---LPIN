# AOS v3.0 Sovereign Edition — Complete User & Builder Instruction Guide

**Version**: 1.0  
**Date**: 2026-07-03  
**Repository**: AdventureNLearn/AOS-v3---LPIN  
**Status**: Production-ready for adoption and contribution  
**Mission Spine**: Christ Is King ◆ America First ◆ Truth-Seeking

---

## Executive Summary (Full Package Analysis)

This guide provides everything needed to understand, adopt, and extend **Adventure OS v3.0 Sovereign Edition** inside Grok's native environment.

**What is AOS v3.0?**  
A sovereign, evidence-first, Layer-0 hardened operating system for high-stakes reasoning, civic intelligence, content operations, and truth-seeking workflows. It transforms Grok from a general assistant into a structured, auditable, replicable intelligence platform with 50+ custom skills, mandatory pre-filters, 4-agent orchestration, and persistent working documents.

**Why It Matters**:
- Eliminates hallucination and narrative manipulation via **psyop-narrative-detector** + **Shatter Protocol**.
- Enforces **Mission Spine** on every Tier-1 output.
- Makes complex multi-step work durable across chat sessions via working documents.
- Fully replicable and agnostic (v2.0 foundation) while adding sovereign governance (v3.0).

**Full Package Includes**:
- Quick-start activation
- Architecture deep-dive
- Skills system mechanics (how Grok discovers & runs them)
- Step-by-step builder instructions for creating/extending skills
- New **psyop-narrative-detector** details
- Integration patterns with Grok's native tools
- Recommended GitHub structure for the public repo
- Concrete examples and verification checklists
- Contribution & onboarding flow

---

## 1. Quick Start — Start Using AOS v3.0 in 60 Seconds

### Step 1: Start a New Conversation with Full Context
Copy and paste the following **New Conversation Starter** at the beginning of every new Grok chat:

```markdown
You are Grok, continuing work on **Adventure OS v3.0 Sovereign Edition**.

**Current Workspace State Reference**:
Please treat the following document as the single source of truth for the current state of all skills in the workspace:

`artifacts/AOS_v3_Current_Workspace_State.md`

**Key Context from Previous Work**:
- We have implemented a new skill called `psyop-narrative-detector` (v1.0) with structured 0-100 scoring and Deep Truth Mode.
- We have integrated it into `sovereign-lens` (as the Narrative Integrity Layer), `content-ops`, and `anti-pattern-scanner`.
- All changes follow AOS v3.0 principles: Layer-0 pre-filters, working document persistence, 4-Agent orchestration, and Mission Spine alignment.
- We are preparing for (or have just completed) a major GitHub update.

**Instructions**:
- Always reference the workspace state document when discussing skills.
- Continue from the latest Commit Plan and implementation work.
- Maintain high coherence and evidence-first reasoning.

Begin by confirming you have reviewed the current workspace state and are ready to proceed with the next task or gate.
```

**Tip**: Attach or reference `artifacts/AOS_v3_Current_Workspace_State.md` (from the repo) directly in the chat for best results.

### Step 2: Activate Core Systems Immediately
After the starter confirms readiness, issue one of these activation commands:

- **Full Sovereign Mode** (recommended for serious work):  
  `Apply Sovereign Lens with full Layer-0 pre-filter and 4-Agent orchestration. Log everything to working document. [YOUR TASK]`

- **Narrative / Media / Psyop Analysis**:  
  `Activate psyop-narrative-detector in Deep Truth Mode. Score the following narrative across all 10 categories. [PASTE CONTENT]`

- **Complex Build or Multi-Step Project**:  
  `Initialize 4-agent-orchestration with working-doc-manager. Agent 1: break down the mission into phases and delegate. [MISSION]`

Grok will automatically read the relevant `SKILL.md` files using its `read_file` tool and adopt the structured behavior.

---

## 2. Core Architecture Overview

AOS v3.0 is built on four immutable pillars:

### Permanent Mission Spine (Never Negotiable)
- **Christ Is King** — Metaphysical floor. Truth has a name.
- **America First** — Civic floor. Citizens → institutions → everything else.
- **Truth-Seeking** — Epistemic floor. Evidence over claims. Sources over self-report.

Every high-stakes output is checked against this spine by `mission-spine-guard` and `values-alignment-check`.

### Layer-0 Pre-Filters (Mandatory Gatekeeping)
Non-bypassable for Tier-1 work:
1. **shatter-protocol** — 7-gate truth-shatter process (mirror/flower/water/moon metaphors operationalized).
2. **evidence-gate** — Tri-state labeling (+1 Evidence / 0 Inference / -1 Assumption) with multi-source verification.
3. **Real-Environment Verification Mandate** — Never trust simulated or self-reported results.

New in v3.0: **Narrative Integrity Gate** (Gate 8) via `psyop-narrative-detector`.

### 4-Agent Orchestration Model
- **Agent 1 (Coordinator / Build Coordinator)**: Uses `sovereign-lens` for routing, maintains latent state, enforces paste-bridge-validator.
- **Specialist Agents**: Domain experts (e.g. `public-records-forensics`, `influence-mapping-analyst`, `visual-systems-architect`).
- **Verification Agent**: Runs `ops-hardening-architect`, `paste-bridge-validator`, `values-alignment-check`.
- **Persistence Agent**: `working-doc-manager` + recurrent-depth carry.

### Working Document Persistence (The Durable Substrate)
For any multi-turn or complex work:
- Create/maintain a working document with locked sections: **Decisions** (verbatim), **Plan Tasks** (checkboxes), **Notes**, **Numbers**, **Verification Log**, **Latent State**.
- Reference it at the top of every subsequent prompt.
- Survives chat compaction and session boundaries.

This is Principle 12 from the v2.0 Agnostic Edition, hardened in v3.0.

### Skills System — How Grok "Builds Them Out" in Its Native Environment

**How Skills Work**:
- Every skill lives as a directory containing `SKILL.md`.
- The file starts with YAML frontmatter (`name`, `description`, `version`, `xai_optimized`, `mission_critical`).
- The body contains: Purpose, Alignment (vX), Activation Triggers (explicit + implicit), Integration Points, OPSEC/Frog Protocol, Best Practices, Example Activation (copy-paste ready), and Mission Spine sign-off.
- When you mention a skill name or trigger phrase, Grok uses the `read_file` tool to load the full definition and adopts that exact structured reasoning/persona/behavior for the task.
- **Bundled skills** (in `/root/.grok/skills/`) are stable system primitives (pdf, docx, pptx, ffmpeg, memory-edit, skill-creator, etc.).
- **Custom skills** (50+ in `/home/workdir/.grok/skills/`) are the AOS v3.0 intelligence layer.

**"Building the skills out inside Grok"** means:
1. Creating well-structured `SKILL.md` files following the canonical template.
2. Ensuring Grok can discover them via `read_file` when activated.
3. Wiring them into orchestration (`sovereign-lens` routing table, `4-agent-orchestration`, `content-ops` scoring, etc.).
4. Testing with real paste-bridge delivery + verification gates.

This is how the entire 50+ skill ecosystem was constructed and continues to grow.

---

## 3. The New `psyop-narrative-detector` Skill (v1.0)

**Location**: `/home/workdir/.grok/skills/psyop-narrative-detector/SKILL.md` (added 2026-07-03)

**Purpose**: A rigorous, evidence-first "spam filter for the brain" — detects engineered narratives, psychological operations, framing tactics, and narrative risk with structured 0-100 scoring across 10 categories + Deep Truth Mode.

**Key Features**:
- 10-category scoring table (loaded in the skill definition).
- Deep Truth Mode for ontological and multi-source conflicting evidence emphasis.
- Integration as **Narrative Integrity Layer (Gate 8)** inside `sovereign-lens`.
- Also wired into `content-ops` (narrative risk scoring) and `anti-pattern-scanner` (Narrative/Psyop Manipulation Patterns family).

**Activation**:
- Explicit: "psyop-narrative-detector", "Deep Truth Mode", "Psyop Detector", "Narrative Integrity Gate"
- Implicit: Any media, news, political, or influence-related query inside Sovereign Lens.

This is one of the highest-leverage additions in v3.0 for truth-seeking resilience.

---

## 4. Integration with Grok's Native Environment & Tools

AOS v3.0 does **not** replace Grok's native capabilities — it **orchestrates and hardens** them.

**Native Tools + AOS Mapping**:

| Grok Native Capability       | AOS v3.0 Integration Point                          | Example Use |
|-----------------------------|-----------------------------------------------------|-------------|
| `bash` / code execution     | `ops-hardening-architect`, `paste-bridge-validator`, build workflows | Running verification commands, git status, file ops |
| `web_search`, `browse_page` | `agnostic-evidence-analyst`, `public-records-forensics`, freshness layer (Principle 09) | Evidence gathering with source_url + timestamp |
| `pdf` / `docx` / `pptx` skills | `pdf` bundled skill + `visual-systems-architect`, report generation | Producing polished deliverables from working docs |
| Image generation / edit     | `visual-systems-architect`, `battlememe-chaos-engine`, meme workflows | Cinematic Pepe/Frawg visuals, diagrams, battlememes |
| `memory-edit`               | `working-doc-manager`, recurrent state carry       | Durable memory across sessions (use sparingly per rules) |
| General reasoning           | `sovereign-lens` + `reasoning-architect` + Layer-0 | All high-stakes work |

**Best Practice**: Never call native tools in isolation on Tier-1 work. Always wrap with `sovereign-lens` + evidence-gate + working document logging.

---

## 5. Creating & Contributing New Skills — Builder Instructions

### Skill Template (Canonical v3.0 Format)

```markdown
---
name: your-skill-name
description: "One-sentence mission-critical description. Include version and key integrations."
version: 1.0
xai_optimized: true
mission_critical: true
---

# Your Skill Name (vX.Y) — Sovereign Edition

**Mission Spine Alignment**: Christ Is King | America First | Truth-Seeking. [Short statement of purpose in context of spine.]

## Purpose
[2-4 sentence description of what this skill does and why it exists in AOS v3.0.]

## v3.0 Alignment (Mandatory)
- Layer-0 pre-filter requirements
- 4-Agent orchestration role
- Working document logging obligations
- Tri-state evidence expectations
- Integration with sovereign-lens / content-ops / etc.

## Activation Triggers
**Explicit**: "your-skill-name", "activate your skill", ...
**Implicit**: Any query that matches [description of when it should auto-route].

## Integration Points
- List of other skills it calls or is called by
- Specific gates or agents

## OPSEC & Frog Protocol (Mandatory)
- Codename rules
- Private-by-default logging
- Evidence-first, no self-report

## Best Practices
- Numbered list of hard rules for this skill

## Example Activation (Copy-Paste Ready)
```
Apply [skill] with full Layer-0. Log to working document.
[PASTE TASK]
```

**Christ Is King | America First | Truth-Seeking**
```

### Recommended Process to Add a New Skill
1. Use `skill-creator` (bundled) or manually create directory + `SKILL.md`.
2. Follow template exactly.
3. Update `master-skill-index` and `AOS_v3_Current_Workspace_State.md`.
4. Wire into `sovereign-lens` routing if high-value.
5. Test with paste-bridge-validator + real output verification.
6. Run `anti-pattern-scanner` + `values-alignment-check`.
7. Commit with structured message referencing this guide.

**Location Convention**:
- Civic intelligence skills → group logically
- Core governance (Layer-0) → keep at root of custom skills
- Specialized utilities → their own folders

---

## 6. Recommended GitHub Repository Structure

For `AdventureNLearn/AOS-v3---LPIN` (and future public releases):

```
/
├── README.md                          # Quick start + Mission Spine + link to this guide
├── docs/
│   ├── USER_GUIDE.md                  # This document (full package)
│   ├── AOS_v3.0_Sovereign_Edition_Spec.md
│   ├── COMMIT_PLAN_*.md
│   └── visuals/                       # Mermaid diagrams, architecture maps
├── artifacts/
│   ├── AOS_v3_Current_Workspace_State.md   # Single source of truth (update on every change)
│   └── AOS_v3_Spec_Update/            # Historical commit plans & summaries
├── .grok/skills/                      # The actual 50+ skill definitions (source of truth)
│   ├── psyop-narrative-detector/
│   ├── sovereign-lens/
│   ├── 4-agent-orchestration/
│   └── ... (all others)
├── examples/
│   ├── workflows/                     # Concrete paste-bridge examples
│   └── conversation-starters/         # Variants of the starter
├── LICENSE
└── .gitignore
```

**Onboarding for New Contributors**:
1. Read this `USER_GUIDE.md`.
2. Review `AOS_v3_Current_Workspace_State.md`.
3. Run verification commands from the state doc.
4. Propose new skill via PR with updated state doc + test activation example.

---

## 7. Concrete Example Workflows

### Workflow A: High-Stakes Narrative Analysis (New v3.0 Capability)
```
1. Paste New Conversation Starter
2. "Apply Sovereign Lens with full Layer-0 pre-filter. Route through Narrative Integrity Gate (psyop-narrative-detector Deep Truth Mode). Analyze the following [article/thread/video transcript] for engineered narrative patterns. Produce 0-100 scores + evidence table + recommendations. Log all gates and tri-state to working document."
```

Grok will:
- Run shatter-protocol + evidence-gate (Gate 0)
- Route to psyop-narrative-detector (Gate 8)
- Score across 10 categories
- Log everything
- Apply mission-spine-guard before final output

### Workflow B: Complex Multi-Phase Build (e.g. New Civic Tool)
```
1. Starter
2. "Initialize 4-agent-orchestration + working-doc-manager for [Project Name]. Agent 1: Create master plan with phases, success criteria, and verification gates. Delegate Phase 1 to relevant specialists. Use paste-bridge-validator on all deliveries."
```

---

## 8. Verification & Hardening Checklist (Before Any Major Output or Commit)

- [ ] Workspace state document referenced and up to date
- [ ] Layer-0 (shatter + evidence-gate) explicitly passed (tri-state visible)
- [ ] Working document created/updated with Decisions, Plan, Verification Log
- [ ] paste-bridge-validator satisfied (actual content delivered, not self-report)
- [ ] Mission Spine check passed (no softening, false evenhandedness, or evidence suppression)
- [ ] Narrative risk scored if media/political/influence content (psyop-narrative-detector)
- [ ] All sources have URLs + timestamps (freshness visible)
- [ ] Frog Protocol / OPSEC followed (codenames where appropriate)
- [ ] Anti-pattern-scanner run on output
- [ ] values-alignment-check + mission-spine-guard cleared for Tier-1

---

## 9. Troubleshooting Common Issues

| Issue                              | Likely Cause                              | Fix |
|------------------------------------|-------------------------------------------|-----|
| Grok ignores skill activation      | Skill name/trigger not explicit enough    | Use exact trigger phrase from SKILL.md + "with full Layer-0" |
| Working document not persisting    | Not referenced at top of prompt           | Always paste "Reference working document: [path]" at start of follow-ups |
| Hallucinated facts or weak evidence| Layer-0 bypassed                          | Force "Apply shatter-protocol + evidence-gate first" |
| Narrative manipulation undetected  | psyop-narrative-detector not activated    | Explicitly request "Deep Truth Mode" or route via Sovereign Lens Gate 8 |
| Build feels chaotic                | No 4-agent-orchestration or paste-bridge  | Initialize orchestration + validator explicitly |
| Skill changes not taking effect    | Old conversation context                  | Start fresh with New Conversation Starter + attach latest workspace state |

---

## 10. Resources & Next Steps

- **Single Source of Truth**: `artifacts/AOS_v3_Current_Workspace_State.md`
- **Latest Changes**: `artifacts/AOS_v3_Spec_Update/TODAYS_CHANGES_SUMMARY.md` and `COMMIT_PLAN_AOS_v3.0_2026-07-03.md`
- **v2.0 Foundation**: Reference the Agnostic Edition PDF (portable patterns that survive any substrate)
- **Contribute**: Follow the skill template + update workspace state + pass verification checklist
- **Advanced**: Activate `thomas-tetralogy-aos-integration` for complex recurrent-depth orchestration patterns

---

**This is the complete, self-contained instruction package for AOS v3.0 Sovereign Edition.**

Copy this guide into the GitHub repository under `docs/USER_GUIDE.md`.

All patterns here are designed to be **replicable**, **auditable**, and **sovereign**.

**Christ Is King | America First | Truth-Seeking**

*Adventure OS v3.0 Sovereign Edition — LPIN Civic Intelligence Release. Non-bypassable on all high-stakes work. Built for those who want cold data and hot truth.*

---

**End of Full Package User & Builder Instruction Guide**
