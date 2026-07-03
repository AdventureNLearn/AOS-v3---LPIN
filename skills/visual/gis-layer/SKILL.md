---
name: gis-layer
version: 3.0
---

# GIS Layer (v3.0)

**Core Alignment**: Evidence-first, OPSEC-hardened, fully replicable framework with strong governance and auditability standards.

## Purpose
GIS Layer adds interactive Leaflet.js GIS mapping and public spatial data layers to standalone HTML files or AOS-generated deliverables. It enables client-side maps for civic intelligence permit visualization, jurisdiction analysis, construction oversight, and spatial reasoning workflows.

It is fully agnostic, replicable, and CORS-compatible using public/open data sources.

v3.0 adds mandatory Layer-0 on Tier 1 spatial/civic mapping work and strengthened governance integration.

## v3.0 Alignment (Mandatory)
- **Layer-0 Pre-Filter**: Non-bypassable on all Tier 1 spatial, permit, jurisdiction, or oversight mapping work. Universe Truth Gate 0 + evidence-gate tri-state must inform all map layer and data decisions.
- **4-Agent Orchestration Default**: Often acts as a specialized visualization agent within 4-Agent workflows for spatial/civic deliverables.
- **Working Document Persistence**: All map layer decisions, data source selections, and tri-state assessments **must** be logged to working-doc-manager.
- **Tri-State Evidence (+1 / 0 / -1)**: Map layers and data representations should clearly reflect evidence strength and tri-state where applicable.
- **Governance Enforcement**: Any map that obscures evidence strength, hides data limitations, or misrepresents spatial relationships triggers revision.

## Core Capabilities

**Interactive Leaflet.js Maps**  
Embeds fully interactive, client-side maps using the lightweight Leaflet.js library.

**Public Spatial Data Layers**  
Integrates open/public spatial datasets (e.g., jurisdiction boundaries, permit locations, infrastructure, environmental layers).

**Civic Intelligence Use Cases**  
Optimized for permit visualization, jurisdiction analysis, construction oversight, and spatial reasoning workflows.

**Agnostic & Replicable**  
Designed to work in any standalone HTML file or AOS-generated deliverable without external dependencies beyond public CDNs.

**CORS-Compatible**  
Works reliably across domains when using appropriate public data sources.

## Activation Triggers
**Explicit**: "gis layer", "add interactive map", "leaflet map", "spatial visualization"
**Implicit**: Any deliverable requiring interactive maps for permits, jurisdictions, construction, or spatial analysis.

## Integration Points
- **Layer-0** — Enforces pre-filter passage on all Tier 1 spatial/civic mapping work.
- **civic-intelligence-coordinator** — Often used within broader civic intelligence deliverables.
- **construction-oversight** & **permit-coordinator** — Provides spatial visualization support.
- **working-doc-manager** — All map layer decisions and data source selections are logged here.
- **visual-systems-architect** — Collaborates on overall visual strategy and governance representation.

## OPSEC & Frog Protocol (Mandatory)
- **Frog Protocol**: Sensitive locations, projects, or investigations represented on maps receive appropriate abstraction or codenames.
- **Private by Default**: Detailed layer configuration and internal spatial analysis remain in the working document. Only final interactive maps are surfaced unless explicit governance/audit mode is requested.
- **Evidence-First, No Self-Report Reliance**: Never accepts self-reported spatial data quality. All layers are sourced from verified public/open datasets where possible.
- **Replicability & Auditability**: Every map includes clear source attribution and configuration logging.

## Best Practices
- Always enforce Layer-0 on Tier 1 spatial/civic mapping work.
- Clearly attribute all data sources and note any limitations.
- Use tri-state or evidence strength indicators where spatial claims are made.
- Keep maps clean, performant, and focused on the core message.
- Log all layer decisions and data source selections.

## Example Activation (Copy-Paste Ready)
```
Act as GIS Layer. 
Apply full Layer-0 pre-filter. 
Add interactive Leaflet.js mapping with relevant public spatial data layers to support the following scope.
Log all layer decisions and data sources to the working document.
[PASTE SCOPE OR REQUIREMENTS]
```

**Interactive spatial visualization. Public data layers. Civic intelligence ready.**

*Core GIS mapping capability of AOS v3.0.*