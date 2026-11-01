import re,os,sys,collections
root=sys.argv[1]
CALL=re.compile(r'\b(animateAlpha|animateScaleSpring\w*|animateScale\w*|animatePosition\w*|animateFrame|animateBounds\w*|animateSpring|animateAdditive|animateRotation|animateBackground|animateBorder|animateCornerRadius|animateTransform|animateContents|animateShadow\w*|animate\(from|_change\(\w+|change\((?:pos|size|opacity)|changeBounds|\.animated\(duration|ContainedViewLayoutTransition\.animated|NSAnimationContext\.runAnimationGroup|CASpringAnimation\(|CABasicAnimation\(|CAKeyframeAnimation\(|makeSpringAnimation|makeSpringBounceAnimation|CATransition\(|\.duration\s*=|settlingDuration|\.mass\s*=|\.stiffness\s*=|\.damping\s*=)')
DUR=re.compile(r'duration\s*[:=]\s*([\w.+\-*/ ]+?|[\w.]+\([^)]*\)[\w.*/ ]*?)\s*(?=[,)\n]|$|\s{2}|\s\w+\s*[=.(])')
TF=re.compile(r'(?:timingFunction|curve)\s*:\s*([\w.]+(?:\([^)]*\))?)')
KP=re.compile(r'keyPath\s*:\s*("[^"]+"|[\w.]+)|Animation\(keyPath:\s*"([^"]+)"|Animation\("([^"]+)"|\(\s*"([\w.]+)"\s*\)')
FUNC=re.compile(r'\bfunc\s+(\w+)')
TYPE=re.compile(r'^\s*(?:public |private |fileprivate |final |open |internal )*(?:class|struct|extension|enum)\s+(\w+)')
rows=[]
for dp,dn,fn in os.walk(root):
    if any(x in dp for x in ('/Tests','/tools','/submodules','/third-party','/core-xprojects','/.git','TelegramThemeShare','GeneralRowsShare')): continue
    for f in fn:
        if not f.endswith('.swift'): continue
        p=os.path.join(dp,f); rel=os.path.relpath(p,root)
        try: L=open(p,encoding='utf-8',errors='ignore').read().split('\n')
        except: continue
        typ='';fun=''
        for i,l in enumerate(L):
            m=TYPE.match(l)
            if m: typ=m.group(1)
            m=FUNC.search(l)
            if m: fun=m.group(1)
            s=l.strip()
            if s.startswith('//'): continue
            m=CALL.search(l)
            if not m: continue
            ctx=' '.join(x.strip() for x in L[i:i+3])
            call=m.group(1).split('(')[0]
            d=DUR.search(ctx); t=TF.search(ctx); k=KP.search(ctx)
            kp=next((g for g in k.groups() if g),'') if k else ''
            if call.startswith('.') and call!='.animated' and not re.search(r'(?i)(anim|spring|transition|group|context|ctx|basic|keyframe)\w*\.(duration|mass|stiffness|damping)', l): continue
            rows.append((rel.split('/')[1] if rel.startswith('packages/') else rel.split('/')[0], rel,i+1,typ,fun,call.strip(),(d.group(1).strip() if d else ''),(t.group(1) if t else ''),kp.strip('"'),s[:140].replace('|','\\|')))
by=collections.defaultdict(list)
for r in rows: by[r[0]].append(r)
print(f'# Полный инвентарь анимаций (авто-извлечение)\n\nВсего вызовов: **{len(rows)}** в {len(set(r[1] for r in rows))} файлах. Сгенерировано скриптом `recon/tools/anims.py` по `refs/Telegram-macOS` (без Tests/tools/submodules). Колонки: тип/функция-контекст, вызов, duration, curve/timingFunction, keyPath, исходная строка. Дефолты хелперов см. в `animations.md` §0.\n')
dc=collections.Counter(r[6] for r in rows if r[6]); tc=collections.Counter(r[7] for r in rows if r[7])
print('## Статистика длительностей (топ)\n\n| duration | вызовов |\n|---|---|'); [print(f'| `{k}` | {v} |') for k,v in dc.most_common(30)]
print('\n## Статистика кривых (топ)\n\n| curve | вызовов |\n|---|---|'); [print(f'| `{k}` | {v} |') for k,v in tc.most_common(25)]
for pkg in sorted(by):
    print(f'\n## {pkg} ({len(by[pkg])})\n\n| file:line | context | call | duration | curve | keyPath | code |\n|---|---|---|---|---|---|---|')
    for r in by[pkg]:
        print(f'| `{r[1]}:{r[2]}` | {r[3]}.{r[4]} | `{r[5]}` | {r[6]} | {r[7]} | {r[8]} | `{r[9]}` |')
