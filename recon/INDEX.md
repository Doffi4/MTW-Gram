# Recon — оглавление

Telegram for macOS 13.1 (build 283357) + исходники `TelegramMessenger/Telegram-macOS`. Окружение — `VERSION.md`.

| Файл / папка | Что внутри |
|---|---|
| `VERSION.md` | версия клиента и исходников, macOS, экран (1x), тема, акцент |
| `tokens.md` | **все цвета по ролям** (110 ролей × Day / Day Classic / Dark / Tinted / System, с file:line), акценты, радиусы, размеры, высоты строк, шрифты (шкала + стили + метрики SF), тени/блюр/liquid glass |
| `layout.md` | окно, колонки и 3 стадии сужения, шапки, строка списка чатов, пузыри (радиусы по позиции, хвост, max width, группировка), дата-пилюля, поле ввода, настройки, меню |
| `animations.md` | примитивы (кривые, пружины с ω/ζ, дефолты хелперов) + ~50 ключевых сценариев: элемент, триггер, длительность, кривая, delay, что анимируется, ссылка |
| `animations-inventory.md` | авто-инвентарь **всех 2421** вызовов анимаций в коде, по пакетам, со статистикой |
| `behavior.md` | горячие клавиши, контекстные меню, drag&drop, скролл, выделение, курсоры, звуки, док/трей, уведомления |
| `hotkeys-raw.txt` | все 139 регистраций шорткатов: клавиша, модификаторы, file:line, тело обработчика |
| `screens/*.png` | 87 скриншотов живого клиента 13.1 (4 темы, 3 ширины окна; все настройки, личный чат, группа, форум, профили), личное запикселено; `NN-экран_состояние_тема.png`, полный список — CHECKLIST §3 |
| `../replica/recon.md` | карта replica-recon: источники, 38 экранов (S01–S38) со ссылками на скриншоты, 14 потоков, компоненты, модель данных, out of scope, размер |
| `../replica/features.csv` | матрица функций (must 30 / should 24 / could 14 / skip 9), колонка `clone` заполняется на Windows |
| `../replica/screens-inventory.md` | все 441 контроллер из исходников: заголовок EN/RU, file:line (`tools/screens_inventory.py`) |
| `measure/*.png` | схемы с размерами (pt), нарисованные из чисел кода: список чатов, пузыри, окно, настройки, меню, мелочи чата |
| `assets/app-resources/` | ресурсы из установленного Telegram.app (звуки, tgs/lottie, json, svg, png, иконка); `_Assets.car-extracted/` — распакованные Assets.car (≈2 600 png @1x/@2x + JSON-описания от `assetutil`). Шрифты SF/SF Compact, ключи (*.pem), GoogleService-Info.plist и metallib **исключены** |
| `assets/source/` | ассеты из исходников с сохранением структуры (`Telegram-Mac/Assets.xcassets`, `Resources/tgs`, `Resources/lottie`, звуки, ассеты пакетов) |
| `tools/` | скрипты: `shot.py` (сохранение и пикселизация скриншотов), `palettes.py` (таблица палитр), `anims.py` (инвентарь анимаций), `springs.py` (численные пружины), `measure.py` (схемы), `carx.swift` (распаковка Assets.car), `fontm.swift` (метрики шрифтов) |
| `CHECKLIST.md` | полнота по каждому пункту + что снять вручную |

Пересобрать производные файлы (из корня репо, при наличии `refs/Telegram-macOS`):
```
python3 recon/tools/palettes.py refs/Telegram-macOS/packages/ColorPalette/Sources/ColorPalette/ColorPalette.swift packages/ColorPalette/Sources/ColorPalette/ColorPalette.swift
python3 recon/tools/anims.py refs/Telegram-macOS > recon/animations-inventory.md
python3 recon/tools/springs.py
python3 recon/tools/measure.py recon/measure
```

## Чего не удалось получить и почему

| Что | Почему | Как закрыть |
|---|---|---|
| часть `screens/` (логин, бот, секретный чат, вьювер медиа, звонки, сторис) | выход из аккаунта / нет данных / падение Telegram при открытии вьювера / звонок — действие наружу | CHECKLIST «Что снять вручную» |
| `animations/` — записи 60 fps и кадры, колонка «замерено по видео» | панель записи экрана macOS скрыта от управления, а `screencapture`/ffmpeg из shell получают только обои (право ещё не применилось к процессу) | записать вручную в QuickTime или перезапустить Claude — см. CHECKLIST |
| `measure/` для профиля, поиска, поповера реакций, вьювера, звонка, логина | нужны скриншоты как подложка | после скриншотов |
| Проверка кривой `.spring` | физическая модель CASpring(3/1000/500) за 0.5 s расходится с тем, что видно глазом; код в ручных переходах использует bezier(0.23,1,0.32,1) — его и рекомендую | одна запись push/pop |
| Сабмодули `third-party/twidget`, `third-party/widget-sandbox` | приватные репозитории (нужна авторизация GitHub) | не нужны — это виджеты рабочего стола |
| Анимации звонков в деталях | большие отдельные пакеты (`CallVideoLayer`, `PrivateCallScreen`, `GroupCallScreenUI`), есть только в inventory | разобрать при работе над звонками |

## Где лежат медиа / перенос на Windows

Видео и кадров пока нет, поэтому `recon-media.zip` не создан; вся папка `recon/` (62 MB) лежит в git. Когда появятся записи — класть в `recon/animations/` и упаковать `zip -r ../recon-media.zip recon/animations recon/screens` **вне git**.

Важно: диск `/Volumes/M.2` (NTFS) смонтирован в macOS **только для чтения**, поэтому recon-работа сделана в клоне `~/Telegram-macOS-Fork` (ветка `main`, коммит с recon). Перенос на Windows — см. итоговое сообщение / README в коммите.
