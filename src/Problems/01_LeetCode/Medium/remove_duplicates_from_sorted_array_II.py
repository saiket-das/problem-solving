# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150


"""
    Optimal: Two-Pointer
        TC: O(n)
        SC: O(1)
"""
def optimal(nums: list[int]) -> int:
    # Get the length of the list and initialize pointer j at index 2 (since we allow up to 2 duplicates)
    n, j = len(nums), 2

    # Start checking from the 3rd element (index 2)
    for i in range(2, n):
        # If the current number is not equal to the number two places before j,
        if nums[i] != nums[j - 2]:
            # it means it's allowed (not a third+ duplicate)
            nums[j] = nums[i] 
            j += 1
    
    # Return the new length of the array with at most two duplicates
    return j


def removeDuplicates(nums: list[int]) -> int:
    print(optimal(nums))


removeDuplicates([1,1,1,2,2,3])          # 5 -> [1,1,2,2,3,_]
removeDuplicates([0,0,1,1,1,1,2,3,3])    # 7 -> [0,0,1,1,2,3,3,_,_]


"""
    Count index of same element to get the count of specific element
"""