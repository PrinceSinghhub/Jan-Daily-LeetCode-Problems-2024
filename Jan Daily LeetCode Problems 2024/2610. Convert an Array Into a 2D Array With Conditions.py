class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = {}
        for i in nums:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
        length = max(res.values())
        result = [[] for i in range(length)]
        for i in res:
            for j in range(res[i]):
                result[j].append(i)
        return result