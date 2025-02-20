# https://leetcode.com/problems/merge-sorted-array/description/


"""
    Do not return anything, modify nums1 in-place instead.
"""
"""
    Approach 1:
        Time Complexity:  O(m + n)
        Spcae Complexity: O(m + n)
"""
# def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
#     # Initialize an empty list 'temp' to store the merged elements
#     temp: list[int] = []

#     # Initialize two pointers for nums1 and nums2
#     l1, l2 = 0, 0

#     # Adjust m and n to represent valid last indices
#     m -= 1
#     n -= 1

#     # Merge both arrays by comparing elements
#     while (l1 <= m and l2 <= n):
#         if (nums1[l1] <= nums2[l2]):
#             temp.append(nums1[l1])    # Append smaller element from nums1
#             l1 += 1
#         else:
#             print(l2)
#             temp.append(nums2[l2])    # Append smaller element from nums2
#             l2 += 1
    
#     # Append remaining elements from nums1 (if any)
#     while (l1 <= m):
#         temp.append(nums1[l1])
#         l1 += 1
#     # Append remaining elements from nums2 (if any)
#     while (l2 <= n):
#         temp.append(nums2[l2])
#         l2 += 1
    
#     # Copy merged elements back from ('temp') to nums1
#     for i in range(len(temp)):
#         nums1[i] = temp[i]


"""
    Approach 2:
        Time Complexity:  O(m + n)
        Spcae Complexity: O(1)
"""
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    # Pointers for the last elements in both arrays
    r1 = m - 1
    r2 = n - 1

    # Last position in 'nums1' array
    last = m + n - 1

    # Merge from the end to avoid shifting elements
    while (r1 >= 0 and r2 >= 0):
        if (nums1[r1] > nums2[r2]):
            nums1[last] = nums1[r1]     # Place larger element at the end
            r1 -= 1
        else:
            nums1[last] = nums2[r2]     # Place larger element at the end
            r2 -= 1
        last -= 1
    
    # If nums2 has remaining elements, place them in nums1
    while (r2 >= 0):
        nums1[last] = nums2[r2]
        r2 -= 1
        last -= 1

    print(nums1)

merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)

"""
    ---------
    Input:
        [1,2,3,0,0,0], 3, [2,5,6], 3
    Output:
        [1,2,2,3,5,6]
    ---------
    Input:
        [0], 0, [1], 1
    Output:
        [1]
    ---------
    Input:
        [1], 1, [], 0
    Output:
        [1]
    ---------
"""

"""
    TC: O(m + n)
    SC: O(m + n)
    Approach 1: [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3
        ** As both arrays are already sorted, no need to divide and sort them **
        1. Initilize Left 1 ('l1') variable for Array 1 and Left 2 variable ('l2') for Array 2
        2. Adjust m and n to represent valid last indices 
        3. Check left and Right array value and Save to Temporary arary ('temp')
            [1, 2, 3] -- [2, 5, 6]
            - [1, 2, 3] -> 'nums1'
            - [1, 2, 3]
            - [1, 2, 2, 3]
            - [1, 2, 2, 3, 5]
            - [1, 2, 2, 3, 5, 6] -> Merged
        4. Copy merged elements back from ('temp') to nums1
    -----------------

    TC: O(m + n)
    SC: O(1)
    Approach 2: [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3
        1. Initilize Right 1 ('r1' = m-1) variable for Array 1 and Rightt 2 ('r2' = n-1) variable for Array 2
        2. Start merging from the last valid index (p = m + n - 1) to avoid shifting elements.
        3. Compare the largest elements from both arrays and place the largest at the end.
        4. Continue until one of the arrays is fully merged.
        5. If 'nums2' has remaining elements, copy them directly into 'nums1' (because nums1 is already sorted).
"""


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
        