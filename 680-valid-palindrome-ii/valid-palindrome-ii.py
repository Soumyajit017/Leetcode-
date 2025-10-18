class Solution:
    def validPalindrome(self, s: str) -> bool:
        def deletechar(i,j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i +=1
                j -=1
            return True
        l,r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return deletechar(l+1,r) or deletechar(l,r-1)
            l +=1
            r -=1
        return True
        # (l+1,r): skip the left pointer value & move to the next and compute the rest values and (l,r-1), move inwards for the right pointer