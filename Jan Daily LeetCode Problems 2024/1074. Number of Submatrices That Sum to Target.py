class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:

        m = len(matrix)
        n = len(matrix[0])

        ans = 0

        for i in range(m):  # enum upper bound
            total = [0] * n

            for j in range(i, m):  # enum lower bound
                for c in range(n):
                    # update each row's sum
                    total[c] += matrix[j][c]

                ans += self.subarrSum(total, target)

        return ans

    def subarrSum(self, nums, k):
        hashmap = defaultdict(int)
        hashmap[0] = 1

        cnt = presum = 0
        for x in nums:
            presum += x

            if presum - k in hashmap:
                cnt += hashmap[presum - k]

            hashmap[presum] += 1

        return cnt
