import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
t = []
n = int(input())
for i in range(n):
    t.append(input())
    print("Debug t: " + str(t), file=sys.stderr)
    t.sort()
    print("Debug t: " + str(t), file=sys.stderr)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(t[0])
