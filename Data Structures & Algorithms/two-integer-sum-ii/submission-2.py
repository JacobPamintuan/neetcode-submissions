class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        
        left = 0
        complement = 0
        while left < n:
            complement = target-numbers[left]

            for i in range(left+1, n):
                if numbers[i] == numbers[left]:
                    continue
                if numbers[i] > complement:
                    break
                if numbers[i] == complement:
                    return [left+1, i+1]

            left += 1
            
