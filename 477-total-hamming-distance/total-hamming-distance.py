class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        for bits in range(32):
            count_ones = 0
            for num in nums:
                count_ones += (num>>bits) & 1
            total += count_ones * (n - count_ones)
        return total