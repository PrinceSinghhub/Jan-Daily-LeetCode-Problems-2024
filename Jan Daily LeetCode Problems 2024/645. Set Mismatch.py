class Solution:
	def findErrorNums(self, nums):
			count = collections.Counter(nums)
			missing = 0
			twice = 0
			for i in range(1, len(nums)+1):
				if i not in count:
					missing = i
				if count[i] == 2:
					twice = i
			return [twice, missing]