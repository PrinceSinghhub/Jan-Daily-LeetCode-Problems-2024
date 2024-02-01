class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        beams = 0
        prev = 0
        for b in bank:
            last = b.count('1')
            if last:
                beams += prev * last
                prev = last
        return beams
