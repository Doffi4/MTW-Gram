# Telegram macOS-look fork for Windows

Цель: форк Telegram Desktop (C++/Qt, GPL) с визуалом и анимациями официального macOS-клиента.
Клиент macOS (Swift/AppKit) на Windows не портируется, поэтому переносим только внешний вид и поведение в Qt.

## Этап 1 — на маке (recon)
Запусти `/replica-recon` для установленного Telegram на macOS и для исходников
https://github.com/TelegramMessenger/Telegram-macOS (клонировать в `refs/Telegram-macOS`, в git не коммитить).
Результат складывать в `recon/` и коммитить:
- `recon/screens/` — скриншоты всех экранов и состояний (светлая и тёмная темы, hover/pressed, пустые состояния, настройки, профиль, медиа-вьювер, звонки)
- `recon/animations/` — записи экрана ключевых анимаций (открытие чата, отправка сообщения, реакции, сайдбар, переключение папок, контекстное меню) и таблица `animations.md`: элемент, длительность, кривая/пружина, ссылка на файл и строку в исходниках
- `recon/tokens.md` — цвета (по ролям, light/dark), радиусы, отступы, размеры шрифтов, тени, высоты строк списков; шрифт SF Pro не переносить, замена Inter
- `recon/layout.md` — размеры и поведение окна, сайдбара, шапок, поля ввода, пузырей сообщений

## Этап 2 — на винде (форк)
1. Склонировать `telegramdesktop/tdesktop` в `refs/tdesktop`, собрать по их инструкции для Windows (VS 2022, Python, Qt из их скриптов).
2. Стили Telegram Desktop лежат в `Telegram/SourceFiles/**/*.style` и `ui/` (lib_ui) — менять токены оттуда.
3. Анимации: `ui/effects/animations`, кривые в `anim::` — подгонять под `recon/animations.md`.
4. Работать патчами поверх tdesktop, чтобы можно было подтягивать апстрим.

## Правила
- Не коммитить `refs/` и сборочные артефакты.
- Лицензия GPL v3 (производная от tdesktop); api_id/api_hash — свои, с my.telegram.org, в репо не класть.
