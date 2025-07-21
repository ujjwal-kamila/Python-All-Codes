# 1290. Convert Binary Number in a Linked List to Integer

from typing import Optional

# define listNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res = 0
        while head:
            res = res * 2 + head.val
            head = head.next
        return res
    
def create_linked_list(binary_list):
    dummy = ListNode()
    current = dummy
    for bit in binary_list:
        current.next = ListNode(bit)
        current = current.next
    return dummy.next

# Test
input = [1, 0, 1]
head = create_linked_list(input)

sol = Solution()
res = sol.getDecimalValue(head)
print(res) 