class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Need to map [i][j] to 1-D
        m = len(matrix) # num rows
        n = len(matrix[0]) # num elements in each row

        left = 0
        right = m*n-1

        while left <= right:
            mid = (left + right) // 2

            i = mid // n
            j = mid % n

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False