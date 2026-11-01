"""Rewrite tdesktop palettes with Telegram-macOS palette values.

usage: python -I tools/mac_palette.py <ColorPalette.swift> <tdesktop root>

colors.palette (Classic)           <- dayClassicPalette
Resources/day-blue  (Day)          <- whitePalette
Resources/night     (Tinted)       <- nightAccentPalette
Resources/night-green (Night)      <- darkPalette
Only the keys in MAP are touched; the rest of tdesktop's palette derives from them.
"""
import io, re, struct, sys, zipfile, zlib
from pathlib import Path

# --- macOS palettes -----------------------------------------------------------

def parse_swift(path):
    lines = Path(path).read_text(encoding='utf-8').split('\n')
    starts = [(i, m.group(1)) for i, l in enumerate(lines)
              for m in [re.match(r'^public let (\w+Palette) = ColorPalette\(', l)] if m]
    pals = {}
    for n, (start, name) in enumerate(starts):
        end = starts[n + 1][0] if n + 1 < len(starts) else len(lines)
        block = '\n'.join(lines[start:end])
        d = {}
        for m in re.finditer(r'(\w+)\s*:\s*NSColor\((0x[0-9a-fA-F]+)(?:\s*,\s*([0-9.]+))?\)', block):
            d.setdefault(m.group(1), rgba(m.group(2), m.group(3)))
        for m in re.finditer(r'(\w+)\s*:\s*\[((?:\s*NSColor\(0x[0-9a-fA-F]+\)\s*,?)+)\]', block):
            cs = [rgba(h, None) for h in re.findall(r'0x[0-9a-fA-F]+', m.group(2))]
            out = cs[0]
            for c in cs[1:]:
                out = mix(out, c, 0.5)  # ColorPalette.blendedOutgoingColors
            d.setdefault(m.group(1), out)
        wall = re.search(r'wallpaper:\s*\.(\w+)', block)
        d['_wallpaper'] = wall.group(1) if wall else 'none'
        pals[name] = d
    return pals

def rgba(h, a):
    v = int(h, 16)
    return ((v >> 16) & 255, (v >> 8) & 255, v & 255, round(float(a) * 255) if a else 255)

def mix(a, b, t):
    return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(4))

def alpha(c, a):
    return c[:3] + (round(255 * a),)

def shade(c, t):  # t < 0 darkens toward black, t > 0 lightens toward white
    return mix(c, (0, 0, 0, c[3]) if t < 0 else (255, 255, 255, c[3]), abs(t))

def hexc(c):
    s = '#%02x%02x%02x' % c[:3]
    return s + ('%02x' % c[3] if c[3] != 255 else '')

WHITE = (255, 255, 255, 255)

# --- tdesktop key -> macOS role ---------------------------------------------
# P = macOS palette dict. Hover has no macOS equivalent (list rows have none),
# so *Over keys sit halfway between background and grayBackground.

def over(P):
    return mix(P['background'], P['grayBackground'], 0.5)

