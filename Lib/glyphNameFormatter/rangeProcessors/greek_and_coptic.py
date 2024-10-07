
def process(self):
    self.replace("GREEK")

    self.edit("COPTIC", "coptic")

    self.edit("ARCHAIC", "archaic")
    self.edit("PAMPHYLIAN", "pamphylian")

    # following the AGD list
    #self.edit("YPOGEGRAMMENI", "iotasubscript")
    # could also be
    # self.edit("YPOGEGRAMMENI", "iotalenissubscript")
    # self.edit("YPOGEGRAMMENI", "ypogegrammeni")

    #self.replace("LETTER LAMDA", "Lambda")
    self.replace("LAMDA", "Lambda")

    self.replace("LETTER DIGAMMA", "Digamma")
    self.replace("LETTER KOPPA", "Koppa")
    self.replace("LETTER STIGMA", "Stigma")
    self.replace("LETTER SAMPI", "Sampi")
    self.replace("LETTER YOT", "yot")

    self.edit("LOWER NUMERAL SIGN", "lownumeralsign")
    self.edit("NUMERAL SIGN", "numeralsign")
    self.edit("QUESTION MARK", "question")

    self.edit("ANO TELEIA", "anoteleia")
    self.edit("SMALL REVERSED LUNATE SIGMA SYMBOL", "sigmalunatereversedsymbol")
    self.edit("SMALL DOTTED LUNATE SIGMA SYMBOL", "sigmalunatedottedsymbol")
    self.edit("SMALL REVERSED DOTTED LUNATE SIGMA SYMBOL", "sigmalunatedottedreversedsymbol")
    self.edit("CAPITAL REVERSED LUNATE SIGMA SYMBOL", "Sigmareversedlunatesymbol")
    self.edit("CAPITAL DOTTED LUNATE SIGMA SYMBOL", "Sigmalunatesymboldotted")
    self.edit("CAPITAL LUNATE SIGMA SYMBOL", "Sigmalunatesymbol")
    self.edit("LUNATE SIGMA SYMBOL", "sigmalunatesymbol")
    self.edit("REVERSED LUNATE EPSILON SYMBOL", "epsilonreversedlunatesymbol")
    self.edit("LUNATE EPSILON SYMBOL", "epsilonlunatesymbol")

    self.edit("RHO WITH STROKE SYMBOL", "rhostrokesymbol")
    self.edit("UPSILON SYMBOL", "upsilonsymbol")
    self.edit("PHI SYMBOL", "phi.math")
    self.edit("CAPITAL KAI SYMBOL", "Kaisymbol")
    self.edit("KAI SYMBOL", "kaisymbol")
    self.edit("PI SYMBOL", "pi.math")
    self.edit("CAPITAL THETA SYMBOL", "Thetasymbol")
    self.edit("THETA SYMBOL", "theta.math") # XX ?
    self.edit("BETA SYMBOL", "betasymbol")
    self.edit("UPSILON SYMBOL", "upsilonsymbol")
    self.edit("KAPPA SYMBOL", "kappa.math")
    self.edit("RHO SYMBOL", "rhosymbol")
    if self.has("SIGMA SYMBOL"):
        if self.replace("SYMBOL"):
            self.suffix("symbol")
    # with
    self.edit("UPSILON WITH HOOK SYMBOL", "Upsilonhooksymbol")
    self.edit("UPSILON WITH ACUTE AND HOOK SYMBOL", "Upsilonacutehooksymbol")
    self.edit("UPSILON WITH DIAERESIS AND HOOK SYMBOL", "Upsilona%shooksymbol" % self.prefSpelling_dieresis)
    self.edit("WITH TONOS", "tonos")

    self.processAs("Helper Greek Diacritics")

    # dont use script tags when greek chars are in latin ranges,
    # the latin char will have automically the script tag prefix/suffix
    greekFirstUnicodes = [
        0x037A,  # iotasubscript
        0x0392,  # Beta
        0x03A7,  # Chi
        0x03A8,  # Psi
        0x03A9,  # Omega
        0x03B1,  # alpha
        0x03B2,  # beta
        0x03B3,  # gamma
        0x03B9,  # iota
        0x039B,  # Lambda  
        0x03BB,  # lambda  
        0x03BC,  # mu
        0x03BD,  # nu
        0x03BE,  # xi
        0x03C0,  # pi
        0x03A5,  # Upsilon
        0x03C5,  # upsilon
        0x03C6,  # phi
        0x03C7,  # chi
        0x03C8,  # psi
        0x03C9,  # omega
        0x03DE,  # Koppa
        0x03DF,  # koppa
        0x03F8,  # sho
        0x0927,  # delta

]

    if self.uniNumber in greekFirstUnicodes:
        self.scriptTag = ""

    self.handleCase()
    self.compress()


if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Greek and Coptic")
