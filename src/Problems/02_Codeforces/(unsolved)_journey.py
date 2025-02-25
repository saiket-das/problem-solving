# https://codeforces.com/problemset/problem/2051/B


def journey():
    # Number of Test cases
    t = int(input())

    while (t > 0):
        n, a, b, c = map(int, input().split())

journey()

"""
    -------------
    Input:
        4
        12 1 5 3
        6 6 7 4
        16 3 4 1
        10 1 1 1
    -------------
    Output:
        5
        1
        6
        1000000000
    -------------
    Explanation:
        In the first example, over the first four days, Monocarp will cover 1 + 5 + 3 + 1 = 10 kilometers. 
        On the fifth day, he will cover another 5 kilometers, meaning that in total over five days he will 
        have covered 10 + 5 = 15 kilometers. Since n = 12 , Monocarp will complete his journey on the fifth day.
    -------------
"""