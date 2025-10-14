class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = set()
        seen = set()
        seen.update(nums1)
        for i in range(0,len(nums2)):
            if nums2[i] in seen:
                output.add(nums2[i])
        return list(output)