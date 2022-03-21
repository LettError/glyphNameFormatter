# -*- coding: UTF-8 -*-
from __future__ import print_function, absolute_import

import unicodedata

from glyphNameFormatter.data import unicodelist, mathUniNumbers
from glyphNameFormatter.data.scriptConflictNames import scriptConflictNames
from glyphNameFormatter.data.preferredAGLNames import preferredAGLNames
from glyphNameFormatter.data.scriptPrefixes import scriptPrefixes, addScriptPrefix, SCRIPTSEPARATOR, SCRIPTASPREFIX
#from .data.mathUniNumbers import mathUniNumbers

from glyphNameFormatter.unicodeRangeNames import getRangeName, getRangeProcessor, getRangeProcessorByRangeName

from glyphNameFormatter.tools import unicodeToChar


__version__ = "0.7"


def debug(uniNumber):
    # trace the processing of a specific number
    glyphName = GlyphName(uniNumber=uniNumber, verbose=True)
    glyphName.process()
    print("debug: %04x" % uniNumber)
    print("name:", glyphName.getName())
    for step in glyphName._log:
        print("\t", step)


class GlyphName(object):

    prefSpelling_dieresis = "dieresis"

    def __init__(self, uniNumber=None, scriptSeparator=None, scriptAsPrefix=None, verbose=False, ignoreConflicts=False):
        self.status = 0 # defaults to draft
        self.uniNumber = uniNumber
        self.uniLetter = None
        self.uniName = ""
        self.uniNameProcessed = self.uniName
        self.uniRangeName = "No Range"
        self.isMath = False # is this a math symbol
        self.isLegacy = False   # if the unicode value is only for legacy support
        self.forceLatinScriptTag = False  # set to True to foxce a scripttag to latin
        self.scriptTag = ""
        if scriptSeparator is None:
            scriptSeparator = SCRIPTSEPARATOR
        if scriptAsPrefix is None:
            scriptAsPrefix = SCRIPTASPREFIX
        self._scriptSeparator = scriptSeparator
        self._scriptAsPrefix = scriptAsPrefix
        self.verbose = verbose
        self._ignoreConflicts = ignoreConflicts # when checking for conflicts we actually need to ignore the scriptConflictNames
        self.lookup()
        self.process()

    def _get_scriptSeparator(self):
        return self._scriptSeparator

    def _set_scriptSeparator(self, separator):
        if separator == self._scriptSeparator:
            return
        self._scriptSeparator = separator
        self.process()

    scriptSeparator = property(_get_scriptSeparator, _set_scriptSeparator)

    def _get_scriptAsPrefix(self):
        return self._scriptAsPrefix

    def _set_scriptAsPrefix(self, asPrefix):
        if asPrefix == self._scriptAsPrefix:
            return
        self._scriptAsPrefix = asPrefix
        self.process()

    scriptAsPrefix = property(_get_scriptAsPrefix, _set_scriptAsPrefix)

    def reset(self):
        self.languageSuffix = []
        self.suffixParts = []
        self.finalParts = []
        self.mustAddScript = False  # set to True if we need to add script to disambiguate
        self.statsPrefixRequested = False
        self._log = []

    def lookup(self):
        # look up all the external references we need.
        if self.uniNumber is None:
            return
        try:
            self.uniLetter = unicodeToChar(self.uniNumber)
        except:
            # print("GlyphName value error for %04X" % self.uniNumber)
            return
        if self.uniNumber in mathUniNumbers:
            self.isMath = True
        try:
            self.uniName = unicodelist.get(self.uniNumber)
            if self.uniName is None:
                self.uniNameProcessed = ""
            else:
                self.uniNameProcessed = self.uniName
            # NOTE: this is still a dependency on the unicodedata module.
            # Would be nice to extract this data directly from the unicode data
            # but the algotirhm is ot trivial..
            self.bidiType = unicodedata.bidirectional(self.uniLetter)
        except ValueError:
            self.uniName = None
            self.uniNameProcessed = ""
            self.uniLetter = None
            self.bidiType = None
        except:
            import traceback
            traceback.print_exc()
        self.uniRangeName = getRangeName(self.uniNumber)

    # these can be called by a range processor to set the status of a name.
    def setRelease(self):
        self.status = 1     # good, checked, ready
    def setDraft(self):
        self.status = 0     # working on it, default
    def setExperimental(self):
        self.status = -1    # new, unchecked, needs work
    def setDeprecated(self):
        self.status = -2    # old, must not include

    def hasName(self):
        if not self.uniName:
            return False
        return True

    def has(self, namePart):
        if self.uniName is None:
            return False
        if namePart in self.uniName:
            return True
        return False

    def handleCase(self):
        upperCaseIndicators = [
            # from complex to simple
            ("LETTER SMALL CAPITAL", "small"),
            ("SMALL CAPITAL LETTER", "smallcapital"),
            ("CAPITAL LETTER", ""),
            ("MODIFIER LETTER CAPITAL", "mod"),
            ("MODIFIER LETTER SMALL CAPITAL", "modsmall"),
            ("CAPITAL", ""),
        ]
        lowercaseIndicators = [
            # from complex to simple
            # ("LATIN SMALL LETTER", ""),
            ("SMALL LETTER", ""),
            ("MODIFIER LETTER SMALL", "mod"),
            ("SMALL", ""),
        ]
        for upperNames, suffix in upperCaseIndicators:
            if self.has(upperNames):
                start = self.uniNameProcessed.find(upperNames)
                if start == -1:
                    continue
                before = after = self.uniNameProcessed[start + len(upperNames):].strip()
                if not before:
                    continue
                elif len(before) == 1:
                    after = before.upper()
                else:
                    after = before[0].upper()+before[1:].lower()
                self.edit(upperNames, suffix)
                self.replace(before, after)
        for lowerNames, suffix in lowercaseIndicators:
            if self.has(lowerNames):
                start = self.uniNameProcessed.find(lowerNames)
                if start == -1:
                    continue
                before = after = self.uniNameProcessed[start + len(lowerNames):].strip()
                after = after.lower()
                self.edit(lowerNames, suffix)
                self.replace(before, after)

    def getName(self, extension=True, scriptSeparator=None, scriptAsPrefix=None):
        if scriptSeparator is not None:
            self.scriptSeparator = scriptSeparator
        if scriptAsPrefix is not None:
            self.scriptAsPrefix = scriptAsPrefix
        # return the name, add extensions or not.
        if self.uniName is None:
            # nothing to see here.
            return None
        if extension is False:
            return self.uniNameProcessed
        if self.mustAddScript:
            # we don't want a script extension,
            # but we've been warned that it might be necessary
            # for disambiguation
            if self.forceLatinScriptTag or (self.scriptTag != scriptPrefixes['latin'] and self.scriptTag != ""):
                if self.mustAddScript and self.scriptTag:
                    return addScriptPrefix(self.uniNameProcessed,
                                self.scriptTag,
                                scriptSeparator=self.scriptSeparator,
                                scriptAsPrefix=self.scriptAsPrefix,
                                )
            else:
                return self.uniNameProcessed
        else:
            # hope for the best then
            return self.uniNameProcessed

    def __repr__(self):
        return "%s\t\t%05x\t\t%s" % (self.getName(extension=False), self.uniNumber, self.uniName)

    def process(self):
        # reset everything
        self.reset()
        # try to find appropriate formatters and
        if self.uniNumber in preferredAGLNames:
            self.uniNameProcessed = preferredAGLNames[self.uniNumber]
        # get the processor
        processor = getRangeProcessor(self.uniNumber)
        if processor:
            # set the script
            self.scriptTag = scriptPrefixes[getRangeName(self.uniNumber)]
            processor(self)
            # make the final name
            self.uniNameProcessed = self.uniNameProcessed + "".join(self.suffixParts) + "".join(self.finalParts)
        if not self._ignoreConflicts:
            if self.uniNameProcessed in scriptConflictNames:
                # the final name has a duplicate in another script
                # take disambiguation action
                self.mustAddScript = True
        if self.isLegacy:
            self.uniNameProcessed = "lgcy_" + self.uniNameProcessed

    def processAs(self, rangeName):
        if not rangeName.lower().startswith("helper"):
            self.scriptTag = scriptPrefixes[rangeName]
        processor = getRangeProcessorByRangeName(rangeName)
        return processor(self)

    def edit(self, pattern, *suffix):
        # look for pattern
        # remove the pattern from the name
        # add any suffix patterns to the suffixParts
        """
        a method that does the same as this:
        if self.has("PATTERN"):
            if self.replace("PATTERN"):
                self.suffix("suffix")
                self.suffix("suffix")
        """
        if self.replace(pattern):
            [self.suffix(s) for s in suffix]

    def compress(self):
        # remove the spaces from the name
        self.uniNameProcessed = self.uniNameProcessed.replace(" ", "")

    def camelCase(self):
        # whole name camelcased to lowercase
        parts = self.uniNameProcessed.split(" ")
        if len(parts) < 2:
            self.lower()
            return
        casedParts = [a[0].upper()+a[1:].lower() for a in parts]
        self.uniNameProcessed = "".join(casedParts)
        self.uniNameProcessed = self.uniNameProcessed[0].lower() + self.uniNameProcessed[1:]

    def lower(self):
        # whole name to lowercase
        self.uniNameProcessed = self.uniNameProcessed.lower()

    def suffix(self, namePart):
        # add a suffix part
        if namePart not in self.suffixParts:
            self.suffixParts.append(namePart)

    def scriptPrefix(self):
        # should add a script prefix
        self.statsPrefixRequested = True
        self.mustAddScript = True

    def forceScriptPrefix(self, rangeName, lookFor=None, replaceWith=None):
        # Force add a prefix for a rangeName
        # as default it will replace the already processed uni name
        # optionally a pattern and replacement can be provided
        if lookFor is None:
            lookFor = self.uniNameProcessed
        if replaceWith is None:
            replaceWith = self.uniNameProcessed
        self.replace(lookFor, addScriptPrefix(replaceWith, script=rangeName, scriptSeparator=self.scriptSeparator, scriptAsPrefix=self.scriptAsPrefix))

    def final(self, namePart):
        # add a final part, for things that have the really last, like name extensions
        if namePart not in self.finalParts:
            self.finalParts.append(namePart)

    def editSuffix(self, lookFor, replaceWith):
        for n, i in enumerate(self.suffixParts):
            if i == lookFor:
                self.suffixParts[n] = replaceWith

    def editToFinal(self, namePart, *finals):
        # similar to edit(), but the parts are added the finalParts, not suffixParts
        # if you want to be really sure the parts end up at the end
        if self.replace(namePart):
            [self.final(s) for s in finals]

    def log(self, lookFor, replaceWith, before, after):
        self._log.append((lookFor, replaceWith, before, after))

    def replace(self, lookFor, replaceWith=""):
        after = self.uniNameProcessed.replace(lookFor, replaceWith)
        if self.uniNameProcessed == after:
            return False
        before = self.uniNameProcessed
        self.uniNameProcessed = self.uniNameProcessed.replace(lookFor, replaceWith)
        self.uniNameProcessed = self.uniNameProcessed.replace("  ", " ")
        self.uniNameProcessed = self.uniNameProcessed.strip()
        self.log(lookFor, replaceWith, before, self.uniNameProcessed)
        return True

    def condense(self, part, combiner=""):
        # remove spaces, remove hyphens, change to lowercase
        if part is None:
            return
        editPart = part.replace(" ", combiner)
        editPart = editPart.replace("-", "")
        editPart = editPart.lower()
        self.replace(part, editPart)


