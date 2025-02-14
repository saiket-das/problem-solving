# https://leetcode.com/problems/add-two-numbers/?envType=daily-question&envId=2025-02-11

"""
    :type l1: Optional[ListNode]
    :type l2: Optional[ListNode]
    :rtype: Optional[ListNode]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # Store the node's value
        self.next = next    # Reference to the next node

def addTwoNumbers(l1, l2) -> ListNode:
    # Initialize Answer Linked List (ans_list) with 0 value
    # Current value to keep track of node
    # Carry (To keep Remainder value of Sum)
    ans_list = ListNode(0)
    current = ans_list
    carry = 0

    while l1 or l2 or carry:
        # Find current node's value of both List
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # Calculate Total and Carry (if Total is more than 10 then rest value is Carry)
        total = val1 + val2 + carry
        carry = total // 10
        # Save Next node's value
        current.next = ListNode(total % 10)
        # Move Current node to Next node
        current = current.next

        # If List 1 or List 2 are not empty then move to Next node
        if l1:
            l1 = l1.next
        if l2: 
            l2 = l2.next
    
    # Return 2nd Node of Answer List (As first list is 0 (which is not part of))
    return ans_list.next

# List Node 1
l1_node7 = ListNode(9)          
l1_node6 = ListNode(9, l1_node7)   
l1_node5 = ListNode(9, l1_node6)   
l1_node4 = ListNode(9, l1_node5)   
l1_node3 = ListNode(9, l1_node4)   
l1_node2 = ListNode(9, l1_node3)   
l1_node1 = ListNode(9, l1_node2)


# List Node 2
l2_node4 = ListNode(9)
l2_node3 = ListNode(9, l2_node4)   
l2_node2 = ListNode(9, l2_node3)   
l2_node1 = ListNode(9, l2_node2)


l1 = l1_node1
l2 = l2_node1
result = addTwoNumbers(l1, l2)

# Print the result list
while result:
    print(result.val, end=" -> " if result.next else "")
    result = result.next
print()
        


"""
    Input: l1 = [2,4,3], l2 = [5,6,4]
        Output: [7,0,8]
        Explanation: 342 + 465 = 807.
    ----------
    Example 2:
        Input: l1 = [0], l2 = [0]
        Output: [0]
    ----------
    Example 3:
        Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
        Output: [8,9,9,9,0,0,0,1]

    Solution
        1. Initialize Answer Linked List (ans_list) with 0 and Current (current = ans_list) to keep track of node 
           and Carry (To keep reminder value of sum)
        2. Iterator though both Linked List and carry until all are not empty 
        3. Find total of both Linked List + Carry (total = l1 + l2 + carry) -> If value available then sum value otherwise 0
        4. Calculate new carry (carry = total / 10)
        5. Save Current.next = (total % 10)
        6. Update current value (current = current.next)
        7. Move to next node of both Linked List (If list is not empty)

"""


