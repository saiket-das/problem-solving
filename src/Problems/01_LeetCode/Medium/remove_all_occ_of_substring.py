# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/description/?envType=daily-question&envId=2025-02-11


"""
    :type s: str
    :type part: str
    :rtype: str
"""


def removeOccurrences(s: str, part: str) -> str:
    # s: axxxxyyyyb, part: xy
    stack: list[chr] = []
    last_char: chr = part[-1]

    # Iterate though String (s - axxxxyyyyb) 
    for c in s:
        # Append character to Stack
        stack.append(c)
        # Check Last character (y) of PART and Current char is same 
        if (c == last_char):
            # If same then pop last 2 elements (why 2, beacuse size of PART string is 2)
            # Save the string Temporary (temp)
            temp: str = ""
            for i in range(len(part)):
                if (stack):     # Check stack is not empty
                    temp += stack.pop()
            # If PART and TEMP (Reverse order) string are not same then Apppend Temp' char to Stack again
            if (part != temp[::-1]):
                # Reverse the Temp string before append
                temp = temp[::-1]
                for ch in temp:
                    stack.append(ch)
    
    # Return as String
    return "".join(stack)

print(removeOccurrences("gjzgbpggjzgbpgsvpwdk", "gjzgbpg"))

# daabcbaabcb -> dabaabcb -> dabab
# gjzgbpggjzgbpgsvpwdk - gjzgbpg

"""
    Example 1
        Input: s = "daabcbaabcbc", part = "abc"
        Output: "dab"
    
    Example 2
        Input: s = "axxxxyyyyb", part = "xy"
        Output: "ab"
"""