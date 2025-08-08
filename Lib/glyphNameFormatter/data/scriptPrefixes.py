import os
from xml.etree import ElementTree as ET

from glyphNameFormatter.tools import GlyphNameFormatterError


SCRIPTSEPARATOR = ":"
SCRIPTASPREFIX = True


def loadScripTags():
    data = {}
    path = os.path.dirname(__file__)
    path = os.path.join(path, "scriptTags.html")
    doc = ET.parse(path)
    table = doc.getroot()

    for row in table:
        for i in row[1:]:
            script, tag = [col.text for col in i]
            script = script.strip()
            tag = tag.strip()
            data[script.lower()] = tag
    return data


class ScriptPrefixesDict(dict):

    _fallbackScripPrefixes = loadScripTags()

    def __getitem__(self, key):
        # get the key
        value = dict.get(self, key, None)
        if value:
            # found it, return it
            return value
        # try with in lower case
        key = key.lower()
        # get the lower case key
        value = dict.get(self, key, None)
        if value:
            # found it, return it
            return value
        # get the existing keys
        existingKeys = list(dict.keys(self))
        # sort them by reversed lenght
        existingKeys.sort(key=len, reverse=True)
        for existingKey in existingKeys:
            # compare with lower case
            if existingKey.lower() in key:
                # found it
                return dict.__getitem__(self, existingKey)
        # fallback
        if key in self._fallbackScripPrefixes:
            return self._fallbackScripPrefixes[key]
        # generate one
        # remove all vowels
        key = [c for c in key if c not in "aeiou -"]
        # return the first four values
        return "".join(key[:4])


def addScriptPrefix(txt, tag=None, script=None, scriptSeparator=SCRIPTSEPARATOR, scriptAsPrefix=SCRIPTASPREFIX):
    if tag is None and script is None:
        raise GlyphNameFormatterError("Need a script or a tag")
    if tag is None:
        tag = scriptPrefixes[script]

    if "{glyphName}" in tag:
        return tag.format(glyphName=txt, scriptSeparator=scriptSeparator)

    if scriptAsPrefix:
        order = tag, scriptSeparator, txt
    else:
        order = txt, scriptSeparator, tag
    return "%s%s%s" % order


# script prefixes are abbreviations of a script
# optionally a pattern can be given:
# '{glyphName}cyr' will add 'cyr' to the end
# '{scriptSeparator}' will insert the separator at a given place

_scriptPrefixes = {
    "arabic": "ar{glyphName}",
    "armenian": "{glyphName}armn",
    "boxdrawings": "bxd",
    "cjk": "cjk",
    "combining diacritical marks": "{glyphName}cmb",
    "cyrillic": "{glyphName}cyr",
    "fullwidth": "fwd",
    "halfwidth": "hwd",
    "greek": "gr",
    "latingreek": "ltgr",   # greek letters, used in latin, need a prefix, so that the actual greek name do not need a gr: prefix.
                            # so this is an artificial prefix.
    "ethiopic": "ethi",
    "hangul": "ko",
    "hebrew": "{glyphName}{scriptSeparator}hb",
    "hiragana": "hira",
    "ipa": "ipa",
    "katakana": "kata",
    "latin": "lt",
    "math": "math",
    "miscellaneous": "misc",
    "musical": "music",
    "optical character recognition": "ocr",
    "oriya": "orya",  # "odia"
    "phonetic": "phon",
    "thai": "th-{glyphName}",
    "vedic": "ve",
    "vertical forms": "vert",
    "Playing Cards": "cards",
    "Zanabazar Square": "zanb",
    "Thai": 'th',
    "Soyombo": "soyo"
}

scriptPrefixes = ScriptPrefixesDict(_scriptPrefixes)


if __name__ == "__main__":
    import doctest

    def _testScriptPrefixes():
        """
        >>> scriptPrefixes["latin"]
        'lt'
        >>> scriptPrefixes["randomScriptName"]
        'rndm'
        >>> scriptPrefixes["Greek and Coptic"]
        'gr'
        >>> scriptPrefixes["Enclosed CJK letters and months"]
        'cjk'
        >>> scriptPrefixes["Tai Le"]
        'tale'
        """

    def _testAddScriptPrefix():
        """
        >>> addScriptPrefix("A", "latin", scriptSeparator="", scriptAsPrefix=True)
        'latinA'
        >>> addScriptPrefix("A", "latin", scriptSeparator="", scriptAsPrefix=False)
        'Alatin'
        >>> addScriptPrefix("A", "latin", scriptSeparator="-", scriptAsPrefix=True)
        'latin-A'
        >>> addScriptPrefix("A", "latin", scriptSeparator="-", scriptAsPrefix=False)
        'A-latin'
        >>> addScriptPrefix("A", "latin", scriptSeparator=":", scriptAsPrefix=True)
        'latin:A'
        >>> addScriptPrefix("A", "latin", scriptSeparator=":", scriptAsPrefix=False)
        'A:latin'
        >>> addScriptPrefix("A", "hebrew", scriptSeparator=":", scriptAsPrefix=False)
        'A:hebrew'
        >>> addScriptPrefix("A", script="hebrew", scriptSeparator=":", scriptAsPrefix=False)
        'A:hb'
        """

    doctest.testmod()

    def testAllPrefixes():
        # let's not just assume all prefixes that end up the same
        # will also be able to disambiguate names.
        from glyphNameFormatter.unicodeRangeNames import getAllRangeNames
        prefixes = {}
        for n in getAllRangeNames():
            pf = scriptPrefixes[n]
            if pf not in prefixes:
                prefixes[pf] = []
            prefixes[pf].append(n)
        from pprint import pprint
        pprint(prefixes)

    testAllPrefixes()
