

# The names in this range are quite long, but not really
# any redundancy in the words. It is all relevant and 
# even contractions from rightward to right already cause
# duplicates. So, camelCase seems like a reasonable approach.
# Names are still very long though. What is the preference?
# arrowPointingRightwardsThenCurvingDownwards                             -                             2967   ⥧    LEFTWARDS HARPOON WITH BARB DOWN ABOVE RIGHTWARDS HARPOON WITH BARB DOWN


def process(self):
    self.setExperimental()
    self.edit("-", " ")
    self.camelCase()


if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Supplemental Arrows-B")
