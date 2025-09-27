class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0 :
                result = result | nums[i]
        return result
        