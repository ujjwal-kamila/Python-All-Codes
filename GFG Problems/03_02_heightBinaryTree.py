# Height of Binary Tree

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def height(self, root) -> int:
        # Base case: if the tree is empty, return -1
        if root is None:
            return -1

        # Recursively calculate the height of the left and right subtrees
        left_height = self.height(root.left)
        right_height = self.height(root.right)

        # The height of the tree is the maximum of the left and right subtree heights plus 1
        return max(left_height, right_height) + 1
