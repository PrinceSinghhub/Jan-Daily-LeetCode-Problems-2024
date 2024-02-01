class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        myDict = Counter(arr)
        return len(myDict.values()) == len(set(myDict.values()))