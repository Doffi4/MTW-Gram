# Layout — Telegram for macOS 13.1

Все размеры в pt. Пути относительно `refs/Telegram-macOS/`. Схемы с подписанными размерами — `recon/measure/*.png` (сгенерированы из этих чисел скриптом `recon/tools/measure.py`).

## 1. Окно

| Параметр | Значение | Ссылка |
|---|---|---|
| Минимальный размер окна (авторизован) | **380 × 550** | `Telegram-Mac/app/ApplicationContext.swift:177, 391` |
| Мин. размер на экранах логина | 400 × 550 | `Telegram-Mac/app/AppDelegate.swift:492, 612` |
| Мин. ширина при видимом сайдбаре папок | 380 + 90 = 470 (+ ещё, если режим minimisize) | `ApplicationContext.swift:1074-1084` |
| Позиция/размер | сохраняется (`WindowSaver`) | `packages/TGUIKit/Sources/WindowSaver.swift` |
| Titlebar (`ChromeMode.standard`) | `fullSizeContentView`, titlebar прозрачный, заголовок скрыт; traffic lights поверх контента со сдвигом **(15, 8)** у главного окна, (10, 6) у прочих; на macOS 26 — пустой NSToolbar без разделителя. Перетаскивание окна — за шапки (navbar 64) | `packages/TGUIKit/Sources/Window.swift:338-362` |

## 2. Колонки (split view)

```
[ Folder sidebar 90 ] [ Chat list  w = 300 (drag 300…W−380) ] [ Chat  ≥380 ] [ Entertainment 358 (опц.) ]
```

| Параметр | Значение | Ссылка |
|---|---|---|
| Ширина списка чатов по умолчанию | **300** (`FastSettings.leftColumnWidth`, сохраняется) | `packages/InAppSettings/Sources/InAppSettings/FastSettings.swift:665` |
| Drag-resize списка | `clamp(x, 300, windowWidth − 380 − fixedLeading)`, round | `ApplicationContext.swift:1136-1145` |
| Курсор разделителя | `resizeLeftRight`; если справа ≤380 — `resizeLeft`; в свёрнутом — `resizeRight` | `ApplicationContext.swift:1125-1134` |
| Мин. ширина колонки чата | **380** | `ApplicationContext.swift:1153` |
| Сайдбар папок (вертикальные папки) | **90**, фиксированный | `ApplicationContext.swift:223, 1003` |
| Свёрнутый список чатов («minimisize») | **90** — только аватары; строки по 70, плашка выделения = аватар ±7 | `ApplicationContext.swift:1187-1195`; `ChatListRowView.swift:3333` |
| Правая панель (стикеры/эмодзи/GIF, «Entertainment») | 358, появляется справа, анимация 0.3 s, кривая (0.25, 0.8, 0.25, 1.0) | `packages/EntertainmentUI/.../EntertainmentSidebarController.swift:65`; `TGSplitView.swift:271` |

**Стадии при сужении** (`packages/TGUIKit/Sources/TGSplitView.swift:458-487`, пропорции `ApplicationContext.swift:399`: dual = min 650 / max 1250):
1. **dual** — ширина основной области ≥ 650: список + чат.
2. **minimisize** — если пользователь утащил разделитель влево до x ≤ 100 (`TGSplitView.swift:85-90`): список сжимается в 90 pt (только аватары), состояние запоминается (`FastSettings.isMinimisize`).
3. **single** — ширина < 650: одна колонка, чат пушится поверх списка как навигация (push/pop со свайпом назад).

Отступы панелей («плавающий» дизайн 13.x): в dual/minimisize `leftController.insets = (top 8, left 8, bottom 8, right 0)`; в single с сайдбаром — 8 со всех сторон. `ApplicationContext.swift:1164-1190`.

## 3. Шапки

| Элемент | Значение | Ссылка |
|---|---|---|
| Высота navbar (шапка чата/списка/настроек) | **64** | `packages/TGUIKit/Sources/NavigationBarView.swift:17` |
| Заголовок чата | medium 15; статус normal 12 | `packages/ChatUI/Sources/ChatUI/ChatTitleBarView.swift:28, 782` |
| Show/hide доп. хедеров (закреп, звонок, плеер) | slide по Y, 0.2 easeOut | `packages/TGUIKit/Sources/NavigationViewController.swift:129-162` |

## 4. Список чатов — строка

| Параметр | Значение | Ссылка |
|---|---|---|
| Высота | 70 | `packages/ChatListUI/Sources/ChatListUI/ChatListRowItem.swift:2638-2656` |
| Аватар | 50×50 @ x10 y10 | `ChatListRowView.swift:1188, 1546` |
| Начало текста (leftInset) | 70 | `ChatListRowItem.swift:1382-1396` |
| margin (верх/право) | 9 | `ChatListRowItem.swift:1192` |
| Имя | y = margin − 1 | `ChatListRowView.swift:3433` |
| Превью | y = высота имени + margin + 1 | `ChatListRowView.swift:3518` |
| Дата / статус-галочки | справа, y = margin + 2 | `ChatListRowView.swift:1510-1527` |
| Бейдж / иконка закрепа | справа снизу, `frame.width − w − margin` | `ChatListRowView.swift:1466, 3241` |
| Разделитель | 1pt, от x=70 до края (у последнего закреплённого — во всю ширину) | `ChatListRowView.swift:1459` |
| Плашка выделения | inset 3 со всех сторон, radius 14 continuous, цвет `chatList.selectedBackgroundColor` (single-layout: `singleLayoutSelectedBackgroundColor`) | `ChatListRowView.swift:701, 1395-1420, 3330-3341` |
| Теги папок под превью | y = h − tagH − 7, bold 10 UPPERCASE | `ChatListRowView.swift:3529`; `ChatListRowItem.swift:859` |

