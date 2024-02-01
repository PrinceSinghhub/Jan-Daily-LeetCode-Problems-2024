import heapq
from heapq import heappush


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        combos = []
        for index in range(len(startTime)):
            combos.append((startTime[index], endTime[index], profit[index]))
        combos.sort(key=lambda x: x[0])

        maxProfit = 0  # this is based on start time
        heap = []  # (endTime, profit)
        for combo in combos:

            start = combo[0]
            while heap and heap[0][0] <= start:
                # pop all with endtime <= curr start time
                # remember our max profit is based start time !
                maxProfit = max(heapq.heappop(heap)[1], maxProfit)

            heappush(heap, (combo[1], maxProfit + combo[2]))

        for remainCombo in heap:
            # update the max profit to endtime based
            maxProfit = max(maxProfit, remainCombo[1])

        return maxProfit