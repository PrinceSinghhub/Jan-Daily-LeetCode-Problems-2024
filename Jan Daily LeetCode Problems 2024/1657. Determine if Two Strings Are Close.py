class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        # if they don't have the same length then
        # we can immediately return False
        if len(word1) != len(word2):
            return False

        else:
            c1 = Counter(word1)
            c2 = Counter(word2)

            # for 2 strings to be close they have to:

            # 1.
            # have the same number of repetitions (values),
            # they don't have to be the same character (key) necessarily

            # 2.
            # keys need to match because - task says: we can only
            # transform every occurrence of one existing character

            if (c1.keys() == (c2.keys())
                    and sorted(c1.values()) == sorted(c2.values())):
                return True

            return False