class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list) #skips the edge case if key not there
        for s in strs:
            count = [0] * 26 #creates an array of 26 zeros
            for ch in s:  #now go for individual elements
                count[ord(ch)-ord('a')] += 1  #for 'eat', e-> count[4] = 1,then goes for all
            key = tuple(count) #coz list ain't be dic keys
            dic[key].append(s)  #appending to the final dics to return
        return list(dic.values()) 

