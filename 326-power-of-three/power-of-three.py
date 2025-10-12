class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n > 0:
            x = math.log10(n) / math.log10(3)
            if float(int(x)) == x:
                return True
        return False