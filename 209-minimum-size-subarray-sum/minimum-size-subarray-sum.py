class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        curr_sum = 0
        low,high = 0,0
        curr_length = 0
        while high<len(nums):
            curr_sum += nums[high]
            high+=1
            while curr_sum >= target:
                curr_length = high-low
                min_length = min(curr_length,min_length)
                curr_sum -= nums[low]
                low+=1
        return min_length if min_length != float('inf') else 0
