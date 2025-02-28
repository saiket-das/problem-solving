
"""
    Brute Force - Using Set
        Time Complexity:  O(n log n) + O(m log m) + O(n + m)
        Space Complexity: O(n + m)    
"""
def brute_force(a, b):
    return a


"""
    Optimal - Using Two-pointer
        Time Complexity:  O(m + n)
        Space Complexity: O(1) -> (No extra space, `intersection` list to return answer)
"""
def optiomal(a, b):
    n1, n2 = len(a), len(b)
    i, j = 0, 0


    intersection = []
    while i < n1 and j < n2:
        if (a[i] == b[j]):
            intersection.append(a[i])
            i += 1
            j += 1
        elif (a[i] < b[j]):
            i += 1
        else:
            j += 1

    return intersection
    

def findIntersection(a: list[int], b: list[int]):
    # print(brute_force(a, b))
    print(optiomal(a, b))


findIntersection([1, 2, 2, 3, 4, 6, 5, 9], [1, 2, 2, 3, 6, 7])