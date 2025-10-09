class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n > 1:
            if n in seen:
                return False
            else:
                seen.add(n)
                n = sum(int(d)**2 for d in str(n))  #list comprehension
        return True