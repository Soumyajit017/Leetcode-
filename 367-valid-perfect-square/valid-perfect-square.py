from math import sqrt
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1,int(sqrt(num))+1):
            if i == num/i:
                return True
        return False