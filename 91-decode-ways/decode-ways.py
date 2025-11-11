class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        n = len(s)
        p1,p2 = 1,1
        for i in range(1,n):
            curr = 0
            ones = int(s[i])
            twos = int(s[i-1:i+1])
            if 1 <= ones <= 9:
                curr += p1
            if 10 <= twos <= 26:
                curr += p2
            p2,p1 = p1, curr
        return p1