if __name__ == "__main__":

    import doctest

    def _testGlyphName():
        # basic tests for the GlyphName object
        """
        >>> g = GlyphName(uniNumber=0x020)
        >>> assert g.uniName == "SPACE"
        >>> g.edit("SPACE", "space")
        >>> g.suffixParts
        ['space']
        >>> g.uniNameProcessed
        'space'
        >>> g.getName()
        'space'

        >>> g = GlyphName(uniNumber=0x021)
        >>> g.uniName
        'EXCLAMATION MARK'
        >>> g.getName()
        'exclam'

        >>> g = GlyphName(uniNumber=0x041)
        >>> g.uniName
        'LATIN CAPITAL LETTER A'
        >>> g.handleCase()
        >>> g.getName()
        'A'
        >>> g = GlyphName(uniNumber=0x061)
        >>> g.uniName
        'LATIN SMALL LETTER A'
        >>> g.handleCase()
        >>> g.getName()
        'a'
        >>> g = GlyphName(uniNumber=0x0ABD, scriptSeparator="$")
        >>> g.getName()  # no, this is not a proposal to use $ as a separator.
        'gujr$avagraha'
        >>> g.scriptSeparator = ":"
        >>> g.getName()
        'gujr:avagraha'
        >>> g.scriptSeparator = ":"
        >>> g.scriptAsPrefix = True
        >>> g.getName()
        'gujr:avagraha'
        >>> g.scriptSeparator = ":"
        >>> g.scriptAsPrefix = False
        >>> g.getName()
        'avagraha:gujr'
        """

    #doctest.testmod()
    debug(0x0600)
    g = GlyphName(uniNumber=0x0600)
    print(g.getName(extension=True))
