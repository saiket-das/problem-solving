# https://codeforces.com/problemset/problem/2069/B


import sys


t = int(sys.stdin.readline().strip())

while t > 0:
    # Row and Column Input
    row, col = map(int, sys.stdin.readline().split())

    # Matrix Input
    matrix = []
    for _ in range(row):
        row = list(map(int, input().split()))
        matrix.append(row)
            
    print(matrix)

    t -= 1