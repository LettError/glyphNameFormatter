from glyphNameFormatter.data.scriptPrefixes import scriptPrefixes

def process(self):
    self.scriptTag = scriptPrefixes['kannada']
    self.edit("KANNADA")
    self.edit("LETTER")
    self.edit("DIGIT")
    self.edit("VOWEL SIGN VOCALIC", "vocalsign")
    self.edit("VOWEL SIGN", "sign")
    self.edit("VOCALIC", "vocal")

    self.edit("LENGTH MARK", "length")

    self.edit("SIGN NUKTA", "nukta")
    self.edit("SIGN VIRAMA", "virama")
    self.edit("SIGN AVAGRAHA", "avagraha")
    self.edit("SIGN VISARGA", "visarga")
    self.edit("SIGN ANUSVARA", "anusvara")
    self.edit("SIGN JIHVAMULIYA", "jihvamuliya")
    self.edit("SIGN UPADHMANIYA", "upadhmaniya")

    self.processAs("Helper Digit Names")
    self.lower()
    self.compress()


if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Kannada")
