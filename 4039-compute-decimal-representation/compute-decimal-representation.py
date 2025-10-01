class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        s = str(n)
        length = len(s)-1
        components = []

        for digits in (s):
            if digits!= '0':
                components.append(int(digits) * 10**length)
            length -=1
        return components