class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n > 0:
            x = math.log10(n) / math.log10(2)
            return float(int(x)) == x
        return False