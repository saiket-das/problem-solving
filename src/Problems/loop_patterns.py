# Pattern 1
"""
*
* *
* * *
* * * *
* * * * *
"""
def partten_1 (n: int):
    for i in range(n):
        for j in range(i+1):
            print("*", end = " ")
        print()

partten_1(5)


# Pattern 2
"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""
print("--------------")
def partten_2 (n: int):
    for i in range(n):
        for j in range(n):
            print("*", end = " ")
        print()

partten_2(5)

# Pattern 3
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
print("--------------")
def partten_3 (n: int):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end = " ")
        print()

partten_3(5)


# Pattern 4
"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
print("--------------")
def partten_4 (n: int):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(i, end = " ")
        print()

partten_4(5)

# Pattern 5
"""
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
"""
print("--------------")
def partten_5 (n: int):
    for i in range(0, n):
        for j in range(n, i, -1):
            print(j, end = " ")
        print()

partten_5(5)

# Pattern 6
"""
1 2 3
1 2
1
"""
print("--------------")
def partten_6 (n: int):
    for i in range(n+1, 1, -1):
        for j in range(1, i):
            print(j, end = " ")
        print()

partten_6(3)


# Pattern 7
"""
   *
  ***
 *****
*******
"""
print("--------------")
def partten_7 (n: int):
    for i in range(0, n):
        # Space
        for j in range(0, n-i-1):
            print("_", end = " ")
        # Star
        for k in range(0, (2*i + 1)):
            print("*", end = " ")
        # Space
        for j in range(0, n-i-1):
            print("_", end = " ")
        print()

partten_7(4)


# Pattern 8
"""
*******
 *****
  ***
   *
"""
print("--------------")
def partten_8 (n: int):
    for i in range(n, 0, -1):
        # Space
        for j in range(n-i, 0, -1):
            print(" ", end = " ")
        # Star
        for k in range((2*i-1), 0, -1):
            print("*", end = " ")
        # Space
        for j in range(n-i, 0, -1):
            print(" ", end = " ")
        print()


partten_8(4)


# Pattern 9
"""
   *            4 space + 1 star + 4 space
  ***           2 space + 3 star + 2 space 
 *****          1 space + 5 star + 1 space
*******         0 space + 7 star + 0 space
 *****          1 space + 5 star + 1 space
  ***           2 space + 3 star + 2 space
   *            4 space + 1 star + 4 space
"""
print("--------------")
def partten_9 (n: int):
    # Pyramid Up
    for i in range(0, n):
        # Space
        for j in range(0, (n-i-1)):
            print(" ", end = "")
        # Star
        for k in range((2*i+1), 0, -1):
            print("*", end = "")
        # Space
        for j in range(0, (n-i-1)):
            print(" ", end = "")
        print()
    
    # pyramid Down
    for i in range(n, 0, -1):
        # Space
        for j in range((n-i), 0, -1):
            print(" ", end = "")
        # Star
        for k in range(0, 2*i-1):
            print("*", end = "")
        # Space
        for j in range((n-i), 0, -1):
            print(" ", end = "")
        print()

partten_9(4)