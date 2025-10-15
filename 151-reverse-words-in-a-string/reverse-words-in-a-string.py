class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        stack = []
        result = []
        for i in s:
            stack.append(i)
        while stack:
            result.append(stack.pop())
        return " ".join(result)