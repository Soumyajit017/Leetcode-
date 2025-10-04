class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1 #since nums has N-1 elements

        for i in range(0,n+1): #go through each number from 1 to N
            found = False #assume not found at the start 
            for j in nums: #array with N-1 elements,missing numbers
                if j == i:
                    found = True #found this number
                    break
            if not found: #if still False after search
                return i

        
