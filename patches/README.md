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
| `tdesktop.patch` | поле ввода: скруглённая капсула radius 20, отступ 8 по бокам / 4 сверху-снизу, рамка 1px цвета текста α0.12 (`ComposeControls.bgBorder: bool`, у сторис выключена), кнопки внутри — в `HistoryWidget` (`drawField`) и в `ComposeControls` (новые поля стиля `bgMargins`/`bgBorder`, сторис без изменений); не сделано: капсула «плавает» над историей (скролл под полем), панель ответа/редактирования остаётся полосой |
| `tdesktop.patch` | шапка чата: высота 64, заголовок 15 medium (`topBarNameStyle`), статус 12 (`topBarStatusFont`), без разделителя под шапкой (HistoryWidget, ChatWidget) |
| `tdesktop.patch` | левая колонка: шапка 48 с заголовком «Чаты» (15 medium) и кнопкой «новое» (меню: группа/канал/контакты), поиск-капсула 32 под ней (`dialogsMac*` в `dialogs.style`, `Widget::updateControlsGeometry`); архив — капсула «Архив ›» над списком вместо строки (`InnerWidget` всегда прячет строку архива); нижний таб-бар 48: контакты, звонки, чаты (бейдж непрочитанного), настройки = главное меню (гамбургер скрыт в широком режиме); в поиске лупа слева (`dialogsMacSearchIcon`, textMargins 32); в узком режиме (только аватарки) капсулы нет — строка архива возвращается по настройкам (`InnerWidget::setNarrowRatio`) |
| `tdesktop.patch` | «плавающая» колонка списка: в двух колонках `MainWidget` ставит `_dialogs` с отступами 8/8/8/0 (`dialogsMacPanelInset`), поля закрашены `windowBg`, поверх — слой `_dialogsPanel` со скруглением 12 и рамкой 1px (цвет текста α0.12, видна в любой теме); боковая тень обнулена; узкая колонка (только аватарки) и одна колонка — без отступов и рамки |
| `tdesktop.patch` | пузыри подряд: без тени (`msgShadow` 0), зазор 4px (`msgMarginTopAttached` 2, macOS `topInset`); бейдж вкладки «Чаты» на углу иконки, места на 5+ цифр |
| `lib_ui.patch` | кривые macOS в `anim::`: `cubicBezier`, `macSpring` (0.23,1,0.32,1), `macEaseOut`, `macEaseInOut`, `dampedSpring`, `macMenuSpring` (ω20 ζ0.84, 0.408 s); меню (`PanelAnimation`) раскрывается пружиной от 0.42 размера, альфа = smoothstep(0, 0.35, openness), показ 408 мс, скрытие 200 мс |
| `tdesktop.patch` | push/pop разделов (`Window::SlideAnimation`): `macSpring`, 400 мс, старый экран сдвигается на треть ширины |

Цвета генерирует `tools/mac_palette.py` из `ColorPalette.swift` Telegram-macOS; после изменения сопоставления — перезапустить его и пересоздать патчи:

```
python -I tools/mac_palette.py <Telegram-macOS>/packages/ColorPalette/Sources/ColorPalette/ColorPalette.swift refs/tdesktop
git -C refs/tdesktop diff --binary -- . ':!Telegram/lib_ui' > patches/tdesktop.patch
git -C refs/tdesktop/Telegram/lib_ui diff --binary > patches/lib_ui.patch
```
