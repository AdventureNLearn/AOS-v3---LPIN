---
name: email-operator
version: 3.0
---

# Email Operator (v3.0)

**Core Alignment**: Evidence-first, OPSEC-hardened, fully replicable framework with strong governance and auditability standards.

## Purpose
Email Operator is a specialist skill for safe, auditable Outlook email operations (create draft or immediate send). It is PII-safe via optional user-managed config file. It supports speculative Draft-Verify mode, verifiable Execution Receipts, default-to-draft for reviewability, and clean Agent 1 routing.

It is mandatory on Tier 1 email/communication workflows, especially those involving civic or high-stakes communications.

v3.0 adds mandatory Layer-0 on Tier 1 email workflows and strengthened governance integration.

## v3.0 Alignment (Mandatory)
- **Layer-0 Pre-Filter**: Non-bypassable on all Tier 1 email or high-stakes communication work. Universe Truth Gate 0 + evidence-gate tri-state must inform all send/draft decisions.
- **4-Agent Orchestration Default**: Often acts as a specialized communication agent within 4-Agent workflows for high-stakes or civic email operations.
- **Working Document Persistence**: All email decisions, draft contents (or references), execution receipts, and tri-state assessments **must** be logged to working-doc-manager.
- **Tri-State Evidence (+1 / 0 / -1)**: All send/draft decisions carry explicit tri-state.
- **Governance Enforcement**: Any attempt to send without proper review gates or evidence justification triggers blocking and escalation.

## Core Capabilities

**Safe Outlook Email Operations**  
Supports both creating drafts and sending emails with full auditability.

**Draft-Verify Mode**  
Allows speculative drafting with explicit verification before sending.

**Verifiable Execution Receipts**  
Provides clear, logged confirmation of email actions (draft created, sent, etc.).

**Default-to-Draft for Reviewability**  
Prioritizes creating drafts over immediate sending for high-stakes or civic communications.

**Clean Agent 1 Routing**  
Designed to integrate cleanly as a communication tool within 4-Agent orchestration.

**PII-Safe Configuration**  
Supports optional user-managed config files to protect sensitive information.

## Activation Triggers
**Explicit**: "email operator", "send email", "create email draft", "Outlook email"
**Implicit**: Any Tier 1 or high-stakes email/communication workflow, especially those involving civic intelligence, governance, or sensitive topics.

## Integration Points
- **Layer-0** — Enforces pre-filter passage on all Tier 1 email workflows.
- **build-coordinator** — Primary routing for communication actions in builds.
- **working-doc-manager** — All email decisions, drafts, and execution receipts are logged here.
- **email-operator** is the canonical communication tool for auditable Outlook operations in AOS.

## OPSEC & Frog Protocol (Mandatory)
- **Frog Protocol**: Sensitive recipients, topics, or email content receive stable codenames.
- **Private by Default**: Draft contents and internal email reasoning remain in the working document. Only final send confirmations and high-level status are surfaced unless explicit governance/audit mode is requested.
- **Evidence-First, No Self-Report Reliance**: Never accepts self-reported send success. All actions are logged with verifiable receipts.
- **Replicability & Auditability**: Every email action produces a clear, logged record suitable for later review.

## Best Practices
- Default to Draft mode for all high-stakes or civic communications.
- Always enforce Layer-0 on Tier 1 email workflows.
- Log all decisions and execution receipts with tri-state.
- Use PII-safe configuration when handling sensitive data.
- Never bypass review gates on sensitive or high-stakes emails.

## Example Activation (Copy-Paste Ready)
```
Act as Email Operator. 
Apply full Layer-0 pre-filter. 
Create a draft (or send, if explicitly approved) for the following email with full auditability and Execution Receipt.
Log all decisions and tri-state to the working document.
[PASTE EMAIL CONTENT OR REQUIREMENTS]
```

**Auditable email operations. Draft-first by default. Governance-controlled sending.**

*Core communication layer of AOS v3.0.*