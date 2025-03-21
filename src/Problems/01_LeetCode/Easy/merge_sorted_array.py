# https://leetcode.com/problems/merge-sorted-array/description/


""" **Do not return anything, modify nums1 in-place instead. ** """

"""
    Brute Force: Two Pointer
        Time Complexity:  O(m + n) + O(m + n) => O(m + n)
        Spcae Complexity: O(m + n)
"""
def brute_force(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    # List to store the merged sorted elements
    merged = []

    # Pointers for nums1 and nums2
    i, j = 0, 0

    # Merge elements from both arrays in sorted order
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    
    # Append remaining elements from `nums1` (if any)
    while i < m:
        merged.append(nums1[i])
        i += 1
    
    # Append remaining elements from `nums2` (if any)
    while j < n:
        merged.append(nums2[j])
        j += 1
    
    # Copy merged elements back to nums1
    for k, num in enumerate(merged):
        nums1[k] = num

    return nums1



"""
    Optimal: Two Pointer
        Time Complexity:  O(m + n)
        Spcae Complexity: O(1)
"""
def optimal(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    # Pointers for the last elements in both arrays
    r1 = m - 1
    r2 = n - 1

    # Last position in `nums1` array
    last = m + n - 1

    # Merge from the end to avoid shifting elements
    while r1 >= 0 and r2 >= 0:
        if nums1[r1] > nums2[r2]:
            nums1[last] = nums1[r1]     # Place larger element at the end
            r1 -= 1
        else:
            nums1[last] = nums2[r2]     # Place larger element at the end
            r2 -= 1
        last -= 1
    
    # If nums2 has remaining elements, place them in `nums1`
    while r2 >= 0:
        nums1[last] = nums2[r2]
        r2 -= 1
        last -= 1

    return nums1


# Main Function
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    # print(brute_force(nums1, m, nums2, n))
    print(optimal(nums1, m, nums2, n))


merge([0], 0, [1], 1)                 # [1]
merge([1], 1, [], 0)                  # [1]
merge([1,2,3,0,0,0], 3, [2,5,6], 3)   # [1,2,2,3,5,6]


"""
    ------------
    Example 1:
        Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
        Output: [1,2,2,3,5,6]
        Explanation: 
            The arrays we are merging are [1,2,3] and [2,5,6].
            The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
    ------------
    Example 2:
        Input: nums1 = [1], m = 1, nums2 = [], n = 0
        Output: [1]
        Explanation: 
            The arrays we are merging are [1] and [].
            The result of the merge is [1].
    ------------
    Example 3:
        Input: nums1 = [0], m = 0, nums2 = [1], n = 1
        Output: [1]
        Explanation: 
            The arrays we are merging are [] and [1].
            The result of the merge is [1].
            Note that because m = 0, there are no elements in nums1. 
            The 0 is only there to ensure the merge result can fit in nums1.
    ------------
"""
        