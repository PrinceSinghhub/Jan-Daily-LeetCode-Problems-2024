# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, root, ans):
        if root:
            ans.append(root.val)

            self.dfs(root.left, ans)
            self.dfs(root.right, ans)
        return ans

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        val = self.dfs(root, [])

        ans = 0

        for i in val:
            if i >= low and i <= high:
                ans += i

        return ans