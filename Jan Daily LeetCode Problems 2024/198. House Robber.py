class Solution:
    def rob(self, nums: List[int]) -> int:

        def solveUtil(n, arr, dp):
            dp[0] = arr[0]
            for i in range(1, n):
                pick = arr[i]
                if i > 1:
                    pick += dp[i - 2]
                non_pick = 0 + dp[i - 1]
                dp[i] = max(pick, non_pick)
            return dp[n - 1]

        dp = [-1 for _ in range(len(nums))]
        return solveUtil(len(nums), nums, dp)
