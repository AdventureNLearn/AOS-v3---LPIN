---
name: master-skill-index
version: 3.0
---

# Master Skill Index (v3.0)

**Core Alignment**: Evidence-first, OPSEC-hardened, fully replicable framework with strong governance and auditability standards.

## Purpose
Master Skill Index is the master reference for active skills and coordination patterns in AOS v3.0. It contains categories, activation triggers, and suggested routing for different types of tasks. It is useful as a living index when building complex multi-step workflows or when needing to quickly identify the right tool or pattern for a job.

v3.0 updates it with explicit Layer-0 routing guidance and strengthened governance integration.

## v3.0 Alignment (Mandatory)
- **Layer-0 Pre-Filter**: Non-bypassable on all high-stakes routing or workflow design decisions. The index explicitly flags which skills require Layer-0 passage and which coordination patterns enforce it.
- **4-Agent Orchestration Default**: The index includes routing guidance that defaults complex work to 4-Agent orchestration and identifies which skills are commonly used as Agent 1–4 delegates.
- **Working Document Persistence**: All routing decisions, index updates, and tri-state assessments of skill suitability **must** be logged to working-doc-manager.
- **Tri-State Evidence (+1 / 0 / -1)**: Skill suitability assessments for high-stakes work carry explicit tri-state.
- **Governance Enforcement**: Any routing decision that bypasses required Layer-0 gates or selects inappropriate skills for the task triggers revision.

## Core Structure

**Skill Categories**  
Organized groupings of skills by function (Core, Civic Intelligence, Content, Visual, Specialized, etc.).

**Activation Triggers**  
Clear, explicit phrases that activate each skill.

**Suggested Routing**  
Guidance on which skills or patterns to use for different task types (e.g., high-stakes governance, complex builds, solo work, civic intelligence, etc.).

**Layer-0 Flags**  
Explicit marking of which skills and coordination patterns require mandatory Layer-0 passage.

**4-Agent Guidance**  
Identification of skills commonly used in Agent 1–4 roles within orchestrated workflows.

## Activation Triggers
**Explicit**: "master skill index", "skill index", "which skill for", "routing guidance"
**Implicit**: Any point in complex workflow design or task planning where the operator needs a quick, reliable reference for skill selection or coordination patterns.

## Integration Points
- **Layer-0** — Serves as the canonical reference for which skills and patterns require pre-filter passage.
- **build-coordinator** & **reasoning-architect** — Primary users when designing complex workflows.
- **working-doc-manager** — All routing decisions and index consultations for high-stakes work are logged here.
- **4-agent-orchestration** — Provides the skill-to-role mapping used in orchestrated work.

## OPSEC & Frog Protocol (Mandatory)
- **Frog Protocol**: Sensitive skills, patterns, or routing logic receive stable codenames or abstraction when operational sensitivity exists.
- **Private by Default**: Detailed internal routing reasoning and index consultations remain in the working document. Only final skill selections and workflow structures are surfaced unless explicit governance/audit mode is requested.
- **Evidence-First, No Self-Report Reliance**: Never accepts self-reported skill suitability. All routing decisions for high-stakes work are logged and justified.
- **Replicability & Auditability**: Every routing decision produces a clear, logged rationale suitable for later review.

## Best Practices
- Always consult the index (and Layer-0 flags) when designing high-stakes or complex workflows.
- Log all routing decisions with tri-state assessment of skill suitability.
- Keep the index living and updated as new skills or patterns emerge.
- Use the index as a shared reference in team or multi-agent settings.
- Escalate any routing decision that bypasses required Layer-0 gates.

## Example Activation (Copy-Paste Ready)
```
Act as Master Skill Index. 
Apply full Layer-0 pre-filter. 
Provide routing guidance and recommended skills for the following task scope.
Log all recommendations and tri-state assessments to the working document.
[PASTE TASK SCOPE OR REQUIREMENTS]
```

**Living skill reference. Layer-0 aware routing. Workflow design support.**

*Master reference layer of AOS v3.0 — enabling reliable skill selection and coordination.*