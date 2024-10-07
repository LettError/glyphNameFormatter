
def process(self):
    self.edit("-", " ")
    self.camelCase()
    

if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Miscellaneous Symbols and Arrows")
