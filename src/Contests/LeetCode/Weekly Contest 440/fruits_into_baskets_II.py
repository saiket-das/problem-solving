# https://leetcode.com/problems/fruits-into-baskets-ii/description/


"""
    Brute Force
        Time Complexity:  O(f * b) + O(b)
        Space Complexity: O(b)

    `f` = The number of fruits & `b` = The number of baskets
"""
def brute_force(fruits: list[int], baskets: list[int]) -> int:
    # Total number of baskets
    num_baskets = len(baskets)

    # Track whether a fruit is placed in each basket
    is_fruit_placed = [False] * num_baskets

    # Try placing each fruit in an available basket
    for fruit in fruits:
        for i in range(num_baskets):
            if fruit <= baskets[i] and not is_fruit_placed[i]:
                # Mark the basket as occupied
                is_fruit_placed[i] = True 
                break    # Move to the next fruit once placed

    # Count baskets that remain unoccupied
    unplaced_baskets_count = sum(not placed for placed in is_fruit_placed)
    
    return unplaced_baskets_count


"""
    Optimal
        Time Complexity:  O(f * b)
        Space Complexity: O(1)
    
    `f` = The number of fruits & `b` = The number of baskets
"""
def optimal(fruits: list[int], baskets: list[int]) -> int:
    # Total number of baskets
    num_baskets = len(baskets)

    # Counter for fruits that couldn't be placed
    unplaced_fruits = 0

    # Try placing each fruit in an available basket
    for fruit in fruits:
        unplaced = True
        for i in range(num_baskets):
            # Check if the fruit fits in the basket
            if fruit <= baskets[i]:
                baskets[i] = 0      # Mark the basket as occupied by setting it to 0
                unplaced = False    # The fruit has been placed
                break               # Move to the next fruit
        
        # Increment count if the fruit remains unplaced
        unplaced_fruits += unplaced
    
    return unplaced_fruits


def numOfUnplacedFruits(fruits: list[int], baskets: list[int]) -> int:
    # print(brute_force(fruits, baskets))
    print(optimal(fruits, baskets))

numOfUnplacedFruits([4,2,5], [3,5,4])    # 1
numOfUnplacedFruits([3,6,1], [6,4,7])    # 0