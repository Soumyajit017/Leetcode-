class Solution:
    def hammingWeight(self, n: int) -> int:
        set_bits = 0
        s = bin(n)[2:]
        for i in range(len(s)):
            c = s.count('1')
        return c