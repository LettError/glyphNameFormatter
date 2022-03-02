

def process(self):
    self.edit("LATIN")
    # edits go here
    self.edit("CAPITAL LETTER D WITH CEDILLA", "Dcommaaccent")
    self.edit("SMALL LETTER D WITH CEDILLA", "dcommaaccent")
    self.replace("CAPITAL LETTER MIDDLE-WELSH LL", "LLwelsh")

    # self.edit("WITH DOT BELOW AND DOT ABOVE", "dotbelow", "dotaccent")
    # self.edit("WITH DOT BELOW", "dotbelow")
    # self.edit("WITH DOT ABOVE", "dotaccent")
    # self.edit("AND DOT ABOVE", "dotacent")
    self.edit("MIDDLE-WELSH", "welsh")

    self.replace("CAPITAL LETTER SHARP S", "Germandbls")

    self.forceScriptPrefix("latin", "SMALL LETTER DELTA", "delta")

    self.processAs("Helper Diacritics")
    self.handleCase()
    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Latin Extended Additional")
