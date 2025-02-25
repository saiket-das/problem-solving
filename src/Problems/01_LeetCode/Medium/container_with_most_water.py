# https://leetcode.com/problems/container-with-most-water/description/


"""
    Time Complexity:  O(n)
    Space Complexity: O(1)
"""

def maxArea(height: list[int]) -> int:
    # Variable to store the maximum water trapped
    max_water = 0

    # Two pointers: left (l) starts at the beginning, right (r) at the end
    l, r = 0, len(height) -1

    # Iterate while left pointer is less than right pointer
    while (l < r):
        # Find the minimum height between the two pointers
        min_height = min(height[l], height[r])
        # Calculate the area of water stored between the two heights
        water = (min_height * (r - l))

        # Update max_water if the current water is greater than the previous maximum
        max_water = max(water, max_water) 

        # Move the pointer with the smaller height, as it is the limiting factor
        if (height[l] < height[r]):
            l += 1
        else:
            r -= 1

    return max_water

print(maxArea([1,8,6,2,5,4,8,3]))

"""
    -----------
    Example 1:
        Input: height = [1,8,6,2,5,4,8,3,7]
        Output: 49
        Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
            In this case, the max area of water (blue section) the container can contain is 49.
    -----------
    Example 2:
        Input: height = [1,1]
        Output: 1
    -----------
"""