class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        while l<r:
            mid = l +(r-l)//2
            if mid %2 == 1:
                mid -=1
            if nums[mid] == nums[mid+1]:
                l = mid + 2 #coz already mid-1, for even & mid+1 checked, so mid+2
            else:
                r = mid # not mid-1, coz already mid -1, if not even
        return nums[l]