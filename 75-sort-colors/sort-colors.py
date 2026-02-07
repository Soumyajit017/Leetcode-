class Solution:
    def sortColors(self, nums: List[int]) -> None:
        s,m,e = 0,0,len(nums)-1
        while m<=e:
                if nums[m] == 0:
                    nums[m],nums[s] = nums[s],nums[m]
                    s+=1
                    m+=1
                elif nums[m] == 1:
                    m+=1
                elif nums[m] == 2:
                    nums[m],nums[e] = nums[e],nums[m]
                    e-=1
                