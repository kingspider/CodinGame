import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
#tempslist = []
n = int(input())  # the number of temperatures to analyse
temps = input()  # the n temperatures expressed as integers ranging from -273 to 5526
print("Debug(line 9): temps: " + temps, file=sys.stderr)
# Debug list
temps = temps.split()
print("Debug(line 12): temps: " + str(temps), file=sys.stderr)

def closeZero(lst, n):
    print("Debug(line 15): closerZero called: " + str(lst) + ", " + str(n), file=sys.stderr)
    negval = []
    posval = []
    print("Debug(line 18): negval, posval: " + str(negval) + ", " + str(posval), file=sys.stderr)
    for val in lst:
        valint = int(val)
        if valint < 0:
            negval.append(valint)
        else:
            posval.append(valint)
    
    # Sort Positive and Negative values in lists
    negval.sort()
    posval.sort()
    print("Debug(line 29): negval, posval: " + str(negval) + ", " + str(posval), file=sys.stderr)
    if len(posval) != 0 and len(negval) != 0:    
    # Find lowest Values using abs()
        if abs(negval[0]) == posval[0]:
            print("Debug(line 33): posval: " + str(posval[0]), file=sys.stderr)
            return posval[0]
        elif abs(negval[0]) < posval[0]:
            print("Debug(line 36): posval: " + str(negval[0]), file=sys.stderr)
            return nagval[0]
        else:
            print("Debug(line 39): posval: " + str(posval[0]), file=sys.stderr)
            return posval[0]
    if len(negval) != 0:         
        negval.sort(reverse=True)
        print("Debug(line 43): posval: " + str(negval[0]), file=sys.stderr)
        return negval[0]
    else:
        return posval[0]


if not temps:
    print('0')
    print('No input was detected.', file=sys.stderr)

elif len(temps) == 1:
    print(temps[0])
    
else:
    print("Debug(line 57): temps: " + str(temps), file=sys.stderr)
    print(closeZero(temps, n))
    