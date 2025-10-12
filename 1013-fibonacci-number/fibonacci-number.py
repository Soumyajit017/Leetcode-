class Solution:
    def fib(self, n: int) -> int:
        if n <=1:
            return n
        return self.fib(n-1) + self.fib(n-2) #callinga method within the same class, self.method_name(arguments)