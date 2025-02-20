# https://www.geeksforgeeks.org/problems/pass-by-reference-and-value/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pass-by-reference-and-value

from typing import List

def passedBy(a, b) -> List[int]:
    # a pass by value. So, (a += 1)
    # b pass by reference. So, (b += 2)
    return [a+1, b+2]

print(passedBy(10, 20))