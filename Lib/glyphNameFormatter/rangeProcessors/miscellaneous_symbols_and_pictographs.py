
def process(self):
    self.replace("EMOJI MODIFIER FITZPATRICK TYPE-1-2", "fitz Patrick Type 1 2")
    self.replace("EMOJI MODIFIER FITZPATRICK TYPE-3", "fitz Patrick Type 3")
    self.replace("EMOJI MODIFIER FITZPATRICK TYPE-4", "fitz Patrick Type 4")
    self.replace("EMOJI MODIFIER FITZPATRICK TYPE-5", "fitz Patrick Type 5")
    self.replace("EMOJI MODIFIER FITZPATRICK TYPE-6", "fitz Patrick Type 6")

    self.replace("-", " ")
    self.replace("EUROPE-AFRICA", "Europe Africa")
    self.replace("ASIA-AUSTRALIA", "Asia Australia")
    self.edit("INPUT SYMBOL FOR SYMBOLS", "inputSymbols")
    self.edit("INPUT SYMBOL FOR NUMBERS", "inputNumbers")
    self.edit("INPUT SYMBOL FOR LATIN CAPITAL LETTERS", "inputCapLatin")
    self.edit("INPUT SYMBOL FOR LATIN SMALL LETTERS", "inputSmallLatin")
    self.edit("INPUT SYMBOL FOR LATIN LETTERS", "inputLatin")

    self.edit("SYMBOL", "")
    self.replace("FORK AND KNIFE", "fork knife")
    self.replace("BELL", "BellSymbol")
    self.replace("WITH PLATE", "plate")
    self.replace("SNOW CAPPED", "snowcapped")
    self.edit("WITH", "")
    self.replace("JACK-O-LANTERN", "jack O Lantern")
    self.edit("UP-POINTING", "Up")
    self.edit("DOWN-POINTING", "Down")
    self.replace("PERFORMING", "Performing")
    self.replace("CLOCK FACE", "clock ")
    self.replace("UPWARDS", "Up")
    self.replace("DOWNWARDS", "Down")
    self.edit("OCLOCK", "")
    self.replace("WITH YEN SIGN", "Yen")
    self.replace("WITH DOLLAR SIGN", "Dollar")
    self.replace("WITH EURO SIGN", "Euro")
    self.replace("WITH POUND SIGN", "Pound")

    self.edit("FOR", "")
    if self.uniNumber == 0x1F48D:
        self.forceScriptPrefix("Miscellaneous Symbols and Pictographs")
    

    self.camelCase()

if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Miscellaneous Symbols and Pictographs")
