class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ans = [0] * len(temperatures)

        stack = []

        for i, temp in enumerate(temperatures):

            if not stack or temp <= temperatures[stack[-1]]:
                stack.append(i)
            
            else:
                while stack and temperatures[stack[-1]] < temp:
                    idx = stack.pop()
                    ans[idx] = i - idx
                stack.append(i)
        
        return ans