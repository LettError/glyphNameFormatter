# Combining Diacritical Marks for Symbols
#combining_diacritical_marks_for_symbols

# camelcase looks good for the longer names
# but the range Combining Diacritical Marks Supplement
# does everything lowercase.

def process(self):

    self.edit("COMBINING")
    self.edit("OPEN")
    self.edit("ACCENT")
    self.edit("FLATTENED", "flat")

    self.processAs("Helper Diacritics")
    self.handleCase()

    self.camelCase()
    self.compress()
    self.scriptPrefix()
        

if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Combining Diacritical Marks for Symbols")
