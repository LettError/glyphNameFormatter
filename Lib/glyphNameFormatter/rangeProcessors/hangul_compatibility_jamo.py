

def process(self):
    self.edit("HANGUL")
    self.edit("LETTER")
    self.edit("-")
    self.lower()
    self.compress()
    self.scriptTag = self.scriptTag + "Compa"
    self.scriptPrefix()

if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Hangul Compatibility Jamo")
