class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = 0
        xor = x ^ y
        count = 0
        while xor:
            xor &= (xor-1)
            count +=1
        return count