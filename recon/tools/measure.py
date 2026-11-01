# Schematic measurement sheets drawn from source constants (pt). Rendered at 2x. No screenshots needed.
import sys, os
from PIL import Image, ImageDraw, ImageFont
OUT = sys.argv[1]; S = 2
def font(sz):
    for p in ['/System/Library/Fonts/SFNS.ttf','/System/Library/Fonts/Helvetica.ttc','/Library/Fonts/Arial.ttf']:
        if os.path.exists(p): return ImageFont.truetype(p, sz*S)
    return ImageFont.load_default()
F, Fs = font(11), font(9)
BG, LINE, DIM, ACC, BUB_IN, BUB_OUT, TXT, GRAY = '#FFFFFF', '#E6E6E6', '#FF2D55', '#2481CC', '#F1F1F4', '#E1FFC7', '#000000', '#999999'
def new(w, h, bg=BG):
    im = Image.new('RGB', (w*S, h*S), bg); return im, ImageDraw.Draw(im)
def R(d, x, y, w, h, fill=None, outline=None, r=0, width=1):
    box = [x*S, y*S, (x+w)*S, (y+h)*S]
    if r: d.rounded_rectangle(box, r*S, fill=fill, outline=outline, width=width*S)
    else: d.rectangle(box, fill=fill, outline=outline, width=width*S)
def T(d, x, y, s, c=TXT, f=None): d.text((x*S, y*S), s, fill=c, font=f or F)
def hdim(d, x1, x2, y, label):
    d.line([x1*S, y*S, x2*S, y*S], fill=DIM, width=S)
    for x in (x1, x2): d.line([x*S, (y-3)*S, x*S, (y+3)*S], fill=DIM, width=S)
    T(d, (x1+x2)/2-len(label)*2.6, y-13, label, DIM, Fs)
def vdim(d, x, y1, y2, label):
    d.line([x*S, y1*S, x*S, y2*S], fill=DIM, width=S)
    for y in (y1, y2): d.line([(x-3)*S, y*S, (x+3)*S, y*S], fill=DIM, width=S)
    T(d, x+4, (y1+y2)/2-6, label, DIM, Fs)
def title(d, s, sub): T(d, 10, 6, s, TXT, font(13)); T(d, 10, 24, sub, GRAY, Fs)

# 1. chat list row
im, d = new(520, 260); title(d, 'Chat list row — 70pt', 'ChatListRowItem.swift:1192,1382,2638 · ChatListRowView.swift:701,1546,3333')
ox, oy, W = 40, 70, 300
for i in range(2):
    y = oy + i*70
    if i == 0: R(d, ox+3, y+3, W-6, 64, fill='#D4E7F8', r=14)
    d.ellipse([(ox+10)*S, (y+10)*S, (ox+60)*S, (y+60)*S], fill='#7EC3F5')
    T(d, ox+70, y+9-1, 'Chat title  (medium 14)'); T(d, ox+W-40, y+11, '12:30', GRAY, Fs)
    T(d, ox+70, y+30, 'Message preview (normal 13)', GRAY)
    R(d, ox+W-9-22, y+70-9-20, 22, 20, fill=ACC, r=10); T(d, ox+W-9-16, y+70-9-17, '3', '#FFFFFF', Fs)
    d.line([(ox+70)*S, (y+69)*S, (ox+W)*S, (y+69)*S], fill=LINE, width=S)
R(d, ox, oy, W, 140, outline='#BBBBBB')
hdim(d, ox, ox+70, oy-8, 'leftInset 70'); hdim(d, ox+10, ox+60, oy+70+64, 'avatar 50')
vdim(d, ox-14, oy, oy+70, 'h 70'); vdim(d, ox+W+8, oy, oy+9, 'margin 9')
T(d, ox+W+14, oy+30, 'selection plate', DIM, Fs); T(d, ox+W+14, oy+42, 'inset 3, r14 continuous', DIM, Fs)
T(d, ox+80, oy+150, 'separator 1pt from x=70 · badge medium 11, right margin 9', DIM, Fs)
im.save(f'{OUT}/chatlist-row.png')

