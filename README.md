---
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
└── specialized/             # Domain-specific and advanced tools
    ├── aos-plugin-mirrors/  # Mirrors of external dev tool integrations
    └── (other specialized skills)
```

## Key Principles

- **Layer-0 Pre-Filters**: Non-bypassable validation gates on all Tier 1 work.
- **4-Agent Orchestration**: Structured multi-agent workflows with clear role separation.
- **Working Document Persistence**: All major decisions, evidence, and state are logged.
- **Tri-State Evidence (+1 / 0 / -1)**: Explicit confidence and evidence strength tracking.
- **Governance Enforcement**: Automatic escalation on detected drift or weakened standards.
- **Frog Protocol**: Codename usage and private-by-default handling for sensitive work.
- **Replicability**: All skills and workflows are designed to be portable and auditable.

## How to Use

Each skill lives in its own folder with a `SKILL.md` file containing:
- Purpose and v3.0 Alignment
- Core Capabilities
- Activation Triggers
- Integration Points
- OPSEC & Frog Protocol guidance
- Best Practices
- Copy-paste ready example activations

To activate a skill, simply reference its name and provide the required context (many skills also support explicit activation phrases).

## Repository Goals

- Full skill expansion with high-quality, detailed documentation
- Clean, logical folder structure
- Strong emphasis on evidence integrity and governance
- Replicable across different environments and use cases

## License

This project is intended for open, replicable use with strong emphasis on evidence-based reasoning and governance.

---

*Built for high-stakes, high-integrity work.*