class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        inp = 0
        for n in range(len(nums)):
            if nums[n] != val:
                nums[inp] = nums[n]
                inp +=1
        return inp

                