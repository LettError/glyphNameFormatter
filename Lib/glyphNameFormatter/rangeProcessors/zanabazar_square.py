
def process(self):
    self.edit("LETTER")
    self.edit("SQUARE")
    self.edit("ZANABAZAR")
    self.edit("-A", 'dashA')
    self.edit("DOUBLE-LINED", 'dbllined')
    self.edit("CLUSTER-INITIAL", 'clusterinit')
    self.edit("CLUSTER-FINAL", 'clusterfina')
    self.scriptPrefix()
    self.lower()
    self.compress()


if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Zanabazar Square")
