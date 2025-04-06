# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/


"""
    Optimal: Binary Search
        Time Complexity:  O(log 500 * n)
        Space Complexity: O(1)
"""
import math




def required_days(weights: list[int], capacity: int) -> int:
    # Start with first day
    total_weight, req_days = 0, 1

    for weight in weights:
        # If adding the current weight exceeds capacity, move to the next day
        if total_weight + weight > capacity:
            req_days += 1             # Increment day count
            total_weight = weight     # Start new day with current weight
        
        else:
            total_weight += weight    # Accumulate weight for current day

    return req_days



def optimal(weights: list[int], days: int) -> int:
    # The minimum possible capacity is the heaviest single weight (can't split it),
    # The maximum possible capacity is the total of all weights (everything in one day)
    min_capacity, max_capacity = max(weights), sum(weights)
    
    # Initialize binary search boundaries
    low, high = min_capacity, max_capacity

    # Binary search for the smallest capacity that works within `days`
    while low <= high:
        # `mid` is the current capacity candidate
        mid = (low + high) // 2
        
        # Calculate how many days are needed to ship all weights with the current capacity (`mid`)
        req_days = required_days(weights, mid)

        # Try to lower capacity
        if req_days <= days:
            high = mid - 1
        # Too many days needed, must increase capacity
        else:
            low = mid + 1
    
    # When loop ends, `low` is the minimum capacity that works
    return low



# Main function
def shipWithinDays(weights: list[int], days: int) -> int:
    print(optimal(weights, days))


shipWithinDays([1,2,3,1,1], 4)               # 3
shipWithinDays([3,2,2,4,1,4], 3)             # 6
shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5)    # 15