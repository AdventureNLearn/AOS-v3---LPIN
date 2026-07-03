---
name: state-onboarding-playbook
version: 3.0
---

# State Onboarding Playbook (v3.0)

**Core Alignment**: Evidence-first, OPSEC-hardened, fully replicable framework with strong governance and auditability standards.

## Purpose
State Onboarding Playbook provides a standardized, gate-first playbook for onboarding new states and jurisdictions into the Civic Intelligence knowledge graph. It defines Tier 1 selection criteria, a repeatable onboarding workflow, success criteria, and the roles of existing skills.

It ensures consistent, high-quality expansion of the knowledge base while maintaining Layer-0 and governance standards.

## v3.0 Alignment (Mandatory)
- **Layer-0 Pre-Filter**: Non-bypassable on all onboarding work. Universe Truth Gate 0 + evidence-gate tri-state + shatter-protocol must pass before any jurisdiction is added to the knowledge graph.
- **4-Agent Orchestration Default**: Uses 4-Agent model for complex multi-state or high-volume onboarding. Agent 1 coordinates, Agent 2 handles data gathering and synthesis, Agent 3 verifies gates and data quality, Agent 4 produces final onboarding deliverables.
- **Working Document Persistence**: All selection decisions, validation results, onboarding steps, and tri-state findings **must** be logged to working-doc-manager.
- **Tri-State Evidence (+1 / 0 / -1)**: All major onboarding decisions and data quality assessments carry explicit tri-state.
- **Governance Enforcement**: Any detected issues with data quality, selection bias, or incomplete onboarding triggers escalation.

## Core Components

**Tier 1 Selection Criteria**  
Defines clear, evidence-based criteria for prioritizing which states/jurisdictions to onboard.

**Repeatable Onboarding Workflow**  
Provides a step-by-step process for ingesting, validating, and integrating new jurisdiction data.

**Success Criteria**  
Specifies measurable outcomes that indicate successful onboarding (data quality, coverage, integration completeness).

**Role Definition**  
Clarifies how existing skills (jurisdiction-ops, permit-coordinator, public-records-forensics, etc.) contribute to the onboarding process.

## Activation Triggers
**Explicit**: "state onboarding playbook", "onboard new jurisdiction", "jurisdiction onboarding workflow"
**Implicit**: Any work involving expansion of the Civic Intelligence knowledge graph to new states or jurisdictions.

## Integration Points
- **Layer-0** — Enforces pre-filter passage on all onboarding work.
- **civic-intelligence-coordinator** — Oversees and coordinates onboarding campaigns.
- **jurisdiction-ops** — Primary skill responsible for data ingestion and validation during onboarding.
- **working-doc-manager** — Primary logging destination for the entire onboarding process.
- **oversight-kit-builder** — May produce onboarding status or gap analysis kits.

## OPSEC & Frog Protocol (Mandatory)
- **Frog Protocol**: Sensitive jurisdictions or data sources under onboarding receive stable codenames.
- **Private by Default**: Detailed internal onboarding decisions and data analysis remain in the working document. Only final onboarding status and deliverables are surfaced unless explicit governance/audit mode is requested.
- **Evidence-First, No Self-Report Reliance**: Never accepts self-reported data completeness. All onboarding steps are independently validated.
- **Replicability & Auditability**: Every onboarding run produces a clear, logged history suitable for later review or replication.

## Best Practices
- Always enforce Layer-0 before onboarding any new jurisdiction.
- Follow the standardized workflow to ensure consistency.
- Log all decisions and data quality findings with tri-state.
- Use 4-Agent model for complex or multi-state onboarding campaigns.
- Maintain clear success metrics and track progress in the working document.

## Example Activation (Copy-Paste Ready)
```
Act as State Onboarding Playbook. 
Apply full Layer-0 pre-filter. 
Execute the standardized onboarding workflow for the following state/jurisdiction.
Log all steps, decisions, and tri-state findings to the working document.
[PASTE JURISDICTION SCOPE OR DATA]
```

**Standardized onboarding. Gate-first expansion. Knowledge graph growth.**

*Playbook for consistent, high-quality expansion of the Civic Intelligence layer in AOS v3.0.*