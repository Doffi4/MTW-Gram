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
