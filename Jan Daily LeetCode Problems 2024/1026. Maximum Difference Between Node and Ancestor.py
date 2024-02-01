# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:

        def dfs(root, maxx, minn):
            if not root:
                return abs(maxx - minn)
            if root.val >= maxx:
                maxx = root.val
            if root.val <= minn:
                minn = root.val
            return max(dfs(root.left, maxx, minn), dfs(root.right, maxx, minn), abs(maxx - minn))

        return dfs(root, -100000, 100000)
