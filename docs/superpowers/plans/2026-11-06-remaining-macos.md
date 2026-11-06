# Remaining macOS styling Implementation Plan

> **For agentic workers:** execute inline, without subagents, as requested by the user.

**Goal:** Complete the remaining recon scope in bounded, buildable stages.
**Architecture:** Reuse tdesktop components and shared style tokens; distribute only fork patches.
**Tech Stack:** C++/Qt, tdesktop styles, Python standard library.
**Spec:** docs/superpowers/specs/2026-11-06-remaining-macos-design.md

## Global Constraints

No subagents or UI automation. No copied macOS code/assets, API credentials, refs or binaries in commits. No push/publication. Preserve the existing 0.2.0-beta candidate.

## Review Focus

Inline and floating Info headers; title/subtitle bounds; centered ripple and search controls; collapsible profile derived heights; selection-mode controls.

## Task 1: Common Info navigation

- [x] Inspect Info::TopBar consumers and styles for inline/floating variants.
- [x] Update info/info.style: height 64, title 15 medium, subtitle 12; adjust fixed title, ripple and search offsets.
- [x] Run Debug and inspect build output. No new permanent test for constant-only styling.
- [x] Regenerate tdesktop.patch, verify clean-base application against current sources, document the stage.

## Task 2: Restore the implementation inventory

- [x] Reconcile features.csv with current patches: yes means implemented in source, partial means only part of macOS styling is covered; neither means visually verified.
- [x] Leave profile/media/calls/stories incomplete until their actual implementation stages are done.

## Later stages

Profile and panels; message state styling; animation remainder; gallery; calls and stories. Each stage requires its owning-source investigation and a concrete diff before being marked done. Do not claim the whole fork finished after Task 1.

## Validation

Debug build tools/build-win.bat Debug: exit 0, build/build-info-navigation.log. Inline source review completed without subagents. UI omitted at user request. Remaining stages above are still pending.

## Task 3: Profile and entertainment panel layout

- [x] Read profile/card/tab/sidebar geometry from the local macOS source and recon screenshots; check all native layout and viewport consumers.
- [x] Add a failing geometry check, then constrain and center profile content/actions; keep media coordinate transforms and search/selection bindings.
- [x] Use existing SettingsButton card painting, card backgrounds for detail sections, 120px avatar, 600px cards, and 40px media tab islands.
- [x] Align popup panel width/radius to 358/16; retain the existing 408ms menu spring instead of applying the sidebar's 300ms timing to a popup.
- [x] Finish Debug build; rerun geometry and compose regression checks.
- [x] Regenerate and verify patches; update implementation evidence without marking every profile/panel state complete.

Excluded from this stage: sidebar width preference/drag constraints, profile editing forms, colored-profile-specific animation, new icons, live UI validation. Existing behavior is preserved where no macOS-specific styling was added.

Task 3 validation: Debug exit 0 (build/build-profile-panels-fixed.log); three profile geometry checks and compose visibility regression pass. Fixed a missing styles/style_info.h include found by the first compile. UI not run.
