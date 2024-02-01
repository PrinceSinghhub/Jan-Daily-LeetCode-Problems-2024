# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfs(self, root, res):

        if root == None:
            return []

        if root:
            if root.left == None and root.right == None:
                res.append(root.val)
            self.dfs(root.left, res)

            self.dfs(root.right, res)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        r1 = []
        r2 = []

        self.dfs(root1, r1)
        self.dfs(root2, r2)

        print(r1, r2)
        return r1 == r2
