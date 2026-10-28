class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        n = len(position)
        arr = sorted(zip(position,speed), reverse=True)

        ans = 0

        stack = []

        for pos, v in arr:
            
            t = (target - pos) / v

            if not stack or t > stack[-1]:
                stack.append(t)

        return len(stack)