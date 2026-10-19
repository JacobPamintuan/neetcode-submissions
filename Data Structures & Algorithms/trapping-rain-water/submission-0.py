class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        n = len(height)
        
        maxLeft = [0] * n
        maxRight = [0] * n

        for i in range(n):
            maxLeft[i] = max(
                height[i],
                maxLeft[i - 1] if i > 0 else 0
            )

            j = n - 1 - i
            maxRight[j] = max(
                height[j],
                maxRight[j + 1] if j < n - 1 else 0
            )

        minLR = [0] * n

        for i in range(n):
            minLR[i] = min(maxLeft[i], maxRight[i])

        for i in range(n):
            total += minLR[i] - height[i]

        return total


            
            


            
            

