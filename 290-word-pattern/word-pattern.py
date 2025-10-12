class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        PS = {}
        SP = {}
        for i in range(len(s)):
            chp,chs = pattern[i],s[i]
            if chp in PS and PS[chp] != chs:
                return False
            if chs in SP and SP[chs] != chp:
                return False
            PS[chp] = chs
            SP[chs] = chp
        return True 