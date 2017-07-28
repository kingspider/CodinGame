import sys
import math

minemap = {}
mineext = []


def extension(filename):
    """ Function takes a filename reverses it and then gets the extension. """
    fileextention = ""
    for char in filename:
        if char == ".":
            fileextention = fileextention[::-1]
            return fileextention.lower()
        else:
            fileextention = fileextention + char


n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
for minedata in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    ext = ext.lower()
    minemap[ext] = mt
    mineext.append(ext)

for lines in range(q):
    fname = input()  # One file name per line.
    if extension(fname[::-1]) in mineext:
        print(minemap[extension(fname[::-1])])
    else:
        print("UNKNOWN")
