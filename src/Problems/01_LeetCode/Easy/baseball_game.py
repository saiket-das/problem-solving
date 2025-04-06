# https://leetcode.com/problems/baseball-game/



"""
    Optimal: Stack
        Time Complexity:  O(n)
        Space Complexity: O(n)
"""
def optimal(operations: list[str]) -> int:
    # Stack to store valid scores
    stack = []

    for char in operations:
        # "C" removes the last valid score if the stack isn't empty
        if char == "C":
            if stack:
                stack.pop() 
        
        # "D" doubles the last valid score and appends it back
        elif char == "D":
            if stack:
                last_num = stack[-1]    # Get the last score without removing it
                stack.append(last_num * 2)
        # "+" adds the sum of the last two valid scores
        elif char == "+":
            if len(stack) > 1:
                last_num = stack[-1]    # Last valid score
                sec_last = stack[-2]    # Second last valid score
                stack.append(last_num + sec_last)
        else:
            # Convert numeric string to an integer and add to stack
            stack.append(int(char))
    
    # Compute the total sum of all valid scores
    return sum(stack)


def calPoints(operations: list[str]) -> int:
    print(optimal(operations))


calPoints(["1","C"])                             # 0
calPoints(["5","2","C","D","+"])                 # 30
calPoints(["5","-2","4","C","D","9","+","+"])    # 27
