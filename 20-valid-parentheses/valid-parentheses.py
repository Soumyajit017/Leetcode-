class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')':'(',
            '}':'{',
            ']': '['
        }
        for x in s: #traversing through each char in the string
            if x in mapping: #does the string, happens to be there in the mapping
                if not stack or stack[-1] != mapping[x]: #the stack is empty & top element ain't the match
                    return False #return false, coz invalid parenthesis
                stack.pop()
            else:
                stack.append(x) #if opening bracket,push 
        return not stack #means the stack is empty, have to return bool
