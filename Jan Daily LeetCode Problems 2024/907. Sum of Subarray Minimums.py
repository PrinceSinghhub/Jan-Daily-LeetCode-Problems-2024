class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        M = 10 ** 9 + 7

        # right bound for current number as minimum
        q = []

        n = len(arr)
        right = [n - 1] * n

        for i in range(n):
            # must put the equal sign to one of the bound (left or right) for duplicate nums (e.g. [71, 55, 82, 55])
            while q and arr[i] <= arr[q[-1]]:
                right[q.pop()] = i - 1
            q.append(i)

        # left bound for current number as minimum
        q = []
        left = [0] * n
        for i in reversed(range(n)):
            while q and arr[i] < arr[q[-1]]:
                left[q.pop()] = i + 1
            q.append(i)

        # calculate sum for each number
        ans = 0
        for i in range(n):
            l, r = abs(i - left[i]), abs(i - right[i])
            # for example:  xx1xxx
            # left take 0, 1, 2 numbers (3 combs) and right take 0, 1, 2, 3 numbers (4 combs)
            covered = (l + 1) * (r + 1)
            ans = (ans + arr[i] * covered) % M

        return ans