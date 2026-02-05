class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()
        l,r=0,0
        max_length=0
        while r < len(s):
            while s[r] in hash_set:
                hash_set.remove(s[l])
                l+=1
            hash_set.add(s[r])
            max_length=max(max_length,r-l+1)
            r+=1
        return max_length
             
            
                