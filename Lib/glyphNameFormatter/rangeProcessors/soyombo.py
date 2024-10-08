
def process(self):
    self.edit("CLUSTER-INITIAL", "ClusterInitial")
    self.edit("SOYOMBO LETTER", "")
    self.edit("SOYOMBO VOWEL SIGN", "VowelSign")
    self.edit("SOYOMBO", "")
    self.camelCase()
    self.forceScriptPrefix("Soyombo")

if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Soyombo")
