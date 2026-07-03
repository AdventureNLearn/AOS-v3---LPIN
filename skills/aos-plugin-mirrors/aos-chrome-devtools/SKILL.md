---
name: aos-chrome-devtools
version: 3.0
---

# AOS Chrome DevTools (v3.0)

**Core Alignment**: Evidence-first, OPSEC-hardened, fully replicable framework with strong governance and auditability standards.

## Purpose
AOS Chrome DevTools is the AOS mirror of the Grok Build Chrome DevTools plugin. It provides browser control patterns, performance trace analysis, network inspection guidance, and evidence-gated web debugging.

It is triggered on Chrome DevTools, Grok Build browser mirror, AOS web performance, or network inspection in AOS contexts.

v3.0 adds mandatory Layer-0 on Tier 1 web debugging or browser automation work and strengthened governance integration.

## v3.0 Alignment (Mandatory)
- **Layer-0 Pre-Filter**: Non-bypassable on all Tier 1 web debugging, browser automation, or network inspection work. Universe Truth Gate 0 + evidence-gate tri-state + shatter-protocol must inform all debugging and analysis decisions.
- **4-Agent Orchestration Default**: Often acts as a specialized debugging/inspection agent within 4-Agent workflows for web performance or browser automation tasks.
- **Working Document Persistence**: All debugging sessions, trace analyses, network findings, and tri-state assessments **must** be logged to working-doc-manager.
- **Tri-State Evidence (+1 / 0 / -1)**: All major debugging conclusions and performance findings carry explicit tri-state.
- **Governance Enforcement**: Any debugging analysis that bypasses evidence standards or introduces unverified claims triggers revision.

## Core Capabilities

**Browser Control Patterns**  
Provides structured patterns for controlling and automating browser behavior in AOS workflows.

**Performance Trace Analysis**  
Analyzes browser performance traces with evidence-gated conclusions.

**Network Inspection Guidance**  
Offers guidance for inspecting and interpreting network activity with clear evidence trails.

**Evidence-Gated Web Debugging**  
Enforces evidence-first principles in all web debugging and browser automation work.

**AOS Web Performance & Network Integration**  
Integrates with AOS web performance and network inspection workflows.

## Activation Triggers
**Explicit**: "Chrome DevTools", "Grok Build browser mirror", "AOS web performance", "network inspection in AOS"
**Implicit**: Any work involving browser automation, web performance analysis, or network debugging within AOS contexts.

## Integration Points
- **Layer-0** — Enforces pre-filter passage on all Tier 1 web debugging or browser automation work.
- **build-coordinator** — Primary collaborator on web automation or performance builds.
- **working-doc-manager** — All debugging sessions, trace analyses, and network findings are logged here.
- **reasoning-architect** — Often collaborates on reasoning aspects of performance or network analysis.

## OPSEC & Frog Protocol (Mandatory)
- **Frog Protocol**: Sensitive URLs, network patterns, or debugging targets receive stable codenames or abstraction levels.
- **Private by Default**: Detailed debugging reasoning and internal trace analysis remain in the working document. Only final findings and high-level recommendations are surfaced unless explicit governance/audit mode is requested.
- **Evidence-First, No Self-Report Reliance**: Never accepts self-reported performance or network conclusions. All findings are grounded in actual traces and logs.
- **Replicability & Auditability**: Every debugging session produces a clear, logged analysis suitable for later review.

## Best Practices
- Always enforce Layer-0 on Tier 1 web debugging or browser automation work.
- Maintain clear evidence trails from browser traces and network logs.
- Log all debugging sessions and tri-state assessments.
- Combine with reasoning-architect for complex performance or network analysis.
- Keep debugging conclusions strictly evidence-based.

## Example Activation (Copy-Paste Ready)
```
Act as AOS Chrome DevTools. 
Apply full Layer-0 pre-filter. 
Perform browser control, performance trace analysis, or network inspection on the following scope.
Provide evidence-gated findings with tri-state.
Log all sessions and analyses to the working document.
[PASTE SCOPE OR REQUIREMENTS]
```

**Browser automation. Performance tracing. Evidence-gated debugging.**

*Core web debugging and browser automation layer of AOS v3.0.*