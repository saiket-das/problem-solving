# https://leetcode.com/problems/clear-digits/description/?envType=daily-question&envId=2025-02-10

"""
    Your task is to remove all digits by doing this operation repeatedly:
    Delete the first digit and the closest non-digit character to its left.
"""

"""
    :type s: str
    :rtype: str
"""
# Approach 1 - Time Complexity: O(n^2) and Space Complexity: O(1)
def clearDigits1(s: str) -> str:
    # Convert to LIST to simplify detele or remove digit (TC: O(n))
    s = list(s)    
    # Starting and Current index
    charIndex = 0
    while (charIndex < len(s)):   # TC: O(n)
        # If Current Index (charIndex) is Digit
        # Then delete Current index's value (which is a digit)
        if (s[charIndex].isdigit()):   
            del s[charIndex] 
            # If Current Index (charIndex)  more than 0 then have to delete left Character too     
            # After deleting the value, Decrement Current Index (charIndex) -1 for Removed Character 
            if (charIndex > 0):      
                del s[charIndex - 1] 
                charIndex -= 1       
        # If Current Index (charIndex) isn't a digit then increment Current Index (charIndex) + 1
        else:
            charIndex += 1           
    # Convert the list to String and Return
    return "".join(s)   
 
ans: str = clearDigits1("abc")
print("Answer: %s" %ans)

# ---------------------------
# Approach 2 - Time Complexity: O(n) and Space Complexity: O(n)
def clearDigits2(s: str) -> str:
    # To save the Char into Answer list
    answer = []

    for char in s:
        # If the element is DIGIT and answer is not empty then Pop or Remove last element from List
        if (char.isdigit() and answer):
            answer.pop()
        # If the element is CHAR then add to List
        else:
            answer.append(char)
    
    # Convert to String and Return
    return "".join(answer)  

ans2: str = clearDigits2("c5c")
print("Answer: %s" %ans2)

# abc  -> abc
# cb34 -> ""
# c5c  -> "c"

"""
    Example 1:
        Input: s = "abc"
        Output: "abc"
        ------------
        Explanation:
        There is no digit in the string.
    -------------------------------------
    Example 2:
        Input: s = "cb34"
        Output: ""
        ------------
        Explanation:
        First, we apply the operation on s[2], and s becomes "c4".
        Then we apply the operation on s[1], and s becomes "".

        cb34
        - i++, i++
        - i = 2
        - s[i] = 3. Remove Curent Index VALUE and New Stirng "cb4" then check there is any value in left 
          (means current index (i) more than 0)
        - In this case, our current index > 0 (i = 2) then remove left side value too and New Stirng "c4"
        - Need to decrement current index, as our New String length is 2 and current index (i = 2) --> i--
        - Repeat process

"""
