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
        for i in range(len(s)-1): #so that the loop doesn't go overbound for the (i+1)element checking
            if roman_map[s[i]] < roman_map[s[i+1]]: #if the next element is greater, than subtract IV-4,V-5
                result -= roman_map[s[i]] #subtracting into the result
            else:
                result += roman_map[s[i]]
        #for adding the last element, coz after the len(n)-1 comparison, last element not getting added , so we need to add it explictly
        result += roman_map[s[-1]]
        return result