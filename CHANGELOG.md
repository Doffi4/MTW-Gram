# Changelog

## 0.2.0-beta

### Added

- An in-window settings sidebar with separate General, Appearance, Data and Storage, and Stickers and Emoji pages.
- A new MTW-Gram icon and separate Windows application identity.

### Changed

- Added crossfades to top-level settings navigation and kept directional slides for nested pages.
- Updated the chat header, composer, folder tabs, profiles, search, reactions, attachments, and emoji, sticker, and GIF panels.
- Used separate application data and disabled upstream auto-updates and crash reporting in the distributed build.

### Fixed

- Prevented recursive sidebar resizing when dragging the chat list divider.
- Kept the camera preview callback alive when closing the capture dialog.
- Excluded messages covered by the floating composer from visibility and read calculations.
- Made Windows light and dark mode follow-system handling use the Windows app preference.

## 0.1.0-beta

- First preview with a floating chat list, settings cards, and macOS-inspired transitions.
