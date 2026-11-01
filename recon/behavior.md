# Behavior — Telegram for macOS 13.1

Пути относительно `refs/Telegram-macOS/`. На Windows ⌘ → Ctrl, ⌥ → Alt.

## 1. Горячие клавиши

Каноничный список, который клиент сам показывает пользователю: **⌘/** → `ShortcutListController` (`Telegram-Mac/app/ApplicationContext.swift:822`). Полная сырая выгрузка всех регистраций (139 шт.) — `recon/hotkeys-raw.txt` (клавиша | модификаторы | file:line | тело обработчика).

### 1.1 Глобальные (окно)
| Клавиша | Действие | Ссылка |
|---|---|---|
| ⌘K | Quick Switcher (поиск чатов) | `Telegram-Mac/Base.lproj/MainMenu.xib` |
| ⌘, | Настройки | MainMenu.xib |
| ⌘F | Глобальный поиск (в пустом состоянии) / поиск по чату (в чате) | `packages/WidgetUI/.../EmptyChatViewController.swift:218`; `packages/ChatUI/Sources/ChatUI/ChatController.swift:11014` |
| ⇧⌘F | (глобальный обработчик) | `ApplicationContext.swift:817` |
| ⌘0 | Saved Messages | `ApplicationContext.swift:586` |
| ⌘1…⌘9 | Открыть N-й чат списка | `ApplicationContext.swift:592-632` |
| ⌥⌘1…⌥⌘9, ⌥⌘− | Открыть N-й чат (в отдельном/закреплённом режиме, `openChat(i, true)`) | `ApplicationContext.swift:662-707` |
| ⌃1…⌃9 | Переключить аккаунт | `ApplicationContext.swift:715-755` |
| ⇧⌘M | Переключатель аккаунтов (QuickSwitcher accounts) | `ApplicationContext.swift:762` |
| ⌃Tab / ⌃⇧Tab | Alt-tab по недавним чатам (оверлей), в списке — след./пред. чат | `ApplicationContext.swift:790-798`; `packages/ChatListUI/Sources/ChatListUI/PeersListController.swift:3634-3639` |
| ⌥↑ / ⌥↓ | Пред./след. чат в списке | `PeersListController.swift:3624` |
| ⌘L | Заблокировать (пасскод) | `ApplicationContext.swift:655` |
| ⌘/ | Список горячих клавиш | `ApplicationContext.swift:822` |
| ⌘W | Скрыть окно (не закрывать) | MainMenu.xib («Hide») |
| ⌘H / ⌥⌘H / ⌘Q / ⌘M / ⌃⌘F | Hide / Hide Others / Quit / Minimize / Full Screen | MainMenu.xib |

### 1.2 Чат и поле ввода
| Клавиша | Действие | Ссылка |
|---|---|---|
| ⌘↑ / ⌘↓ | Навигация по сообщениям/ответам (скролл 0.35 linear) | `ChatController.swift:10933-10961`; `TGUIKit/Sources/TableView.swift:2205` |
| ↑ (пустое поле) | Редактировать последнее своё (если нет — скролл вверх) | `packages/ChatUI/Sources/ChatUI/ChatController.swift:10870-10888` |
| Esc | Отмена ответа/редактирования → выход из выделения → закрыть чат (pop) | ⚠ не сверено построчно; обработчики Escape в `Window`/`NavigationViewController` |
| ⌘O | Прикрепить файл | `ChatController.swift:11020` |
| ⌘R | Начать запись голосового | `ChatController.swift:11066` |
| ⌘B / ⌘I / ⌘U | Жирный / курсив / ссылка | `ChatController.swift:11025-11060` |
| ⇧⌘U / ⇧⌘X / ⇧⌘P / ⇧⌘I / ⇧⌘K | Подчёркнутый / зачёркнутый / спойлер / цитата / моноширинный | `ChatController.swift:11030-11072` |
| ⌘\ | Снять форматирование | `ChatController.swift:11050` |
| ⌘Z / ⇧⌘Z | Undo/redo в поле (в т.ч. восстановление удалённого черновика) | `ChatInputView.swift:940-1001` |
| ⌘E (меню сообщения) | Редактировать | `ChatMessageMenuItems.swift:1126` |
| ⌘R (меню сообщения) | Ответить | `ChatMessageMenuItems.swift:802` |
| ⌘C / ⌘S | Копировать / сохранить медиа | `ChatMessageMenuItems.swift:461, 1465` |
| Enter / ⌘Enter | Отправить (переключатель в Settings → General) | `packages/SettingsUI/Sources/SettingsUI/GeneralSettingsViewController.swift`, `packages/InAppSettings/Sources/InAppSettings/FastSettings.swift` |

### 1.3 Медиа-вьювер
| Клавиша | Действие | Ссылка |
|---|---|---|
| ⌘S | Сохранить как | `packages/GalleryUI/Sources/GalleryUI/GalleryViewer.swift:468` |
| ⌘R | Повернуть влево | `GalleryViewer.swift:463` |
| ⌥⌘− / ⌥⌘= | Скорость видео −/+ | `GalleryViewer.swift:453-458` |
| ← → / Space / Esc | Пред./след., пауза, закрыть | GalleryViewer |

## 2. Контекстные меню

Иконки пунктов — **анимированные** (Lottie `.tgs`, `MenuAnimation.menu_*`, 191 файл в `Resources/tgs/menu_*.tgs` → скопированы в `recon/assets/source/Resources/tgs/`). Меню само — `AppMenu` (см. tokens/animations).

### 2.1 Сообщение (порядок в коде `packages/ChatUI/Sources/ChatUI/ChatMessageMenuItems.swift`)
Блок 1 (действия): **Reply** (`menu_reply`, ⌘R) · Send gift · Unvote/Stop poll · View stats · Delete option · View replies · Translate · Summarize · **Copy selected text / Copy text** (`menu_copy`, ⌘C) · Copy link · **Edit** (`menu_edit`, ⌘E) · Add task · **Pin/Unpin** · **Forward** (`menu_forward`) · Folders · Forward more · Share · **Select** (`menu_select_messages`)
Блок 2 (медиа): Save as (`menu_save_as`) · Remove/Save GIF · View sticker set · Add to favorites · Save ringtone · Copy media (⌘C) · Save media (⌘S)
Блок 3 (опасные): Fact check · **Report** (`menu_report`) · Cancel editing · **Delete** (`menu_delete`, красный)
Подвал: «edited/seen at …» (`menu_edited`), реакции-полоса сверху меню (если разрешены).
Строки: `ChatMessageMenuItems.swift:802-1587`.

### 2.2 Чат в списке
`packages/ChatListUI/Sources/ChatListUI/` — `ChatListRowItem.menuItems`: Open in new window · Pin/Unpin · Mute/Unmute (подменю с длительностями) · Mark as read/unread · Archive/Unarchive · Add to folder · Clear history · Delete. Свайп по строке влево/вправо открывает reveal-кнопки (pin/mute/archive/delete/read) с Lottie `anim_*.json` (`Resources/lottie/anim_pin.json` и т.д.).

### 2.3 Аватар / профиль
`packages/PeerInfoUI` — Open photo, Set as main, Save, Delete и т.п.

## 3. Drag & drop
- Файлы/изображения на окно чата → оверлей с двумя зонами («Send as file» / «Send compressed»), затем `PreviewSenderController` (`packages/PreviewSenderUI`).
- Drag строк в списке: переупорядочивание закреплённых (`ChatListRowView` `isResorting`, фон `activeDraggingBackgroundColor`), перетаскивание чата в папку сайдбара.
- Drag медиа из чата наружу (Finder) — поддерживается.

## 4. Скролл
- Системный NSScrollView: инерция и rubber band — штатные macOS (для Qt: эмулировать kinetic + overscroll-пружину; стандартный Qt этого не даёт).
- Скролл к сообщению/ответу: `TableView.scroll(to:)`, кривая по умолчанию `.spring` (`TGUIKit/Sources/TableView.swift:4225`); ⌘↑/⌘↓ — 0.35 s linear (`:2205-2212`).
- Открытие чата: позиция у первого непрочитанного с разделителем «Unread messages» (`ChatUnreadRowItem.swift`), иначе — низ.
- Кнопка «вниз» появляется при отрыве от низа; бейджи упоминаний/реакций над ней (`ChatController.swift:895-915, 1451, 1523`).
- Дата-пилюля липнет к верху (stick header) и прячется при остановке скролла.

## 5. Выделение текста и сообщений
- Выделение текста мышью — через несколько сообщений (`ChatSelectText.swift`, `ChatBubbleTextSelection.swift`); ⌘A в чате (`ChatSelectText.swift:742`).
- Режим выделения сообщений: чекбоксы слева (scaleSpring), нижняя панель действий (`MessageActionsPanelView.swift`); Shift+клик — диапазон; Esc — выход.

## 6. Курсоры
- Разделитель колонок: resizeLeftRight / resizeLeft (у минимума) / resizeRight (в свёрнутом) (`ApplicationContext.swift:1125-1134`).
- Ссылки/кнопки — pointingHand; текст — IBeam.

## 7. Звуки
Файлы: `recon/assets/source/Resources/audio`, `…/sounds`, `…/notifies` (уведомления 0–111.m4a).

| Звук | Когда | Ссылка |
|---|---|---|
| `sent` | отправка сообщения (если включено «Sent message sound») | `packages/ChatUI/Sources/ChatUI/SoundEffects.swift:23`; `Telegram-Mac/app/AppDelegate.swift:435` |
| `quiz-correct` / `quiz-incorrect` / `confetti` | ответ в викторине / конфетти | `SoundEffects.swift:17-21` |
| `begin_record.caf` | начало записи голосового | `Resources/audio` |
| `opening`, `voip_ringback`, `voip_connecting`, `voip_busy`, `voip_fail`, `voip_end` | звонки | `packages/TelegramCallsCore/.../PCallSession.swift:1344-1354` |
| `call up` / `call down` / `reconnecting` / `voip_group_unmuted` / `voip_group_recording_started` | групповые звонки | `packages/GroupCallScreenUI/.../GroupCallController.swift:1735-2116` |
| `Pop` / `Purr` | push-to-talk | `packages/PushToTalk/Sources/PushToTalk/PushToTalk.swift:509-513` |
| `notifies/N.m4a` | входящее уведомление (выбор в настройках) | `Resources/notifies` |

## 8. Окно, док, трей
- ⌘W скрывает окно, приложение остаётся (Dock). Клик по иконке в Dock возвращает окно.
- Бейдж Dock: число непрочитанных (`NSApplication.shared.dockTile.badgeLabel`), учитывает настройку «считать muted» (`packages/GeneralRows/Sources/GeneralRows/GlobalBadgeNode.swift:197-234`).
- Иконка в меню-баре (status item) опционально, с меню (`Telegram-Mac/account/SharedAccountContext.swift:145-229`). Аналог для Windows — tray.
- Перетаскивание окна — за шапки (fullSizeContentView).

## 9. Уведомления
- Системные `UNUserNotification` с ответом инлайн (Reply), Mark as read; превью текста скрывается при включённом пасскоде/настройке. `Telegram-Mac/utils/UNUserNotifications.swift`.
- In-app: тосты `showModalText` (снизу/по центру, авто-скрытие) — `packages/TGUIKit/Sources/Modal.swift`, `TooltipController.swift`.

## 10. Наблюдения на живом клиенте (13.1, скриншоты в `screens/`)
- Меню-бар (ru): **Telegram** (О Telegram · Настройки… ⌘, · Проверить обновления · Services · Быстрый поиск ⌘K · Скрыть ⌘W · Скрыть Telegram ⌘H · Скрыть все, кроме Telegram ⌥⌘H · Показать все · Закрыть Telegram ⌘Q); **Изменить** (Отмена · Повтор · Глобальный поиск · Вырезать · Копировать · Вставить · Вставить без форматирования · Удалить · Выбрать все · Орфография и грамматика · Автозамена · Преобразования); **Вид** (На полный экран); **Окно** (Свернуть ⌘M · Развернуть · Заполнить · Поместить в центре · Переместить и изменить размер ▸ · Плитка на весь экран ▸ · На передний план). `screens/80`, `81`.
- При ширине окна 380 (single) включается **compact chrome**: обычный titlebar с заголовком «Telegram @ <имя>», навбар с кнопкой «назад» (`Window.applyChrome(.compact)`, `packages/TGUIKit/Sources/Window.swift:338`). `screens/71`.
- Hover по строке списка чатов **не подсвечивает** строку (`screens/11`).
- Пустое состояние правой колонки — онбординг «Тема оформления / Оформление чата» с кнопками Назад/Дальше (`screens/14`).
- Контекстное меню сообщения: сверху отдельная «пилюля» с 7 быстрыми реакциями и стрелкой раскрытия, ниже меню (`screens/41`).
- При отключённой автосмене темы нельзя сменить тему без подтверждения — Telegram показывает alert «Ночной режим» (`screens/60`).
- Открытие медиа-вьювера на этом hackintosh (NVIDIA) роняет Telegram; после перезапуска в списке появляется баннер «Telegram неожиданно завершился — Отправьте отчёт» (`screens/15`, `42-*_tinted`).
