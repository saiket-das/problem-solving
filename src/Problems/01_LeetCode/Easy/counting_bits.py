# https://leetcode.com/problems/counting-bits/description/

"""
    Time Complexity:  O(n log n)
    Space Complexity: O(n)

    Approach:
      - 5 => [0, 1, 1, 2, 1, 2]
      - Initialize `bits` array of size (n+1) to store results.
      - Iterate through numbers from `0` to `n`:
          - Convert each number to binary by counting the number of 1s.
          - Append the count to the `bits` array.
      - Return the final list.
"""

def countBits(n: int) -> list[int]:
    # Edge case: If n is 0, return [0] since its binary representation has zero 1s
    if n == 0:
        return [0]
    # List to store the count of 1s in binary representation for numbers 0 to n
    bits = []

    # Iterate through all numbers from 0 to n
    for i in range(n+1):
        # Temporary variable to store the current number
        temp: int = i
        # Counter for 1s in binary representation
        value: int = 0

        # Convert the number to binary and count the 1s
        while (temp != 0):
            remainder: int = temp % 2
            value += remainder    # Add 1 if the last bit is 1
            temp //= 2            # Right shift by dividing by 2
        
        # Store the count of 1s for this number
        bits.append(value)

    return bits

result = countBits(7)
print(result)


"""
    ** It is very easy to come up with a solution with a runtime of O(n log n). 
    Can you do it in linear time O(n) and possibly in a single pass? **
    -----------
    Example 1:
        Input: n = 2
        Output: [0,1,1]
        Explanation:
        0 --> 0
        1 --> 1
        2 --> 10
    -----------
    Example 2:
        Input: n = 5
        Output: [0,1,1,2,1,2]
        Explanation:
        0 --> 0
        1 --> 1
        2 --> 10
        3 --> 11
        4 --> 100
        5 --> 101
    -----------
"""