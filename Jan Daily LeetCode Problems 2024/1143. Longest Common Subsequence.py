class Solution:

    def sol(self, str1, str2, indx1, indx2, dp):

        if indx1 < 0 or indx2 < 0:
            return 0

        if dp[indx1][indx2] != -1:
            return dp[indx1][indx2]

        if str1[indx1] == str2[indx2]:
            return 1 + self.sol(str1, str2, indx1 - 1, indx2 - 1, dp)

        take = self.sol(str1, str2, indx1 - 1, indx2, dp)
        notTake = self.sol(str1, str2, indx1, indx2 - 1, dp)

        dp[indx1][indx2] = max(take, notTake)
        return dp[indx1][indx2]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n = len(text1)
        m = len(text2)
        dp = [[-1] * (m + 1) for _ in range(n)]
        return self.sol(text1, text2, n - 1, m - 1, dp)
