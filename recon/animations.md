# Animations — Telegram for macOS 13.1

Пути относительно `refs/Telegram-macOS/packages/`. Полный автоматический список всех 2421 вызова — `animations-inventory.md`. Здесь — ключевые сценарии, вручную разобранные по коду.

Колонка **«замерено по видео»**: записи экрана в этом заходе не сделаны (нет разрешения «Запись экрана», см. `INDEX.md`) — помечено `—`. Код читался напрямую, поэтому значения из кода точные; видео нужно только для проверки ощущения кривой `.spring` (см. §0.3).

## 0. Примитивы (переносить в `anim::` tdesktop в первую очередь)

### 0.1 Кривые
| Имя в коде | Что это | Для Qt | Ссылка |
|---|---|---|---|
| `.easeOut` | CAMediaTimingFunction easeOut = cubic-bezier(0, 0, 0.58, 1) | `anim::easeOutCubic`-подобная; точнее — bezier(0,0,0.58,1) | `TGUIKit/Sources/CAAnimationUtils.swift:478` |
| `.easeInEaseOut` / `.easeInOut` | bezier(0.42, 0, 0.58, 1) | bezier(0.42,0,0.58,1) | `TGUIKit/Sources/ContainableController.swift:17-19` |
| `.linear` | linear | `anim::linear` | |
| **`.spring`** | Псевдо-имя `"CAAnimationUtilsSpringCurve"`. Для CA-анимаций: `CASpringAnimation(mass 3, stiffness 1000, damping 500, v0 0)`, `duration 0.5`, затем `speed = 0.5 / requestedDuration` (т.е. растягивается/сжимается до запрошенной длительности). Для ручных (display-link) переходов: **bezier(0.23, 1.0, 0.32, 1.0)** | **bezier(0.23, 1, 0.32, 1)** (`listViewAnimationCurveSystem`) | `CAAnimationUtils.swift:28-60, 76-100`; `ContainableController.swift:14-16, 40-46` |
| `springBounce` | `CASpringAnimation(mass 5, stiffness 900, damping 88 (параметр), v0)`, duration = settlingDuration, speed масштабируется на запрошенную длительность | damped spring ω0=13.4, ζ=0.656 (перелёт ~5%) | `CAAnimationUtils.swift:62-71` |
| `animateScaleSpring(bounce: true)` | springBounce на `transform` | | `CAAnimationUtils.swift:211-253` |
| `animateScaleSpring(bounce: false)` | `.spring` на `transform` | | там же |
| Split trailing panel | bezier(0.25, 0.8, 0.25, 1.0), 0.3 s | | `TGUIKit/Sources/TGSplitView.swift:271` |
| Голос: горизонталь | bezier(0.23, 1.0, 0.32, 1.0) | | `ChatUI/Sources/ChatUI/ChatVoiceSendFlight.swift:10` |
| Голос: вертикаль | bezier(0.199, 0.0106, 0.279, 0.910) | | `ChatVoiceSendFlight.swift:11` |

### 0.2 Дефолтные длительности хелперов
- `view.change(pos/size/opacity:)`, `_change(...)`: **0.2 s, easeOut** (`TGUIKit/Sources/View.swift:461-468`, `Extensions.swift:852-982`).
- `layer.animatePosition / animateBounds`: 0.2 s easeOut (`CAAnimationUtils.swift:522-540`).
- `animateAlpha`: easeOut по умолчанию (`CAAnimationUtils.swift:478`).
- `animateScale*`: easeInEaseOut по умолчанию (`CAAnimationUtils.swift:291-518`).
- `ViewController.animationStyle` (push/pop): **0.4 s `.spring`** (`TGUIKit/Sources/ViewController.swift:531`).
- `Popover.animationStyle`: 0.2 s `.spring` (`TGUIKit/Sources/Popover.swift:49`).
- `TableView` вставки/удаления: 0.2 s easeOut (`TGUIKit/Sources/TableView.swift:19, 2640-2641`).
- Топ длительностей по всему коду: 0.2 (648 вызовов) ≫ 0.3 (84) > 0.25 (61) > 0.35/0.4 (46) > 0.5 (22) > 0.15 (20) > 0.18 (13). Топ кривых: `.spring` (152) > `.easeOut` (105) > `.easeInEaseOut` (37) > `.linear` (23). → **Правило по умолчанию для порта: 200 мс easeOut; навигация/модалки/морфы — spring-кривая bezier(0.23,1,0.32,1).**

