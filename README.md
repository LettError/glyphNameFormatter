# GlyphNameFormatter

![GlyphNameFormatter Banner](banner.png)

A system for generating glyph name lists from official Unicode data. 

* Unicode has long and descriptive names for each character.
* Font editors need glyph names to easily identify the glyphs, short, unique, can't use spaces, non-ascii characters.
* Raw Unicode names are unsuitable for this purpose in font editors
* Font editors use their own lists that map names to unicode values.
* So this system parses, generates and tweaks.

### Glyph Name Formatted Unicode List Release 0.3 (ɣNUFL)

[download](https://github.com/LettError/glyphNameFormatter/releases)

* Release 0.1 offers (almost) the same coverage as the Adobe Glyph Dictionary, AGD.txt
Look at `/names/glyphNamesToUnicode.txt` for a useful name to unicode map.
* Release 0.2 offers more ranges from Unicode 10.0.0.
* Release 0.3 offers more ranges from Unicode 11.0.0.
* Release 0.4 fixes a bug in the conflict analysis. Better names for all.

### Contributions

This release is not meant to be final. Many ranges have basic coverage but could be improved. Some Unicode names are wrong and then get translated wrong. The list does not claim authority or completeness. 

If you find things wrong and would like to share this insight, we're accepting comments, [open an issue](https://github.com/LettError/glyphNameFormatter/issues). If you see how the system works we will also gladly consider pull requests. If you would like to see certain ranges supported, let us know.

This version acknowledges the help by Frederik, Just, Adam, Daniel, Bahman and Ilya.

## Using conversion functions

After all the processing is done, the lists can be used with a couple of convenient functions.

* u2n(value) Unicode value to glyphname
* n2u(name) Glyphname to Unicode value
* u2c(value) Unicode value to Unicode category
* n2c(name) Glyphname to Unicode category
* u2r(value) Unicode value to range name
* n2N(name) name to uppercase
* N2n(name) name to lowercase
* u2U(uni) unicode to uppercase unicode
* U2u(uni) unicode to lowercase unicode

### Naming guidelines

* Glyph names should, as much as possible, only have script tags to disambiguate.
* Detect when script specific prefix or suffix is necessary
* Keep script prefix or suffix short
* Some scripts already have a preference for pre- or suffix.
* Some names look better with camelCase.

## Generating lists

Run `data/buildFlatUnicodeList.py` to download the current (or previous) data from Unicode.org. This is a large file. This script downloads and processes the data to a  more practical size, stored in `data/flatUnicode.txt`.

Run `data/buildJoiningTypesList.py` to download the current data from Unicode.org. This stored in a separate file, `data/joiningTypes.txt`

Run `exporters/exportFlatLists.py` to generate a text file with <name> <unicode> pairs, exclusively with the available range processors. The results are in [names/glyphNamesToUnicode.txt](https://github.com/LettError/glyphNameFormatter/blob/master/Lib/glyphNameFormatter/names/glyphNamesToUnicode.txt)

Run `test/buildRanges.py` to make all the name lists. They will be deposited in `names/ranges`. There will be other methods and other lists, but for now this is the place to make things.
You can also run each of the range scripts in `rangeProcessors/` and they will print a nice readable table with the processed name, unicode value, original name. There is also a column for names from the Adobe AGL if it has a different name for that entry. 

Run `exporters/analyseConflicts.py` to get an overview of all name clashes and how they are addressed. The results are in a text file in [data/conflict.txt](https://github.com/LettError/glyphNameFormatter/blob/master/Lib/glyphNameFormatter/data/conflict.txt)

## Range Processors

Given the rather large task of handling thousands of exceptions and tweaks, the package has a modules that each take care of a single unicode range. This makes it easier to work in different places at once. Also testing is easier.

The `GlyphName` class is initialised with a single unicode number. It then finds the unicode name. Based on the range name it tries to find a module with a corresponding name in `rangeProcessors/`. If it finds such a module it will run the `process()` function and apply it. The `process()` function will try to transform the unicode name by editing or replacing parts of the name.

Each range processor has a handy debugginh print function that will show an overview of the unicode value, the generated name, a comparison with the AGD name and the unicode names.

### On the internals

* `GlyphName.uniNumber` integer, the unicode number we're working on.
* `GlyphName.uniName` string, the original unicode character name
* `GlyphName.uniNameProcessed` string, the edited name.
* `GlyphName.suffixParts` list of name parts that are added at the end. Please use:
* `GlyphName.suffix(namePart)` use this method to add name parts to the suffix list.
* `GlyphName.replace(oldPattern, [newPattern])` If no newPattern is given it will assume it is `""` and delete `oldPattern`
* `GlyphName.edit(oldPattern, [*suffixes])` This is more elaborate: it will remove `oldPattern` from the name, and then append any number of suffix strings to `GlyphName.suffixParts`. When the processing is done all strings in suffixParts are appended to the end of the glyph name.

