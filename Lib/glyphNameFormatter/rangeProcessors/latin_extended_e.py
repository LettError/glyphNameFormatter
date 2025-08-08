from glyphNameFormatter.data.scriptPrefixes import scriptPrefixes


def process(self):

    self.edit("MODIFIER LETTER LEFT TACK", "modLetterLeftTack")
    self.edit("MODIFIER LETTER RIGHT TACK", "modLetterRightTack")

    self.edit("LENIS", "lenis")
    self.edit("WITH CROSSED-TAIL", "tail")
    self.edit("SCRIPT", "script")
    self.edit("BLACKLETTER", "fractur")
    self.edit("REVERSED-SCHWA", "reversedschwa")
    self.edit("WITH INVERTED LAZY S", "lazyinverteds")
    self.edit("OPEN-O", "oopen")
    if self.has("LATIN SMALL LETTER CHI"):
        self.edit("LATIN SMALL LETTER CHI", 'chi')
        self.edit("WITH LOW RIGHT RING", 'lowrightring')
        self.edit("WITH LOW LEFT SERIF", 'lowleftserif')
        self.scriptTag = scriptPrefixes['latingreek']


    self.processAs("Latin Extended-C")

    self.edit("MODIFIER", "mod")

    if self.has("GREEK"):
        self.edit("GREEK")

    self.processAs("Helper Latin Greeks")


    self.edit("-")

    self.compress()


if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Latin Extended-E")
