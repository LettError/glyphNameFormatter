from glyphNameFormatter.data.scriptPrefixes import scriptPrefixes

def process(self):
    # edits go here
    self.edit("LATIN")

    self.replace("MODIFIER LETTER LOW CIRCUMFLEX ACCENT", "circumflexlow")

    latinGreeks = [
        # these need to be prefixed as latin. 
        0xA7B3, #   LATIN CAPITAL LETTER CHI
        0xA7B4, #   LATIN CAPITAL LETTER BETA
        0xA7B5, #   LATIN SMALL LETTER BETA
        0xA7B6, #   LATIN CAPITAL LETTER OMEGA
        0xA7B7, #   LATIN SMALL LETTER OMEGA
        0xA7DA, #   LATIN CAPITAL LETTER LAMBDA
        0xA7DB, #   LATIN SMALL LETTER LAMBDA
        0xA7DC, #   LATIN CAPITAL LETTER LAMBDA WITH STROKE

    ]
    if self.uniNumber in latinGreeks:
        self.scriptTag = scriptPrefixes['latingreek']

    self.edit("MODIFIER", "mod")
    self.edit("REVERSED", "reversed")
    self.replace("EGYPTOLOGICAL", "egypt")

    self.edit("WITH HORIZONTAL", "horizontal")
    self.edit("HORIZONTAL", "horizontal")
    self.edit("BROKEN", "broken")
    self.edit("INSULAR", "insular")
    self.edit("EPIGRAPHIC", "epigraphic")

    self.replace("WITH STROKE THROUGH DESCENDER", "strokedescender")
    self.replace("WITH DOT", "dot")
    self.replace("WITH STROKE", "stroke")
    self.replace("WITH DIAGONAL", "diagonal")
    self.replace("WITH SQUIRREL TAIL", "tail")

    self.edit("SIGN")
    self.replace("SHORT", "short")

    self.processAs("Helper Diacritics")
    self.processAs("Helper Shapes")

    self.edit("LONG")
    self.edit("OVERLAY")
    self.edit("HIGH")
    self.edit("AND")
    self.edit("WITH")

    allCaps = [
        "AA", "AO", "AU", "AV", "AY",
        "OO"
        ]
    shouldHandleShape = True
    for cap in allCaps:
        if self.has("CAPITAL LETTER %s" % cap):
            shouldHandleShape = False

    if shouldHandleShape:
        self.handleCase()
    else:
        self.replace("CAPITAL")




    self.edit("LETTER")


    if not self.has("CAPITAL"):
        self.lower()

    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Latin Extended-D")
