# https://leetcode.com/problems/split-array-largest-sum/description/



def countSubarraysWithMaxSum(nums, n, i):
    subarray_count = 1
    current_sum = 0

    for j in range(0, n):
        if current_sum + nums[j] <= i:
            current_sum += nums[j]
        else:
            # Start a new subarray
            current_sum = nums[j]
            subarray_count += 1
    
    return subarray_count


"""
    Brute Force:
        TC: O(n) + O(sum(nums) * n)
        SC:
"""
def bruteForce(nums: list[int], k: int) -> int:
    # Get length of the list
    n = len(nums)

    # The minimum possible largest sum is the largest element
    # The maximum possible largest sum is the total sum of the array
    min_possible = max(nums)
    max_possible = sum(nums)

    for target_max_sum in range(min_possible, max_possible + 1):
        if countSubarraysWithMaxSum(nums, n, target_max_sum) == k:
            return target_max_sum
    
    # Should never happen if input is valid
    return -1



"""
    Optimal: Binary Search
        TC: O(log (sum - max + 1) * n)
        SC: O()
"""
def optimal(nums: list[int], k: int) -> int:
    # Get length of the list
    n = len(nums)

    # The minimum possible largest sum is the largest element
    # The maximum possible largest sum is the total sum of the array
    low = max(nums)
    high = sum(nums)

    while low <= high:
        # `mid` as the largest subarray sum
        mid = (low + high) // 2

        if countSubarraysWithMaxSum(nums, n, mid) > k:
            # More subarrays needed the limit is too small, increase it
            low = mid + 1
        else:
            # try a smaller limit
            high = mid - 1
    
    # 'low' is the smallest value where it's possible to split into exactly k subarrays
    return low
        


    


# Main function
def splitArray(nums: list[int], k: int) -> int:
    # print(bruteForce(nums, k))
    print(optimal(nums, k))

splitArray([1,2,3,4,5], 2)     # 9 [4, 5]
splitArray([7,2,5,10,8], 2)    # 18 [10, 8]