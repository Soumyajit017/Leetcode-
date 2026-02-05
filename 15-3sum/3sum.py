class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sum = 0
        hash_set = set()
        for i in range(len(nums)-2):
            if nums[i] > 0: break
            right = len(nums)-1
            left = i+1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    hash_set.add((nums[i],nums[left],nums[right]))
                    left+=1
                    right-=1
                elif sum < 0:
                    left+=1
                else:
                    right-=1
        return list(hash_set)