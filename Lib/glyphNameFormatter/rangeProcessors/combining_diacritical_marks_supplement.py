
def process(self):
    self.edit("LATIN")

    self.edit("BREVE-MACRON", "brevemacron")
    self.edit("MACRON-BREVE", "macronbreve")
    self.edit("GRAVE-MACRON", "gravemacron")
    self.edit("MACRON-GRAVE", "macrongrave")
    self.edit("ACUTE-MACRON", "acutemacron")
    self.edit("MACRON-ACUTE", "macronacute")

    self.edit("GRAVE-ACUTE-GRAVE", "graveacutegrave")
    self.edit("ACUTE-GRAVE-ACUTE", "acutegraveacute")

    self.edit("COMBINING")
    self.edit("OPEN")
    self.edit("ACCENT")
    self.edit("FLATTENED", "flat")

    self.processAs("Helper Diacritics")
    self.handleCase()

    self.lower()
    self.compress()
    self.scriptPrefix()

if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Combining Diacritical Marks Supplement")
