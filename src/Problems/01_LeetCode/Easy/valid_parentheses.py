# https://leetcode.com/problems/valid-parentheses/description/


"""
    Time Complexity:  O(n)
    Space Complexity: O(n)
    
    Approach:
      - Use a stack to track open brackets.
      - Iterate through each character:
          - If it's an opening bracket, push it onto the stack.
          - If it's a closing bracket:
            - Check if the stack is empty (invalid case).
            - Pop the last opening bracket and check if it matches.
            - If mismatched, return False.
      - At the end, if the stack is empty, return True; otherwise, return False.
"""

def isValid(s: str) -> bool:
    # Edge case: If the length of the string is odd, it can't be a valid pair
    if len(s) % 2 != 0:
        return False
    
    # Stack to keep track of opening brackets
    stack = []
    # Mapping of closing to opening brackets
    brackets = {')': '(', '}': '{', ']': '['}

    for ch in s:
        # If it's a closing bracket
        if (ch in brackets ):
            # Invalid if stack is empty or mismatched bracket
            if ((not stack) or (brackets[ch] != stack.pop())):
                return False
        # Else, Push opening brackets onto the stack
        else:
            stack.append(ch)
    
    # If the stack is empty, all brackets were matched properly
    return not stack  

print(isValid("()"))

"""
    -----------
    Example 1:
        Input: s = "()"
        Output: true
    -----------   
    Example 2:    
        Input: s = "()[]{}"
        Output: true
    -----------    
    Example 3:    
        Input: s = "(]"
        Output: false
    -----------
    Example 4:    
        Input: s = "([])"
        Output: true
    -----------
"""