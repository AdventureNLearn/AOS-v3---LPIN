---
name: xai-reflection
version: 3.0
---

# xAI Reflection (v3.0)

**Core Alignment**: Evidence-first, OPSEC-hardened, fully replicable framework with strong governance and auditability standards.

## Purpose
xAI Reflection is a structured self-review pattern for improving coherence and catching drift before major outputs or decisions. It can be used as an optional but recommended step in complex workflows.

It is particularly useful after Layer-0 pre-filter application and before final governance loop decisions. It helps operators catch internal inconsistencies, unaddressed evidence gaps, or subtle drift in reasoning.

## v3.0 Alignment (Mandatory)
- **Layer-0 Pre-Filter**: Recommended after Layer-0 passage on high-stakes work. The reflection explicitly checks that evidence-gate and shatter-protocol findings were properly incorporated.
- **4-Agent Orchestration Default**: Useful for solo operators simulating Agent 3 (Verification) role or for Agent 1 to perform pre-governance self-review.
- **Working Document Persistence**: All reflection findings, identified drift, and corrective actions **must** be logged to working-doc-manager.
- **Tri-State Evidence (+1 / 0 / -1)**: Every reflection dimension receives explicit tri-state assessment.
- **Governance Enforcement**: Reflection findings feed into values-alignment-check and mission-spine-guard when used before governance gates.

## Core Reflection Dimensions

**Coherence**  
Does the output/decision maintain internal logical consistency across all sections? Are there contradictions or unexplained jumps in reasoning?

**Evidence Integration**  
Have all major claims been properly labeled and verified through Evidence-Gate? Are low-confidence or conflicted claims explicitly addressed?

**Illusion / Softening Detection**  
Has Shatter Protocol been applied? Are there remaining intact illusion layers or softening language that should be surfaced?

**Governance & Fairness**  
Does the output align with evidence standards? Is language free from false evenhandedness or evidence minimization of uncomfortable findings?

**Recurrent-Depth Readiness**  
Is latent state properly summarized with key evidence, locked decisions, and open gaps for future handoff?

## Activation Triggers
**Explicit**: "xai reflection", "self-review", "coherence check", "drift detection"
**Implicit**: Any complex output or decision where the operator wants an internal quality gate before final governance review.

## Integration Points
- **Layer-0** — Recommended after upstream pre-filters.
- **working-doc-manager** — Primary logging destination for findings.
- **values-alignment-check** — Feeds directly into this final gate when used on Tier 1 work.
- **4-agent-orchestration** — Useful for solo operators or Agent 1 self-review.
- **mission-spine-guard** — Escalates persistent issues detected during reflection.

## OPSEC & Frog Protocol (Mandatory)
- **Frog Protocol**: Sensitive topics or decisions under self-review receive stable codenames.
- **Private by Default**: Detailed reflection reasoning remains in the working document. Only high-level findings and corrective actions are surfaced unless explicit audit mode is requested.
- **Evidence-First, No Self-Report Reliance**: The reflection itself is a form of self-audit and should be logged transparently.
- **Replicability & Auditability**: Every xAI Reflection produces structured, logged findings suitable for later review.

## Best Practices
- Use after Layer-0 pre-filters but before final governance gates on complex work.
- Be honest and specific in identifying drift or weaknesses.
- Log corrective actions taken as a result of the reflection.
- Treat it as a genuine internal quality gate rather than a formality.

## Example Activation (Copy-Paste Ready)
```
Act as xAI Reflection. 
Perform structured self-review on the following output.
Check coherence, evidence integration, illusion detection, governance alignment, and recurrent-depth readiness.
Log all findings and recommended corrections to the working document.
[PASTE OUTPUT]
```

**Structured self-review. Drift detection. Coherence enforcement.**

*Recommended internal quality gate of AOS v3.0 — catching issues before they reach final governance.*