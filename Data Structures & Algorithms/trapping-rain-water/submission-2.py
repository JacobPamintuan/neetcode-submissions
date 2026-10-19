class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        n = len(height)
        
        l, r = 0, n-1
        maxL, maxR = height[l], height[r]

        while l < r:



            if maxL < maxR:
                l += 1
                val = maxL - height[l]
                maxL = max(maxL, height[l])

            else:
                r -= 1
                val = maxR - height[r]
                maxR = max(maxR, height[r])

            total += val if val > 0 else 0
        return total


            
            


            
            