# 2. bubbles group
im, d = new(600, 330, '#DCE8D5'); title(d, 'Bubbles — radii by group position', 'ChatMessageBubbleImages.swift:13-75 · ChatRowItem.swift:3306-3314, 1549')
def bubble(x, y, w, h, tl, tr, bl, br, tail, fill):
    R(d, x, y, w, h, fill=fill, r=8)  # base
    # emulate per-corner radii: draw main body then cover corners
    im2 = Image.new('L', (w*S, h*S), 0); dd = ImageDraw.Draw(im2)
    dd.rounded_rectangle([0, 0, w*S-1, h*S-1], max(tl,tr,bl,br)*S, fill=255)
    for (cx, cy, r) in [(0,0,tl),(w-r if False else w,0,tr),(0,h,bl),(w,h,br)]: pass
    if tail: d.polygon([((x+w-2)*S,(y+h-12)*S),((x+w+6)*S,(y+h)*S),((x+w-8)*S,(y+h)*S)], fill=fill)
ox = 200
rows = [(70, 'single · none', (16,16,16,16), True), (130, 'first · top', (16,16,16,8), False), (174, 'middle · both', (16,8,16,8), False), (218, 'last · bottom', (16,8,16,16), True)]
for y, lab, (tl,tr,bl,br), tail in rows:
    w, h = 200, 40
    big = lambda r: r == 16
    d.rounded_rectangle([ox*S, y*S, (ox+w)*S, (y+h)*S], 16*S, fill=BUB_OUT, corners=(big(tl), big(tr), big(br), big(bl)))
    for r, cx, cy in [(tl, ox, y), (tr, ox+w-16, y), (br, ox+w-16, y+h-16), (bl, ox, y+h-16)]:
        if r == 8:
            d.rectangle([cx*S, cy*S, (cx+16)*S, (cy+16)*S], fill='#DCE8D5')
            # rebuild corner square with radius 8
            x0 = cx if cx == ox else cx; y0 = cy
            d.rectangle([x0*S, y0*S, (x0+16)*S, (y0+16)*S], fill=BUB_OUT)
            bx = ox if cx == ox else ox+w-8; by = y if cy == y else y+h-8
            d.rectangle([bx*S, by*S, (bx+8)*S, (by+8)*S], fill='#DCE8D5')
            px = ox if cx == ox else ox+w-16; py = y if cy == y else y+h-16
            d.pieslice([px*S, py*S, (px+16)*S, (py+16)*S], {(True,True):180,(False,True):270,(False,False):0,(True,False):90}[(cx==ox, cy==y)], {(True,True):270,(False,True):360,(False,False):90,(True,False):180}[(cx==ox, cy==y)], fill=BUB_OUT)
    if tail: d.polygon([((ox+w-4)*S,(y+h-14)*S),((ox+w+6)*S,(y+h)*S),((ox+w-14)*S,(y+h)*S)], fill=BUB_OUT)
    T(d, ox+11, y+12, 'text 13pt'); T(d, ox+w-40, y+h-17, '12:30 ✓', GRAY, Fs)
    T(d, 20, y+12, f'{lab}  TL{tl} TR{tr} BL{bl} BR{br}', DIM, Fs)
hdim(d, ox, ox+11, 268, 'inset 11'); T(d, ox+30, 264, 'tail side +6 · tail width 6 · time y = maxY−h−6', DIM, Fs)
T(d, 20, 290, 'Group: same author & Δt < 10 min (ChatEntryTypes.swift:3). Incoming = mirrored.', DIM, Fs); T(d, 20, 304, 'Max content width = min(width − offsets − 36 − 20, 450) (ChatRowItem.swift:320-345).', DIM, Fs)
im.save(f'{OUT}/chat-bubbles.png')

