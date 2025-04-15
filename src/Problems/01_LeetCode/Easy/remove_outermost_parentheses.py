# https://leetcode.com/problems/remove-outermost-parentheses/description/


"""
    Optimal:
        TC: O(n)
        SC: O(n)
"""
def optimal(s: str) -> str:
    # Initialize a list to store the final result and a counter to track open parentheses
    ans, opened = [], 0

    # Iterate through each character in the input string
    for ch in s:
        # If it's an opening parenthesis and it's not the first one, include it
        if ch == '(' and opened > 0:
            ans.append(ch)
        
        # If it's a closing parenthesis and there's more than one open, include it
        if ch == ')' and opened > 1:
            ans.append(ch)
        
        # Update the count of open parentheses
        # Increment if '(', otherwise decrement (assumed to be ')')
        opened += 1 if ch == '(' else -1
    
    # Join the valid parentheses into a string and return
    return "".join(ans)
        
def removeOuterParentheses(s: str) -> str:
    print(optimal(s))


removeOuterParentheses("()()")                  # ""
removeOuterParentheses("(()())(())")            # "()()()"
removeOuterParentheses("(()())(())(()(()))")    # "()()()()(())"