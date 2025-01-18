# Problem: Reverse a Linked List
# Given the head of a linked list, the task is to reverse this list and return the reversed head.


# Input: A singly linked list with nodes: 1 -> 2 -> 3 -> 4 -> 5 -> None
# Output: The reversed linked list: 5 -> 4 -> 3 -> 2 -> 1 -> None

'''
Approach:
Use two pointers (prev and curr):
prev: Tracks the previous node (initially None).
curr: Tracks the current node (starts at head).
For each node:
Save the next node in a temporary variable (next_node).
Reverse the current node’s pointer (curr.next = prev).
Move prev to the current node (prev = curr) and move curr to next_node.
Repeat until all nodes are reversed (curr becomes None).
The new head of the list is prev (previous node after reversal).
'''

# Create a node in Singly linked list
class LinkList:
    def __init__(self,data= None,next= None):
        self.data = data
        self.next = next

#  Reverse a linked list
class Solution:
    def reverseList(self, head):
        # Initialize variables
        prev = None  # This will become the new head
        curr = head  # Start from the current head of the list
        
        # Traverse the list
        while curr:
            next_node = curr.next  # Save the next node
            curr.next = prev      # Reverse the current node's pointer
            prev = curr           # Move `prev` to the current node
            curr = next_node      # Move `curr` to the next node
        
        # At the end, `prev` will point to the new head
        return prev



# Create a linked list
def create_linked_list(values):
    if not values:
        return None
    
    head = LinkList(values[0])
    current = head
    for val in values[1:]:
        current.next = LinkList(val)
        current = current.next
    return head

# Print linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" --> ")
        current = current.next
    print("None")
    
# test case

head = create_linked_list([1, 2, 3, 4, 5])
print("Original linked list: ")
print_linked_list(head)

print("\nReversed linked list: ")
reversed_head = Solution().reverseList(head)
print_linked_list(reversed_head)