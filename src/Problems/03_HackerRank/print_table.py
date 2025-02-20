# https://www.geeksforgeeks.org/problems/while-loop-printtable-java/1

# Using while loop
def printTable ():
    n = int(input())

    i: int = 10
    while (i > 0):
        print(i * n, end = " ")
        i -= 1 
    
    print()
printTable()
"""
    Input: n = 1
    Output: 10 9 8 7 6 5 4 3 2 1
    ------
    Input: n = 2
    Output: 20 18 16 14 12 10 8 6 4 2
"""