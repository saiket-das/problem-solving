# https://leetcode.com/problems/distribute-candies/description/


"""
    Brute Force: Sorting
        TC: O(n log n) + O(n)
        SC: O(1)
"""
def brute_froce(candyType: list[int]) -> int:
    n = len(candyType)
    can_eat = n // 2

    candyType.sort()

    last_type, count = candyType[0], 1
    for i in range(1, n):
        if last_type != candyType[i]:
            last_type = candyType[i]
            count += 1
        
        if count == can_eat:
            break
    
    return count if count <= can_eat else can_eat
    


"""
    Optimal: HashSet
        TC: O(n)
        SC: O(n)
"""
def better(candyType: list[int]) -> int:
    # Calculate the maximum number of different candy types You can eat
    total_candies = len(candyType)
    # You can eat only half of the candies
    max_candies_allowed = total_candies // 2

    unique_candy_types = set(candyType)
    total_unique_types = len(unique_candy_types)
    
    # You can eat at most `max_candies_allowed` types, or all unique types if fewer
    return total_unique_types if total_unique_types <= max_candies_allowed else max_candies_allowed


# Main function
def distributeCandies(candyType: list[int]) -> int:
    # print(brute_froce(candyType))
    print(better(candyType))



distributeCandies([1,2])           # 1
distributeCandies([1,1,2,3])       # 2
distributeCandies([6,6,6,6])       # 1
distributeCandies([1,1,2,2,3,3])   # 3
distributeCandies([1,1,1,2,2,2])   # 2
