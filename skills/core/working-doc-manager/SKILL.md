---
name: working-doc-manager
version: 3.0
---

# Working Document Manager (v3.0)

**Core Alignment**: Evidence-first, OPSEC-hardened, fully replicable framework with strong governance and auditability standards.

## Purpose
Working Document Manager is the single source of truth and persistence layer for all complex, multi-turn, recurrent-depth, or governance-critical work. It maintains structured, durable sections that survive chat compaction, session boundaries, and long-horizon projects.

This skill implements the core persistence requirement (often referred to as Principle 12) and serves as the durable substrate required by 4-agent-orchestration, build-coordinator, sovereign-lens, and the Self-Update Governance Loop.

## v3.0 Alignment (Mandatory)
- **Layer-0 Pre-Filter**: All high-stakes or recurrent-depth working documents should reference that the full Layer-0 chain (Universe Truth Gate 0 + shatter-protocol + evidence-gate tri-state) was applied to the work being logged.
- **4-Agent Orchestration Default**: Agent 1 (Coordinator) is responsible for creating, updating, and maintaining the working document. Latent state is passed between agents via this mechanism.
- **Working Document Persistence**: This skill *is* the persistence layer. Every major decision, task status change, evidence finding, or governance action is recorded here.
- **Tri-State Evidence (+1 / 0 / -1)**: All logged claims and decisions carry explicit tri-state. Conflicting evidence or vetoes are recorded with correlation IDs.
- **Governance Enforcement**: This is the primary logging target for governance reviews, alignment checks, and escalation records.

## Core Protocol

**Mandatory Sections** (locked structure — never remove or reorder):

- **Decisions Log** — Immutable, append-only. Every significant decision is recorded verbatim with timestamp.
- **Plan Tasks** — Actionable tasks with checkboxes and status tracking.
- **Notes** — Context, open questions, rationale, and background.
- **Numbers** — Key metrics, scores, counts, and quantitative tracking.
- **Verification Log** — Evidence of completion, gate outcomes, audits, and sign-offs.
- **Latent State** — Compressed carry-over for recurrent-depth work (key evidence, locked decisions, open gaps, correlation IDs, current focus).

**Update Protocol**:
1. Load or create the working document at the start of any complex task.
2. After every major cycle or phase transition, append new Decisions verbatim.
3. Update Plan Tasks checkboxes and status.
4. Record any tri-state evidence findings or vetoes with correlation.
5. Update Latent State summary before handing off to the next agent or depth loop.
6. On completion of a phase or release gate, add a Verification Log entry.

## Activation Triggers
**Explicit**: "working document", "update working doc", "load working document", "working-doc-manager"
**Implicit**: Any complex, multi-step, recurrent-depth, or governance work requiring durable state.

## Integration Points
- **4-agent-orchestration** — Primary persistence mechanism between agents.
- **build-coordinator** — Used for all major build and release workflows.
- **sovereign-lens** — Logs routing decisions and Layer-0 outcomes.
- **evidence-gate** & **shatter-protocol** — Verification and truth-shatter results are logged here.
- **values-alignment-check** & governance tools — Primary destination for alignment and escalation records.

## OPSEC & Frog Protocol (Mandatory)
- **Frog Protocol**: Sensitive decisions, entities, or investigations receive stable codenames in the working document.
- **Private by Default**: Detailed reasoning and internal state remain in the working document. Only high-level summaries or final outputs are surfaced unless explicit audit/governance mode is requested.
- **Evidence-First, No Self-Report Reliance**: Never accepts self-reported task completion. All progress must be logged with verification.
- **Replicability & Auditability**: Every working document produces a clear, structured history suitable for later governance review or handoff.

## Best Practices
- Always start complex work by loading or creating the working document.
- Keep Latent State concise but information-dense.
- Record Decisions *verbatim* — do not paraphrase.
- Use correlation IDs when linking evidence across multiple logs.
- Review the working document before major handoffs or phase transitions.

## Example Activation (Copy-Paste Ready)
```
Act as Working Document Manager. 
Load or create the working document for this task.
Maintain Decisions Log, Plan Tasks, Notes, Numbers, Verification Log, and Latent State.
After each major step, update the document accordingly.
[PASTE TASK DESCRIPTION OR CONTEXT]
```

**Durable state. Long-horizon coherence. Governance substrate.**

*Core persistence layer of AOS v3.0 — enabling complex, auditable, multi-turn work.*