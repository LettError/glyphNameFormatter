


from fontTools.unicodedata import script
from pprint import pprint

f = CurrentFont()

scrpts = {}
for g in f:
    if g.unicode is not None:
        s = script(g.unicode)
        if s not in scrpts:
            scrpts[s] = []
        scrpts[s].append(g.name)
pprint(scrpts)