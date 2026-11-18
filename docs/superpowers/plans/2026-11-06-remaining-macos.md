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

## Task 4: Edit-profile cards

- [x] Compare the form against recon screenshot S17 (`2Bi-settings_edit-profile_system.png`) and the 600 px cap in `GeneralRowItem.swift`.
- [x] Center the existing settings form and match the bio card width, corner radius and inner padding to the surrounding cards. Keep the existing editor, character limit and save callbacks.
- [x] Check narrow and wide form widths and verify the regenerated patch against `patches/BASE`.
- [x] Build Debug and run the five local regression checks (`build/build-profile-edit-layout.log`).

The photo and name editors still use the existing Telegram Desktop controls. The side panel animation is pending.

## Task 5: Global search sections

- [x] Compare results against recon screenshot S07 (`31-search_results_tinted.png`).
- [x] Label the chats and contacts section and use its height for painting, hit testing and row offsets. Preserve the existing result groups and filters.
- [x] Build Debug (`build/build-search-sections-final.log`), run the six local checks and apply the patch to the clean base.

Task 6 covers the search tabs and global peers expander from S07.

## Task 6: Global search and message surfaces

- [x] S07. Style the native global search tabs and fold global peers to five rows. Keep the other rows available through the section action.
- [x] S08. Draw the unread bar as a rounded separator and retain the existing first-unread anchor. Animate chip insertion, removal, movement and selection, then apply the hover panel press, reveal and loading states.
- [x] S10. Use the message menu reaction pill with up to seven quick choices and an expand button. Keep the PopupMenu action and keyboard handlers.
- [x] S14. Style the attachment dropdown and route the paperclip through it in both composers when available. Open camera captures in the existing media confirmation.
- [x] Run local regression checks and replay both patches from the BASE commits.
- [x] Finish the Debug build.

Debug passed with exit code 0 (`build/build-must-ui-verified.log`). All 14 local regression checks passed. Both patches applied to clean BASE indexes and matched the working sources.

Visual comparison and live account scenarios remain open.

## Task 7. Emoji, stickers and GIF panels

- [x] Review the S13 popup and sidebar references.
- [x] Place the category strip above the grid and the rounded tab control below it. Preserve scrolling, search, peer restrictions, selection and the current tab across both panel hosts.
- [x] Check the viewport and tab animation. Build Debug and replay both patches from BASE.

Debug passed with exit code 0 (`build/build-entertainment-panel.log`). All 16 local checks passed. Both patches replayed on BASE and matched the working sources. Visual comparison and the sidebar entrance animation remain open.

## Task 8. Remaining required settings and window states

- [x] Keep the Windows caption strip at 24 px, match it to the window background, and hide it in fullscreen.
- [x] Use a shared 90 px width for the compact dialogs list and a 100 px drag snap. Center avatars and use the new layout when going back from one column to two.
- [x] Read the Windows app color preference during startup and on settings changes. Keep the Qt fallback.
- [x] Lay out right-hand values and render native radio buttons as grouped settings rows.

Debug passed with exit code 0 (`build/build-required-ui-verified.log`). All 20 local regression checks passed. Both patches applied to their BASE commits and matched the working sources. An isolated executable read the Windows app preference and ran 16 cases for the follow-system decision with palette application stubbed. Visual comparison and a live OS theme change with the main client open remain unverified.
