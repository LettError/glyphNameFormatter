from glyphNameFormatter.data.scriptPrefixes import scriptPrefixes

def process(self):
    # edits go here
    self.edit("LATIN")

    self.replace("MODIFIER LETTER LOW CIRCUMFLEX ACCENT", "circumflexlow")
    

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

    self.processAs("Helper Latin Greeks")



    self.edit("LETTER")


    if not self.has("CAPITAL"):
        self.lower()

    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Latin Extended-D")
