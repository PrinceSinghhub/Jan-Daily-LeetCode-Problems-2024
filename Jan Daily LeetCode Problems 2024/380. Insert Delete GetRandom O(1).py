class RandomizedSet:
    def __init__(self):
        self.stack = []
        self.dict = {}

    def insert(self, val: int) -> bool:
        # dictionary is on average O(1) where as
        # checking the array is on average O(n)
        if val in self.dict:
            return False

        self.dict[val] = len(self.stack)
        self.stack.append(val)
        return True

    def remove(self, val: int) -> bool:
        # dictionary is on average O(1) where as
        # checking the array is on average O(n)
        if val not in self.dict:
            return False
        last = self.stack[-1]
        ind = self.dict[val]

        self.dict[last] = ind
        self.stack[ind] = last

        self.stack.pop()

        self.dict.pop(val)

        return True

    def getRandom(self) -> int:
        return random.choice(self.stack)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()