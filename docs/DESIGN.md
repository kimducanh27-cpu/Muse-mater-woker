> Derived. Not authoritative. On disagreement the Control File wins.
> Generated from this repository at commit `7432476`, 2026-11-13.

# Design decisions

This repository has no user interface, so this file does not contain colours or fonts. It contains the design decisions that shape the kit, and the design contract the kit will impose on the product once one exists.

## Why three tabs and not one agent

A single agent asked to design a whole interface will produce something coherent and untraceable. Splitting into three sessions with file-based handoff forces each step to be reconstructible from disk. If tab 02 needs something tab 01 decided, it must find it in a file. Anything that exists only in a conversation is lost by design.

## Why the gates use exact commands

`APPROVE SCREEN UX MODEL` is a string a human must type. It is not a button, and it is not something an agent may infer from context.

The reason is narrow: an agent that can infer approval will eventually infer it. The exact string is the only thing that distinguishes "the human decided" from "the agent believed the human would agree".

## Why every artifact carries a hash

A hash proves byte identity and nothing else. It does not prove the artifact is good, complete or correct. It proves that the file a later stage read is the file the gate approved.

Without it, "approved" means "approved at some point, possibly a different version". That is not a gate.

## Why the process produces no UI in stages 01–05

Values are forbidden before Process 06 on purpose. A UX specification that names a button has already made a design system decision, badly, without a token layer, and Process 06 becomes a rubber stamp.

Process 06 is the first stage allowed to produce a hex value. That permission is not an accident of ordering; it is the point at which the product stops being an argument and becomes a system.

## Platform

**Android native.** Jetpack Compose, Material 3. No web target, no iOS target, no cross-platform framework in v1.

Recorded in `process-charters/06-DESIGN-SYSTEMS.md` section 8a. It binds Processes 06–08: Material 3 target sizes and type scale, tonal elevation, dynamic colour, system and predictive back, window insets, window size classes.

Process 05 stays platform-neutral even though the product is Android. It states the requirement — "the user must be able to abandon this task without losing input" — and Process 06 decides which affordance satisfies it. Absorbing platform idioms earlier would pre-empt the design system with decisions nobody audited.

## What the product design system must contain

Defined in `.agents/skills/design-system/SKILL.md`. In brief:

- Three token tiers, Material 3's model: reference (`ref`), system (`sys`), component (`comp`). A component token may not reach past the system tier.
- A component exists only if a frozen screen cites it. `components_defined` must equal `components_cited` at Gate 2.
- Contrast is measured from resolved values with the method stated. A declared ratio is not evidence.

The first of those three rules was tested and held: an agent given a two-screen spec admitted six components and rejected four Material 3 defaults by name — `NavigationDrawer`, `FloatingActionButton`, `Tabs`, `Slider` — because no screen required them.

## Visual identity of the kit itself

None, deliberately. The kit is markdown, YAML and five Python checking scripts. Adding a visual identity to a process kit is the kind of work that feels like progress and produces nothing a user can use.
