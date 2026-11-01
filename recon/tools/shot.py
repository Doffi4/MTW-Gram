# Save the newest computer-use capture as recon/screens/<name>.png, pixelating personal data.
# usage: shot.py <name> [list] [hdr] [x0,y0,x1,y1 ...]   (coords in window px, 1x = pt)
import sys, os, glob
from PIL import Image
SRC = '/Users/doffi/.claude/projects/-Volumes-M-2-Telegram-macOS-Fork/9679faff-e4da-484b-92df-7a50f8335764/tool-results'
OUT = os.path.expanduser('~/Telegram-macOS-Fork/recon/screens')
os.makedirs(OUT, exist_ok=True)
FILES = sorted(glob.glob(SRC + '/mcp-computer-use-blob-*.jpg'), key=os.path.getmtime)
def pix(b, k=10):
    x0, y0, x1, y1 = [int(v) for v in b]
    x1, y1 = min(x1, im.width), min(y1, im.height)
    if x1 <= x0 or y1 <= y0: return
    r = im.crop((x0, y0, x1, y1)); w, h = r.size
    r = r.resize((max(1, w // k), max(1, h // k)), Image.BILINEAR).resize((w, h), Image.NEAREST)
    im.paste(r, (x0, y0))
def run(f, name, args):
  global im
  im = Image.open(f).convert('RGB')
  if im.width < 1281 and 'raw' not in args: im = im.resize((1281, 832), Image.LANCZOS)
  top = 136
  bottom = 770
  for a in args:
      if a.startswith('top='): top = int(a[4:])
      if a.startswith('bottom='): bottom = int(a[7:])
  for a in args:
      if a == 'list':
          for y in range(top, bottom - 60, 70):
              pix((14, y + 2, 70, min(y + 68, bottom))); pix((76, y + 2, 258, min(y + 24, bottom))); pix((76, y + 24, 300, min(y + 68, bottom)))
      elif a.startswith('rows:'):
          _, t, h, tx1 = a.split(':'); t, h, tx1 = int(t), int(h), int(tx1)
          for y in range(t, bottom, h):
              pix((14, y + 2, 58, min(y + h - 2, bottom))); pix((60, y + 2, tx1, min(y + h - 2, bottom)))
      elif a == 'hdr':
          pix((112, 14, 150, 50))
      elif a.count(',') == 3:
          pix(a.split(','))
  for a in args:
      if a.startswith('crop='): im = im.crop((0, 0, int(a[5:]), im.height))
  im.save(f'{OUT}/{name}.png', optimize=True)
  print(name, im.size, os.path.basename(f))

# usage: shot.py "name preset..." ["name2 preset..." ...]  -> mapped onto the N newest captures in order
# spec: "<blob-suffix> <name> [presets...]"
for spec in sys.argv[1:]:
    parts = spec.split()
    f = [x for x in FILES if x.endswith(parts[0] + '.jpg')][0]
    run(f, parts[1], parts[2:])