MAP = {
    'windowBg': lambda P: P['background'],
    'windowFg': lambda P: P['text'],
    'windowBgOver': lambda P: P['grayBackground'],
    'windowBgRipple': lambda P: P['grayForeground'],
    'windowSubTextFg': lambda P: P['grayText'],
    'windowSubTextFgOver': lambda P: P['grayText'],
    'windowBoldFg': lambda P: P['text'],
    'windowBoldFgOver': lambda P: P['text'],
    'windowBgActive': lambda P: P['accent'],
    'windowFgActive': lambda P: WHITE,
    'windowActiveTextFg': lambda P: P['link'],
    'windowShadowFgFallback': lambda P: P['border'],
    'activeButtonBg': lambda P: P['accent'],
    'activeButtonBgOver': lambda P: shade(P['accent'], -0.06),
    'activeButtonBgRipple': lambda P: shade(P['accent'], -0.14),
    'activeLineFg': lambda P: P['accent'],
    'activeLineFgError': lambda P: P['redUI'],
    'lightButtonBg': lambda P: P['background'],
    'lightButtonBgOver': lambda P: mix(P['background'], P['accent'], 0.1),
    'lightButtonBgRipple': lambda P: mix(P['background'], P['accent'], 0.2),
    'lightButtonFg': lambda P: P['link'],
    'attentionButtonFg': lambda P: P['redUI'],
    'attentionButtonFgOver': lambda P: P['redUI'],
    'attentionButtonBgOver': lambda P: mix(P['background'], P['redUI'], 0.1),
    'attentionButtonBgRipple': lambda P: mix(P['background'], P['redUI'], 0.2),
    'menuBg': lambda P: P['background'],
    'menuBgOver': lambda P: P['grayBackground'],
    'menuBgRipple': lambda P: P['grayForeground'],
    'menuIconFg': lambda P: P['grayIcon'],
    'menuIconFgOver': lambda P: P['grayIcon'],
    'menuSeparatorFg': lambda P: P['border'],
    'checkboxFg': lambda P: P['grayIcon'],
    'placeholderFg': lambda P: P['grayText'],
    'placeholderFgActive': lambda P: P['grayText'],
    'inputBorderFg': lambda P: P['border'],
    'filterInputBorderFg': lambda P: P['accent'],
    'filterInputActiveBg': lambda P: P['grayBackground'],
    'filterInputInactiveBg': lambda P: P['grayBackground'],
    'titleBg': lambda P: P['background'],
    'titleBgActive': lambda P: P['background'],
    'titleFg': lambda P: P['grayText'],
    'titleFgActive': lambda P: P['text'],
    'titleButtonFg': lambda P: P['grayIcon'],
    'titleButtonFgOver': lambda P: P['text'],
    'titleButtonBgOver': lambda P: P['grayBackground'],
    'boxBg': lambda P: P['background'],
    'boxTextFg': lambda P: P['text'],
    'boxTextFgGood': lambda P: P['greenUI'],
    'boxTextFgError': lambda P: P['redUI'],
    'boxTitleFg': lambda P: P['text'],
    'boxTitleAdditionalFg': lambda P: P['grayText'],
    'boxDividerBg': lambda P: P['listBackground'],
    'layerBg': lambda P: P['blackTransparent'],
    'dialogsBg': lambda P: P['background'],
    'dialogsBgOver': over,
    'dialogsRippleBg': lambda P: P['grayBackground'],
    'dialogsBgActive': lambda P: P['accentSelect'],
    'dialogsRippleBgActive': lambda P: shade(P['accentSelect'], -0.1),
    'dialogsNameFg': lambda P: P['text'],
    'dialogsNameFgOver': lambda P: P['text'],
    'dialogsDateFg': lambda P: P['grayText'],
    'dialogsDateFgOver': lambda P: P['grayText'],
    'dialogsTextFg': lambda P: P['grayText'],
    'dialogsTextFgOver': lambda P: P['grayText'],
    'dialogsTextFgService': lambda P: P['text'],  # chatList.peerTextColor ("You:", author)
    'dialogsDraftFg': lambda P: P['redUI'],
    'dialogsSendingIconFg': lambda P: P['grayIcon'],
    'dialogsSentIconFg': lambda P: P['accentIcon'],
    'dialogsSentIconFgOver': lambda P: P['accentIcon'],
    'dialogsUnreadBg': lambda P: P['badge'],
    'dialogsUnreadBgMuted': lambda P: P['badgeMuted'],
    'dialogsUnreadFg': lambda P: P['background'],
    'dialogsVerifiedIconBg': lambda P: P['accent'],
    'dialogsOnlineBadgeFg': lambda P: P['greenUI'],
    'dialogsDraftFgActive': lambda P: WHITE,
    'dialogsUnreadBgMutedActive': lambda P: alpha(WHITE, 0.7),
    'emojiPanBg': lambda P: P['background'],
    'emojiPanCategories': lambda P: P['background'],
    'emojiPanHeaderBg': lambda P: alpha(P['background'], 0.95),
    'emojiIconFg': lambda P: P['grayIcon'],
    'topBarBg': lambda P: P['background'],
    'historyTextInFg': lambda P: P['textBubble_incoming'],
    'historyTextOutFg': lambda P: P['textBubble_outgoing'],
    'historyLinkInFg': lambda P: P['linkBubble_incoming'],
    'historyLinkOutFg': lambda P: P['linkBubble_outgoing'],
    'historyOutIconFg': lambda P: P['accentIconBubble_outgoing'],
    'historyOutIconFgSelected': lambda P: P['accentIconBubble_outgoing'],
    'historySendingOutIconFg': lambda P: P['grayIconBubble_outgoing'],
    'historySendingInIconFg': lambda P: P['grayIconBubble_incoming'],
    'historyCallArrowInFg': lambda P: P['greenUI'],
    'historyCallArrowInFgSelected': lambda P: P['greenUI'],
    'historyUnreadBarBg': lambda P: P['grayBackground'],
    'historyUnreadBarFg': lambda P: P['grayText'],
    'historyComposeAreaBg': lambda P: P['background'],
    'historyComposeAreaFg': lambda P: P['text'],
    'historyComposeAreaFgService': lambda P: P['grayText'],
    'historyComposeIconFg': lambda P: P['grayIcon'],
    'historyComposeIconFgOver': lambda P: P['text'],
    'historySendIconFg': lambda P: P['accentIcon'],
    'historySendIconFgOver': lambda P: P['accentIcon'],
    'historyComposeButtonBgOver': lambda P: P['grayBackground'],
    'historyComposeButtonBgRipple': lambda P: P['grayForeground'],
    'historyToDownBg': lambda P: P['background'],
    'historyToDownFg': lambda P: P['grayIcon'],
    'historyToDownFgOver': lambda P: P['text'],
    'msgInBg': lambda P: P['bubbleBackground_incoming'],
    'msgOutBg': lambda P: P['bubbleBackground_outgoing'],
    'msgInBgSelected': lambda P: P['bubbleBackgroundHighlight_incoming'],
    'msgOutBgSelected': lambda P: P['bubbleBackgroundHighlight_outgoing'],
    'msgSelectOverlay': lambda P: alpha(P['accent'], 0.3),
    'msgInShadow': lambda P: P['bubbleBorder_incoming'],
    'msgInShadowSelected': lambda P: P['bubbleBorder_incoming'],
    'msgOutShadow': lambda P: P['bubbleBorder_outgoing'],
    'msgOutShadowSelected': lambda P: P['bubbleBorder_outgoing'],
    'msgInServiceFg': lambda P: P['chatReplyTitleBubble_incoming'],
    'msgInServiceFgSelected': lambda P: P['chatReplyTitleBubble_incoming'],
    'msgOutServiceFg': lambda P: P['chatReplyTitleBubble_outgoing'],
    'msgOutServiceFgSelected': lambda P: P['chatReplyTitleBubble_outgoing'],
    'msgInDateFg': lambda P: P['grayTextBubble_incoming'],
    'msgInDateFgSelected': lambda P: P['grayTextBubble_incoming'],
    'msgOutDateFg': lambda P: P['grayTextBubble_outgoing'],
    'msgOutDateFgSelected': lambda P: P['grayTextBubble_outgoing'],
    'msgInReplyBarColor': lambda P: P['chatReplyTitleBubble_incoming'],
    'msgInReplyBarSelColor': lambda P: P['chatReplyTitleBubble_incoming'],
    'msgOutReplyBarColor': lambda P: P['chatReplyTitleBubble_outgoing'],
    'msgOutReplyBarSelColor': lambda P: P['chatReplyTitleBubble_outgoing'],
    'msgInMonoFg': lambda P: P['monospacedCodeBubble_incoming'],
    'msgOutMonoFg': lambda P: P['monospacedCodeBubble_outgoing'],
    'msgFileThumbLinkInFg': lambda P: P['linkBubble_incoming'],
    'msgFileThumbLinkOutFg': lambda P: P['linkBubble_outgoing'],
    'msgFileThumbLinkOutFgSelected': lambda P: P['linkBubble_outgoing'],
    'msgFileInBg': lambda P: P['fileActivityBackgroundBubble_incoming'],
    'msgFileInBgOver': lambda P: P['fileActivityBackgroundBubble_incoming'],
    'msgFileInBgSelected': lambda P: P['fileActivityBackgroundBubble_incoming'],
    'msgFileOutBg': lambda P: P['fileActivityBackgroundBubble_outgoing'],
    'msgFileOutBgSelected': lambda P: P['fileActivityBackgroundBubble_outgoing'],
    'historyFileInIconFg': lambda P: P['fileActivityForegroundBubble_incoming'],
    'historyFileInIconFgSelected': lambda P: P['fileActivityForegroundBubble_incoming'],
    'historyFileOutIconFg': lambda P: P['fileActivityForegroundBubble_outgoing'],
    'historyFileOutIconFgSelected': lambda P: P['fileActivityForegroundBubble_outgoing'],
    'msgWaveformInActive': lambda P: P['waveformForegroundBubble_incoming'],
    'msgWaveformInActiveSelected': lambda P: P['waveformForegroundBubble_incoming'],
    'msgWaveformInInactive': lambda P: P['waveformBackgroundBubble_incoming'],
    'msgWaveformInInactiveSelected': lambda P: P['waveformBackgroundBubble_incoming'],
    'msgWaveformOutActive': lambda P: P['waveformForegroundBubble_outgoing'],
    'msgWaveformOutActiveSelected': lambda P: P['waveformForegroundBubble_outgoing'],
    'msgWaveformOutInactive': lambda P: P['waveformBackgroundBubble_outgoing'],
    'msgWaveformOutInactiveSelected': lambda P: P['waveformBackgroundBubble_outgoing'],
    'historyPeer1NameFg': lambda P: P['groupPeerNameRed'],
    'historyPeer2NameFg': lambda P: P['groupPeerNameGreen'],
    'historyPeer3NameFg': lambda P: P['groupPeerNameOrange'],
    'historyPeer4NameFg': lambda P: P['groupPeerNameBlue'],
    'historyPeer5NameFg': lambda P: P['groupPeerNameViolet'],
    'historyPeer7NameFg': lambda P: P['groupPeerNameCyan'],
    'historyPeer8NameFg': lambda P: P['groupPeerNameOrange'],
    'historyPeer1UserpicBg': lambda P: P['peerAvatarRedTop'],
    'historyPeer1UserpicBg2': lambda P: P['peerAvatarRedBottom'],
    'historyPeer2UserpicBg': lambda P: P['peerAvatarGreenTop'],
    'historyPeer2UserpicBg2': lambda P: P['peerAvatarGreenBottom'],
    'historyPeer3UserpicBg': lambda P: P['peerAvatarOrangeTop'],
    'historyPeer3UserpicBg2': lambda P: P['peerAvatarOrangeBottom'],
    'historyPeer4UserpicBg': lambda P: P['peerAvatarBlueTop'],
    'historyPeer4UserpicBg2': lambda P: P['peerAvatarBlueBottom'],
    'historyPeer5UserpicBg': lambda P: P['peerAvatarVioletTop'],
    'historyPeer5UserpicBg2': lambda P: P['peerAvatarVioletBottom'],
    'historyPeer6UserpicBg': lambda P: P['peerAvatarPinkTop'],
    'historyPeer6UserpicBg2': lambda P: P['peerAvatarPinkBottom'],
    'historyPeer7UserpicBg': lambda P: P['peerAvatarCyanTop'],
    'historyPeer7UserpicBg2': lambda P: P['peerAvatarCyanBottom'],
    'historyPeer8UserpicBg': lambda P: P['peerAvatarOrangeTop'],
    'historyPeer8UserpicBg2': lambda P: P['peerAvatarOrangeBottom'],
    'sideBarBg': lambda P: P['grayUI'],
    'sideBarBgActive': lambda P: P['grayBackground'],
    'sideBarBgRipple': lambda P: P['grayForeground'],
    'sideBarTextFg': lambda P: P['grayText'],
    'sideBarTextFgActive': lambda P: P['accent'],
    'sideBarIconFg': lambda P: P['grayIcon'],
    'sideBarIconFgActive': lambda P: P['accentIcon'],
    'sideBarBadgeBg': lambda P: P['badge'],
    'sideBarBadgeBgMuted': lambda P: P['badgeMuted'],
    'sideBarBadgeFg': lambda P: P['background'],
}