# 3. window / split layout
im, d = new(760, 360, '#ECECEC'); title(d, 'Window & split — dual layout', 'ApplicationContext.swift:177,223,399,1136-1195 · TGSplitView.swift:458 · NavigationBarView.swift:17')
ox, oy, H = 20, 50, 290
R(d, ox, oy, 600, H, fill='#FFFFFF', outline='#999999', r=10)
for i, c in enumerate(['#FF5F57', '#FEBC2E', '#28C840']): d.ellipse([(ox+15+i*20)*S, (oy+8)*S, (ox+27+i*20)*S, (oy+20)*S], fill=c)
R(d, ox+8, oy+8, 300, H-16, fill='#F6F6F6', outline='#CCCCCC', r=16); T(d, ox+120, oy+120, 'Chat list', GRAY)
R(d, ox+308, oy, 292, 64, fill='#FAFAFA'); T(d, ox+400, oy+24, 'Navbar 64', GRAY)
R(d, ox+320, oy+H-12-52, 268, 52, fill='#FFFFFF', outline='#CCCCCC', r=20); T(d, ox+380, oy+H-12-32, 'Input glass r20, min 40', GRAY, Fs)
hdim(d, ox+8, ox+308, oy+H+12, 'list 300 (drag 300 … W−380)'); hdim(d, ox+308, ox+600, oy+H+12, 'chat ≥ 380')
vdim(d, ox+604, oy, oy+64, '64'); vdim(d, ox+604, oy+H-12, oy+H, '12')
T(d, ox+10, oy+H+26, 'insets (8,8,8,0) · traffic lights offset (15,8) · min window 380×550 · dual if main ≥ 650 · sidebar 90 · minimisize 90 · trailing panel 358', DIM, Fs)
im.save(f'{OUT}/window-layout.png')

# 4. settings group
im, d = new(420, 250, '#F2F2F7'); title(d, 'Settings group (modern rows)', 'GeneralRowItem.swift:160-230,385,436 · GeneralRowView.swift:128')
ox, oy, W = 30, 60, 360
R(d, ox, oy, W, 120, fill='#FFFFFF', r=20)
for i in range(3):
    y = oy + i*40; T(d, ox+14, y+12, f'Row {i+1}  (40pt, inner 12/14)')
    if i < 2: d.line([(ox+14)*S, (y+40)*S, (ox+W)*S, (y+40)*S], fill=LINE, width=S)
hdim(d, ox, ox+14, oy+130, '14'); vdim(d, ox+W+6, oy, oy+40, '40'); T(d, ox, oy+150, 'radius 20 · block max width 600 · row inset 20/20', DIM, Fs)
im.save(f'{OUT}/settings-group.png')

# 5. context menu
im, d = new(360, 260, '#DDDDDD'); title(d, 'Context menu (AppMenu)', 'AppMenuController.swift:112 · AppMenuRowItem.swift:59,149-150,333')
ox, oy = 60, 50
R(d, ox, oy, 220, 4+28*5+4+5, fill='#FFFFFF', r=18)
items = ['Reply  ⌘R', 'Copy Text  ⌘C', 'Edit  ⌘E', '—', 'Delete']
y = oy+4
for it in items:
    if it == '—': d.line([(ox+11)*S, (y+2)*S, (ox+209)*S, (y+2)*S], fill=LINE, width=S); y += 5; continue
    if it.startswith('Copy'): R(d, ox+4, y, 212, 28, fill='#E8F1FB', r=5)
    T(d, ox+11+22, y+7, it, '#FF3B30' if it == 'Delete' else TXT); R(d, ox+11, y+6, 16, 16, outline=GRAY, r=3); y += 28
vdim(d, ox+226, oy+4, oy+32, 'row 28'); hdim(d, ox, ox+11, oy+170, '11'); T(d, ox, oy+182, 'radius 18 · hover plate r5 inset 4 · text medium 13 · separator 4–5', DIM, Fs)
T(d, ox, oy+196, 'open: spring ω20 ζ0.84, scale 0.42→1 from cursor', DIM, Fs)
im.save(f'{OUT}/context-menu.png')

# 6. date header + swipe reply + send button
im, d = new(420, 200, '#DCE8D5'); title(d, 'Date pill · send button · swipe-reply', 'ChatMessageDateHeader.swift:180,511 · ChatInputSendButton.swift:110 · ChatRowView.swift:23,2808')
R(d, 150, 50, 120, 22, fill='#00000040', r=11); T(d, 168, 54, 'November 1', '#FFFFFF')
T(d, 110, 78, 'row h 30 · pill = text+16 × text+6, r = h/2', DIM, Fs)
R(d, 40, 120, 40, 32, fill=ACC, r=16); T(d, 30, 158, 'send 40×32, inset 4, gap 6', DIM, Fs)
d.ellipse([260*S, 116*S, 293*S, 149*S], fill='#FFFFFF'); T(d, 230, 158, 'swipe-reply 33×33, threshold 100pt', DIM, Fs)
im.save(f'{OUT}/chat-misc.png')
print('ok')
