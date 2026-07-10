# AOS v3.0 Sovereign Edition

**Adventure OS v3.0 Sovereign Edition** is a modular, evidence-first AI operating system framework designed for high-integrity, replicable, and governable workflows.

It emphasizes strict Layer-0 pre-filters, 4-Agent orchestration, working document persistence, tri-state evidence tracking, and strong governance enforcement across all skills and processes.

## Current Structure

```
skills/
├── core/                    # Foundational runtime and governance skills
├── civic-intelligence/      # Permit, jurisdiction, oversight, and regulatory tools
├── content/                 # Content operations and systems architecture
├── visual/                  # Visual systems, GIS, and symbolic encoding
└── specialized/             # Domain-specific and advanced tools (including 9 expanded operators)
```

## Recently Expanded Skills

The following **9 specialized operators** have been expanded to full AOS v3.0 format:

- `recon-operator` — Initial reconnaissance and attack surface mapping
- `scanning-operator` — Active scanning and vulnerability identification
- `exploit-operator` — Weaponizing vulnerabilities for initial access
- `post-ex-operator` — Post-exploitation, enumeration, and preparation
- `privesc-operator` — Privilege escalation
- `lateral-operator` — Lateral movement using credentials and trust
- `persistence-operator` — Establishing long-term access
- `exfil-operator` — Controlled data exfiltration
- `report-operator` — Final evidence-based reporting

These skills are now available in `skills/specialized/` with rich documentation, activation triggers, integration points, best practices, and OPSEC guidance.

## Key Principles

- **Layer-0 Pre-Filters**: Non-bypassable validation gates on all Tier 1 work.
- **4-Agent Orchestration**: Structured multi-agent workflows with clear role separation.
- **Working Document Persistence**: All major decisions, evidence, and state are logged.
- **Tri-State Evidence (+1 / 0 / -1)**: Explicit confidence and evidence strength tracking.
- **Governance Enforcement**: Automatic escalation on detected drift or weakened standards.
- **Frog Protocol**: Codename usage and private-by-default handling for sensitive work.
- **Replicability**: All skills and workflows are designed to be portable and auditable.

## Researcher Tools

A **Researcher Workbench** is available to help researchers and developers:
- Browse and understand the full skill inventory
- Map their own work/projects to AOS skills and principles
- Customize categorizations and export structured outputs

The Workbench is designed to be self-contained and can be used directly from the repo.

## How to Use Skills

Each skill lives in its own folder with a `SKILL.md` file containing:
- Purpose and v3.0 Alignment
- Core Capabilities
- Activation Triggers
- Integration Points
- OPSEC & Frog Protocol guidance
- Best Practices
- Copy-paste ready example activations

To activate a skill, simply reference its name and provide the required context.

## Swapping & Customizing Skills

Developers are encouraged to pull individual skills or categories from this repo to customize their own installations. The `skills/` folder is designed to be modular.

## Repository Goals

- Full skill expansion with high-quality, detailed documentation
- Clean, logical folder structure
- Strong emphasis on evidence integrity and governance
- Replicable across different environments and use cases

## License

This project is intended for open, replicable use with strong emphasis on evidence-based reasoning and governance.

---

*Built for high-stakes, high-integrity work.*