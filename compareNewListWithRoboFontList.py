# https://robofont.com/documentation/reference/api/mojo/mojo-robofont/?highlight=version
import mojo.roboFont
from glyphNameFormatter.reader import u2r

s = f'{mojo.roboFont.version} {mojo.roboFont.buildNumber}'

codes = {}

# these paths are very specific for Erik. 
# Edit as you need. 

uniPath = "/Users/erik/code/glyphNameFormatter/Lib/glyphNameFormatter/names/glyphNamesToUnicode.txt"
rfPath = "/Applications/RoboFont_4.5b.app/Contents/Resources/glyphNamesToUnicode.txt"
reportPath = "/Users/erik/code/glyphNameFormatter/robofontUpdate.md"

text = []
text.append("# Changes between this current list and the list embedded in RoboFont")


# read the list at the path, return a dict with uni: name pairs
def readList(newPath, rfPath):    
    uniCurrent = {}
    # codes from the current list
    with open(newPath, 'r') as file:
        lines = file.read().split("\n")
        lines = [l for l in lines if l[0]!="#"]
        countNew = len(lines)
        for l in lines:
            p = l.split()
            name = p[0]
            uni = int(f"0x{p[1]}", 16)
            if not uni in uniCurrent:
                uniCurrent[uni] = dict(rf=[], new=[])
            uniCurrent[uni]['new'].append(name)
    with open(rfPath, 'r') as file:
        lines = file.read().split("\n")
        lines = [l for l in lines if l[0]!="#"]
        countRF = len(lines)
        for l in lines:
            p = l.split()
            name = p[0]
            uni = int(f"0x{p[1]}", 16)
            if not uni in uniCurrent:
                uniCurrent[uni] = dict(rf=[], new=[])
            uniCurrent[uni]['rf'].append(name)
    return countNew, countRF, uniCurrent

countNew, countRF, data = readList(uniPath, rfPath)

text.append(f"\n\nCurrent list has {countNew} names.")
text.append(f"Current RoboFont {s} has {countRF} names.")

text.append("\n\n## Additions")
text.append("| Unicode | Glyphname | Range Name |")
text.append("| ----- | ----- |  ----- |")

newCount = []
updateCount = []

for uni in sorted(data):
    old = data[uni]['rf']
    new = data[uni]['new']
    if old == new: continue
    if old == [] and new != []:
        text.append(f"| 0x{uni:0x} | {' '.join(new)} | {u2r(uni)} |")

text.append("\n\n## Added Names")
text.append("| Unicode | Old Glyphname | New Glyphname | Range Name |")
text.append("| ----- | ----- | ----- | ----- |")

newCount = []
updateCount = []

for uni in sorted(data):
    old = data[uni]['rf']
    new = data[uni]['new']
    if old == new: continue
    if old != [] and new != [] and new != old:
        text.append(f"| 0x{uni:0x} | {' '.join(old)}  | {' '.join(new)} | {u2r(uni)} |")

if False:


    lines = []

    lines = [l for l in lines if l[0]!="#"]
    rfNames = len(lines)

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


    lines.append("\n\n\n")
    lines.append(f'\n## Changed Names {len(changed)}')

    changed = []
    added = []

    for u in sortedUnis:
        c = codes[u]
        if len(c['new']) > 0 and len(c['rf']) == 0:
            changed.append(f"| {c['new'][0]} |  |")
        elif c['new'] != c['rf']:
            added.append(f"| {c['new'][0]} | {c['rf'][0]} |")

    lines.append("| Unicode | Old | New |")
    lines.append("| ----- | ----- | ----- |")
    for item in changed:
        lines.append(item)

    lines.append("| Unicode | Glyphname |")
    lines.append("| ----- | ----- |")
    for item in changed:
        lines.append(item)


with open(reportPath, 'w') as out:
    out.write("\n".join(text))

print('done')