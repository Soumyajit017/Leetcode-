class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum,max_sum =0,0
        window_sum += sum(nums[0:k])
        max_sum = window_sum
        for i in range(k,len(nums)):
            window_sum = window_sum-nums[i-k]+nums[i]
            max_sum = max(window_sum,max_sum)
        return float(max_sum/k)
