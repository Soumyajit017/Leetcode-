class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        Map_ST = {}
        Map_TS = {}
        for i in range(len(s)):
            if s[i] in Map_ST and Map_ST[s[i]] != t[i]:
                return False
            if t[i] in Map_TS and Map_TS[t[i]] != s[i]:
                return False
            Map_ST[s[i]] = t[i]
            Map_TS[t[i]] = s[i]
        return True

        
