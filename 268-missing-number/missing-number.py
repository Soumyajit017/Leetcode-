class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n+1)//2 #formula for sum of numbers , from 0 to n
        actual_sum = sum(nums) #sum of the (n-1) numbers present in the given array
        return (expected_sum - actual_sum) #the difference, spills out the missing number
        
