# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/


"""
    Approach: Dynamic Programming
        Time Complexity:  O(n)
        Space Complexity: O(1)
"""
def maxProfit(prices: list[int]) -> int:
    # Initialize the first buy price as the first element and max profit as 0
    buy_price, max_profit = prices[0], 0

    # Iterate through each price in the list
    for curr_price in prices:
        # Calculate the profit if we were to sell at the current price
        curr_profit = curr_price - buy_price

        # Update the maximum profit if the current profit is greater
        max_profit = max(curr_profit, max_profit)
        
        # Update the buy price to the lowest price seen so far
        buy_price = min(curr_price, buy_price)

    return max_profit

print(maxProfit([7,4,1,5,3,6,4]))    # 5
print(maxProfit([7,6,4,3,1]))        # 0

"""
    ----------
    Example 1:
        Input: prices = [7,1,5,3,6,4]
        Output: 5
        Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
                     Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
    ----------
    Example 2:
        Input: prices = [7,6,4,3,1]
        Output: 0
        Explanation: In this case, no transactions are done and the max profit = 0.
    ----------
"""