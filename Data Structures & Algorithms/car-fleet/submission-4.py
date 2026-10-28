class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        n = len(position)
        arr = sorted(zip(position,speed), reverse=True)

        fleets = 0
        min_time = -1

        for pos, v in arr:
            t = (target - pos) / v

            if t > min_time:
                fleets += 1

                min_time = t

        return fleets
