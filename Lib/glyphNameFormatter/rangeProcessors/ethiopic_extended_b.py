def process(self):
    self.edit("ETHIOPIC")
    self.edit("SYLLABLE")
    self.edit("TONAL")
    self.edit("GURAGE", "gurage")
    self.editToFinal("MARK", "mark")
    self.lower()
    self.compress()
    self.scriptPrefix()


if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange

    printRange("Ethiopic Extended-B")
