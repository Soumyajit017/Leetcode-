from math import sqrt
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        curr_sum = 1
        if num > 1:
            for i in range(2,int(sqrt(num)+1)):
                if num % i == 0:
                    curr_sum += i
                    if i != num // i:
                        curr_sum += num //  i 
            return curr_sum == num
        return False