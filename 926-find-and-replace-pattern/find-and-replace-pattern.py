class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        final = []
        for word in words:
            PW = {}
            WP = {}
            matched = True 
            for w,p in zip(word,pattern):
                if w in WP and WP[w] != p:
                    matched = False
                    break
                if p in PW and PW[p] != w:
                    matched = False
                    break
                WP[w] = p
                PW[p] = w
            if matched:
                final.append(word)
        return final