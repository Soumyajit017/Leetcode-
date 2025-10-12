class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            curr_sum = 0
            while num > 0:
                re = num%10
                curr_sum +=re
                num //=10
            num = curr_sum
        return num