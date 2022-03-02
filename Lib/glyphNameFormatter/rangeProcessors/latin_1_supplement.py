
def process(self):
    self.edit("LATIN")

    self.edit("NO-BREAK SPACE", "nbspace")

    self.replace("EXCLAMATION MARK", "exclam")
    self.replace("QUESTION MARK", "question")
    if self.has("INVERTED"):
        if self.replace("INVERTED"):
            self.suffix("down")

    self.replace("CENT SIGN", "cent")
    self.replace("POUND SIGN", "sterling")
    self.replace("CURRENCY SIGN", "currency")
    self.replace("YEN SIGN", "yen")
    self.replace("BROKEN BAR", "brokenbar")
    self.replace("SECTION SIGN", "section")
    self.replace("COPYRIGHT SIGN", "copyright")
    self.replace("FEMININE ORDINAL INDICATOR", "ordfeminine")
    self.replace("MASCULINE ORDINAL INDICATOR", "ordmasculine")
    self.replace("NOT SIGN", "logicalnot")
    self.replace("SOFT HYPHEN", "hyphensoft")
    self.replace("REGISTERED SIGN", "registered")
    self.replace("DEGREE SIGN", "degree")
    self.replace("PLUS-MINUS SIGN", "plusminus")
    self.replace("SUPERSCRIPT ONE", "one.superior")
    self.replace("SUPERSCRIPT TWO", "two.superior")
    self.replace("SUPERSCRIPT THREE", "three.superior")
    self.replace("MICRO SIGN", "mu.math")
    self.replace("PILCROW SIGN", "paragraph")
    self.replace("MIDDLE DOT", 'periodcentered')

    self.edit("ACUTE ACCENT", "acute")
    self.edit("CIRCUMFLEX ACCENT", "circumflex")
    self.edit("GRAVE ACCENT", "grave")

    self.edit("LEFT-POINTING DOUBLE ANGLE QUOTATION MARK", "guillemet", "left")  # or guillemot ?
    self.edit("RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK", "guillemet", "right")  # or guillemot ?

    self.replace("VULGAR FRACTION ONE QUARTER", "onequarter")
    self.replace("VULGAR FRACTION ONE HALF", "onehalf")
    self.replace("VULGAR FRACTION THREE QUARTERS", "threequarters")

    self.replace("MULTIPLICATION SIGN", "multiply")
    self.replace("DIVISION SIGN", "divide")

    self.replace("CAPITAL LETTER AE", "AE")
    self.replace("WITH STROKE", "slash")
    self.replace("SMALL LETTER SHARP S", "germandbls")

    self.processAs("Helper Diacritics")

    self.handleCase()
    self.compress()


if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange

    printRange("Latin-1 Supplement")
