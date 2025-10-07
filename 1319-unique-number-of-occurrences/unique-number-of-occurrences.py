class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Step 1: Create a list to store unique numbers
        unique_nums = []
        
        # Step 2: Build list of unique elements manually (O(n^2))
        for num in arr:
            found = False
            for x in unique_nums:
                if x == num:
                    found = True
                    break
            if not found:
                unique_nums.append(num)
        
        # Step 3: Count frequency of each unique number (O(n^2))
        freq = []
        for num in unique_nums:
            count = 0
            for x in arr:
                if x == num:
                    count += 1
            freq.append(count)
        
        # Step 4: Compare every pair of frequencies (O(n^2))
        for i in range(len(freq)):
            for j in range(i + 1, len(freq)):
                if freq[i] == freq[j]:
                    return False
        
        return True