# Without a wallpaper the chat is a flat chatBackground, so the translucent
# "service" pills (dates, service messages) take macOS chatDate colors instead.
FLAT_CHAT = {
    'msgServiceBg': lambda P: P['grayBackground'],
    'msgServiceBgSelected': lambda P: P['grayForeground'],
    'msgServiceFg': lambda P: P['chatDateText'],
    'msgDateImgFg': lambda P: WHITE,
    'msgImgReplyBarColor': lambda P: WHITE,
    'msgBotKbIconFg': lambda P: WHITE,
    'historyScrollBarBg': lambda P: alpha(P['grayIcon'], 0.48),
    'historyScrollBarBgOver': lambda P: alpha(P['grayIcon'], 0.74),
    'historyScrollBg': lambda P: alpha(P['grayIcon'], 0.3),
    'historyScrollBgOver': lambda P: alpha(P['grayIcon'], 0.42),
}

def values_for(P):
    m = dict(MAP)
    if P['_wallpaper'] == 'none':
        m.update(FLAT_CHAT)
    return {k: hexc(f(P)) for k, f in m.items()}

# --- tdesktop palette text rewriting -----------------------------------------

LINE = re.compile(r'^(\w+)(\s*:\s*)([^;]+?)(\s*;.*)$')

def rewrite(text, values, append_missing):
    seen, out = set(), []
    for line in text.split('\n'):
        m = LINE.match(line)
        if m and m.group(1) in values:
            k, sep, val, rest = m.groups()
            fallback = val[val.index('|'):] if '|' in val else ''
            val = values[k] + (' ' + fallback if fallback else '')
            line = k + sep + val + rest
            seen.add(k)
        out.append(line)
    if append_missing:
        missing = [k for k in values if k not in seen]
        while out and out[-1] == '':
            out.pop()
        out += ['%s: %s;' % (k, values[k]) for k in missing] + ['']
    else:
        assert seen == set(values), 'keys not in palette: %s' % (set(values) - seen)
    return '\n'.join(out)

