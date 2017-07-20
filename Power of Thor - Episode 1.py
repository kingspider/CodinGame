import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
print('Starting desX,desY, X, Y: ' + str(light_x) + ":" + str(light_y) + "," + str(initial_tx) + ":" + str(initial_ty), file=sys.stderr) 

currentx = [initial_tx]
currenty = [initial_ty]

def direction(x, y, dx, dy):
    
    rdirection = ''
    
    if y > dy:
        rdirection = rdirection + "N"
        currenty[0] += 0.5
        if x < dx:
            rdirection = rdirection + "E"
            currentx[0] += 0.5
            return rdirection
        elif x > dx:
            rdirection = rdirection + "W"
            currentx[0] -= 0.5
            return rdirection
        else:
            return rdirection

    elif y < dy:
        rdirection = rdirection + "S"
        currenty[0] += 0.5
        if x < dx:
            rdirection = rdirection + "E"
            currentx[0] += 0.5
            return rdirection
        elif x > dx:
            rdirection = rdirection + "W"
            currentx[0] -= 0.5
            return rdirection
        else:
            return rdirection

    else:

        if x < dx:
            rdirection = rdirection + "E"
            currentx[0] += 0.5
            return rdirection
        elif x > dx:
            rdirection = rdirection + "W"
            currentx[0] -= 0.5
            return rdirection
        else:
            return rdirection
        


# game loop
while True:
    
    print('Current Position: ' + str(currentx) + ':' + str(currenty) , file=sys.stderr)
    
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    print('Remaining turns: ' + str(remaining_turns), file=sys.stderr)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    
    # A single line providing the move to be made: N NE E SE S SW W or NW
    print('Direction: ' + str(direction(currentx[0], currenty[0], light_x, light_y)), file=sys.stderr)
    print(str(direction(currentx[0], currenty[0], light_x, light_y)))
    