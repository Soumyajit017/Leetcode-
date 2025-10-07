class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        if len(s) != len(t):
            return False
        for ch in s:
            dic[ch] = dic.get(ch,0) + 1
        for ch in t:
            dic[ch] = dic.get(ch,0) -1
        for values in dic.values():
            if values != 0:
                return False
        return True