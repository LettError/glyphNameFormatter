from __future__ import print_function
import os
import sys
import tempfile
from zipfile import ZipFile
from xml.etree import cElementTree as ET
from argparse import ArgumentParser, RawDescriptionHelpFormatter
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

__doc__ = """
This will parse the large ucd xml from unicode.org
into a simple list that is workable and
is fair enough for download and embedding.

starts with the # unicode description/version

format
<unicode> \t <unicode name>
"""

URL = "http://www.unicode.org/Public/{version}/ucdxml/ucd.all.flat.zip"

UNICODE_VERSION = "15.0.0"
UCD_ZIP_FILE = "ucd.all.flat.zip"
UCD_FILE = UCD_ZIP_FILE[:-3] + "xml"
FLAT_FILE = "flatUnicode.txt"

parser = ArgumentParser(description=__doc__,
                        formatter_class=RawDescriptionHelpFormatter)
group = parser.add_mutually_exclusive_group(required=False)
group.add_argument("-u", "--unicode-version",
                   help="Unicode version to use for download and processing")
group.add_argument("-i", "--input", metavar="UCD_FILE",
                   help="Path to copy of {ucd_file} for processing. "
                   "Use if you already have an up-to-date local copy of "
                   "{ucd_file}.".format(ucd_file=UCD_FILE))
options = parser.parse_args()

if options.input:
    path = options.input
else:
    tempdir = tempfile.mkdtemp()
    filename = os.path.join(tempdir, UCD_ZIP_FILE)
    if options.unicode_version:
        version = options.unicode_version
    else:
        version = UNICODE_VERSION
    print(">> Downloading {} to {} (version {})".format(UCD_ZIP_FILE, filename, version))
    print(URL.format(version=version))
    url = urlopen(URL.format(version=version))
    with open(filename, "wb") as fp:
        blocksize = 8192
        while True:
            buffer = url.read(blocksize)
            if not buffer:
                break
            fp.write(buffer)
    zipped = ZipFile(filename)
    print(">> Extracting {} to {}"
          .format(UCD_FILE, os.path.join(tempdir, UCD_FILE)))
    path = zipped.extract(UCD_FILE, tempdir)


print(">> Building {} from {}".format(FLAT_FILE, path))
tree = ET.parse(path)

flat = []
for i in tree.iter():
    if i.tag.endswith("description"):
        flat.insert(0, "# %s" % i.text)
    if i.tag.endswith("char"):
        n = i.attrib.get("na")
        if n:
            uc = i.attrib.get("uc")
            if uc == "#":
                uc = ''
            lc = i.attrib.get("lc")
            if lc == "#":
                lc = ''
            mth = i.attrib.get('Math')
            if mth != "N":
                mth = "M"
            else:
                mth = ""
            # codepoint / tab / uppercase / tab / lowercase / tab / category / tab / name
            flat.append("%s\t%s\t%s\t%s\t%s\t%s" % (i.attrib.get("cp"), uc, lc, i.attrib.get("gc"), mth, n))


f = open(FLAT_FILE, "w")
f.write("\n".join(flat))
f.close()
