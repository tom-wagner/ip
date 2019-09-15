from collections import deque
from math import inf

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root) -> bool:
        if not root:
            return True

        q = deque()
        q.append((root, -inf, inf))

        while q:
            curr, min_valid_value, max_valid_value = q.popleft()
            if curr.left:
                if curr.left.val >= curr.val or curr.left.val <= min_valid_value:
                    return False
                q.append((curr.left, min_valid_value, curr.val))
            if curr.right:
                if curr.right.val <= curr.val or curr.right.val >= max_valid_value:
                    return False
                q.append((curr.right, curr.val, max_valid_value))
        return True
