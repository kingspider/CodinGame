import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
    Targets = []
    Targets_Sorted = []
    for i in range(8):
        Targets.append(int(input()))  # represents the height of one mountain.
    print("Inputs: " + str(Targets), file=sys.stderr)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    print("List Targets: " + str(Targets), file=sys.stderr)
    Targets_Sorted = Targets[:]
    print("List Targets Sorted: " + str(Targets_Sorted), file=sys.stderr)
    Targets_Sorted.sort(reverse=True)
    print("Sorted list: " + str(Targets_Sorted), file=sys.stderr)
    
    #for value in Targets_Sorted:
    print(Targets.index(Targets_Sorted[0]))
   
    # The index of the mountain to fire on.
    #print("4")