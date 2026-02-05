class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        area=0
        max_area=0
        while l<r:
            area = (r-l) * min(height[l],height[r])
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
            max_area = max(area,max_area)
        return max_area
            