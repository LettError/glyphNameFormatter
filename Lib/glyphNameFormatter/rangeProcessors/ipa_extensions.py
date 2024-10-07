from glyphNameFormatter.data.scriptPrefixes import scriptPrefixes

def process(self):


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
    self.processAs("Helper Latin Greeks")
    self.compress()


if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("IPA Extensions")
