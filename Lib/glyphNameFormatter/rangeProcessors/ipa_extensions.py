from glyphNameFormatter.data.scriptPrefixes import scriptPrefixes

def process(self):

    latinGreeks = [
        # these need to be prefixed as latin. 
        0xA7DA, #   LATIN CAPITAL LETTER LAMBDA
        0xA7DB, #   LATIN SMALL LETTER LAMBDA
        0xA7DC, #   LATIN CAPITAL LETTER LAMBDA WITH STROKE
        0xA7DC, #   LATIN CAPITAL LETTER LAMBDA WITH STROKE
        0xA7B3, #   LATIN CAPITAL LETTER CHI
        0xA7B4, #   LATIN CAPITAL LETTER BETA
        0xA7B5, #   LATIN SMALL LETTER BETA
        0xA7B6, #   LATIN CAPITAL LETTER OMEGA
        0xA7B7, #   LATIN SMALL LETTER OMEGA
        0x0278, #   LATIN SMALL LETTER PHI
        0x0277, #   LATIN SMALL LETTER CLOSED OMEGA
        0x0269, #   LATIN SMALL LETTER IOTA
        0x0263, #   LATIN SMALL LETTER GAMMA
        0x0251, #   LATIN SMALL LETTER ALPHA
    ]
    if self.uniNumber in latinGreeks:
        self.forceLatinScriptTag = True
        self.scriptTag = scriptPrefixes['latingreek']

    self.edit("LATIN")
    self.edit("OPEN", "open")
    self.edit("WITH FISHHOOK", "fishhook")
    self.edit("SCRIPT", "script")
    self.edit("WITH BELT", "belt")
    self.edit("WITH MIDDLE TILDE", "middletilde")
    self.edit("WITH LONG LEG", "longleg")
    self.edit("WITH CROSSED-TAIL", "crossedtail")
    self.edit("BILABIAL", "bilabial")
    self.edit("BIDENTAL", "bidental")
    self.edit("STRETCHED", "stretched")
    self.edit("WITH STROKE", "stroke")
    self.edit("SQUAT", "squat")
    self.edit("INVERTED", "inverted")
    self.edit("REVERSED", "reversed")
    
    self.replace("DZ", "dzed")
    self.replace("LZ", "lzed")
    self.replace("DIGRAPH")
    self.replace("PERCUSSIVE", "percussive")
    self.replace("GLOTTAL", "glottal")
    self.replace("STOP", "stop")
    self.replace("PHARYNGEAL", "pharyngeal")
    self.replace("VOICED", "voiced")
    self.replace("FRICATIVE", "fricative")

    self.replace("LETTER CLICK", "click")
    self.replace("LETTER GLOTTAL STOP WITH STROKE", "glottalstopstroke")
    self.replace("LETTER SMALL CAPITAL OE", "OEsmall")

    


    self.processAs("Helper Diacritics")
    self.processAs("Helper Shapes")

    self.handleCase()
    self.replace("LETTER")
    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("IPA Extensions")
