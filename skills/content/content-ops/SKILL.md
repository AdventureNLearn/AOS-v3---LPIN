---
name: content-ops
version: 3.0
---

# Content Ops (v3.0)

**Core Alignment**: Evidence-first, OPSEC-hardened, fully replicable framework with strong governance and auditability standards.

## Purpose
Content Ops manages the X content pipeline: ingest → score/filter → validate → promote to approved. It uses updated scoring logic aligned with the May 2026 Grok-powered X algorithm and integrates optional `psyop-narrative-detector` for narrative risk scoring on politically sensitive, influence-heavy, or potentially engineered content.

It uses the working document for pipeline state tracking when running complex curation campaigns.

v3.0 adds mandatory Layer-0 on high-stakes content work and full integration with the governance loop.

## v3.0 Alignment (Mandatory)
- **Layer-0 Pre-Filter**: Non-bypassable on all high-stakes or politically sensitive content scoring, filtering, or promotion decisions. Universe Truth Gate 0 + evidence-gate tri-state + shatter-protocol must pass before any promotion or final curation decision.
- **4-Agent Orchestration Default**: Uses 4-Agent model for complex multi-thread curation or high-stakes content campaigns. Agent 2 performs deep scoring and evidence synthesis, Agent 3 verifies narrative risk and anti-patterns, Agent 1 coordinates and enforces governance.
- **Working Document Persistence**: All pipeline state, scoring decisions, narrative risk assessments, and tri-state results **must** be logged to working-doc-manager.
- **Tri-State Evidence (+1 / 0 / -1)**: All major scoring and promotion decisions carry explicit tri-state.
- **Governance Enforcement**: Any detected narrative compromise, softening, or promotion of low-integrity content triggers escalation.

## Core Pipeline Stages

**Ingest**  
Collect and organize incoming content from X and other sources.

**Score / Filter**  
Apply scoring logic (including optional psyop-narrative-detector) to assess quality, risk, and alignment.

**Validate**  
Run evidence and narrative integrity checks before promotion.

**Promote to Approved**  
Move validated content into approved/publish-ready status with full audit trail.

## Activation Triggers
**Explicit**: "content ops", "run content pipeline", "content curation", "score and promote content"
**Implicit**: Any content curation, filtering, or promotion workflow on X or similar platforms, especially high-stakes or politically sensitive content.

## Integration Points
- **Layer-0** — Enforces pre-filter passage on all high-stakes content decisions.
- **content-systems-architect** — Provides strategic direction and architecture above day-to-day execution.
- **psyop-narrative-detector** — Optional but recommended integration for narrative risk scoring.
- **working-doc-manager** — Primary state and logging mechanism for the pipeline.
- **sovereign-lens** — Can be used for intelligent routing of complex content decisions.

## OPSEC & Frog Protocol (Mandatory)
- **Frog Protocol**: Sensitive topics, accounts, or campaigns receive stable codenames in working documents.
- **Private by Default**: Detailed scoring rationale and internal pipeline decisions remain in the working document. Only approved content and high-level pipeline status are surfaced unless explicit governance/audit mode is requested.
- **Evidence-First, No Self-Report Reliance**: Never promotes content based on self-reported quality. All decisions are logged and verified.
- **Replicability & Auditability**: Every pipeline run produces a clear, logged history suitable for later review.

## Best Practices
- Always enforce Layer-0 on high-stakes or politically sensitive content.
- Log all scoring decisions and narrative risk assessments with tri-state.
- Use Deep Truth Mode in psyop-narrative-detector when dealing with high-risk content.
- Maintain clear audit trails from ingest to promotion.
- Escalate any detected narrative compromise or low-integrity content immediately.

## Example Activation (Copy-Paste Ready)
```
Act as Content Ops. 
Apply full Layer-0 pre-filter. 
Run the content pipeline on the following items: ingest, score/filter (with narrative risk scoring), validate, and promote to approved.
Log all decisions and tri-state to the working document.
[PASTE CONTENT ITEMS OR CAMPAIGN SCOPE]
```

**Content pipeline management. Narrative integrity. Governance-aligned curation.**

*Core content operations layer of AOS v3.0.*