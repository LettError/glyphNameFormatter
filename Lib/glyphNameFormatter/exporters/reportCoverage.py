from __future__ import print_function
from glyphNameFormatter.unicodeRangeNames import getAllRangeNames, rangeNameToModuleName, getRangeByName
from glyphNameFormatter import GlyphName

from glyphNameFormatter.data import name2unicode_AGD, unicodeVersion
import importlib
from pprint import pprint

#   find which unicode ranges are needed to cover the AGD names
#   so we can prioritize the support

def reportCoverage():
    uncountables = [
        'Hangul Syllables',
        'CJK Unified Ideographs',
        'Private'
    ]
    uncounted = []
    text = []
    text.append("\n\n# Coverage")
    wantRanges = {}
    glyphCount = {}
    for thisRange in getAllRangeNames():
        a, b = getRangeByName(thisRange)
        countThis = True
        for uc in uncountables:
            if thisRange.find(uc)!=-1:
                uncounted.append(" * %s"%thisRange)
                print(thisRange, "uncountable")
                countThis = False

        moduleName = rangeNameToModuleName(thisRange)
        if thisRange not in glyphCount:
            glyphCount[thisRange] = {'nameable': 0, 'uniNames':0, 'total':b-a, 'rangeProcessor':None}
        try:
            module = importlib.import_module('glyphNameFormatter.rangeProcessors.%s' % moduleName)
            glyphCount[thisRange]['rangeProcessor']=True
        except ImportError:
            pass
        for uniNumber in range(a,b):
            g = GlyphName(uniNumber)
            if g.uniName is not None:
                glyphCount[thisRange]['uniNames'] += 1
                if countThis:
                    glyphCount[thisRange]['nameable'] += 1

    totalGlyphs = 0     # the total of all glyph counts in all ranges
    totalCovered = 0    # the total of all glyphs that this package has rangeprocessors for
    totalPoints = 0     # the total of all ranges
    totalNameable = 0   # the total of all glyphs that can be named

    for key, items in glyphCount.items():
        #print(key, items)
        totalGlyphs += items['uniNames']
        totalPoints += items['total']
        if items['rangeProcessor'] is not None:
            totalCovered += items['uniNames']
            totalNameable += items['nameable']

    text = []
    text.append("")

    text.append("\n\n * [Supported Ranges](https://github.com/LettError/glyphNameFormatter/blob/master/coverage.md)")
    text.append(" * [Changes compared to RoboFont](https://github.com/LettError/glyphNameFormatter/blob/master/robofontUpdate.md)")
    text.append(" * [GlyphnameFormatter on GitHub](https://github.com/LettError/glyphNameFormatter)")

    text.append("## Version %s"%unicodeVersion)
    text.append("\n\n\n")
    text.append("### Note:\n")
    text.append(" * Not all ranges need to count. Private Use ranges are ignored, perhaps others need to as well.")
    text.append("\n\n\n")

    # if uncounted:
    #     text.append("The following ranges are skipped:")
    #     for line in uncounted:
    #         text.append(line)

    # text.append("\n\n\n")
    # text.append("| Stats                                      | :)        |")
    # text.append("| ------------------------------------------ | --------: |")
    # text.append('| Total code points in the available ranges  |   `%d`    |'%totalPoints)
    # text.append('| Total glyphs in the available ranges       |   `%d`    |'%totalGlyphs)
    # text.append('| Total glyphs that can be named             |   `%d`    |'%totalNameable)
    # text.append('| Total names covered in GlyphNameFormatter  | `%d`      |'%totalCovered)
    # text.append('| Progress                                   | `%3.3f%%` |'%(100.0*totalCovered/totalGlyphs))

    text.append("\n\n\n")
    text.append("| Range name | # | has processor | Start | End |")
    text.append("| ----- | ----- |----- | ----- | ----- |")

    for thisRange in getAllRangeNames():
        if not thisRange in glyphCount: continue
        a, b = getRangeByName(thisRange)
        items = glyphCount[thisRange]
        if items['rangeProcessor']!=None:
            has = "**Yes**"
            n = "**%s**"%items['uniNames']
        else:
            has = "No"
            n = items['uniNames']
        text.append("| %s | %s | %s | `%04X` | `%04X` |"%(thisRange, n, has, a, b))

    text.append("\n\n")
    path = "../../../coverage.md"
    f = open(path, 'w')
    f.write("\n".join(text))
    f.close()


if __name__ == "__main__":
    reportCoverage()
