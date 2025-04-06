# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/



"""
    Brute Force
        Time Complexity:  O(n) + O(max(bloomDay) * (O(n) + O(n)))
        Space Complexity: O(n)
"""
def brute_force(bloomDay: list[int], m: int, k: int) -> int:
    n = len(bloomDay)

    # Edge case: If the total number of flowers is less than the number needed for all bouquets, return -1
    if n < m * k:
        return -1
    
    # Find the maximum number of days it takes for any flower to bloom
    max_bloom_day = max(bloomDay)    # TC: O(n)

    # Iterate over each possible day (from 1 to max_bloom_day)
    for current_day in range(1, max_bloom_day + 1):
        # List to track if a flower is blooming on the current day
        is_blooming = [0] * n

        # Mark each flower that has bloomed by the current day
        for idx, bloom_day in enumerate(bloomDay):
            # Flower blooms on or before 'current_day'
            if current_day >= bloom_day:
                is_blooming[idx] = 1
            else:
                is_blooming[idx] = 0
        

        # Variables to count adjacent blooming flowers and completed bouquets
        adj_count, bouquet_count = 0, 0

        # Count consecutive blooming flowers to form bouquets
        for bloom_status in is_blooming:
            if bloom_status:
                adj_count += 1
            else:
                adj_count = 0    # Reset count if no blooming flower is found
            
            # When 'k' consecutive blooming flowers are found, form a bouquet and reset count
            if adj_count == k:
                bouquet_count += 1
                adj_count = 0
        
        # If the required number of bouquets are formed, return the current day
        if bouquet_count == m:
            return current_day
    
    # If it's not possible to form 'm' bouquets by any day, return -1
    return -1



"""
    Optimal
        Time Complexity:  O(n) + O(log max(bloomDay) * (O(n) + O(n)))
        Space Complexity: O(n)
"""
def optimal(bloomDay: list[int], m: int, k: int) -> int:
    # Get the length of the list
    n = len(bloomDay)

    # Edge Case: Number of flowers need to more than flower we need to make total bouquets
    if n < m * k:
        return -1

    # Find the minimum and maximum number of days it takes for any flower to bloom
    min_bloom_day, max_bloom_day = float('inf'), float('-inf')
    for day in bloomDay:    # TC: O(n)
        min_bloom_day = min(day, min_bloom_day)
        max_bloom_day = max(day, max_bloom_day)

    # Binary search to find the minimum day on which 'm' bouquets can be made
    low, high = min_bloom_day, max_bloom_day

    while low <= high:
        # Set the middle day in the current range as the candidate day
        mid = (low + high) // 2
        
        # Variables to count adjacent blooming flowers and completed bouquets
        adj_count, bouquet_count = 0, 0

        # Count consecutive blooming flowers
        for bloom_day in bloomDay:
            if bloom_day <= mid:    # If the flower has bloomed by the current day (`mid`)
                adj_count += 1      # Increase the count of consecutive blooming flowers
            else:
                adj_count = 0       # Reset count if an unbloomed flower is encountered
            
            # If `k` consecutive blooming flowers are found, form a bouquet
            if adj_count == k:
                bouquet_count += 1    # Increase bouquet count
                adj_count = 0         # Reset consecutive count to start forming the next bouquet
        
        # If the required number of bouquets are formed, return the current day
        if bouquet_count < m:
            low = mid + 1
        else:
            high = mid - 1
    
    # Return the minimum day when it's possible to form 'm' bouquets
    return low



def minDays(bloomDay: list[int], m: int, k: int) -> int:
    # print(brute_force(bloomDay, m, k))
    print(optimal(bloomDay, m, k))


"""
    bloomDay = [Number of days a flower to bloom]
    m = Number of bouquets need to make
    k = Need to use `k` is_blooming flowers make one bouquet

    Return: Minimum days to make `m` bouquets
"""

minDays([1,10,3,10,2], 3, 1)       # 3
minDays([1,10,3,10,2], 3, 2)       # -1
minDays([7,7,7,7,12,7,7], 2, 3)    # 12



# Mine
minDays([1,2,3,4,5,6,7], 2, 3)    # 6
minDays([1,2,3,4,5,6,7], 2, 2)    # 4
minDays([7,7,7,7,7,7,7], 2, 3)    # 7