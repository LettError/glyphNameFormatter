from __future__ import print_function
import os
import time
import sys
import tempfile
from argparse import ArgumentParser, RawDescriptionHelpFormatter

try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

UNICODE_VERSION = "16.0.0"

#parser = ArgumentParser(description=__doc__,
#                        formatter_class=RawDescriptionHelpFormatter)
#group = parser.add_mutually_exclusive_group(required=True)
#group.add_argument("-u", "--unicode-version",
#                   help="Unicode version to use for download and processing")
#options = parser.parse_args()

#if options.unicode_version:
#    version = options.unicode_version
#else:
version = UNICODE_VERSION

JOININGTYPES_FILE = "ArabicShaping.txt"
ASURL = "http://www.unicode.org/Public/{version}/ucd/ArabicShaping.txt"

print(ASURL.format(version=version))

print(">> Downloading {} to {}".format(os.path.basename(ASURL), JOININGTYPES_FILE))
#if options.unicode_version:
#    version = options.unicode_version
#else:
version = UNICODE_VERSION
url = urlopen(ASURL.format(version=version))
with open(JOININGTYPES_FILE, "wb") as fp:
    blocksize = 8192
    while True:
        buffer = url.read(blocksize)
        if not buffer:
            break
        fp.write(buffer)
# fp.rewind()
# print(len(fp))


# coding: utf-8


def readArabicShaping(path):
    # makes joiningTypes.txt
    names = {}
    categories = dict()
    explanation = """# Joining types
# R Right_Joining
# L Left_Joining
# D Dual_Joining
# C Join_Causing
# U Non_Joining
# T Transparent"""

    f = open(path, 'r')
    d = f.read()
    f.close()
    source = None
    for l in d.split("\n"):
        if not l: continue
        if l.find("ArabicShaping-")!=-1:
            source = l
            continue
        if l[0] == "#": continue
        parts = l.split(";")
        parts = [p.strip() for p in parts]
        parts[0] = u"0x"+parts[0]
        try:
            uni = parts[0] = int(parts[0],0)
        except ValueError:
            print(parts)
        categories[uni] = parts[2]
    txt = []
    txt.append(explanation)
    txt.append("# Generated on %s" % time.strftime("%Y %m %d %H:%M:%S"))
    txt.append("# Source: %s"%source)
    txt.append("# <unicode> <joiningtype>")
    k = list(categories.keys())
    k.sort()
    for uni in k:
        txt.append("%05X\t%s"%(uni, categories.get(uni)))
    path = "joiningTypes.txt"
    f = open(path, 'w')
    f.write('\n'.join(txt))
    f.close()

def suggestExtension(names, categories, uni):
    # based on the category data, give suggestion for which extensions we need for any unicode
    extensions = {

    # XXXX no idea if it works this way...


    #   D Dual_Joining
    #       &----G----&
    'D': ['isol', 'ini', 'medi', 'fina'],

    #   C Join_Causing
    #       &----G----&     ????
    'C': ['isol', 'ini', 'medi', 'fina'],

    #   R Right_Joining
    #          x G----&
    'R': ['isol',                'fina'],

    #   L Left_Joining
    #       &----G x
    'L': ['isol', 'ini',         'fina'],

    #   U Non_Joining
    #          x G x
    'U': [                             ],

    #   T Transparent
    #          x G x
    'T': [                             ],
    
    }
    if not uni in categories.get('_used'):
        return [], None
    for k, v in categories.items():
        if k == "_used": continue
        if uni in v:
            return extensions.get(k), names.get(uni)
    return [], None


if __name__ == "__main__":
    from pprint import pprint
    arabicRange = 1536, 125251
    path = "ArabicShaping.txt"
    readArabicShaping(path)

    path = "joiningTypes.txt"

