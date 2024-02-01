class Solution:
    def dailyTemperatures(self, temperatures):

        dp = [0] * len(temperatures)

        stack = []

        for i in range(len(temperatures)):

            while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                current = stack.pop()

                dp[current] = i - current
            stack.append(i)
        return dp

        # brutoforce Approch
        ''''ans =[]

        for i in range(len(temperatures)):
            flag = True
            for j in range(i+1,len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    ans.append(j-i)
                    flag = False
                    break
            if flag == True:
                ans.append(0)



        return ans'''



