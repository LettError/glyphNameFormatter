from fontTools.unicodedata import script
f = CurrentFont()
for g in f:
    if g.unicode is not None:
        print(g.name, g.unicode, script(g.unicode))
