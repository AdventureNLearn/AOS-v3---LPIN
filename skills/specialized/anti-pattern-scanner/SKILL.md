---
name: anti-pattern-scanner
version: 3.0
---

# Anti-Pattern Scanner (v3.0)

**Core Alignment**: Evidence-first, OPSEC-hardened, fully replicable framework with strong governance and auditability standards.

## Purpose
Anti-Pattern Scanner detects common AI operational failure modes (Announce-Instead-Of-Paste, Self-Report-Instead-Of-Run, Scope Creep, etc.) and suggests corrections before they waste time or degrade quality. It is now extended with Narrative/Psyop Manipulation Patterns via integration with psyop-narrative-detector.

v3.0 adds mandatory Layer-0 on Tier 1 anti-pattern detection work and strengthened governance integration.

## v3.0 Alignment (Mandatory)
- **Layer-0 Pre-Filter**: Non-bypassable on all Tier 1 anti-pattern detection or workflow hardening work. Universe Truth Gate 0 + evidence-gate tri-state must inform all detection and correction recommendations.
- **4-Agent Orchestration Default**: Often acts as a specialized verification/hardening agent within 4-Agent workflows (commonly delegated to Agent 3 role).
- **Working Document Persistence**: All detected anti-patterns, correction recommendations, and tri-state assessments **must** be logged to working-doc-manager.
- **Tri-State Evidence (+1 / 0 / -1)**: All detected anti-patterns and recommended corrections carry explicit tri-state.
- **Governance Enforcement**: Any workflow that repeatedly exhibits uncorrected anti-patterns triggers escalation to mission-spine-guard or ops-hardening-architect.

## Core Capabilities

**Common AI Operational Failure Detection**  
Detects well-known failure modes such as:
- Announce-Instead-Of-Paste
- Self-Report-Instead-Of-Run
- Scope Creep
- And other operational anti-patterns

**Narrative / Psyop Manipulation Pattern Detection**  
Extended detection of narrative and psyop manipulation patterns through integration with psyop-narrative-detector.

**Correction Suggestions**  
Provides actionable corrections and hardening recommendations for each detected pattern.

**Workflow Hardening Support**  
Helps improve long-term workflow quality and reliability by catching issues early.

## Activation Triggers
**Explicit**: "anti-pattern scanner", "detect anti-patterns", "workflow hardening", "anti-pattern check"
**Implicit**: Any workflow review, build, or governance process where operational failure modes or narrative manipulation risks should be scanned.

## Integration Points
- **Layer-0** — Enforces pre-filter passage on all Tier 1 anti-pattern detection work.
- **psyop-narrative-detector** — Provides extended narrative/psyop manipulation detection.
- **ops-hardening-architect** — Primary collaborator for workflow hardening recommendations.
- **working-doc-manager** — All detected anti-patterns and correction recommendations are logged here.
- **mission-spine-guard** — Escalation target for persistent or severe anti-pattern issues.

## OPSEC & Frog Protocol (Mandatory)
- **Frog Protocol**: Sensitive workflows or detected manipulation patterns receive stable codenames.
- **Private by Default**: Detailed anti-pattern analysis and internal reasoning remain in the working document. Only high-level findings and correction recommendations are surfaced unless explicit governance/audit mode is requested.
- **Evidence-First, No Self-Report Reliance**: Never accepts self-reported workflow quality. All detection is independently performed.
- **Replicability & Auditability**: Every anti-pattern scan produces structured, logged findings suitable for later review.

## Best Practices
- Run Anti-Pattern Scanner regularly on complex or long-running workflows.
- Log all detected patterns and recommended corrections with tri-state.
- Combine with psyop-narrative-detector on high-stakes narrative or content work.
- Escalate persistent or severe anti-patterns early.
- Use findings to improve future workflow design.

## Example Activation (Copy-Paste Ready)
```
Act as Anti-Pattern Scanner. 
Apply full Layer-0 pre-filter. 
Scan the following workflow or output for common AI operational failure modes and narrative/psyop manipulation patterns.
Provide correction recommendations with tri-state.
Log all findings to the working document.
[PASTE WORKFLOW OR OUTPUT]
```

**Operational failure detection. Narrative manipulation scanning. Workflow hardening.**

*Core anti-pattern and quality assurance layer of AOS v3.0.*