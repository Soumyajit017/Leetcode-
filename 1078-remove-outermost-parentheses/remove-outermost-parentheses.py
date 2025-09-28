class Solution:
    def removeOuterParentheses(self, s: str) -> str:
            result = []  #launching an empty stack 
            counter = 0   #counter to check, if 0: outermost/at begining, if 1:Innermosy

            for char in s:
                if char == '(': 
                    if counter >0: #skip outermost '('
                        result.append(char)
                    counter +=1
                else:
                    counter -=1
                    if counter > 0: #skip outermost ')'
                        result.append(char)
            return "".join(result)  #concatenation of the strings
