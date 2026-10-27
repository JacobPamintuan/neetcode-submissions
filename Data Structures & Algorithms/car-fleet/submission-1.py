class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        n = len(position)
        arr = []

        for i in range(n):
            arr.append((position[i],speed[i]))

        arr.sort(reverse=True)

        stack = []

        ans = 0

        for i in range(n):
            if not stack or arr[i][1] <= stack[-1][1]:
                stack.append(arr[i])
                continue

            steps = (arr[i][0]-stack[-1][0]) / (stack[-1][1]-arr[i][1])
            pos = arr[i][1] * steps + arr[i][0]

            if steps < 0 or pos > target:
                stack.append(arr[i])





        return len(stack)
