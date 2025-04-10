# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/



"""
"""
def brute_force(digits: str) -> list[str]:
    ans = []

    call = {"2": {"a", "b", "c"},
            "3": {"d", "e", "f"},
            "4": {"g", "h", "i"},
            "5": {"j", "k", "l"},
            "6": {"m", "n", "o"},
            "7": {"p", "q", "r", "s"},
            "8": {"t", "u", "v"},
            "9": {"w", "x", "y", "z"},
            }

    if not digits:
        return ans
    
    for digit in digits:
        print(digit)

    return ans



def letterCombinations(digits: str) -> list[str]:
    print(brute_force(digits))

letterCombinations("")      # []
letterCombinations("2")     # ["a", "b", "c"] 
letterCombinations("23")    # ["ad","ae","af","bd","be","bf","cd","ce","cf"]

"""
   0 -> 0
   1 -> 3
   2 -> 9
   3 -> 27
   4 -> 81
"""

"""
    Constraints:
      - 0 <= digits.length <= 4
      - digits[i] is a digit in the range ['2', '9'].
"""