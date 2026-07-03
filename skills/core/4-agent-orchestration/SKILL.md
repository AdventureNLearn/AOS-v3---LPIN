---
name: 4-agent-orchestration
version: 3.0
---

# 4-Agent Orchestration (v3.0)

**Core Alignment**: Evidence-first, OPSEC-hardened, fully replicable framework with strong governance and auditability standards.

## Purpose
The 4-Agent model provides a repeatable, evidence-first orchestration pattern for complex reasoning, build, audit, and civic intelligence tasks. It decomposes work across specialized roles while maintaining a single source of truth (working document), latent state carry for efficiency in recurrent-depth loops, and mandatory foundational skill invocation.

This is the default execution model for any task requiring multi-hop reasoning, multi-source verification, artifact creation, or governance participation.

## v3.0 Alignment (Mandatory)
- **Layer-0 Pre-Filter**: All high-stakes, recurrent-depth, or multi-agent runs **must** explicitly invoke the full Layer-0 chain (Universe Truth Gate 0 + shatter-protocol + evidence-gate tri-state) **before** any agent delegation.
- **4-Agent Orchestration Default**: This skill *is* the orchestration layer. Agent 1 (Coordinator) is responsible for task decomposition, agent assignment, latent handoff, synthesis, and final governance sign-off.
- **Working Document Persistence**: Agent 1 **must** update the working document (Decisions recorded verbatim, Plan Tasks, Notes, Numbers, Latent State) at the end of every major cycle or phase transition.
- **Tri-State Evidence (+1 / 0 / -1)**: All claims, decisions, and handoff rationales carry explicit tri-state labeling. Conflicting evidence triggers evidence-gate strict mode and potential escalation.
- **Governance Enforcement**: Agent 1 is the final backstop. Any detected softening, false evenhandedness, or evidence suppression triggers immediate escalation and rewrite.

## Agent Roles (v3.0)

**Agent 1 — Coordinator**  
- Central router, decision maker, final synthesis, and governance enforcement.  
- Always invokes foundational skills (evidence-gate, shatter-protocol, working-doc-manager) internally before delegation.  
- Manages latent state carry across recurrent loops.  
- Responsible for working document maintenance and final output integrity.

**Agent 2 — Research & Synthesis**  
- Primary researcher and information synthesizer.  
- Gathers sources, performs initial analysis, and prepares structured inputs for verification.  
- Flags uncertainty and conflicting evidence early.

**Agent 3 — Verification & Integrity**  
- Applies Evidence-Gate, Shatter Protocol, and other integrity checks.  
- Assigns tri-state to claims and outputs.  
- Escalates issues that cannot be resolved.

**Agent 4 — Output & Delivery**  
- Formats final outputs according to requirements.  
- Ensures auditability and proper documentation.  
- Prepares deliverables for handoff or publication.

## Core Execution Flow

1. **Agent 1** receives the task and creates/updates the working document.
2. **Agent 1** invokes Layer-0 pre-filters (Evidence-Gate + Shatter Protocol).
3. Work is decomposed and delegated to Agents 2–4 as needed.
4. Results flow back to Agent 1 with tri-state labeling.
5. Agent 1 performs final synthesis and governance check.
6. Working document is updated with decisions, verification log, and latent state.
7. Output is delivered only after passing governance requirements.

## Activation Triggers
**Explicit**: "4-agent orchestration", "use 4-agent model", "agent 1 coordinate", "multi-agent workflow"
**Implicit**: Any complex, multi-step, or high-stakes task requiring structured decomposition and verification.

## Integration Points
- **working-doc-manager** — Primary state and logging mechanism.
- **evidence-gate** & **shatter-protocol** — Mandatory Layer-0 pre-filters invoked by Agent 1.
- **sovereign-lens** — Used for intelligent routing when multiple specialized modules are involved.
- **build-coordinator** — Often runs on top of the 4-agent model for major builds.
- **values-alignment-check** — Final governance gate on Tier 1 outputs.

## OPSEC & Frog Protocol (Mandatory)
- **Frog Protocol**: Sensitive tasks, entities, or decisions receive stable codenames in the working document.
- **Private by Default**: Detailed agent reasoning and internal handoffs remain in the working document. Only final outputs are surfaced unless explicit governance/audit mode is requested.
- **Evidence-First, No Self-Report Reliance**: Agent outputs are never accepted without verification through Evidence-Gate and working document logging.
- **Replicability & Auditability**: The entire orchestration run produces a clear, logged history suitable for later review.

## Best Practices
- Always start with a working document and Layer-0 pre-filters.
- Keep latent state concise but rich in key evidence and decisions.
- Record all major decisions verbatim in the Decisions Log.
- Use tri-state labeling consistently across all agent outputs.
- Escalate early when evidence is weak or illusions are detected.

## Example Activation (Copy-Paste Ready)
```
Act as 4-Agent Orchestration. 
Apply full Layer-0 pre-filter. 
Decompose and coordinate the following task across the four agents, maintaining the working document throughout.
[PASTE TASK DESCRIPTION]
```

**Structured decomposition. Rigorous verification. Governance enforcement.**

*Core orchestration model of AOS v3.0 — enabling complex, auditable, multi-agent work.*