### 0.3 Пружины (численно, `recon/tools/springs.py`)
ω0 = √(k/m), ζ = c / (2√(km)). x — доля пути.

| spring | ω0 | ζ | settle(0.1%) s | x@0.125s | x@0.25s | x@0.375s | x@0.5s |
|---|---|---|---|---|---|---|---|
| `.spring` m3 k1000 c500 | 18.26 | 4.564 | 1.500 | 0.214 | 0.390 | 0.526 | 0.632 |
| springBounce m5 k900 c88 | 13.42 | 0.656 | 0.772 | 0.625 | 1.036 | 1.049 | 1.006 |
| Отправка текста, вертикаль m1 k272 c33 | 16.49 | 1.000 | 0.561 | 0.611 | 0.917 | 0.985 | 0.998 |
| Кнопка send (поле) m1 k555.027 c47.118 | 23.56 | 1.000 | 0.393 | 0.793 | 0.981 | 0.999 | 1.000 |
| Switch (response 0.47, ζ 0.7) | 13.37 | 0.700 | 0.769 | 0.603 | 1.006 | 1.039 | 1.008 |

⚠ **Расхождение под проверку видео:** по классической физике `.spring` (m3/k1000/c500) за свои 0.5 s проходит только 63% и в конце «прыгает» — на экране такого нет. Код сам для `.spring` в ручных переходах использует bezier(0.23,1,0.32,1) (`ContainableController.swift:14-16, 44-45`), это же значение у iOS-клиента для «системной» кривой. **Для порта брать bezier(0.23, 1, 0.32, 1).** Проверить одной записью push/pop (см. CHECKLIST, ручные задачи).

Таблица сравнения кривых (t/T → прогресс):

| t/T | CASpring 3/1000/500 | bezier(0.23,1,0.32,1) | easeOut | easeInOut |
|---|---|---|---|---|
| 0.1 | 0.085 | 0.398 | 0.161 | 0.020 |
| 0.2 | 0.173 | 0.682 | 0.308 | 0.082 |
| 0.3 | 0.253 | 0.843 | 0.445 | 0.187 |
| 0.4 | 0.325 | 0.925 | 0.571 | 0.332 |
| 0.5 | 0.390 | 0.966 | 0.685 | 0.500 |
| 0.6 | 0.449 | 0.986 | 0.785 | 0.668 |
| 0.7 | 0.502 | 0.995 | 0.870 | 0.813 |
| 0.8 | 0.550 | 0.999 | 0.938 | 0.918 |
| 0.9 | 0.593 | 1.000 | 0.983 | 0.980 |

### 0.4 Аналитические пружины (ω, ζ) — меню и модалки-морфы
x(t) при ζ<1: `1 − e^(−ζωt)(cos ωd t + ζω/ωd sin ωd t)`, ωd = ω√(1−ζ²); при ζ=1: `1 − (1+ωt)e^(−ωt)`. Длительность = время, после которого |остаток| ≤ tolerance, с шагом 1/120 s.

| Пружина | ω | ζ | Ссылка |
|---|---|---|---|
| Меню: открытие (scale, alpha, cornerRadius) | 20.0 | 0.84 | `TGUIKit/Sources/AppMenuController.swift:15-38` (settling: tol 0.002, min 0.2, max 0.7 s) |
| Модалка-морф: open position | 20.5 | 0.82 | `TGUIKit/Sources/ModalMorphTransition.swift:28` |
| open width / height | 22.0 / 19.0 | 0.74 / 0.76 | `:29-30` |
| open fade | 21.0 | 1.0 | `:31` |
| close position / width / height / fade | 22 / 23 / 21 / 23.5 | 1.0 | `:32-35` |
| Морф: maxDuration 1.5 s, sampleRate 120 Hz, geom tol 0.2pt, unit tol 0.002 | | | `:16-19` |

