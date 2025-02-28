# https://www.geeksforgeeks.org/problems/who-will-win-1587115621/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=who-will-win


"""
    Brute Force
        Time Complexity:  O(n)
        Space Complexity: O(1)
"""

def linear_search(arr, k) -> int:
    
    for i in range(len(arr)):
        if (arr[i] == k):
            return i
    
    return -1

"""
    Optional
        Time Complexity:  O(log n)
        Space Complexity: O(1)
"""
def binary_search(arr, k)  -> int:
    # Length of List
    n = len(arr)

    # Initialize two pointers (left and right) for binary search
    l, r = 0, n - 1

    # Perform binary search
    while (l <= r):
        # Calculate the middle index
        m = (r + l) // 2 

        # Check if the middle element is the target
        if (arr[m] == k):
            return m    # Return the index if found
        
         # If target is smaller, search in the left half
        elif (k < arr[m]):
            r = m - 1  

        # If target is greater, search in the right half
        else:
            l = m + 1

    # Target not found, return -1
    return -1

def searchInSorted(arr, k):

    # print(linear_search(arr, k))
    print(binary_search(arr, k))


searchInSorted([1, 2, 3, 4, 6], 6)