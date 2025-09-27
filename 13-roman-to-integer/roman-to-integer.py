class Solution:
    def romanToInt(self, s: str) -> int:

        roman_map={ #creating an hash map to add the value wrt alphabets
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        result = 0 #declaring the result variable with 0 
        for i in range(len(s)): #so that the loop doesn't go overbound for the (i+1)element checking
            if  i+1 < len(s) and roman_map[s[i]] < roman_map[s[i+1]]: #if the next element is greater, than subtract IV-4,V-5, also check the bouding statement, i+1 < len(s), so that the loop never goes unbounded 
                result -= roman_map[s[i]] #subtracting into the result
            else:
                result += roman_map[s[i]]
        return result