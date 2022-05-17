# -*- coding: UTF-8 -*-
from __future__ import print_function, absolute_import

import glyphNameFormatter
from glyphNameFormatter.unicodeRangeNames import getRangeByName, getAllRangeNames, getSupportedRangeNames
from glyphNameFormatter.data import upperToLower, lowerToUpper

import os

"""

Find the sanctioned export file
Provide conversions for

name to unicode
unicode to name

maybe later: some version info
header:

# Glyph Name Formatted Unicode List - GNFUL
# GlyphNameFormatter version 0.28 - git commit: 400
# Unicode version: Unicode 10.0.0
# Source code: https://github.com/LettError/glyphNameFormatter/tree/fcca7b3
# Generated on 2018 03 23 20:36:46
# <glyphName> <hex unicode> <unicodeCategory>
#


Parse the file when the module loads, then save the data in 3 dicts.

"""

sanctionedNameList = 'glyphNamesToUnicodeAndCategories.txt'

name2uni = {}
uni2name = {}
uni2cat = {}
ranges = {}

# these are unicode ranges for the CJK ideographs
ideographRanges = {
	(0x4E00, 0x9FFF):		"CJK Unified Ideographs",
	(0x3400, 0x4DBF):		"CJK Unified Ideographs Extension A",
	(0x20000, 0x2A6DF):		"CJK Unified Ideographs Extension B",
	(0x2A700, 0x2B73F):		"CJK Unified Ideographs Extension C",
	(0x2B740, 0x2B81F):		"CJK Unified Ideographs Extension D",
	(0x2B820, 0x2CEAF):		"CJK Unified Ideographs Extension E",
	(0x2CEB0, 0x2EBEF):		"CJK Unified Ideographs Extension F",
	(0xF900, 0xFAFF):		"CJK Compatibility Ideographs",
	(0x2F800, 0x2FA1F):		"CJK Compatibility Ideographs Supplement",
	(0x1F200, 0x1F2FF):		"Enclosed Ideographic Supplement",
	}

def isIdeograph(value):
	for a, b in ideographRanges.keys():
		if a<=value<=b:
			return True
	return False


def readJoiningTypes(path):
    # read the joiningTypes.txt
    joiningTypes = {}
    f = open(path, 'r')
    d = f.read()
    f.close()
    lines = d.split("\n")
    for l in lines:
        if not l: continue
        if l[0] == "#": continue
        parts = l.split("\t")
        uni = int('0x'+parts[0], 0)
        jT = parts[1]
        joiningTypes[uni] = jT
    return joiningTypes


def uniPatternName(v):
	return "uni{:X}".format(v)


def u2n(value):
	"""Unicode value to glyphname"""
	if value is None:
	    return None
	if isIdeograph(value):
		return uniPatternName(value)
	global uni2name
	return uni2name.get(value)

def n2u(name):
	"""Glyphname to Unicode value"""
	global name2uni
	v = name2uni.get(name)
	if v is not None:
		return v
	if name[:3] == "uni":
		# parse uniXXXX name
		try:
			return int(name[3:], 16)
		except:
			pass


def u2c(value):
	"""Unicode value to Unicode category"""
	global uni2cat
	return uni2cat.get(value)


def n2c(name):
	"""Glyphname to Unicode category"""
	global name2uni, uni2cat
	return uni2cat.get(name2uni.get(name))


def _parse(path):
	lines = None
	global name2uni, uni2name, uni2cat
	with open(path, 'r') as f:
		lines = f.read().split("\n")
	if lines:
		for l in lines:
			if not l: continue
			if l[0]=="#": continue
			parts = l.split(" ")
			assert(len(parts)==3)
			name = parts[0]
			value = int(parts[1], 16)
			cat = parts[2]
			name2uni[name] = value
			uni2name[value] = name
			uni2cat[value] = cat

root = os.path.dirname(glyphNameFormatter.__file__)
path = os.path.join(root, 'data', sanctionedNameList)
if os.path.exists(path):
	_parse(path)
else:
	print("GNUFL error: can't find name lists at %s"%(path))


rangeNames = getSupportedRangeNames()
for rangeName in rangeNames:
	start, end = getRangeByName(rangeName)
	ranges[(start, end)] = rangeName

def n2jT(name):
	"""name to joiningType"""
	pass

def u2r(value):
	"""Unicode value to range name"""
	if value is None:
		return None
	for k, v in ranges.items():
		if k[0]<=value<=k[1]:
			return v
	for k, v in ideographRanges.items():
		if k[0]<=value<=k[1]:
			return v
	return None

def n2N(name):
	# name to uppercase
	uni = n2u(name)
	if uni:
		uprUni = lowerToUpper.get(uni)
		if uprUni:
			return u2n(uprUni)
	return name

def N2n(name):
	# name to lowercase
	uni = n2u(name)
	if uni:
		lwrUni = upperToLower.get(uni)
		if lwrUni:
			return u2n(lwrUni)
	return name

def u2U(uni):
	# unicode to uppercase unicode
	uprUni = lowerToUpper.get(uni)
	if uprUni is not None:
		return uprUni
	return uni

def U2u(uni):
	# unicode to lowercase unicode
	lwrUni = upperToLower.get(uni)
	if lwrUni is not None:
		return lwrUni
	return uni

def isUpper(uni):
	if uni is None:
		return False
	return chr(uni).isupper()

if __name__ == "__main__":
    print("upperToLower map:", len(upperToLower))
    print("lowerToUpper map:", len(lowerToUpper))

    print("A", isUpper(ord("A")))
    print("a", isUpper(ord("a")))
    print("!", isUpper(ord("!")))

    allNames = list(name2uni.keys())
    allNames.sort()
    print("\ntest lower -> upper -> lower")
    if False:
        for n in allNames:
            upr = n2N(n)
            if upr != n and upr is not None:
                lwr = N2n(upr)
                if n != lwr:
                    print("\t\tn2N failed", n, "->", upr, "->", lwr)

            lwr = N2n(n)
            if lwr != n and lwr is not None:
                upr = n2N(lwr)
            if n != upr:
                print("\t\tN2n failed", n, "->", lwr, "->", upr)
    assert N2n("non-existing-glyphname") == "non-existing-glyphname"
    assert n2N("non-existing-glyphname") == "non-existing-glyphname"
    assert n2N("germandbls") == "germandbls"
    assert N2n("A") == 'a'
    assert n2N("a") == 'A'
    assert U2u(65) == 97	# A -> a
    assert u2U(97) == 65	# a -> A

    # ideograph support
    assert isIdeograph(1) == False
    assert isIdeograph(0x2A700) == True
    print(u2n(0x2A700))
    testIdeographValues = [0x2A700, 0x3401, 0x9FFF]
    for v in testIdeographValues:
        assert n2u(u2n(v)) == v
    # check if a value an ideographRange returns the proper name

    for k, v in ideographRanges.items():
        a, b = k
        c = int(.5*(a+b))
        assert u2r(c) == v

    if False:    # really long print of all possible names
        minUni = min(uni2name.keys())
        maxUni = max(uni2name.keys())
        for u in range(minUni, maxUni):
            r = u2n(u)
            if r is not None:
                print(f'{u}:\t{u2n(u)}')
