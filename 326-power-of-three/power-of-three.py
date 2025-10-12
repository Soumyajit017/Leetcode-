class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n > 0:
            return 1162261467 % n == 0 #1162261467 -> largest power of 3 within the given range, so if n is a power of 3, it will always divide 1162261467...
        return False