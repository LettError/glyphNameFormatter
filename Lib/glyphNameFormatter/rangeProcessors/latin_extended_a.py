
def process(self):
    self.edit("LATIN")

    self.edit("CAPITAL LETTER G WITH CEDILLA", "Gcommaaccent")
    self.edit("SMALL LETTER G WITH CEDILLA", "gcommaaccent")
    self.edit("CAPITAL LETTER H WITH STROKE", "Hbar")
    self.edit("SMALL LETTER H WITH STROKE", "hbar")
    self.edit("CAPITAL LETTER K WITH CEDILLA", "Kcommaaccent")
    self.edit("SMALL LETTER K WITH CEDILLA", "kcommaaccent")
    self.edit("CAPITAL LETTER L WITH CEDILLA", "Lcommaaccent")
    self.edit("SMALL LETTER L WITH CEDILLA", "lcommaaccent")
    self.edit("CAPITAL LETTER N WITH CEDILLA", "Ncommaaccent")
    self.edit("SMALL LETTER N WITH CEDILLA", "ncommaaccent")
    self.edit("CAPITAL LETTER R WITH CEDILLA", "Rcommaaccent")
    self.edit("SMALL LETTER R WITH CEDILLA", "rcommaaccent")
    self.edit("CAPITAL LETTER T WITH STROKE", "Tbar")
    self.edit("SMALL LETTER T WITH STROKE", "tbar")
    self.edit("CAPITAL LETTER L WITH STROKE", "Lslash")
    self.edit("SMALL LETTER L WITH STROKE", "lslash")
    self.edit("CAPITAL LETTER D WITH STROKE", "Dcroat")
    self.edit("SMALL LETTER D WITH STROKE", "dcroat")

    self.edit("WITH DOUBLE ACUTE", "hungarumlaut")

    self.edit("SMALL LETTER L WITH MIDDLE DOT", "ldot")
    self.edit("CAPITAL LETTER L WITH MIDDLE DOT", "Ldot")

    self.replace("CAPITAL LIGATURE IJ", "IJ")
    self.replace("SMALL LIGATURE IJ", "ij")

    self.replace("SMALL LIGATURE OE", "oe")
    self.replace("CAPITAL LIGATURE OE", "OE")

    self.processAs("Helper Diacritics")

    self.editSuffix("dot", 'dotaccent')
    self.handleCase()
    self.compress()


if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Latin Extended-A")
