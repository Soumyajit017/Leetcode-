class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for i in s+t:
            res ^= ord(i)
        return chr(res)

        #xor only works for comparing numbers , so convert the string char's into numbers and comapre, the left out is the diff, then convert back to str

    