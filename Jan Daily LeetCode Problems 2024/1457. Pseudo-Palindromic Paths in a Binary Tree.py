# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        # only 1-9, space O(1)
        arr = [0] * 10
        cnt = 0

        def helper(node):
            nonlocal cnt
            # base case
            if not node: return
            # include the current node, similar to path construction in backtracking
            arr[node.val] += 1
            # path is ended, check whether pseudoPalindromic
            if not node.left and not node.right:
                # odd item can be at most 1
                cnt += int(len([item for item in arr if item % 2 == 1]) <= 1)
            helper(node.left)
            helper(node.right)
            # remove the current node, similar to backtracking
            arr[node.val] -= 1

        helper(root)
        return cnt