class Solution:

    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        n = len(nums)
        f = [0] * n
        for i in range(n):
            length, max_lis = 1, 0
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    max_lis = max(max_lis, f[j])
            f[i] = max_lis + 1
        return max(f)