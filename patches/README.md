# Патчи поверх tdesktop

База — коммиты в `BASE`. Наложить на чистый клон `refs/tdesktop` (из корня репо):

```
git -C refs/tdesktop apply --binary ../../patches/tdesktop.patch
git -C refs/tdesktop/Telegram/lib_ui apply --binary ../../../../patches/lib_ui.patch
```

Собрать: `tools\build-win.bat`.

| Патч | Что внутри |
|---|---|
| `lib_ui.patch` | палитра Classic ← macOS Day Classic (`ui/colors.palette`), шрифт Inter (OFL, `fonts/`) вместо Open Sans, «semibold» = Inter Medium |
| `tdesktop.patch` | темы Day/Tinted/Night ← macOS Day/Tinted/Dark, акценты тем из macOS, строка списка чатов 70 / аватар 50, радиус стыка пузырей 8 |
| `tdesktop.patch` | список чатов: плашка выделения/hover — скруглённая (inset 3, radius 14, `PaintRowBackground` в `dialogs_layout.cpp`), имя 14 medium (`dialogsNameFont`/`dialogsNameStyle`), nameTop/textTop 14/37 |
| `lib_ui.patch` | меню: окно попапа radius 18, строка 28 (`itemPadding` 6/6), hover-плашка radius 5 с отступом 4 по бокам (`Menu.itemBgRadius/itemBgSkip`, `Menu::Action::paintBackground`) |
| `tdesktop.patch` | поле ввода в `HistoryWidget`: скруглённая капсула radius 20 с отступом 8 вместо полосы во всю ширину (`historyComposeCapsule*`); ComposeControls (темы/ответы/отложенные) и плавающее положение над историей — не сделаны |
| `tdesktop.patch` | шапка чата: высота 64, заголовок 15 medium (`topBarNameStyle`), статус 12 (`topBarStatusFont`), без разделителя под шапкой (HistoryWidget, ChatWidget) |

Цвета генерирует `tools/mac_palette.py` из `ColorPalette.swift` Telegram-macOS; после изменения сопоставления — перезапустить его и пересоздать патчи:

```
python -I tools/mac_palette.py <Telegram-macOS>/packages/ColorPalette/Sources/ColorPalette/ColorPalette.swift refs/tdesktop
git -C refs/tdesktop diff --binary -- . ':!Telegram/lib_ui' > patches/tdesktop.patch
git -C refs/tdesktop/Telegram/lib_ui diff --binary > patches/lib_ui.patch
```
