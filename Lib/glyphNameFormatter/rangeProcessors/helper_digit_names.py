
def process(self):

    self.replace("JANUARY", "january")
    self.replace("FEBRUARY", "february")
    self.replace("MARCH", "march")
    self.replace("APRIL", "april")
    self.replace("MAY", "may")
    self.replace("JUNE", "june")
    self.replace("JULY", "july")
    self.replace("AUGUST", "august")
    self.replace("SEPTEMBER", "september")
    self.replace("OCTOBER", "october")
    self.replace("NOVEMBER", "november")
    self.replace("DECEMBER", "december")

    self.replace("HUNDRED", "hundred")
    self.replace("THOUSAND", "thousand")
    self.replace("THIRTY SIX", "thirtysix")
    self.replace("THIRTY SEVEN", "thirtyseven")
    self.replace("THIRTY EIGHT", "thirtyeight")
    self.replace("THIRTY NINE", "thirtynine")
    self.replace("FORTY ONE", "fortyone")
    self.replace("FORTY TWO", "fortytwo")
    self.replace("FORTY THREE", "fortythree")
    self.replace("FORTY FOUR", "fortyfour")
    self.replace("FORTY FIVE", "fortyfive")
    self.replace("FORTY SIX", "fortysix")
    self.replace("FORTY SEVEN", "fortyseven")
    self.replace("FORTY EIGHT", "fortyeight")
    self.replace("FORTY NINE", "fortynine")

    self.replace("FOURTEEN", "fourteen")
    self.replace("SIXTEEN", "sixteen")
    self.replace("SEVENTEEN", "seventeen")
    self.replace("EIGHTEEN", "eighteen")
    self.replace("NINETEEN", "nineteen")

    self.replace('ZERO', 'zero')
    self.replace('ONE', 'one')
    self.replace('TWO', 'two')
    self.replace('THREE', 'three')
    self.replace('FOUR', 'four')
    self.replace('FIVE', 'five')
    self.replace('SIX', 'six')
    self.replace('SEVEN', 'seven')
    self.replace('EIGHT', 'eight')
    self.replace('NINE', 'nine')
    self.replace("TEN", "ten")
    self.replace("ELEVEN", "eleven")
    self.replace("TWELVE", "twelve")
    self.replace("THIRTEEN", "thirteen")
    self.replace("FIFTEEN", "fifteen")
    self.replace("TWENTY", "twenty")
    self.replace("THIRTY", "thirty")
    self.replace("FORTY", "forty")
    self.replace("FIFTY", "fifty")
    self.replace("SIXTY", "sixty")

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Helper Digit Names")