def png_1x1(c):
    def chunk(t, d):
        return struct.pack('>I', len(d)) + t + d + struct.pack('>I', zlib.crc32(t + d) & 0xffffffff)
    return (b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', 1, 1, 8, 2, 0, 0, 0))
            + chunk(b'IDAT', zlib.compress(b'\x00' + bytes(c[:3]))) + chunk(b'IEND', b''))

def rewrite_theme(path, P):
    src = zipfile.ZipFile(path)
    files = {n: src.read(n) for n in src.namelist()}
    src.close()
    colors = files['colors.tdesktop-theme'].decode('utf-8')
    files['colors.tdesktop-theme'] = rewrite(colors, values_for(P), True).encode('utf-8')
    if P['_wallpaper'] == 'none':
        files['background.png'] = png_1x1(P['chatBackground'])
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as z:
        for n, d in files.items():
            z.writestr(n, d)
    Path(path).write_bytes(buf.getvalue())

def main():
    pals = parse_swift(sys.argv[1])
    root = Path(sys.argv[2]) / 'Telegram'
    palette = root / 'lib_ui/ui/colors.palette'
    values = values_for(pals['dayClassicPalette'])
    palette.write_text(rewrite(palette.read_text(encoding='utf-8'), values, False), encoding='utf-8', newline='\n')
    for theme, name in [('day-blue', 'whitePalette'), ('night', 'nightAccentPalette'), ('night-green', 'darkPalette')]:
        rewrite_theme(root / 'Resources' / (theme + '.tdesktop-theme'), pals[name])
        print(theme, '<-', name, pals[name]['background'][:3])

if __name__ == '__main__':
    main()
