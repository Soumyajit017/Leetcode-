class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r = 0, len(nums)-1
        if not nums:
            return [-1,-1]
        while l <=r:
            mid = l + (r-l)//2
            if nums[mid]>=target:
                r = mid-1
            else:
                l = mid+1 #returns the lower bound, also includes the insert position where it can be inserted if not present
        if l < len(nums) and nums[l] == target: #for the safety, if the l doesn't exist why need to go for the right part
            left = l
        else:
            return [-1,-1]
        l,r = 0,len(nums)-1
        while l<=r:
            mid = l + (r-l)//2
            if nums[mid] <= target:
                l = mid+1
            else:
                r = mid-1
        right = r 
        return [left,right]