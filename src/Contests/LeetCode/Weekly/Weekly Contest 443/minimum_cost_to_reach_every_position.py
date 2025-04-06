# https://leetcode.com/problems/minimum-cost-to-reach-every-position/description/


def minCosts(cost: list[int]) -> list[int]:
    # Get the length of the list
    n = len(cost)

    # Iterate through the list starting from index 1
    for i in range(1, n):
        # Update the current cost to be the minimum of the previous cost and the current cost
        cost[i] = min(cost[i - 1], cost[i])
    
    return cost