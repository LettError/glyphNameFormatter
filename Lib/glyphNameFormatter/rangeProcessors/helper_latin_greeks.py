from glyphNameFormatter.data.scriptPrefixes import scriptPrefixes

# Some Greek letters make a guest appearance in the Latin ranges.
# Some in Latin extended, some in IPa
# This gives all these a separate script prefix, "ltgr" or "latingreek".
# This designation has no linguistic value. By setting the "latingreek"
# script, all these letters will get the same treatment.

def process(self):
    latinGreeks = [
        # these need to be prefixed as latin. 
        0x0251, #   LATIN SMALL LETTER ALPHA
        0x0263, #   LATIN SMALL LETTER GAMMA
        0x0269, #   LATIN SMALL LETTER IOTA
        0x0277, #   LATIN SMALL LETTER CLOSED OMEGA
        0x0278, #   LATIN SMALL LETTER PHI
        0xA7B3, #   LATIN CAPITAL LETTER CHI
        0xA7B4, #   LATIN CAPITAL LETTER BETA
        0xA7B5, #   LATIN SMALL LETTER BETA
        0xA7B5, #   LATIN SMALL LETTER BETA
        0xA7B6, #   LATIN CAPITAL LETTER OMEGA
        0xA7B7, #   LATIN SMALL LETTER OMEGA


        0xA7DA, #   LATIN CAPITAL LETTER LAMBDA
        0xA7DB, #   LATIN SMALL LETTER LAMBDA
        0xA7DC, #   LATIN CAPITAL LETTER LAMBDA WITH STROKE
        0xAB30, #   ꬰ    LATIN SMALL LETTER BARRED ALPHA
        0xAB53, #   ꭓ    LATIN SMALL LETTER CHI
        0xAB54, #   ꭔ    LATIN SMALL LETTER CHI WITH LOW RIGHT RING
        0xAB55, #   ꭕ    LATIN SMALL LETTER CHI WITH LOW LEFT SERIF
        0xAB64, #   ꭤ    LATIN SMALL LETTER INVERTED ALPHA
        0xAB65, #   ꭥ    GREEK LETTER SMALL CAPITAL OMEGA
    ]

    if self.uniNumber in latinGreeks:
        self.scriptTag = scriptPrefixes['latingreek']

