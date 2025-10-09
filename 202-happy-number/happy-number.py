class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n > 1:
            if n in seen:
                return False
            seen.add(n)
            sq_num = 0
            while n >0:
                d = n%10
                sq_num += d*d
                n //=10
            n = sq_num    
        return True