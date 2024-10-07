

def process(self):
    # edits go here
    self.edit("LATIN")

    self.edit("WITH")

    parts = [
        "OPEN", "STROKE", "TURNED", "REVERSED",
        "SIDEWAYS", "SUBSCRIPT",
        "TOP", "BOTTOM",
        "RETROFLEX", "SCRIPT",
        "HALF", "INSULAR",
        "VOICED", "LARYNGEAL",
        ]
    for part in parts:
        self.edit(part, part.lower())

    self.edit("BARRED", "bar")
    self.edit("STRIKETHROUGH", "strike")
    self.edit("DIAERESIZED", self.prefSpelling_dieresis+"ed")

    self.replace("SPIRANT", "spirant")
    self.replace("LAMDA", "lambda")
    self.replace("LETTER SMALL CAPITAL L", "Lsmall")
    self.replace("LETTER SMALL CAPITAL N", "Nsmall")
    self.replace("LETTER SMALL CAPITAL R", "Rsmall")
    self.replace("SMALL CAPITAL LETTER U", "Usmall")
    self.replace("SMALL CAPITAL LETTER I", "Ismall")
    self.replace("LETTER SMALL CAPITAL EL", "Elsmall")

    if self.has("AIN"):
        # this is a conflic with ARABIC LETTER AIN
        # and we prefer to not have the prefix in arabic
        self.replace("AIN", "ain")
        self.scriptPrefix()

    self.replace("LETTER SMALL CAPITAL AE", "AEsmall")
    self.replace("LETTER SMALL CAPITAL OU", "OUsmall")

    self.edit("FISHHOOK AND MIDDLE TILDE", "fishmiddletilde")
    self.processAs("Helper Diacritics")

    if self.has("GREEK"):
        self.edit("GREEK")
        self.forceScriptPrefix("greek")
        self.handleCase()
    elif self.has("CYRILLIC"):
        self.edit("CYRILLIC")
        self.handleCase()
        self.forceScriptPrefix("cyrillic")
    else:
        self.handleCase()

    self.edit("MODIFIER", "mod")
    self.edit("LETTER")

    self.compress()
    #self.scriptPrefix()

if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Phonetic Extensions")
