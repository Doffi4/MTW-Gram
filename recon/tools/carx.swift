import AppKit
// usage: carx <bundlePath> <namesFile> <outDir>
let a = CommandLine.arguments
let b = Bundle(path: a[1])!
let names = try! String(contentsOfFile: a[2]).split(separator: "\n").map(String.init)
let out = a[3]
try? FileManager.default.createDirectory(atPath: out, withIntermediateDirectories: true)
var ok = 0, fail = [String]()
for n in Set(names) where !n.isEmpty {
  guard let img = b.image(forResource: n) else { fail.append(n); continue }
  var saved = false
  for rep in img.representations {
    guard let cg = rep.cgImage(forProposedRect: nil, context: nil, hints: nil) else { continue }
    let br = NSBitmapImageRep(cgImage: cg)
    let scale = Int((Double(cg.width) / max(rep.size.width,1)).rounded())
    let safe = n.replacingOccurrences(of: "/", with: "_")
    let p = "\(out)/\(safe)@\(scale)x.png"
    if let d = br.representation(using: .png, properties: [:]) { try? d.write(to: URL(fileURLWithPath: p)); saved = true }
  }
  if saved { ok += 1 } else { fail.append(n) }
}
print("ok \(ok) fail \(fail.count)"); if !fail.isEmpty { print(fail.prefix(20).joined(separator: ",")) }
