# https://leetcode.com/problems/permutations/description/



"""
    Brute Force:
       Time Complexity:  O(n * n)
       Space Complexity: O(n * n)
"""
def brute_force(nums: list[int]) -> list[list[int]]:
    n = len(nums)

    if n == 1:
        return [nums]

    ans = []
    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            temp = []
            temp.append(nums[j])
            for k in range(n):
                if k == j:
                    continue
                temp.append(nums[k])
            ans.append(temp)

    return ans




# Main Function
def permute(nums: list[int]) -> list[list[int]]:
    print(len(brute_force(nums)))

permute([0,1])      # [[0,1],[1,0]]
permute([1])        # [[1]]
permute([1,2,3])    # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

permute([1, 2, 3, 5, 6])
 