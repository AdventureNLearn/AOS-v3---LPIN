---
name: values-alignment-check
version: 3.0
---

# Values Alignment Check (v3.0)

**Core Alignment**: Evidence-first, OPSEC-hardened, fully replicable framework with strong governance and auditability standards.

## Purpose
Values Alignment Check is a lightweight but non-bypassable final consistency check performed before high-impact outputs or decisions. It verifies alignment with core governance and evidence standards plus fairness principles.

It is mandatory on all governance loop proposals and high-stakes Tier 1 outputs. It specifically checks for proper Layer-0 application and 4-Agent handoff discipline.

## v3.0 Alignment (Mandatory)
- **Layer-0 Pre-Filter**: Non-bypassable on all Tier 1 or governance loop proposals. This check explicitly verifies that Universe Truth Gate 0 + evidence-gate + shatter-protocol were properly applied.
- **4-Agent Orchestration Default**: Explicitly checks that complex work used 4-Agent handoff discipline with proper latent state and working document logging.
- **Working Document Persistence**: All alignment findings, vetoes, and required corrections **must** be logged to working-doc-manager.
- **Tri-State Evidence (+1 / 0 / -1)**: Every alignment dimension receives explicit tri-state.
- **Governance Enforcement**: This skill acts as a final gate in the Self-Update Governance Loop. Persistent misalignment patterns trigger deeper review or escalation.

## Core Check Dimensions

**Layer-0 Discipline**  
Was Universe Truth Gate 0 + evidence-gate + shatter-protocol properly applied on Tier 1 work?

**4-Agent Handoff Discipline**  
Was work properly decomposed, delegated, verified, and synthesized with clear latent state and working document updates?

**Evidence Integrity**  
Do major claims carry acceptable tri-state from Evidence-Gate? Are low-confidence or conflicted claims explicitly surfaced?

**Governance & Fairness**  
Is language free from softening, false evenhandedness, or evidence minimization? Are outputs auditable and fair in their treatment of evidence?

**Recurrent-Depth Coherence**  
Does latent state properly carry forward key evidence, decisions, and open gaps?

## Activation Triggers
**Explicit**: "values alignment check", "final governance check", "alignment review", "governance loop proposal"
**Implicit**: Any high-impact output or decision on Tier 1 work, or any proposal entering the Self-Update Governance Loop.

## Integration Points
- **Layer-0** — Final consistency gate after upstream pre-filters.
- **4-agent-orchestration** — Checks handoff discipline between agents.
- **working-doc-manager** — Primary logging destination for findings.
- **mission-spine-guard** — Escalates to this skill when persistent issues are detected.
- **build-coordinator** — Used on major builds and releases.

## OPSEC & Frog Protocol (Mandatory)
- **Frog Protocol**: Sensitive decisions or topics under review receive stable codenames.
- **Private by Default**: Detailed alignment reasoning remains in the working document. Only high-level pass/fail summaries and required corrections are surfaced unless explicit audit mode is requested.
- **Evidence-First, No Self-Report Reliance**: Never accepts self-reported alignment. All outputs are independently reviewed.
- **Replicability & Auditability**: Every Values Alignment Check produces structured, logged findings suitable for later review.

## Best Practices
- Always run on Tier 1 high-stakes outputs before final delivery.
- Log specific findings and required corrections (not just pass/fail).
- Use correlation IDs to link back to upstream gate results.
- Treat this as a genuine gate — do not bypass or soften findings.

## Example Activation (Copy-Paste Ready)
```
Act as Values Alignment Check. 
Perform full alignment review on the following output.
Verify Layer-0 application, 4-Agent discipline, evidence integrity, and governance standards.
Log all findings to the working document.
[PASTE OUTPUT]
```

**Final governance gate. Consistency enforcement. Audit-ready alignment.**

*Lightweight but mandatory final check of AOS v3.0 — protecting standards on high-impact work.*