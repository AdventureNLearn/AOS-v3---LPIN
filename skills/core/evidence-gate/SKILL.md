---
name: evidence-gate
version: 3.0
---

# Evidence-Gate (v3.0)

**Core Alignment**: Evidence-first, OPSEC-hardened, fully replicable framework with strong governance and auditability standards.

## Purpose
Evidence-Gate is a mandatory verification layer that forces explicit labeling of every major claim as **Evidence**, **Inference**, or **Assumption**. It requires multi-source verification, assigns confidence scores, applies tri-state activation (+1 / 0 / -1), and generates lightweight but durable audit trails.

This skill exists to reduce hallucination, prevent overclaiming, and maintain transparency — especially on Tier 1 work (civic intelligence, audits, regulatory analysis, high-stakes reasoning).

v3.0 strengthens integration with Layer-0 pre-filters, working document persistence, and governance enforcement.

## v3.0 Alignment (Mandatory)
- **Layer-0 Pre-Filter**: This is a core component of Layer-0. All high-stakes outputs should pass through Evidence-Gate (strict mode) before final delivery.
- **4-Agent Orchestration Default**: Typically invoked by Agent 3 (Verification). Results are carried in latent state and reviewed by Agent 1.
- **Working Document Persistence**: All strict mode runs and complex claim sets must be logged to working-doc-manager with scoring, sources, conflicts, and verification notes.
- **Tri-State Evidence (+1 / 0 / -1)**: Every claim receives explicit tri-state. Conflicting evidence or single-source dependency triggers 0 or -1 and potential escalation.
- **Governance Enforcement**: Attempts to soften language, hide low-confidence claims, or present inference as evidence trigger escalation.

## Core Protocol — Strict Mode (Recommended for Tier 1 Work)

For every major factual, contested, or high-impact claim:

1. **Label Explicitly** — State whether the claim is Evidence, Inference, or Assumption.
2. **Source Requirements** — Demand primary or high-quality secondary sources. Note source strength.
3. **Conflict Check** — Identify and surface any contradictory evidence.
4. **Confidence Scoring** — Assign a confidence level (High / Medium / Low) with justification.
5. **Tri-State Activation** — Apply +1 (supported), 0 (uncertain/mixed), or -1 (contradicted or unsupported).
6. **Audit Trail** — Log the claim, labeling, sources, scoring, and tri-state in the working document.

## Activation Triggers
**Explicit**: "evidence gate", "apply evidence-gate", "strict mode verification", "claim verification"
**Implicit**: Any high-stakes reasoning, analysis, or output where claims must be rigorously verified.

## Integration Points
- **Layer-0** — Core component of the mandatory pre-filter stack.
- **working-doc-manager** — Primary logging destination for verification results.
- **sovereign-lens** & **shatter-protocol** — Frequently used in combination.
- **4-agent-orchestration** — Invoked by Agent 3 during verification phases.
- **values-alignment-check** — Outputs that pass Evidence-Gate feed into governance review on Tier 1 work.

## OPSEC & Frog Protocol (Mandatory)
- **Frog Protocol**: Sensitive claims, sources, or investigations receive stable codenames in working documents.
- **Private by Default**: Detailed verification reasoning and source analysis remain in working documents. Only final tri-state results and high-level summaries are surfaced unless explicit audit mode is requested.
- **Evidence-First, No Self-Report Reliance**: Never accepts self-reported verification quality. All claims are independently evaluated.
- **Replicability & Auditability**: Every Evidence-Gate run produces structured, logged output suitable for later review.

## Best Practices
- Use **strict mode** on all Tier 1 and high-stakes work.
- Always log results to the working document.
- Surface low-confidence or conflicted claims explicitly rather than burying them.
- Combine with Shatter Protocol when narrative or framing risks are present.

## Example Activation (Copy-Paste Ready)
```
Act as Evidence-Gate. 
Apply strict mode. 
Process the following claims with full labeling, source requirements, confidence scoring, and tri-state activation.
Log all results to the working document.
[PASTE CLAIMS OR SECTION]
```

**Evidence-first. Governance-aligned. Built for auditability.**

*Core verification layer of AOS v3.0 — reducing hallucination and enforcing transparency.*