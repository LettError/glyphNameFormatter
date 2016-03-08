
def processDiacritics(self):
    if self.verbose:
        print "processDiacritics"
    # WITH ___ AND ___
    self.edit("WITH CIRCUMFLEX AND HOOK ABOVE", "circumflex", "hoi")
    self.edit("WITH CIRCUMFLEX AND DOT BELOW", "circumflex", "dotbelow")
    self.edit("WITH DOT BELOW AND DOT ABOVE", "dotbelow", "dotabove")
    self.edit("WITH CIRCUMFLEX AND TILDE", "circumflex", "tilde")
    self.edit("WITH CARON AND DOT ABOVE", "caron", "dot")
    self.edit("WITH ACUTE AND DOT ABOVE", "acute", "dotaccent")
    self.edit("WITH HORN AND GRAVE", "horn", 'grave')
    self.edit("WITH HORN AND ACUTE", "horn", 'acute')
    self.edit("WITH HORN AND TILDE", "horn", 'tilde')
    self.edit("WITH HORN AND HOOK ABOVE", "horn", "hoi")
    self.edit("WITH HORN AND DOT BELOW", "horn", "dotbelow")
    self.edit("WITH BREVE AND TILDE", "breve", "tilde")
    self.edit("WITH BREVE AND ACUTE", "breve", "acute")
    self.edit("WITH BREVE AND HOOK ABOVE", "breve", "hoi")
    self.edit("WITH BREVE AND DOT BELOW", "breve", "dotbelow")
    self.edit("WITH BREVE BELOW", "breve", "below")
    self.edit("WITH TILDE AND DIAERESIS", "tilde", self.prefSpelling_dieresis)
    self.edit("WITH BREVE AND GRAVE", "breve", "grave")
    self.edit("WITH DOT BELOW AND MACRON", "macron", "dot")
    self.edit("WITH DIAERESIS AND GRAVE", self.prefSpelling_dieresis, "grave")
    self.edit("WITH DIAERESIS AND ACUTE", self.prefSpelling_dieresis, "acute")
    self.edit("WITH DIAERESIS AND TILDE", self.prefSpelling_dieresis, "tilde")
    self.edit("WITH DIAERESIS AND CARON", self.prefSpelling_dieresis, "caron")
    self.edit("WITH TILDE BELOW", "tilde", "below")
    self.edit('WITH CIRCUMFLEX AND ACUTE', 'circumflex', 'acute')
    self.edit('WITH CIRCUMFLEX AND GRAVE', 'circumflex', 'grave')
    self.edit("WITH CIRCUMFLEX BELOW", "circumflex", "below")
    self.edit("WITH CEDILLA AND ACUTE", "cedilla", "acute")
    self.edit("WITH CEDILLA AND BREVE", "cedilla", 'breve')
    self.edit("WITH MACRON AND DIAERESIS", "macron", self.prefSpelling_dieresis)
    self.edit("WITH MACRON AND ACUTE", "macron", "acute")
    self.edit("WITH MACRON AND GRAVE", "macron", "grave")
    self.edit("WITH TILDE AND ACUTE", "tilde", "acute")
    self.edit("WITH TILDE AND MACRON", "tilde", "macron")
    self.edit("WITH DIAERESIS AND MACRON", self.prefSpelling_dieresis, "macron")
    self.edit("WITH DOT ABOVE AND MACRON", "dot", "macron")
    # PRECEDED BY ___
    self.edit("PRECEDED BY APOSTROPHE", "apostrophe")
    # WITH ___
    self.edit("WITH INVERTED BREVE", "inverted", "breve")
    self.edit("WITH TOPBAR", "topbar")
    self.edit("WITH MIDDLE DOT", "dot")
    self.edit("WITH DOUBLE ACUTE", "dblacute")
    self.edit("WITH DOUBLE GRAVE ACCENT", "dblgrave")
    self.edit("WITH DOUBLE GRAVE", "dblgrave")
    self.edit("WITH DOT ABOVE", "dot")
    self.edit("WITH DOT BELOW", "dotbelow")
    self.edit("WITH GRAVE", "grave")
    self.edit("GRAVE", "grave")
    self.edit("WITH HORN", "horn")
    self.edit("WITH BREVE", "breve")
    self.edit("BREVE", "breve")
    self.edit("WITH DIAERESIS BELOW", self.prefSpelling_dieresis, "below")
    self.edit("WITH DIAERESIS", self.prefSpelling_dieresis)
    self.edit("DIAERESIS", self.prefSpelling_dieresis)
    self.edit("WITH OGONEK AND MACRON", "ogonek", "macron")
    self.edit("WITH MACRON", "macron")
    self.edit("MACRON", "macron")
    self.edit("WITH STROKE AND ACUTE", "slash", "acute")
    self.edit("WITH RING ABOVE AND ACUTE", "ring", "acute")
    self.edit("WITH ACUTE", "acute")
    self.edit("ACUTE", "acute")
    self.edit("WITH CARON", "caron")
    self.edit("CARON", "caron")
    self.edit("WITH CIRCUMFLEX", "circumflex")
    self.edit("CIRCUMFLEX", "circumflex")
    self.edit("WITH TILDE", "tilde")
    self.edit("TILDE", "tilde")
    self.edit("WITH CEDILLA", "cedilla")
    self.edit("CEDILLA", "cedilla")
    self.edit("WITH OGONEK", "ogonek")
    self.edit("OGONEK", "ogonek")

    self.edit("WITH RING ABOVE", "ring")
    self.edit("WITH RING BELOW", "ringbelow")
    self.edit("WITH RIGHT HALF RING", "right", "halfring")
    self.edit("WITH RETROFLEX HOOK", "retroflex")
    self.edit("WITH LINE BELOW", "linebelow")
    self.edit("WITH BAR", "bar")
    self.edit("WITH MACRON", "macron")
    self.edit("WITH MIDDLE TILDE", 'middletilde')
    self.edit("WITH HOOK TAIL", "hook", "tail")
    self.edit("WITH MIDDLE HOOK", "middlehook")
    self.edit("WITH LOOP", "loop")
    self.edit("WITH LEFT HOOK", "hook", "left")
    self.edit("WITH HOOK ABOVE", "hoi")
    self.edit("WITH HOOK", "hook")
    self.edit("AND HOOK", "hook")
    self.edit("HOOK", "hook")
    self.edit("WITH CURL", "curl")

    self.edit("WITH STROKE", "stroke")
    self.edit("STROKE", "stroke")

    if self.has("BAR") and not self.has("AKBAR") and not self.has("TOPBAR") and not self.has("BARRED"):
        if self.replace("BAR"):
            self.suffix("bar")
