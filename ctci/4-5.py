# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderSuccessor(self, root, p):
        if p.right:
            curr = p.right
            while True:
                if not curr.left:
                    return curr
                curr = curr.left

        branch = []
        curr = root

        while True:
            branch.append(curr)
            if curr.val == p.val:
                # we found the node, break
                break
            if curr.val > p.val:
                curr = curr.left
            if curr.val < p.val:
                curr = curr.right

        for i in range(len(branch) -1, -1, -1):
            if branch[i].val > p.val:
                return branch[i]

        return None
