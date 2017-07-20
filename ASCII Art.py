import sys
import math
import re
parsedline = []
count = ''
Abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','?']
charmap = {}
line = ''

def build_carmap(lsts, ab):
    for character in ab:
        char = []
        for lst in lsts:
            char.append(lst[Abc.index(character)])
            charmap[character] = char[:] 
        char = []
                   
l = int(input())
for x in range(l):
    count += '.'
h = int(input())
t = input()

for i in range(h):
    row = input()
    row = re.findall(count, row)
    parsedline.append(list(row))


build_carmap(parsedline, Abc)

for lin in range(h):
    for char in t.upper():
        if char in charmap.keys():
            line = line + str(charmap[char][lin])
        else:
             line = line + str(charmap['?'][lin])
    print(line)
    line = ''
    

 
 