## 5. Чат

### 5.1 Колонка и отступы

| Параметр | Значение | Ссылка |
|---|---|---|
| leftInset строки | 13 (+36 при наличии аватара в группе) | `packages/ChatUI/Sources/ChatUI/ChatRowItem.swift:288-299, 692-712` |
| rightInset | 12 (в режиме выделения без пузырей 44) | `ChatRowItem.swift:281-287` |
| topInset | 2 | `ChatRowItem.swift:270` |
| Отступ контента сверху | 10 (пузыри) / 6 (список) | `ChatRowItem.swift:273-279` |
| Макс. ширина контента пузыря | `min(width − contentOffset.x − bubbleInnerInset − 36 − 20 [−35 если share] [−35 если like], 450)` | `ChatRowItem.swift:320-345` (`min_block_width = 450`) |
| Внутренний отступ пузыря | `bubbleContentInset` 11 по бокам; +`additionBubbleInset` 6 со стороны хвоста | `ChatRowItem.swift:3306-3312` |
| Отступ контент ↔ время | 10 | `ChatRowItem.swift:3314` |
| Время в пузыре | правый нижний угол, y = bubble.maxY − h − 6 | `ChatRowGeometry.swift:52-80` |
| Default inner inset (без пузырей) | 7 | `ChatRowItem.swift:518-524` |

### 5.2 Пузыри
- Радиусы: 16 главный / 8 на стыке группы. Правила по позиции (`ChatMessageBubbleImages.swift:20-75`, маппинг `ChatRowItem.swift:1549-1558`):

| Позиция в группе | neighbors | TL | TR | BL | BR | хвост |
|---|---|---|---|---|---|---|
| одиночное | none | 16 | 16 | 16 | 16 | да |
| первое (ниже есть) | top | 16 | 16 | 16 | 8 | нет |
| среднее | both | 16 | 8 | 16 | 8 | нет |
| последнее | bottom | 16 | 8 | 16 | 16 | да |
| (для outgoing; incoming — зеркально по горизонтали) | | | | | | |

- Хвост: ширина 6, рисуется только у последнего в группе; форма — квадратичные кривые по эллипсам (см. tokens §2).
- Группировка: тот же автор и разница во времени < **10 мин** (`simpleDif = 10*60`), `packages/ChatHistoryModel/Sources/ChatHistoryModel/ChatEntryTypes.swift:3`, `ChatHistoryEntry.swift:1107`. Каналы не группируются (всегда Full).
- Исходящие справа (`x = rowWidth − w − leftInset`), входящие слева. `ChatRowGeometry.swift:41-47`.

### 5.3 Дата-разделитель
Высота строки 30; «пилюля» по центру, ширина = текст + 16, высота = текст + 6, radius = h/2, стекло/блюр; липнет к верху при скролле (stick header). `packages/ChatUI/Sources/ChatUI/ChatMessageDateHeader.swift:180, 511-515`.

### 5.4 Поле ввода
| Параметр | Значение | Ссылка |
|---|---|---|
| Контейнер | плавающее стекло, radius **20**, тень+рамка | `packages/ChatUI/Sources/ChatUI/ChatInputStateContainers.swift:55-59` |
| Мин. высота текстового поля | 40 | `packages/InputTextView/Sources/InputTextView/UIInputView.swift:93` |
| Макс. высота (авто-рост) | `superview.height / 2 + 50` | `ChatInputView.swift:2030` |
| Отступ снизу | 12 (`inputBottomInset`); bottomPadding 10 | `ChatInputView.swift:622, 1050` |
| Мин. перекрытие истории полем | 40; зазор сообщение↔поле 20; compact 12 | `ChatRowItem.swift:49-52` |
| Кнопка отправки | 40×32, inset 4, gap до текста 6; voice ↔ send морф | `ChatInputSendButton.swift:110-122` |
| Кнопка «вниз» (scroll-to-bottom) | справа, y = над полем ввода +6 | `ChatController.swift:1451` |

### 5.5 Медиа/стикеры/эмодзи
- Альбомы: `packages/ChatUI/Sources/ChatUI/GroupedLayout.swift` (мозаика, как на iOS).
- Большие эмодзи (1–3 эмодзи без текста): `BigEmojiMessage.swift`, без пузыря, время в овальной плашке.
- Стикеры: без пузыря, `ChatAnimatedStickerMediaLayoutParameters.swift`.
- Превью ссылок: `ChatUrlPreviewModel.swift`, `WPLayout` — блок с цветной левой линией (BlockQuoteLine) внутри пузыря.

## 6. Настройки

- Строки в группах «modern»: radius 20, inner insets 12/14, max ширина блока 600, центрирование. `packages/GeneralRows/Sources/GeneralRows/GeneralRowItem.swift:160-230, 436-447`, `GeneralRowView.swift:128`.
- Высота строки по умолчанию 40. Строка с аватаром (ShortPeerRow) 50, аватар 36.

## 7. Меню, поповеры, тултипы
- Контекстное меню (AppMenu): radius 18, строка 28, текст medium 13, плашка hover radius 5. `packages/TGUIKit/Sources/AppMenuController.swift:112`, `AppMenuRowItem.swift:149-339`.
- Поповеры: `Popover.swift`, scale из точки-якоря.
- Тултипы: `TooltipController.swift`, radius анимируется.
