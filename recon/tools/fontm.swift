import AppKit
let weights: [(String, NSFont.Weight)] = [("regular(.normal)", .regular), ("medium(.medium)", .medium), ("semibold(.semibold/.bold)", .semibold)]
print("| size pt | weight (TGFont) | family/name | ascender | descender | leading | lineHeight (LM default) | capHeight | xHeight |")
print("|---|---|---|---|---|---|---|---|---|")
let lm = NSLayoutManager()
for s in [10.0, 11, 12, 13, 14, 15, 16, 18, 22] {
  for (n,w) in weights {
    let f = NSFont.systemFont(ofSize: s, weight: w)
    print(String(format: "| %.0f | %@ | %@ | %.2f | %.2f | %.2f | %.2f | %.2f | %.2f |", s, n, f.fontName, f.ascender, f.descender, f.leading, lm.defaultLineHeight(for: f), f.capHeight, f.xHeight))
  }
}
