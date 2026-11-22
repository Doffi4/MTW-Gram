# Changelog

## 0.2.4-beta

- Aligned the option cards in chat folder settings.
- Added a fade when returning from Settings to Chats and when switching between open chats.
- Added optional smooth mouse wheel scrolling in Chat Settings, off by default.

## 0.2.3-beta

- Smoothed the chat list transition when opening and closing forum topics.

## 0.2.2-beta

- Restored the slide-out animation when closing the emoji, sticker, and GIF sidebar.

## 0.2.1-beta

### Changed

- Updated the Telegram Desktop base to 7.4.4.
- Added GitHub update checking and installation under Settings → General.
- Restyled desktop notifications and added a new default notification sound.

### Fixed

- Sized the chat header capsule to the visible status, including typing and other animated actions.
- Prevented the notification stack's Hide All button from restarting its fade after the last notifications close.
- Fixed a crash when opening the send menu and restored click animations in the emoji, sticker, and GIF sidebar.

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
