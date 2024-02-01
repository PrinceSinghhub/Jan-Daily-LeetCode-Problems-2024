from collections import Counter


class Solution:

    def findAns(self, myarr, intHashSet):
        finalAns = 0

        for pairKey, pairValue in intHashSet.items():
            if pairValue < 2:
                return -1
            data = (pairValue + 2)
            data = data // 3
            finalAns += data

        return finalAns

    def minOperations(self, myarr):
        intHashSet = Counter(myarr)

        return self.findAns(myarr, intHashSet)