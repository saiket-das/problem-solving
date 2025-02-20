# https://www.geeksforgeeks.org/problems/java-switch-case-statement3529/1

import math

def switchCase(choice, arr):
    match choice:
        case 1:
            circle = arr[0]
            area = (circle**2) * math.pi    # Calculate area of Circle
            return area
        case 2:
            length = arr[0]
            width = arr[1]
            area = length * width           # Calculate area of Rectangle
            return area
    

print(switchCase(2, [5, 6]))