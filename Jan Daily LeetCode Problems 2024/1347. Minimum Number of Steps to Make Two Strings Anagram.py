from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        x=list((Counter(s) & Counter(t)).elements())
        return len(s)-len(x)