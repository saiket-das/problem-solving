# https://leetcode.com/problems/median-of-two-sorted-arrays/description/



"""
    Brute Force: Merge + Sorting
        TC: O(n + m)
        SC: O(n + m)

        `n` = The length of List 1 and `m` = The length of List 2
"""
def bruteForce(nums1: list[int], nums2: list[int]) -> float:
    # Get the length of `nums1` and `nums2`
    n1, n2 = len(nums1), len(nums2)

    # Merger both (nums1 and nums2) list
    merged = []
    i, j = 0, 0
    while i < n1 and j < n2:
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append( nums2[j])
            j += 1

    # Append the left-out curr_elements
    merged.extend(nums1[i:])
    merged.extend(nums2[j:])
    
    # Get the length of merged list
    n = n1 + n2

    # If the length is odd, return the middle curr_element as the median
    if n % 2 == 1:
        return float(merged[n // 2])
    
    # If the length is event, return the average of the two middle curr_elements
    median = (merged[n // 2] + merged[n // 2 - 1]) / 2
    return median
    


"""
    Better: Two-Pointer
        TC: O(n + m)
        SC: O(n + m)

        `n` = The length of List 1 and `m` = The length of List 2
"""
def better(nums1: list[int], nums2: list[int]) -> float:
    # Get the length of `nums1` and `nums2`
    n1, n2 = len(nums1), len(nums2)

    # Calculate the median index (and the one before it, for even total length)
    median_idx = (n1 + n2) // 2
    first_idx, second_idx = median_idx - 1, median_idx

    # Initialize variables to store the two middle elements
    first_ele, second_ele = -1, -1 
    count = 0

    # Pointers for traversing nums1 and nums2
    i, j = 0, 0
    while i < n1 and j < n2:
        if nums1[i] < nums2[j]:
            if count == first_idx:  first_ele = nums1[i]
            if count == second_idx: second_ele = nums1[i]
            i += 1
        else:
            if count == first_idx:  first_ele = nums2[j]
            if count == second_idx: second_ele = nums2[j]
            j += 1
            
        count += 1

    # If any elements remain in `nums1`, continue processing
    while i < n1:
        if count == first_idx:  first_ele = nums1[i]
        if count == second_idx: second_ele = nums1[i]
        count += 1
        i += 1
    
    # If any elements remain in `nums2`, continue processing
    while j < n2:
        if count == first_idx:  first_ele = nums2[j]
        if count == second_idx: second_ele = nums2[j]
        count += 1
        j += 1
    
    # If the total length is odd, return the middle (second) element
    if (n1 + n2) % 2 == 1:
        return float(second_ele)
    
    # If the total length is even, return the average of the two middle elements
    return (first_ele + second_ele) / 2
   


"""
    Optimal: Binary Search
        TC: O(n + m)
        SC: O(1)

        `n` = The length of List 1 and `m` = The length of List 2
"""
def optimal(nums1: list[int], nums2: list[int]) -> float:
    # Get the length of `nums1` and `nums2` list
    n1, n2 = len(nums1), len(nums2)

    # Ensure we always binary search the smaller list (nums1)
    if n1 > n2:
        return optimal(nums2, nums1)
    
    # Total length
    n = n1 + n2
    # The length of the left half (or the median index)
    half_length = (n1 + n2 + 1) // 2

    # Initialize the binary search bounds for the smaller array
    low, high = 0, n1

    while low <= high:
        partition1 = (low + high) // 2
        partition2 = half_length - partition1

        # Set boundaries for the left and right partitions
        left1, left2, right1, right2 = float('-inf'), float('-inf'), float('inf'), float('inf')

         # Check the elements at the current partition indices
        if partition1 < n1: right1 = nums1[partition1]
        if partition2 < n2: right2 = nums2[partition2] 
        if partition1 - 1 >= 0: left1 = nums1[partition1 - 1]
        if partition2 - 1 >= 0: left2 = nums2[partition2 - 1]
        
        # Check if the partition is correct
        if left1 <= right2 and left2 <= right1:
            # If the combined length is odd, return the max of left elements
            if n % 2 == 1:
                return float(max(left1, left2))
            # If the combined length is even, return the average of the max left and min right elements
            else:
                return (max(left1, left2) + min(right1, right2)) / 2
        
        # Adjust the binary search bounds based on partition comparison
        elif left1 > right2:
            high = partition1 - 1
        else:
            low = partition1 + 1

    # Return -1 if no valid partition is found (should not happen)
    return -1
   


# Main function
def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    # print(bruteForce(nums1, nums2))
    # print(better(nums1, nums2))
    print(optimal(nums1, nums2))


findMedianSortedArrays([10], [])                       # 10
findMedianSortedArrays([1,3], [2])                     # 2.000
findMedianSortedArrays([1,2], [3,4])                   # 2.500
findMedianSortedArrays([1,3,4,7,10], [2,3,6,15])       # 4.00
findMedianSortedArrays([1,3,4,7,10,12], [2,3,6,15])    # 5.00


"""
    Approach
      - Get the lengths of both input arrays
      - Ensure we always binary search the smaller array
      - Calculate the total length of both arrays combined
      - Calculate the length of the left half (or the median index)
      - Initialize the binary search bounds for the smaller array
      - Start binary search to find the correct partition  
      - Set boundaries for the left and right partitions
      - Check the elements at the current partition indices
      - Check if the partition is correct
        - If the combined length is odd, return the max of the left elements
        - If the combined length is even, return the average of the max left and min right elements
  
      - 10: Adjust the binary search bounds based on partition comparison
        - Move the high pointer left if the left side of partition1 is greater than right side of partition2
        - Move the low pointer right if the left side of partition2 is greater than right side of partition1
  
      - Return -1 if no valid partition is found (should not happen)
"""


"""
    [1,3,4,7,10,12], [2,3,6,15]

    req = 5

    2 3 6 14
    L   M  H
    partition1 = 2
    partition2 = 5 - 2 = 3



"""


"""
    Constraints:
      - nums1.length == m
      - nums2.length == n
      - 0 <= m <= 1000
      - 0 <= n <= 1000
      - 1 <= m + n <= 2000
      - -106 <= nums1[i], nums2[i] <= 106
"""