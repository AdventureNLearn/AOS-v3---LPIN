# AOS v3.0 Sovereign Edition — Skill Inventory

**Last Updated:** 2026-07-10  
**Source of Truth:** `skills/` folder in this repository

This document provides a quick-reference inventory of available skills for developers who want to pull, swap, or customize their own AOS v3.0 installations.

---

## Recently Expanded Skills (Full AOS v3.0 Format)

These 9 specialized operators were expanded with rich documentation in July 2026:

| Skill | Category | Purpose | File Path |
|-------|----------|---------|-----------|
| `recon-operator` | specialized | Initial reconnaissance & attack surface mapping | `skills/specialized/recon-operator/SKILL.md` |
| `scanning-operator` | specialized | Active scanning & vulnerability identification | `skills/specialized/scanning-operator/SKILL.md` |
| `exploit-operator` | specialized | Weaponizing vulnerabilities for initial access | `skills/specialized/exploit-operator/SKILL.md` |
| `post-ex-operator` | specialized | Post-exploitation, enumeration & preparation | `skills/specialized/post-ex-operator/SKILL.md` |
| `privesc-operator` | specialized | Privilege escalation | `skills/specialized/privesc-operator/SKILL.md` |
| `lateral-operator` | specialized | Lateral movement using credentials & trust | `skills/specialized/lateral-operator/SKILL.md` |
| `persistence-operator` | specialized | Establishing long-term access | `skills/specialized/persistence-operator/SKILL.md` |
| `exfil-operator` | specialized | Controlled data exfiltration | `skills/specialized/exfil-operator/SKILL.md` |
| `report-operator` | specialized | Final evidence-based reporting | `skills/specialized/report-operator/SKILL.md` |

---

## Core Governance & Layer-0 Skills

| Skill | Key Role |
|-------|----------|
| `4-agent-orchestration` | Multi-agent coordination & working document management |
| `sovereign-lens` | Module 0 router + 8-gate validation + Narrative Integrity Layer |
| `evidence-gate` | Tri-state claim labeling (+1 Evidence / 0 Inference / -1 Assumption) |
| `shatter-protocol` | 7-gate truth-shatter pre-filter (🐸) |
| `mission-spine-guard` | Real-time enforcement of Christ Is King | America First | Truth-Seeking |
| `working-doc-manager` | Durable working document persistence across sessions |
| `values-alignment-check` | Final governance & fairness alignment check |
| `paste-bridge-validator` | Enforces real paste-bridge delivery (anti self-report) |

---

## Civic Intelligence Skills

| Skill | Key Role |
|-------|----------|
| `permit-coordinator` | Regulatory pathway engine (Industry × Jurisdiction) |
| `jurisdiction-ops` | Jurisdiction intelligence & knowledge graphs |
| `civic-intelligence-coordinator` | Central orchestrator for civic/permit/oversight work |
| `public-records-forensics` | Deep forensic analysis of permits, contracts, minutes |
| `oversight-kit-builder` | Packages evidence bundles & audit kits for accountability |
| `influence-mapping-analyst` | Organizational & influence network mapping |
| `regulatory-routing-engine` | Thin routing layer for regulatory intelligence |
| `construction-oversight` | Construction code compliance & site-level regulatory reasoning |

---

## How to Swap Skills

1. Clone or download the desired skill folder from `skills/`
2. Place it in your local `skills/` directory
3. Reference it by its `id` or activation triggers
4. All skills follow the same `SKILL.md` format for consistency

**Example:**
```bash
git clone https://github.com/AdventureNLearn/AOS-v3---LPIN.git
cp -r AOS-v3---LPIN/skills/specialized/recon-operator ./my-aos/skills/specialized/
```

---

## Researcher Workbench

A self-contained HTML Researcher Workbench is available at:

`researcher/AOS_Researcher_Workbench_v3.0.html`

Use it to:
- Browse the full skill inventory
- Map your work to AOS skills
- Customize categorizations
- Export structured outputs for your working documents

---

*This inventory reflects the current state of the LPIN repository. Skills continue to be refined and expanded.*