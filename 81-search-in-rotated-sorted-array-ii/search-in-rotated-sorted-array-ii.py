class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l,r = 0,len(nums)-1
        while l<=r:
            mid = l + (r-l)//2
            if nums[mid] == target: #mid is the target, found
                return True
            if nums[l] == nums[mid] == nums[r]:
                l +=1
                r -=1
                continue
            if nums[l]<=nums[mid]: #left side of the array is sorted
                if nums[l] <= target < nums[mid]:
                    r = mid -1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]: #right side of the array is sorted
                    l = mid + 1
                else:
                    r = mid - 1
        return False           