## 1. Ключевые сценарии

| # | Элемент / триггер | Длительность | Кривая / пружина | Delay | Что анимируется | Ссылка | Замерено по видео |
|---|---|---|---|---|---|---|---|
| A1 | **Открытие чата** из списка, layout **dual** | 0 (мгновенно) | — | — | правая колонка заменяется без анимации; плашка выделения в списке переезжает | `ChatListUI/Sources/ChatListUI/PeersListController.swift:3463-3465` (`animated = layout == .single`) | — |
| A2 | Плашка выделения в списке → другая строка/размер | 0.2 | easeOut | — | bounds + position плашки (с presentation-значения, прерываемо); появление: alpha 0→1 0.2 | `ChatListRowView.swift:714-730, 1636-1642` | — |
| A3 | **Push** навигации (чат в single, настройки, профиль) | 0.4 × (1 + slotLeadingInset/width) | `.spring` → bezier(0.23,1,0.32,1) | — | новый: x от `width` → 0; старый: x 0 → −round(width/3) (параллакс 1/3); backdrop нового alpha 0→1 за 1/3 длительности | `TGUIKit/Sources/NavigationViewController.swift:562-568, 1040-1100, 1186-1232`; `ViewController.swift:531` | — |
| A4 | **Pop** (кнопка назад / Esc) | то же | то же | — | текущий: x 0 → width; предыдущий: −width/3 → 0; backdrop старого 1→0 за 1/3 | `NavigationViewController.swift:1079-1099, 1229-1231` | — |
| A5 | Свайп «назад» трекпадом | интерактив; отпускание — `animationStyle` (0.4 spring), alpha за 0.2 | следует за пальцем, предыдущий двигается с делителем 3 (полный слайд — 1) | — | x обоих контейнеров | `NavigationViewController.swift:1436-1570` | — |
| A6 | Хедеры навбара (закреп, звонок, плеер) show/hide | 0.2 | easeOut | — | y (въезд сверху), frame | `NavigationViewController.swift:104-162, 612-613` | — |
| B1 | **Отправка текста** («полёт» из поля в пузырь) | горизонт 0.185; вертикаль — пружина до settle (~0.56 s) | горизонт: easeInEaseOut; вертикаль: spring m1 k272 c33 (крит. демпф.) | вертикаль +0.07 | маска-пузырь растёт от рамки поля до пузыря (x/w — горизонт., y/h — вертикал.); снимок текста из поля alpha 1→0 за 0.1; пузырь alpha 0→1 0.1; текст пузыря alpha 0→1 0.08; время/галочки alpha 0→1 0.25 + сдвиг по x; превью ссылки — вертикальный сдвиг | `ChatUI/Sources/ChatUI/ChatTextSendFlight.swift:8-13, 200-319` | — |
| B2 | Отправка медиа (полёт превью) | 0.185 / пружина | то же | — | transform scale + position; припаркованное превью alpha 1→0 0.15 | `ChatMediaSendFlight.swift:170, 290-354` | — |
| B3 | Отправка голосового | 0.3; fade 0.06 | X: bezier(0.23,1,0.32,1); Y и scale: bezier(0.199,0.011,0.279,0.910) | — | позиция + scale от кнопки записи в пузырь; оверлей записи scaleSpring 1→0.1 0.3 (bounce off) + alpha 0.18 | `ChatVoiceSendFlight.swift:6-11, 110-230` | — |
| B4 | **Появление нового сообщения** (входящее или после отправки без полёта) | 0.2 | easeOut | — | все строки ниже точки вставки сдвигаются (additive y от −height), новая строка alpha 0→1; contentView bounds 0.2 easeOut | `TGUIKit/Sources/TableAnimationInterface.swift:77-138` | — |
| B5 | Кнопка send ↔ voice ↔ edit (морф иконки) | 0.2 (иконка), появление в поле: fade 0.08 + spring m1 k555 c47.1 (~0.39 s), blur 6→0 за 0.15 | spring | — | scale 0.2/0.1 → 1, alpha, blur, «самолётик» улетает на (−22, 18) | `ChatUI/Sources/ChatUI/ChatInputSendButton.swift:110-122, 440-560` | — |
| B6 | Поле ввода: стекло-морф (ответ/редактирование панели) | 0.22 | easeOut; fade out 0.08 / in 0.12 | — | frame контейнера ввода | `ChatUI/Sources/ChatUI/ChatInputView.swift:709-712` | — |
| B7 | Авто-рост поля ввода при наборе | 0.2 | easeOut | — | высота поля и сдвиг истории (TableView.change(size)) | `TGUIKit/Sources/TableView.swift:4196-4221`; `ChatInputView.swift:300-310` | — |
| C1 | **Пузырь/хвост** | статичный | — | — | хвост рисуется только у последнего в группе; при перегруппировке пузырь перерисовывается (без морфа) | `TelegramTheme/.../ChatMessageBubbleImages.swift:20-130` | — |
| C2 | **Реакции**: появление чипа под сообщением | 0.2 | scaleSpring(bounce) 0.2→1 + alpha easeOut | — | scale, alpha; соседи сдвигаются position 0.2 easeOut (additive); новые — сдвиг от x=index·12 | `ChatUI/Sources/ChatUI/ChatReactionsView.swift:1269-1303, 1722-1756` | — |
| C3 | Реакции: удаление чипа | 0.2 | alpha easeOut + scaleSpring 1→0.2 | — | | `ChatReactionsView.swift:1269-1272` | — |
| C4 | Реакции: фон «выбрано» | 0.3 / 0.2 | scaleSpring 0.1→1 / alpha | — | | `ChatReactionsView.swift:1334-1344` | — |
| C5 | Быстрая реакция (hover-кнопка у сообщения) удержание | 0.8 (hold) | scale 1→1.5; отпускание 0.2 →1; клик 1→0.8→1 по 0.2 | — | scale | `ChatUI/Sources/ChatUI/AddReactionManager.swift:21, 242-320` | — |
| C6 | Панель реакций: появление иконок | 0.35 | scaleSpring bounce 0.1→1 | — | | `AddReactionManager.swift:352` | — |
| C7 | Панель реакций: загрузка (точки) | вход 0.25 spring; цикл 0.7 ∞ | easeInEaseOut | 0.25 + i·0.08 | translation.y [0,3,0] | `AddReactionManager.swift:405-425` | — |
| D1 | **Свайп-ответ** (трекпад влево на сообщении) | интерактив; возврат 0.2 easeOut | — | — | строка сдвигается за пальцем; справа кнопка 33×33 с круговым прогрессом (порог **100 pt**, reveal 40); при успехе кольцо r35, lineWidth 2→18 за 0.3 linear | `ChatUI/Sources/ChatUI/ChatRowView.swift:23-30, 100-190, 2798-2890` | — |
| E1 | **Контекстное меню** (AppMenu) открытие | settling пружины ω20 ζ0.84 (≈0.3–0.45 s, клип 0.2–0.7) | keyframes на 120 Hz | — | scale от якоря-курсора 0.42→1, alpha = smoothstep(0, 0.35, openness), cornerRadius пилюля→18 | `TGUIKit/Sources/AppMenuController.swift:15-38, 138-206` | — |
| E2 | Контекстное меню: закрытие | 0.2 | easeOut | — | alpha 1→0 | `AppMenuController.swift:641-660` | — |
| E3 | Подменю: появление/скрытие | 0.2 / 0.28 | alpha 0.1→1 + scaleSpringFrom(anchor) 0.2→1 bounce, 0.28 | — | | `AppMenuController.swift:807, 947-967` | — |
| F1 | **Поповер** показ | 0.4 (scale), 0.2 (alpha) | scaleSpringFrom(anchor) 0.1→1 без bounce (= `.spring`) | — | scale от точки-якоря, alpha | `TGUIKit/Sources/Popover.swift:285-301` | — |
| F2 | Поповер скрытие | 0.15 | easeOut | — | alpha | `Popover.swift:451` | — |
| F3 | **Тултип** показ/скрытие | 0.2 / 0.2 | easeOut | — | alpha 0.3→1 / 1→0; при смене размера cornerRadius 0.2 | `TGUIKit/Sources/TooltipController.swift:115, 258-275` | — |
| G1 | **Модалка** показ (bottomToCenter, дефолт) | 0.25 alpha; position — `.spring` 0.2 | spring | — | container alpha 0.1→1, y +100 → 0; фон-затемнение alpha 0→1 0.15 | `TGUIKit/Sources/Modal.swift:1715-1761, 1845` | — |
| G2 | Модалка: scaleCenter | 0.35 | springBounce 0.5→1 | — | | `Modal.swift:1735` | — |
| G3 | Модалка: морф из кнопки/пункта меню | пружины §0.4 (до 1.5 s) | ω/ζ | — | position/width/height/fade; dim 0.4 easeOut | `TGUIKit/Sources/ModalMorphTransition.swift:13-120`; `Modal.swift:1513-1530` | — |
| G4 | Модалка: закрытие | 0.25 | `.spring` alpha + фон 0.25 | — | | `Modal.swift:1577-1590` | — |
| G5 | Модалка: смена размера контента | 0.25 | `.spring` | — | position + scaleX/Y | `Modal.swift:1615-1617` | — |
| H1 | **Переключение папок** (табы сверху) | 0.4 | `.spring` | — | индикатор/таб: frame + transform | `TGUIKit/Sources/TabBarView.swift:478-601` | — |
| H2 | Папки: скролл-сегмент (табы-капсулы) | 0.2 | easeOut | — | | `TGUIKit/Sources/ScrollableSegmentView.swift:443-648` | — |
| H3 | Сайдбар папок (вертикальный) появление | resize окна + split | см. layout §2 | — | | `Telegram-Mac/app/ApplicationContext.swift:958-1010` | — |
| H4 | Правая панель (эмодзи/стикеры/GIF) | 0.3 | bezier(0.25, 0.8, 0.25, 1.0) (display link) | — | ширина trailing-панели | `TGUIKit/Sources/TGSplitView.swift:260-290` | — |
| I1 | **Выделение сообщений** (чекбокс) | 0.3 scale / 0.2 alpha | scaleSpring 0.2↔1 (bounce) | — | галочка | `TGUIKit/Sources/SelectingControl.swift:65-80` | — |
| J1 | **Кнопка «вниз»** show/hide | 0.2 | easeOut | — | alpha + frame (вместе с mentions/reactions-кнопками) | `ChatUI/Sources/ChatUI/ChatController.swift:895-915` | — |
| K1 | **Индикатор «печатает»** (3 точки) | цикл 0.7 s, 42 кадра, ∞ | keyframes | смещения фаз 0.4/0.2/0.0 | радиус и alpha (0.75→1) точек; шаг 6pt | `ShortPeerRow/Sources/ShortPeerRow/ChatActivitiesModel.swift:121-160`; `TelegramTheme/.../ThumbUtils.swift:301-316` | — |
| K2 | «записывает голосовое» / «загружает» / «выбирает стикер» | 0.7 / 1.75 / 2.0 цикл | keyframes | | | `ChatActivitiesModel.swift:66-112` | — |
| L1 | **Запись голосового**: оверлей кнопки | 0.4 / 0.2 | scaleSpring 0.1→1 (bounce) + alpha | — | | `ChatUI/Sources/ChatUI/ChatInputRecordingView.swift:217-218` | — |
| L2 | Запись: блоб (волна громкости) | presence in 0.35 / out 0.15; уровень сглаживание 0.9 | собственная (`ChatRecordingBlobMotion`) | — | scale волн 0.627…1.18, centre 0.45 | `ChatUI/Sources/ChatUI/ChatRecordingBlobMotion.swift:6-20` | — |
| L3 | Запись: плавающие контролы (lock, pause) | 0.3 | `.spring` | — | layout | `ChatInputRecordingView.swift:687, 817` | — |
| L4 | Запись: отмена | 0.3 | scaleSpring 1→0.1 no-bounce + fade `.spring` | — | | `ChatInputRecordingView.swift:571-603` | — |
| M1 | **Медиа-вьювер** открытие | 0.25 | `.spring` | — | морф из миниатюры: position + scaleX/Y от rect миниатюры; alpha новой за 0.125; фон `_change(opacity:1)` 0.2 easeOut; контролы animateIn | `GalleryUI/Sources/GalleryUI/GalleryPageController.swift:1425-1450`; `GalleryViewer.swift:1661-1710` | — |
| M2 | Медиа-вьювер закрытие (Esc/клик/жест) | 0.25 | `.spring` | — | обратный морф в миниатюру; фон 0.2 | `GalleryViewer.swift:1722-1740` | — |
| M3 | Вьювер: прогресс/смена слайда | 0.25 linear / 0.2 | | — | alpha | `GalleryPageController.swift:188, 1015, 1063, 1139` | — |
| N1 | **Смена темы** | 0.2 | easeOut | — | снимок окна поверх, alpha 1→0 (кроссфейд) | `TelegramTheme/Sources/TelegramTheme/Appearance.swift:2239-2260` | — |
| O1 | **Поиск** (поле): кнопка очистки, теги | 0.2 | `.spring`/easeOut (`animationStyle`) | — | alpha; теги scaleSpring 1→0.3 + alpha | `TGUIKit/Sources/SearchView.swift:150-220, 600-655` | — |
| P1 | **Switch** (тумблер) | пружина response 0.47, ζ 0.7 (~0.99 s settle); нажатие 0.2 easeInOut | CASpring | — | позиция кружка, «линза» (liquid glass) | `TGUIKit/Sources/SwitchView.swift:50-90, 385-410` | — |
| Q1 | Hover-состояния (строки, кнопки) | 0.2 (типично) | easeOut | — | фон плашки alpha | `TGUIKit/Sources/Control.swift`, `ChatListRowView.swift:1636-1642` | — |
| R1 | Лоадер-спиннер (InfiniteProgressView) | strokeEnd 0→1 1.25 + strokeStart 0→1 1.25 в группе 2.5 ∞; вращение 1.5 s ∞; появление 0.2 | linear | — | stroke, rotation.z (старт π+0.58) | `TGUIKit/Sources/InfiniteProgressView.swift:91-150` | — |
| R1b | Радиальный прогресс загрузки | flow 0.4 × max(0.35, остаток) | curve параметр | — | strokeEnd | `TGUIKit/Sources/RadialProgressView.swift:331, 529` | — |
| R2 | Шиммер (скелетоны) | см. ShimmerLayer | | | | `TGUIKit/Sources/ShimmerLayer.swift` | — |
| S1 | Скролл к сообщению / вверх-вниз по ⌘↑↓ | 0.35 | linear (clipView.scroll) | — | | `TGUIKit/Sources/TableView.swift:2205-2212` | — |
| S2 | Скролл таблицы к состоянию (scroll to unread и т.п.) | по умолчанию `.spring` | spring | — | | `TableView.swift:4225` | — |
| T1 | Звонки (окно звонка) | см. `CallVideoLayer/Sources/CallWindowTransition.swift`, `PrivateCallScreen` | | | | inventory: CallVideoLayer / PrivateCallScreen | — |
| U1 | Пустое состояние таблицы | 0.2 | easeOut | — | alpha | `TableView.swift:4015-4041` | — |

### Bounce / rubber band
- Скролл списков — системный NSScrollView (инерция и rubber band — штатные macOS; для Qt нужно эмулировать: kinetic + overscroll с пружиной).
- Явные bounce: springBounce (ζ≈0.66) в реакциях, чекбоксах, модалке scaleCenter, подменю.
