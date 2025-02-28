# https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=union-of-two-sorted-arrays

from sortedcontainers import SortedSet

"""
    Brute Force - Using Set
        Time Complexity:  O(n log n) + O(m log m) + O(n + m)
        Space Complexity: O(n + m)    
"""
def brute_force(a: list[int], b: list[int]):
    union_set = SortedSet()

    for num in a:    # TC: O(n log n)
        union_set.add(num)
        
    for num in b:    # TC: O(m log m)
        union_set.add(num)

    return list(union_set)    #TC: O(n + m)


"""
    Optimal - Using Two-pointer
        Time Complexity:  O(n + m)
        Space Complexity: O(n + m)  
"""
def optiomal(a: list[int], b: list[int]):
    # Get the lengths of both input lists
    n1, n2 = len(a), len(b)

    # Initialize two pointers for both lists
    i, j = 0, 0

    # Result list to store the union of the two sorted arrays
    union = []

    # Merge both lists while removing duplicates

    while (i < n1 and j < n2):
        # If the current element of 'a' is smaller or equal, add it to 'union'
        if (a[i] <= b[j]):
            # Avoid duplicates
            if not union or union[-1] != a[i]:    
                union.append(a[i])
            i += 1    # Move pointer in 'a'
        
        # If the current element of 'b' is smaller, add it to 'union'
        else:
            # Avoid duplicates
            if not union or union[-1] != b[j]:
                union.append(b[j])
            j += 1    # Move pointer in 'b'
    
    # Add remaining elements from 'a' (since 'b' is exhausted)
    while (i < n1):
        if union[-1] != a[i]:   
            union.append(a[i])
        i += 1
    
    # Add remaining elements from 'b' (since 'a' is exhausted)
    while (j < n2):
        if union[-1] != b[j]:  
            union.append(b[j])
        j += 1
    
    # Return the final merged sorted list without duplicates
    return union

def findUnion(a: list[int], b: list[int]):
    # print(brute_force(a, b))
    print(optiomal(a, b))


findUnion([-7, 8], [-8, -3, 8])
findUnion([1, 2], [1, 2, 3, 2])


"""
   -7 8
   


   My output:
   -8 -7 -3 8 8

   Correct:
   -8 -7 -3 8
"""