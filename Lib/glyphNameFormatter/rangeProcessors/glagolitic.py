
def process(self):

    # handle conflict with Yu Arabic
    if self.uniNumber == 0x2C53:
        self.forceScriptPrefix("Glagolitic")

    self.edit("GLAGOLITIC")


    self.handleCase()
    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Glagolitic")
