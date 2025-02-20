# https://leetcode.com/problems/two-sum/description/

"""
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
"""
from typing import List

def twoSum(nums: List[int], target: int):
    hashMap: int = {}  # (NUM: INDEX of Num) -> {2: 0, 11: 1, 7: 2}

    for i in range(len(nums)):
        # Find the COMPLEMENT Num of CURRENT Num
        complement: int = target - nums[i]

        # If COMPLEMENT Num is available in HASHMAP then return the INDEX of COMPLEMENT Num's and CURRENT Num's INDEX
        if (complement in hashMap):
            return [hashMap.get(complement), i]
        # If COMPLEMENT Num is not available in HASHMAP then add COMPLEMENT Num into HASHMAP like {NUM: INDEX of Num}
        else:
            hashMap[nums[i]] = i

print(twoSum([3,2,4], 6))


"""
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    -------
    Input: nums = [3,2,4], target = 6
    Output: [1,2]
    -------
    Input: nums = [3,3], target = 6
    Output: [0,1]
"""

"""
    nums = [2,7,11,15], target = 9

    1. hashMap = {}
    2. Iterate through nums LIST or ARRAY
    3. Find the COMPLEMENT number of current number
    4. If COMPLEMENT Num is available in HASHMAP then return the INDEX of COMPLEMENT Num's and CURRENT Num's INDEX
    5. If COMPLEMENT Num is not available in HASHMAP then add COMPLEMENT Num into HASHMAP like {NUM: INDEX of Num}
"""
        