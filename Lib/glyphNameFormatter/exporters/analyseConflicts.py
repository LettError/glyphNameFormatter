from __future__ import print_function
import shutil
import os

import glyphNameFormatter
from glyphNameFormatter.unicodeRangeNames import getRangeByName, getAllRangeNames
from glyphNameFormatter.data import unicode2name_AGD

#   Find duplicate names for different unicodes

def findConflict(makeModule=True, makeReport=False, printReport=False):
    names = {}
    dontReport = [
        'tang:tangutideograph#',
        'cjk:cjkunifiedideograph#',
        'cjk:cjkcompatibilityideograph#',
        'nsh:nushucharacter#',
        'tangutideograph#',
        'cjkunifiedideograph#',
        'cjkcompatibilityideograph#',
        'nushucharacter#',
        'khitansmallscriptcharacter#'
        ]
    #extendedNames = {}
    lines = []
    for rangeName in getAllRangeNames():
        start, end = getRangeByName(rangeName)
        for uniNumber in range(start, end+1):
            glyphName = glyphNameFormatter.GlyphName(uniNumber, ignoreConflicts=True)
            if glyphName.hasName():
                # name = glyphName.getName(extension=False)
                name = glyphName.getName(extension=True)
                if name not in names:
                    names[name] = []
                names[name].append(glyphName)
    n = list(names.keys())
    n.sort()

    conflictNames = []
    conflictUniNumbers = []
    conflictsPerRange = {}
    if makeReport:
        line = "{0:>6s} | {1:<50}{2:<25}{3:<40}{4:<40}{5:<20}".format("hex", "basic formatted name", "AGL name", "with extension", "range", "uni name")
        if printReport:
            print(line)
        lines.append(line)
        line = "{0:->6s} + {1:-<50}{2:-<25}{3:-<40}{4:-<40}{5:-<20}".format("", "", "+", "+", "+", "+")
        if printReport:
            print(line)
        lines.append(line)
    for name in n:
        if len(names[name]) > 1:
            conflictNames.append(name, )
            line = ""
            if printReport:
                print()
            lines.append(line)
            for g in names[name]:
                rangeName = g.uniRangeName
                extendedName = g.getName(extension=True)
                AGLname = unicode2name_AGD.get(g.uniNumber, "-")
                nn = g.getName()
                if nn in dontReport:
                    continue
                conflictUniNumbers.append(g.uniNumber)
                if makeReport:
                    line = "{0:>6X} : {1:<50}{2:<25}{3:<40}{4:<40}{5:<20}".format(g.uniNumber, nn, AGLname[:25], g.getName(), g.uniRangeName[:40], g.uniName)
                    if printReport:
                        print(line)
                    lines.append(line)

                if rangeName not in conflictsPerRange:
                    conflictsPerRange[rangeName] = []
                conflictsPerRange[rangeName].append(line)

    if makeReport:
        stats = "# %d names with conflicts, affecting %d unicodes" % (len(conflictNames), len(conflictUniNumbers))
        if printReport:
            print(stats)
        lines.append(stats)

    dirName = os.path.dirname(__file__)

    k = list(conflictsPerRange.keys())
    if makeReport:
        lines.append("")
        lines.append("")
        lines.append("Conflicts by rangename")
        k.sort()
        for rangeName in k:
            lines.append("\n%s" % rangeName)
            for line in conflictsPerRange[rangeName]:
                lines.append(line)
        path = os.path.join(dirName, "..", "data", "conflict.txt")
        f = open(path, 'w')
        f.write("\n".join(lines))
        f.close()

        # separate report for conflicts per range name
        for rangeName in k:
            rlines = []
            for line in conflictsPerRange[rangeName]:
                rlines.append(line)
            d = os.path.join(dirName, "..", "data", "conflicts")
            if not os.path.exists(d):
                # remove it first
                shutil.rmtree(d)
                os.makedirs(d)
            path = os.path.join(dirName, "..", "data", "conflicts", "conflict_%s.txt" % rangeName.replace(" ", "_").lower() )
            f = open(path, 'w')
            f.write("\n".join(rlines))
            f.close()



    if makeModule:
        path = os.path.join(dirName, "..", "data", "scriptConflictNames.py")

        pyText = ["# Table with conflicting names. Generated by /exporters/analyseConflicts.py", "\nscriptConflictNames = ["]
        conflictNames.sort()
        for name in conflictNames:
            pyText.append("    \"%s\"," % name)
        pyText.append("]\n\n")
        f = open(path, 'w')
        f.write("\n".join(pyText))
        f.close()

if __name__ == "__main__":
    findConflict(True, True, True)
