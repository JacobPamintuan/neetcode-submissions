class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        most = 0
        n = len(heights)

        l = 0
        r = n-1

        while l < r:
            lh = heights[l]
            rh = heights[r]

            area = min(lh, rh) * (r-l)
            most = max(most, area)

            if lh > rh:
                r -= 1
            else:
                l += 1

        return most
