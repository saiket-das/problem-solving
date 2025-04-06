# https://leetcode.com/problems/koko-eating-bananas/description/


import math

"""
    Brute Force: 
        Time Complexity: O(n) +  O(max(piles) * n) => (Time Limit Exceeded)
        Space Complexity: O(1)
"""
def brute_force(piles: list[int], h: int) -> int:
    # Find the maximum number of bananas in a single pile
    max_banans = max(piles)

    # Iterate over possible eating speeds from 1 to max_bananas
    for banana in range(1, max_banans + 1):
        # Variable to store the total hours required for this speed
        req_times = 0

        # Calculate total hours needed to eat all piles at the current speed
        for pile in piles:
            # Compute the hours needed for each pile
            req_times += math.ceil(pile / banana)
        
        # If the total required time is within the given hours limit, return this speed
        if req_times <= h:
            return banana
        

"""
    Optimal: 
        Time Complexity:  O(n) + O(log n * max(piles))
        Space Complexity: O(1)
"""
def optimal(piles: list[int], h: int) -> int:
    # Find the maximum number of bananas in a single pile
    max_banans = max(piles)

    # Define the search range for the minimum eating speed (1 to max_bananas)
    low, high = 1, max_banans

    # Perform binary search to find the optimal eating speed
    while low <= high:
        # Calculate the middle value as the current eating speed
        mid = (low + high) // 2

        # Variable to store the total hours required for this speed
        req_times = 0

        for pile in piles:
            # Compute the hours needed for each pile
            req_times += math.ceil(pile / mid)
        
        # If Koko can finish within the given hours, try a lower eating speed
        if req_times <= h:
            high = mid - 1
        # If Koko needs more time, increase the eating speed  
        else:
            low = mid + 1
    
    # After the loop, 'low' holds the smallest valid eating speed
    return low


# Main function
def minEatingSpeed(piles: list[int], h: int) -> int:
    # print(brute_force(piles, h))
    print(optimal(piles, h))


minEatingSpeed([3,6,7,11], 8)         # 4
minEatingSpeed([30,11,23,4,20], 5)    # 30
minEatingSpeed([30,11,23,4,20], 6)    # 23
minEatingSpeed([1,1,1,999999999], 10)    # 142857143

