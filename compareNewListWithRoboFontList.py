

codes = {}

uniPath = "/Users/erik/code/glyphNameFormatter/Lib/glyphNameFormatter/names/glyphNamesToUnicode.txt"
rfPath = "/Applications/RoboFont_4.5b.app/Contents/Resources/glyphNamesToUnicode.txt"

lines = []
with open(uniPath, 'r') as file:
    lines = file.read().split("\n")

lines = [l for l in lines if l[0]!="#"]
newNames = len(lines)
#print(lines)
for l in lines:
    p = l.split()
    name = p[0]
    uni = int(f"0x{p[1]}", 16)
    if not uni in codes:
        codes[uni] = dict(rf=[], new=[])
    codes[uni]['new'].append(name)

print(f'names in new export: {len(codes)}')






lines = []
with open(rfPath, 'r') as file:
    lines = file.read().split("\n")
    print(f"names in RF {len(lines)}")

lines = [l for l in lines if l[0]!="#"]
rfNames = len(lines)
print(f'names added: {newNames-rfNames}')
#print(lines)
for l in lines:
    p = l.split()
    name = p[0]
    uni = int(f"0x{p[1]}", 16)
    #print(name, uni)
    if not uni in codes:
        codes[uni] = dict(rf=[], new=[])
    codes[uni]['rf'].append(name)

sortedUnis = list(codes.keys())
sortedUnis.sort()

removed = []
added = []
changed = []

for u in sortedUnis:
    c = codes[u]
    if len(c['new']) > 0 and len(c['rf']) == 0:
        added += c['new']
    elif c['new'] != c['rf']:
        changed.append(f"{c['rf'][0]} -> {c['new'][0]}")

print(f'\nremoved {len(removed)} names:\n', "\n\t".join(removed))
print(f'\nadded {len(added)} names:\n', "\n\t".join(added))
print(f'\nchanged {len(changed)} names:\n', "\n\t".join(changed))
