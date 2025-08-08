
def process(self):
    self.handleCase()
    self.camelCase()
    

if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Latin Extended-F")
