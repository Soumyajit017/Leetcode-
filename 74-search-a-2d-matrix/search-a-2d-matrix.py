class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c = len(matrix),len(matrix[0])
        low,high = 0, r*c - 1
        row,col = 0,0
        while low<=high:
            mid = low + (high-low)//2
            row = mid // c
            col = mid % c
            value = matrix[row][col]
            if value == target: 
                return True
            elif value < target: 
                low = mid+1
            else: 
                high = mid-1
        return False
