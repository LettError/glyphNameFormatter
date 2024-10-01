from glyphNameFormatter.data.scriptPrefixes import scriptPrefixes


def process(self):
    #self.setDraft()


    latinGreeks = [
        # these need to be prefixed as latin. 
        0xAB30, #   ꬰ    LATIN SMALL LETTER BARRED ALPHA
        0xAB53, #   ꭓ    LATIN SMALL LETTER CHI
        0xAB54, #   ꭔ    LATIN SMALL LETTER CHI WITH LOW RIGHT RING
        0xAB55, #   ꭕ    LATIN SMALL LETTER CHI WITH LOW LEFT SERIF
        0xAB64, #   ꭤ    LATIN SMALL LETTER INVERTED 
        0xAB64, #   ꭤ    LATIN SMALL LETTER INVERTED ALPHA
        0xAB65, #   ꭥ    GREEK LETTER SMALL CAPITAL OMEGA
    ]
    if self.uniNumber in latinGreeks:
        #self.suffix("ltgr")
        self.scriptTag = scriptPrefixes['latingreek']


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
        self.forceScriptPrefix("latin")


    self.processAs("Latin Extended-C")

    self.edit("MODIFIER", "mod")

    if self.has("GREEK"):
        self.edit("GREEK")
        #self.forceScriptPrefix("greek")
        self.forceScriptPrefix("latingreek")

    self.edit("-")

    self.compress()


if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Latin Extended-E")
