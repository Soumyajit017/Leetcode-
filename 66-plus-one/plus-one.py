class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''.join(str(x) for x in digits)
        res = int(num) + 1
        res = str(res)
        words = list(res)
        fr=[]
        for i in words:
            fr.append(int(i))
        return fr
        