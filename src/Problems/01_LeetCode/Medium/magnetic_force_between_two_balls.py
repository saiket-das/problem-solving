# https://leetcode.com/problems/magnetic-force-between-two-balls/description/




# Function to check if all balls can be placed at a given distance.
def can_placed(position: list[int], distance: int, m: int) -> bool:
    n = len(position)
    remaining_to_place = m - 1    # One is already placed at the first position
    last_placed_index = 0         # First item placed at position[0]
    
    for i in range(1, n):
         # If the current position is far enough from the last placed item
        if distance <= (position[i] - position[last_placed_index]):
            remaining_to_place -= 1
            last_placed_index = i
        
        # All items placed successfully
        if remaining_to_place == 0:
            break
    
    # Return True or False 
    return remaining_to_place == 0
    

"""
    Brute Force: Linear Search
        TC: O(n log n) + O(max(position) * n)
        SC: O(1)
"""
def brute_force(position: list[int], m: int) -> int:
    # Sort the positions to ensure increasing order
    position.sort()

    max_pos = max(position)
    min_pos = min(position)

    # Initialize answer to the smallest possible value
    max_force = float('-inf')

    # Try every possible force from 1 up to the max possible distance
    for distance in range(1, max_pos - min_pos + 1):
    
        # Attempt to place remaining balls using at least `distance` between them
        isPlaced = can_placed(position, distance, m)
        
        # If all balls placed successfully, update max_force
        if isPlaced:
            max_force = max(max_force, distance)
        else:
            # Can't place more with this force or higher
            break
    
    return max_force



"""
    Optimal: Binary Search
        TC: O(n log n) + O(log max(position) * n)
        SC: O(1)
"""
def optimal(position: list[int], m: int) -> int:
    # Sort the positions to ensure increasing order
    position.sort()

    # Define the search range for the minimum distance
    min_pos = min(position)
    max_pos = max(position)
    low, high = 1, max_pos - min_pos  # Min possible distance = 1, max = spread

    
    # Initialize result to the lowest possible value
    max_force = float('-inf')

    # Binary search to find the largest minimum distance possible
    while low <= high:
        # `mid` candidate for minimum distance
        mid = (low + high) // 2

        is_possible = can_placed(position, mid, m)

        # If all balls placed successfully, update max_force
        if is_possible:
            # Valid placement found — try to increase the distance
            max_force = max(max_force, mid)
            low = mid + 1
        else:
            # Placement failed — reduce the distance
            high = mid - 1
    
    # Return the largest minimum distance found
    return max_force


# Main function
def maxDistance(position: list[int], m: int) -> int:
    # print(brute_force(position, m))
    print(optimal(position, m))


maxDistance([1,2,3,4,7], 3)               # 3
maxDistance([0,3,4,7,9,10], 4)            # 3
maxDistance([5,4,3,2,1,100000000], 2)    # 999999999

