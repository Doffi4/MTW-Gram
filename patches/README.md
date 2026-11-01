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

Цвета генерирует `tools/mac_palette.py` из `ColorPalette.swift` Telegram-macOS; после изменения сопоставления — перезапустить его и пересоздать патчи:

```
python -I tools/mac_palette.py <Telegram-macOS>/packages/ColorPalette/Sources/ColorPalette/ColorPalette.swift refs/tdesktop
git -C refs/tdesktop diff --binary -- . ':!Telegram/lib_ui' > patches/tdesktop.patch
git -C refs/tdesktop/Telegram/lib_ui diff --binary > patches/lib_ui.patch
```
