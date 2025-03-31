# O(log(n)) Time Complexity


"""
    Perform binary search on a sorted array to find the target index.
    
    Time Complexity: O(log N)
    
    Explanation:
        log N (2^x = N)
        Example:
            1. If array length is 8 → Loop runs ≈ 3 times
            2. 2^3 = 8 (since log₂(8) = 3)
"""

def binary_search(arr, target) -> list[int]:
    loop = 0    # To keep track of total loop
    # Two pointer
    left, right = 0, len(arr) - 1 
    while (left <= right):
        mid = (right + left) // 2
        loop += 1
        # Mid index's value == Target then return
        if (arr[mid] == target):
            return [mid, loop]
        elif (arr[mid] < target):
            left = mid + 1
        else:
            right = mid - 1
    
    return [-1, loop]




sorrted_arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
# Return the index of Target value
result = binary_search(sorrted_arr, 11)
print("Index: %d" %result[0])
print("Loop: %d" %result[1])

"""
    Array = [1, 3, 5, 7, 9, 11, 13, 15] and Target = 11
    left = 0, mid = 3, right = 7

    1. 1st loop
        i) mid = (7 + 0) / 2 = 3
            [1(left), 3, 5, 7(mid), 9, 11, 13, 15(right)]
            left = 0, mid = 3 and right = 7
        ii) Array[mid] (7) != Target (11) and Target is greater then Array[mid]
            [1 , 3, 5, 7 (mid), 9(left), 11, 13, 15 (right)]

    2. 2nd loop
        i) mid = (7 + 4) / 2 = 5
            [1, 3, 5, 7, 9(left), 11(mid), 13, 15(right)]
            left = 4, mid = 5 and right = 7
        ii) Array[mid] (11) == Target (11) return mid (5)
"""
