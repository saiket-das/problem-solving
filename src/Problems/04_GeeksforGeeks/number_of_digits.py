# Count total number of digits in a number
import math

# Time Complexity: O(log10(n)) 
def numberOfDigit (n) -> int:
    count: int = int(math.log10(n) + 1)

    return count
    # count: int  = 0
    # while (n != 0):
    #     count +=1
    #     n //= 10

    # return count

print(numberOfDigit(2356))