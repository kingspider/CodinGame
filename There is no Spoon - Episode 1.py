import sys
import math

grid = []


width = int(input()) 
height = int(input()) 

for i in range(height):
    line = input() 
    grid.append(line)
    
for y in range(height):  # loop from top to bottom
    for x in range(width):  # loop for left to right
        
        if grid[y][x] == "0":  # Check if first index in a Node.
            x2, y2 = -1, -1
            x3, y3 = -1, -1
            
            for right in range(x + 1, width):  # Get the next node to the Right
                if grid[y][right] == "0":
                    x2, y2 = right, y
                    break
            
            for bottom in range(y + 1, height):  # Get next nod to the Bottom
                if grid[bottom][x] == "0":
                    x3, y3 = x, bottom
                    break
            
            print(x, y, x2, y2, x3, y3)
