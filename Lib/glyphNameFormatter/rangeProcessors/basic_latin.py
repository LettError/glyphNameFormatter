# -*- coding: UTF-8 -*-


def process(self):
    self.edit("LATIN")
    if self.has("DIGIT"):
        self.edit("DIGIT", "")
        self.lower()
    self.edit("SPACE", "space")
    self.edit("EXCLAMATION MARK", "exclam")
    self.edit("QUESTION MARK", "question")
    self.edit("QUOTATION MARK", "quotedbl")
    self.edit("NUMBER SIGN", "numbersign")
    self.edit("DOLLAR SIGN", "dollar")
    self.edit("PERCENT SIGN", "percent")
    self.edit("PLUS SIGN", "plus")
    self.edit("SEMICOLON", "semicolon")
    self.edit("MULTIPLICATION SIGN", "multiply")
    self.edit("DIVISION SIGN", "divide")
    self.edit("COLON", "colon")
    self.edit("COMMA", "comma")
    self.edit("EQUALS SIGN", "equal")
    self.edit("LESS-THAN SIGN", "less")
    self.edit("GREATER-THAN SIGN", "greater")
    self.edit("REVERSE SOLIDUS", "backslash")
    self.edit("SOLIDUS", "slash")
    self.edit("VERTICAL LINE", "bar")
    self.edit("HYPHEN-MINUS", "hyphen")
    self.edit("AMPERSAND", "ampersand")
    self.edit("ASTERISK", "asterisk")
    self.edit("APOSTROPHE", "quotesingle")
    self.edit("FULL STOP", "period")
    self.edit("LOW LINE", "underscore")
    self.edit("CIRCUMFLEX ACCENT", "asciicircum")
    self.edit("GRAVE ACCENT", "grave")
    self.edit("TILDE", "tilde")

    self.edit("SQUARE BRACKET", "bracket")
    self.edit("CURLY BRACKET", "brace")
    self.edit("PARENTHESIS", "parenthesis")
    self.edit("LEFT", "left")
    if self.has("RIGHT") and not self.has("COPYRIGHT"):
        self.replace("RIGHT")
        self.suffix("right")
    self.handleCase()
    return True

if __name__ == "__main__":
    from glyphNameFormatter import GlyphName
    from glyphNameFormatter.unicodeRangeNames import getRangeByName

    for u in range(*getRangeByName("Basic Latin")):
        g = GlyphName(uniNumber=u)
        print g.getName().ljust(50), "%04X" % g.uniNumber, "\t", g.uniName