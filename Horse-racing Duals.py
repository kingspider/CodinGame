import sys
import math

horses = []
lowest = 100000

n = int(input())
for i in range(n):
    pi = int(input())
    horses.append(pi)
horses.sort(reverse=True)
lasthorse = horses[-1] 


def getdist(item1, item2):
    """ Returns the distance between two values... """
    return item1 - item2


for horse in range(len(horses) - 1):
    horseOne = horses[horse]
    horsetwo = horses[horse + 1]
    if getdist(horseOne, horsetwo) < lowest:
        lowest = getdist(horseOne, horsetwo)
    
   
print(lowest)