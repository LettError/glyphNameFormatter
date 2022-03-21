import subprocess
import os, time

# Experimental script to extract the history of unicode values and the names these lists associate them with.
# It iterates through all the commits, retrieves the file in <listFileName> and interprets the table. 
# All tables are collected in the history global.
# The historyForUni() can be used to collate a list of all the names that were associated with this unicode value.

# For instance:
# 128571 ['smilingCatFaceWithHeartShapedEyes', 'smiling_cat_face_with_heart_shaped_eyes', 'smiling_cat_face_with_heart-shaped_eyes']

# Todo: limit to the commits that belong to an actual release. This also shows intermediate commits, and can contain mistakes.


listFileName = "glyphNamesToUnicode.txt"

def readList(text):
    patterns = {
        "# <glyphName> <hex unicode> <unicodeCategory>": (0,1,3),
        "# <glyphName> <hex unicode>": (0,1,2),
    }
    unis = {}
    date = None
    lines = text.split("\n")
    nameIndex = 0
    uniIndex = -1
    expectedLength = 2
    version = None
    for l in lines:
        l = l.strip()
        if "# Generated on" in l:
            date = l[15:]
            #print('-'*30, l, date)
        else:
            date = None
        if "<<<<<<<" in l:
            # this commit has conflicts, it is not going to be useful
            return False, None, {}
        if not l: continue
        if "# GlyphNameFormatter version" in l:
            version = l[29:]
            #print(version)
        #if l[0] == "#":
        #   print("\t\t", l)
        if "<glyphName>" in l:
            if l not in patterns:
                print("patterns!", l)
        for pt, idx in patterns.items():
            if pt == l:
                nameIndex = idx[0]
                uniIndex = idx[1]
                expectedLength = idx[2]
                break
        if l[0] == "#":
            #print(l)
            continue
        p = l.split(" ")
        #print(p)
        if len(p) == expectedLength:
            name = p[nameIndex]
            uni = int(f"0x{p[uniIndex]}", 16)
            unis[uni] = name
        else:
            print(f"ignoring improperly formatted line: expected {expectedLength} items: \"{l}\"" )
    return True, date, unis



# global for all the things we find
history = []
hashes = []

topLevelDir = subprocess.check_output(["git", "rev-parse", "HEAD", "--show-toplevel"]).decode("utf-8")
topLevelDir = topLevelDir.split('\n')[1]
absPath = os.path.join(topLevelDir, "Lib", 'glyphNameFormatter', "names", listFileName)
relPath = os.path.join("Lib", 'glyphNameFormatter', "names", listFileName)

# interrogate the repo

# hashToTag = {}
# tags = subprocess.check_output(["git", "tag", "-l", "--sort=refname"]).decode("utf-8")
# print(tags)
# tags = [t.strip() for t in tags.split("\n")]
# for tag in tags:
#   print(tag)
#   if not tag: continue
#   mm = subprocess.check_output(["git", "rev-list", "-n", "1", tag]).decode("utf-8")
#   print(mm)

#   mf = subprocess.check_output(["git", "rev-list", "--tags", tag, absPath, ]).decode("utf-8")
#   print("-----", mf)
#   for hsh in mf.split("\n"):
#       hashToTag[hsh] = tag
# #print('topLevelDir', topLevelDir)
# print(hashToTag)

output = subprocess.check_output(["git", "rev-list", "--all", "--reverse", absPath, ])
output = str(output, encoding="utf-8")

# for i, hsh in enumerate(hashToTag.keys()):
#   tag = hashToTag[hsh]
#   cmd = ["git", "show", f"{hsh}:{relPath}"]
#   #print(cmd)
#   #continue
#   f = subprocess.check_output(cmd)
#   f = str(f, encoding="utf-8")



for i, hsh in enumerate(output.split('\n')):
    if not hsh:
        continue
    hashes.append(hsh)
    cmd = ["git", "show", f"{hsh}:{relPath}"]
    f = subprocess.check_output(cmd)
    f = str(f, encoding="utf-8")
    #git show git_hash:./file.py

    ok, date, unis = readList(f)
    if ok:
        history.append((date, unis))

print(f"found {len(history)} items")


def historyForUni(uni):
    # find the names associated with this uni
    # return values from new to old
    hst = []
    global history, hashes
    for date, unis in history:
        #print(f"looking at {date}, {len(unis)} items")
        name = unis.get(uni, None)
        #print(date, name, uni)
        if not name: continue
        if not hst:
            hst.append(name)
            continue
        if hst[-1] != name:
            hst.append(name)
    hst.reverse()
    return hst

def exportHistory(minUnicode=1, maxUnicode=0xFFFFF):
    global history, hashes
    count = 0
    txt = []
    txt.append("# List of unicodes that had different names in earlier GNUFL releases.")
    txt.append("# Generated on %s" % time.strftime("%Y %m %d %H:%M:%S"))
    txt.append("# Compiled from these hashes:")
    for hsh in hashes:
        txt.append(f"# {hsh}")
    txt.append("# <unicode> <historic name>")
    for u in range(minUnicode, maxUnicode):
        h = historyForUni(u)
        if len(h) > 1:
            count += 1
            txt.append(f"{hex(u)[2:]} {' '.join(h)}")
    path = "nameHistory.txt"
    f = open(path, 'w')
    f.write('\n'.join(txt))
    f.close()
    return count



if __name__ == "__main__":
    r = exportHistory()
    print(f"Exported history for {r} names")
    print('done')