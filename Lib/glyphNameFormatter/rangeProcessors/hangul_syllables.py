
def process(self):
    self.setExperimental()
    self.edit("HANGUL")
    self.edit("SYLLABLE")
    self.lower()
    self.scriptPrefix()


if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Hangul Syllables")
