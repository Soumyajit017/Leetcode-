class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = {}
        output = []
        for i in nums1:
            n1[i] = n1.get(i,0) + 1
        for i in nums2:
            if i in n1 and n1[i] > 0:
                output.append(i)
                n1[i] -= 1
        return output