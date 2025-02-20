from collections import Counter

# https://leetcode.com/problems/top-k-frequent-elements/description/


"""
    Time Complexity:  O(N^2) -> O(N) + O((N - K) * N)
    Space Complexity: O(N)
"""

def topKFrequent(nums: list[int], k: int) -> list[int]:
    # Count frequency
    freq = Counter(nums)    # TC: O(N) and SC: O(N)

    # Continue until only k elements remain in the frequency map
    while (len(freq) > k):     # TC: O(N - K)
        # Find the element with the minimum frequency
        min_ele = min(freq, key=freq.get)    # TC: O(N)
        # Removes the minimum frequency element
        del freq[min_ele]
    
    return list(freq.keys())    # SC: O(K)
    


    

result = topKFrequent([1,1,1,2,2,3],  2)
print(result)

"""
[1,1,1,2,2,3],  2
[1], 1
"""


"""
    -----------
    Example 1:
        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1,2]
    -----------
    Example 2:
        Input: nums = [1], k = 1
        Output: [1]
    -----------
"""