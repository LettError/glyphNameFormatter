
def process(self):
    self.edit("Characters")
    self.edit("MAHJONG TILE", "Mahjong")
    self.camelCase()
    

if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Mahjong Tiles")
