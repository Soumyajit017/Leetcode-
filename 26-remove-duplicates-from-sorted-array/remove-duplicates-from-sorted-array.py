class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        f,s=1,0
        while f<n:
            if nums[s] != nums[f]:
                s+=1
                nums[s] = nums[f]
            f+=1
        return s+1