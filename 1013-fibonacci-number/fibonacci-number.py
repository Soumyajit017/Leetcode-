class Solution:
    def fib(self, n: int) -> int:
        if n <=1:
            return n
        a,b = 0,1
        for _ in range(2,n+1): # _ throwaway loop counter variable
            a, b = b, a+b # -> shift windom forward 
        return b 
