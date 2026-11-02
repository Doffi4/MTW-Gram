# Enumerate every screen-like controller in Telegram-macOS sources.
import re, os, sys, collections
root = sys.argv[1]
BASES = r'(ModalViewController|TelegramGenericViewController|TableViewController|EditableViewController|GenericViewController|ViewController|SectionViewController|TelegramViewController|NavigationViewController|MajorNavigationController|SplitViewController|TableModalViewController|InputDataModalController|ModalController|EmptyChatViewController|PeersListController|ChatController|PeerMediaController)(<[^>{]*>)?'
cls = re.compile(r'^\s*(?:public |open |final |private |fileprivate |internal )*class\s+(\w+)\s*(?:<[^>]*>)?\s*:\s*' + BASES + r'\b')
fn = re.compile(r'^\s*(?:public |private |fileprivate |internal )*func\s+(\w+)\s*\([^)]*\)?.*->\s*(InputDataController|InputDataModalController|ModalViewController|ViewController)\b')
title = re.compile(r'title:\s*(?:strings\(\)\.)?(\w+)')
rows = []
for dp, dn, fs in os.walk(root):
    if any(x in dp for x in ('/Tests', '/tools', '/submodules', '/third-party', '/core-xprojects', 'Share/', 'Share\\')): continue
    if dp.endswith('Share'): continue
    for f in fs:
        if not f.endswith('.swift'): continue
        p = os.path.join(dp, f); rel = os.path.relpath(p, root)
        L = open(p, errors='ignore').read().split('\n')
        for i, l in enumerate(L):
            m = cls.match(l)
            kind = None
            if m: name, kind = m.group(1), 'class:' + m.group(2)
            else:
                m = fn.match(l)
                if m: name, kind = m.group(1), 'func->' + m.group(2)
            if not kind: continue
            t = ''
            for j in range(i, min(i + 400, len(L))):
                mt = re.search(r'(?:InputDataController\(|InputDataModalController\(|ModalInteractions\(|setCenterTitle\(|\.title\s*=|title:)\s*[^,)]*?strings\(\)\.(\w+)', L[j])
                if mt: t = mt.group(1); break
            pkg = rel.split('/')[1] if rel.startswith('packages/') else rel.split('/')[0] + '/' + rel.split('/')[1]
            rows.append((pkg, name, kind, t, f'{rel}:{i+1}'))
rows.sort()
by = collections.defaultdict(list)
for r in rows: by[r[0]].append(r)
print(f'# Инвентарь экранов из исходников\n\nВсего: **{len(rows)}** контроллеров в {len(by)} пакетах. Сгенерировано `recon/tools/screens_inventory.py`. `title` — ключ локализации заголовка (значения в `Telegram-Mac/en.lproj/Localizable.strings`).\n')
for pkg in sorted(by):
    print(f'\n## {pkg} ({len(by[pkg])})\n\n| controller | kind | title key | file:line |\n|---|---|---|---|')
    for r in by[pkg]: print(f'| `{r[1]}` | {r[2]} | {r[3]} | `{r[4]}` |')
