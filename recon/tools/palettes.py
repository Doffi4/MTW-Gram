import re,sys
path=sys.argv[1]; rel=sys.argv[2]
L=open(path).read().split('\n')
pal_starts=[(i,m.group(1)) for i,l in enumerate(L) for m in [re.match(r'^public let (\w+)(?:: ColorPalette)? = (?:ColorPalette\(|\{)',l)] if m]
pals={}
order=[]
for idx,(start,name) in enumerate(pal_starts):
    end=pal_starts[idx+1][0] if idx+1<len(pal_starts) else len(L)
    d={}; meta={}
    for i in range(start,end):
        for m in re.finditer(r'(\w+)\s*:\s*NSColor\((0x[0-9a-fA-F]+)(?:\s*,\s*([0-9.]+))?\)',L[i]):
            k,h,a=m.group(1),m.group(2),m.group(3)
            if k in d: continue
            hx='#'+h[2:].upper().rjust(6,'0')
            if a and float(a)!=1: hx+=' α%s'%a
            d[k]=(hx,i+1)
        for m in re.finditer(r'(name|tinted|isDark)\s*:\s*("?[\w ]+"?)',L[i]):
            meta.setdefault(m.group(1),m.group(2))
        for m in re.finditer(r'(\w+)\s*:\s*(\.[\w]+|nil|NSColor\.\w+|\w+Color)\s*[,)]',L[i]):
            if m.group(1) not in d and m.group(1) not in ('parent','wallpaper'): d[m.group(1)]=(m.group(2),i+1)
    if len(d)>20: pals[name]=(d,meta,start+1); order.append(name)
keys=[]
for n in order:
    for k in pals[n][0]:
        if k not in keys: keys.append(k)
print('| Палитра | name | isDark | tinted | строка |\n|---|---|---|---|---|')
for n in order:
    d,m,s=pals[n]; print(f'| `{n}` | {m.get("name","")} | {m.get("isDark","false")} | {m.get("tinted","")} | `{rel}:{s}` |')
print()
print('| Роль | '+' | '.join(order)+' |')
print('|---|'+'---|'*len(order))
for k in keys:
    row=[]
    for n in order:
        v=pals[n][0].get(k)
        row.append(f'{v[0]} <sub>:{v[1]}</sub>' if v else '—')
    print(f'| `{k}` | '+' | '.join(row)+' |')
