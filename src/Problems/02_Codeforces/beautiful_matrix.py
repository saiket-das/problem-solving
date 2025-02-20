# https://codeforces.com/problemset/problem/263/A

def beautiful_matrix():
    matrix = []

    # Matrix Input
    for _ in range(5):
        row = list(map(int, input().split())) 
        matrix.append(row)
    
    move: int = 0
    isFound: bool = False
    # Iterate over 5 rows and columns
    for row in range(5):
        for column in range(5):
            # If 1 is found, set flag (isFound) to True and Calculaete distance from (2, 2)
            if (matrix[row][column] == 1):
                isFound = True
                move = abs(row - 2) + abs(column - 2)
                break    # Exit inner loop
        # If flag (isFound) is true then Exit outer loop
        if (isFound):
            break
    
    print(move)


beautiful_matrix()


"""
Input:
0 0 0 0 0
0 0 0 0 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0

Output:
3

----------
Input:
0 0 0 0 0
0 0 0 0 0
0 1 0 0 0
0 0 0 0 0
0 0 0 0 0

Output:
1
"""