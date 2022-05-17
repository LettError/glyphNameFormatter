# export to glyphNameData package

import os, shutil

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd()))))
path = os.path.join(root, "glyphData")
if not os.path.exists(path):
	print(f"Please put the glyphData package at {path}")
	exit()

print(path)

destinationFolder = os.path.join(path, "Lib", "glyphData")
sourceFolderLib = os.path.join(root, "glyphNameFormatter", "Lib", "glyphNameFormatter")

# which file: 
# why		: 


# which file: Lib/glyphNameFormatter/names/glyphNamesToUnicodeAndCategories_experimental.txt
# why		: this is the main names list

nameFiles = ["glyphNamesToUnicodeAndCategories.txt"]
for n in nameFiles:
	src = os.path.join(sourceFolderLib, "names", n)
	dst = os.path.join(destinationFolder, n)
	print(f'copying {os.path.basename(src)} to {dst}')
	shutil.copy(src, dst)

dataFiles = [	"joiningTypes.txt",
				"nameHistory.txt",
				"mirrored.py",
]
for n in dataFiles:
	src = os.path.join(sourceFolderLib, "data", n)
	dst = os.path.join(destinationFolder, n)
	print(f'copying {os.path.basename(src)} to {dst}')
	shutil.copy(src, dst)

dataFiles = [	"reader.py",
]
for n in dataFiles:
	src = os.path.join(sourceFolderLib, n)
	dst = os.path.join(destinationFolder, n)
	print(f'copying {os.path.basename(src)} to {dst}')
	shutil.copy(src, dst)
