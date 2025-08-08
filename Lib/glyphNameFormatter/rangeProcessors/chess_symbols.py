
def process(self):
    self.edit("CHESS", "")

    knightPieces = {
        0xFA4E:     'white Knight Queen'  ,   # 🩎    WHITE CHESS KNIGHT-QUEEN
        0x1FA4F:    'white Knight Rook' ,   #  🩏    WHITE CHESS KNIGHT-ROOK
        0x1FA50:    'white Knight Bishop' ,   #  🩐    WHITE CHESS KNIGHT-BISHOP
        0x1FA51:    'black Knight Queen' ,   #  🩑    BLACK CHESS KNIGHT-QUEEN
        0x1FA52:    'black Knight Rook' ,   #  🩒    BLACK CHESS KNIGHT-ROOK
        0x1FA53:    'black Knight Bishop' ,   #  🩓    BLACK CHESS KNIGHT-BISHOP    self.edit("ROTATED FORTY-FIVE DEGREES", "45")
    }
    if self.uniNumber in knightPieces:
        self.uniNameProcessed = knightPieces[self.uniNumber]


    self.edit("ROTATED FORTY-FIVE DEGREES", "45")
    self.edit("ROTATED NINETY DEGREES", "90")
    self.edit("ROTATED ONE HUNDRED THIRTY-FIVE DEGREES", "135")
    self.edit("ROTATED TWO HUNDRED TWENTY-FIVE DEGREES", "225")
    self.edit("ROTATED TWO HUNDRED SEVENTY DEGREES", "270")
    self.edit("ROTATED THREE HUNDRED FIFTEEN DEGREES", "315")
    self.edit("TURNED", "Turned")
    self.edit("XIANGQI", "Xq")
    self.camelCase()
    #self.edit("TAMIL")
    #self.edit("LETTER")
    pass
    

if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Chess Symbols")
