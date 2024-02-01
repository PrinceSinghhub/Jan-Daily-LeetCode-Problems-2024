class Solution:
    def findContentChildren(self, children: [int], cookies: [int]) -> int:
        children.sort()
        cookies.sort()
        counter = 0
        for cookie in cookies:
            if counter == len(children):
                break
            if cookie >= children[counter]:
                counter += 1
        return counter