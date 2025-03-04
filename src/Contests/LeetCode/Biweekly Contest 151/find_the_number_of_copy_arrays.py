# https://leetcode.com/problems/find-the-number-of-copy-arrays/description/



def countArrays(original: list[int], bounds: list[list[int]]) -> int:
    l, r = -2**9, 2**9
    for i in range(len(original)):
        ai = original[i]
        u, v = bounds[i][0], bounds[i][1]
        l = max(l, u - ai)
        r = min(r, v - ai)

    if (l > r):
        return 0
    return r - l + 1


print(countArrays([1,2,3,4], [[1,2],[2,3],[3,4],[4,5]]))
print(countArrays([1,2,3,4], [[1,10],[2,9],[3,8],[4,7]]))
print(countArrays([1,2,1,2], [[1,1],[2,3],[3,3],[2,3]]))