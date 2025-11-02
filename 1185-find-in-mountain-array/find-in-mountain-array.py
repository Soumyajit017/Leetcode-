# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        #finding the peak element
        l,r = 0, mountainArr.length()-1
        peak = 0
        while l < r:
            mid = l + (r-l)//2
            if mountainArr.get(mid) < mountainArr.get(mid+1):
                l = mid + 1
            else:
                r = mid
        peak = l
        #Binary search on the ascending order
        l,r = 0, peak
        while l <= r:
            mid = l + (r-l)//2
            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) < target:
                l = mid +1
            else:
                r = mid -1
        #Binary search on the Decending order
        l,r = peak+1,mountainArr.length() - 1
        while l <= r:
            mid = l + (r-l)//2
            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) > target:
                l = mid + 1
            else:
                r = mid - 1
        return -1         
